import httpx
import streamlit as st


API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="AI Endpoint Demo",
    page_icon="🤖",
)

st.title("AI Endpoint Demo")
st.write("Ask a question and view the API response.")

question = st.text_area(
    "Question",
    placeholder="What is an AI endpoint?",
)

if st.button("Ask AI", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating an answer..."):
            try:
                response = httpx.post(
                    API_URL,
                    json={"question": question},
                    timeout=60.0,
                )
                response.raise_for_status()
                data = response.json()

                st.subheader("Answer")
                st.write(data["answer"])

                st.metric("Tokens used", data["tokens_used"])
                st.metric("Estimated cost", f"${data['cost_usd']:.8f}")

            except httpx.HTTPError as exc:
                st.error(f"API request failed: {exc}")
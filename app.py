import streamlit as st

from rag import ask_question

st.set_page_config(
    page_title="Medical RAG Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Medical RAG Assistant")

st.write("Ask questions from your uploaded medical PDFs.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a medical question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Searching medical documents..."):

        answer, sources = ask_question(question)

    with st.chat_message("assistant"):

        st.markdown(answer)

        st.markdown("---")

        st.subheader("📚 Sources")

        for source in sources:
            st.write(source)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
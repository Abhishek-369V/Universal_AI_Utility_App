import streamlit as st
# from Backend import Utility
from Backend import Utility
from Prompt import create_prompt


st.set_page_config(
    page_title="AI Utility App"
)

st.title("Universal AI Utility")
st.caption("AI application that performs multiple tasks using a single interface.")

task = st.selectbox(
"Select Task",
[
    "Summarize",
    "Translate",
    "Explain",
    "Generate Email",
    "Rewrite"
])

text = st.text_area( "Enter Input" )

option = ""

if task=="Translate":
    option = st.selectbox(
        "Language",
        [
            "French",
            "Hindi",
            "Spanish"
        ]
)

# initializing session state
if "response" not in st.session_state:
    st.session_state.response = ""
if "prompt" not in st.session_state:
    st.session_state.prompt = "" 

# inside generate button — save to session state
if st.button("Generate"):
    if text:
        with st.spinner("Generating..."):
            st.session_state.prompt = create_prompt(task, text, option)
            st.session_state.response = Utility(st.session_state.prompt)
    else:
        st.warning("Provide input")

if st.session_state.response:
    st.subheader("Prompt")
    st.code(st.session_state.prompt)

    st.subheader("Response")
    st.write(st.session_state.response)

    st.download_button(
        label="Download Response",
        data=st.session_state.response,
        file_name="Generated_response.txt",
        mime="text/plain",
        icon=":material/download:",
    )
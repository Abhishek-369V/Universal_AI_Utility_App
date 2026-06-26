import streamlit as st
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

if st.button("Generate"):
    if text:
        with st.spinner("Generating..."):
            prompt = create_prompt(task, text, option)
            st.subheader("Prompt")
            st.code(prompt)

            output = Utility(prompt)
            st.subheader("Output")
            st.write(output)

    else:
        st.warning("Provide input")

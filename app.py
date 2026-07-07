import streamlit as st
from Backend_google import Utility_google
from Backend_openai import Utility_openai
from Prompt import create_prompt


st.set_page_config(
    page_title="AI Utility App"
)

st.title("Universal AI Utility")
st.caption("AI application that performs multiple tasks using a single interface.")

task = st.selectbox(
    label="Choose AI Action",
    options=[
        "Summarize",
        "Translate",
        "Explain",
        "Generate Email",
        "Rewrite"
    ],
    index=None,
    placeholder="Pick an operation...",
)

text = st.text_area(
    label="Source Content",
    placeholder="Provide the content for the selected task...",
    height=200, 
)


option = ""

languages = [
    "Hindi", "Bengali", "Marathi", "Telugu", "Tamil", "Gujarati", 
    "Urdu", "Kannada", "Odia", "Malayalam","French", "Spanish", 
    "Chinese", "Japanese", "Arabic", "Russian", "Indonesian",
]

if task == "Translate":
    option = st.selectbox(
        label="Select Target Language",
        options=languages,
        index=None,  # Forces the user to select an option manually, preventing accidental triggers
        placeholder="Choose a language...",  # Displayed when index is None
        help="Choose the language you want your text translated into."  # Adds a sleek hover icon
    )

# initializing session state
if "response" not in st.session_state:
    st.session_state.response = ""
if "prompt" not in st.session_state:
    st.session_state.prompt = "" 

# Selecting Model
model_choice = st.selectbox(
    label="Choose AI Model",
    options=("Google Gemini", "OpenAI"),)

# openai key as input - shows only when user selects "OpenAI model"
user_openai_key = None
if model_choice == "OpenAI":
    st.info("""
            ⚠️ Sorry! For the Inconvinience, this model is not available for free now!..
            - It charges credits for every request. We are Looking forward to fix this and make available for free!.. 
            - So till then, Use Google Gemini or Enter your own OpenAI API key to continue.
            > 👉 **Get your key here**: https://platform.openai.com/api-keys  → Sign up → API Keys → Create new secret key
    """)
    user_openai_key = st.text_input(
        "Enter your OpenAI API key",
        type="password",
        placeholder="sk-...."
    )
        

# inside generate button — save to session state
if st.button("Generate"):
    if text:
        with st.spinner("Generating..."):
            st.session_state.prompt = create_prompt(task, text, option)

            # based on model user choose:--> route based on selection
            if model_choice == "OpenAI" and not user_openai_key:
                st.warning("⚠️ Please enter your OpenAI API key above to continue.")
            elif model_choice == "OpenAI" and not user_openai_key.startswith("sk-"):
                st.error("Provide a valid API key")
            elif model_choice == "OpenAI" and user_openai_key.startswith("sk-"):
                st.session_state.response = Utility_openai(st.session_state.prompt, api_key=user_openai_key)
            else:
                st.session_state.response = Utility_google(st.session_state.prompt)
    else:
        st.warning("Please Provide required input!")

# Fetching Response:
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
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
        **OpenAI requires your own API key.**
    
        - 🔑 Get your key at: https://platform.openai.com/api-keys | Sign up → API Keys → Create new secret key
    
        - 💡 **Tip:** Try Google Gemini above — it works without any key!
    """)
    user_openai_key = st.text_input(
        "Enter your OpenAI API key",
        type="password",
        placeholder="sk-...."
    )
        
# Validating user_openai_key!
def is_valid_openai_key(key):
    return key.startswith("sk-") and len(key)>20

# inside generate button — save to session state
if st.button("Generate"):
    if not task:
        st.warning("⚠️ AI Action is Not Selected!... Please Choose AI Action")
    elif not text.strip():
        st.warning("⚠️ Source content can't be empty!....Please Provide Source Content!")
    elif task=="Translate" and not option:
        st.warning("⚠️ Please Provide a Target Language!... ")
    elif model_choice == "OpenAI" and not user_openai_key:
        st.warning("⚠️ Please enter your OpenAI API key above to continue.")
    elif model_choice == "OpenAI" and not is_valid_openai_key(user_openai_key):
        st.error("Invalid API key: Plz Provide a valid API key") 
    
    else: 
        with st.spinner("Generating..."):
            st.session_state.prompt = create_prompt(task, text, option)
            if model_choice == "OpenAI" and is_valid_openai_key(user_openai_key):
                st.session_state.response = Utility_openai(st.session_state.prompt, api_key=user_openai_key)
            else:
                st.session_state.response = Utility_google(st.session_state.prompt)


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
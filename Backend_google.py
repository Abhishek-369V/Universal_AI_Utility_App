from google import genai 
import streamlit as st

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

def Utility_google(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config = {
                "system_instruction" : "You are a helpful AI assistant",
                "temperature" : 0.7
            }
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"
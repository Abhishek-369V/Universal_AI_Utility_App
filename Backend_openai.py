from openai import OpenAI
import streamlit as st


# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def Utility_openai(prompt, api_key=None):
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages = [{"role":"system",
                         "content":"You are a helpful AI assistant."
                        },
                        {"role": "user", 
                         "content": prompt}],
            temperature = 0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

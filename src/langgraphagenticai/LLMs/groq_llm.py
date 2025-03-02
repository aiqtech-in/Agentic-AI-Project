from langchain_groq import ChatGroq
import os
import streamlit as st

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_control_input = user_controls_input

    def get_llm_models(self):
        try:
            groq_api_key = self.user_control_input['GROQ_API_KEY']
            selected_groq_model = self.user_control_input['selected_groq_models']
            if groq_api_key =='' or os.environ['GROQ_API_KEY'] == '':
                st.error("Please ENter the Griq API Key")

            llm = ChatGroq(api_key= groq_api_key, model= selected_groq_model)
        
        except Exception as e:
            raise ValueError(f"Error Occured with Exception: " + e)
        
        return llm

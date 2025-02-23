import streamlit as st
import google.generativeai as genai

# Configure Google AI API
genai.configure(api_key="your API key")

# Function to analyze Python code
def analyze_code(code):
    model = genai.GenerativeModel("gmodels/gemini-2.0-flash-exp")
    prompt = f"Analyze the following Python code, identify any bugs, and suggest improvements. Provide fixed code snippets if needed.\n\nCode:\n{code}"
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("AI Code Reviewer")
st.write("Submit your Python code for AI-powered analysis and improvements.")

# Text area for user code input
code_input = st.text_area("Enter your Python code:", height=200)

if st.button("Analyze Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code..."):
            feedback = analyze_code(code_input)
        
        st.subheader("Analysis Report")
        st.write(feedback)
    else:
        st.warning("Please enter some Python code before submitting.")

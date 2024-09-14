import streamlit as st
import requests

# Function to get the essay response from Gemma (via FastAPI)
def get_response(topic, model):
    endpoint = "http://127.0.0.1:8000/essay" if model == "Gemma" else "http://127.0.0.1:8000/poem"
    response = requests.post(
        endpoint,
        json={"topic": topic}
    )
    if response.status_code == 200:
        return response.json().get("output", "No response")
    return f"Error: {response.status_code}"

# Streamlit UI
st.title("Langchain Chatbot: Essay & Poem Generator")

# Initialize session state for chat history if not already initialized
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar for chat history
st.sidebar.title("Chat History")
if st.session_state.history:
    for entry in st.session_state.history:
        st.sidebar.write(f"**{entry['model']}**: {entry['topic']}")
        

# Dropdown to select model
model = st.selectbox("Select LLM Model:", ["Gemma", "Llama2"])

# Text input for topic
topic = st.text_input(f"Enter a topic for the {model}:")

# Button to generate response
if st.button("Generate"):
    if topic:
        response = get_response(topic, model)
        
        # Display response
        st.subheader(f"Generated {model}:")
        st.write(response)
        
        # Save to chat history
        st.session_state.history.append({
            'model': model,
            'topic': topic,
            'response': response
        })
    else:
        st.warning("Please enter a topic.")

# Optionally, clear history
if st.sidebar.button("Clear History"):
    st.session_state.history = []
    st.sidebar.write("Chat history cleared.")

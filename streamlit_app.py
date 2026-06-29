"""Streamlit Web Interface for the LangChain Conversational AI Chatbot.

This module provides a user-friendly web interface for interacting with the chatbot.

To run:
    streamlit run streamlit_app.py
"""

import os
import streamlit as st
from dotenv import load_dotenv
from chatbot import ConversationalChatbot

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
    <style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        gap: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .assistant-message {
        background-color: #f5f5f5;
        border-left: 4px solid #4caf50;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def initialize_session_state():
    """Initialize Streamlit session state."""
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ConversationalChatbot(
            model_name=st.session_state.get("model_name", "gpt-3.5-turbo"),
            temperature=st.session_state.get("temperature", 0.7),
            max_tokens=st.session_state.get("max_tokens", 500),
        )
    if "messages" not in st.session_state:
        st.session_state.messages = []


def display_chat_message(role: str, content: str):
    """Display a chat message in the appropriate style.
    
    Args:
        role: Either 'user' or 'assistant'
        content: The message content
    """
    if role == "user":
        st.markdown(
            f'<div class="chat-message user-message"><div><strong>You:</strong><br>{content}</div></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="chat-message assistant-message"><div><strong>Assistant:</strong><br>{content}</div></div>',
            unsafe_allow_html=True,
        )


def main():
    """Main Streamlit application."""
    # Initialize session state
    initialize_session_state()

    # Sidebar configuration
    with st.sidebar:
        st.title("⚙️ Configuration")
        st.markdown("---")

        # Model selection
        model_name = st.selectbox(
            "Model",
            ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"],
            index=0,
        )

        # Temperature slider
        temperature = st.slider(
            "Temperature (Creativity)",
            min_value=0.0,
            max_value=2.0,
            value=0.7,
            step=0.1,
            help="Higher values = more creative, Lower values = more focused",
        )

        # Max tokens slider
        max_tokens = st.slider(
            "Max Response Length",
            min_value=100,
            max_value=2000,
            value=500,
            step=100,
        )

        st.markdown("---")

        # Buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Reset Chat", use_container_width=True):
                st.session_state.messages = []
                if "chatbot" in st.session_state:
                    st.session_state.chatbot.clear_memory()
                st.rerun()

        with col2:
            if st.button("💾 Save History", use_container_width=True):
                if "chatbot" in st.session_state:
                    st.session_state.chatbot.save_history("conversation_history.txt")
                    st.success("Conversation saved!")

        st.markdown("---")
        st.markdown(
            "📚 **About**\n\n"
            "This chatbot uses LangChain with OpenAI's GPT models "
            "to provide intelligent conversations with memory."
        )

    # Main chat area
    st.title("🤖 AI Conversational Chatbot")
    st.markdown("Have a conversation with AI while maintaining context and memory.")
    st.markdown("---")

    # Display chat history
    for message in st.session_state.messages:
        display_chat_message(message["role"], message["content"])

    # Input area
    st.markdown("---")
    user_input = st.text_input(
        "Type your message:",
        placeholder="Ask me anything...",
        key="user_input",
    )

    if user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})
        display_chat_message("user", user_input)

        # Get response from chatbot
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chatbot.chat(user_input)
                st.session_state.messages.append({"role": "assistant", "content": response})
                display_chat_message("assistant", response)
            except Exception as e:
                st.error(f"Error: {str(e)}")

        st.rerun()


if __name__ == "__main__":
    main()

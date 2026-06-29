"""Example usage of the LangChain Conversational AI Chatbot.

This script demonstrates various ways to use the chatbot.
"""

from chatbot import ConversationalChatbot


def example_basic_conversation():
    """Example: Basic conversation with the chatbot."""
    print("\n=== Example 1: Basic Conversation ===")
    chatbot = ConversationalChatbot()

    # Engage in a conversation
    user_inputs = [
        "What is machine learning?",
        "Can you explain neural networks?",
        "How are they different from traditional programming?",
    ]

    for user_input in user_inputs:
        print(f"\nUser: {user_input}")
        response = chatbot.chat(user_input)
        print(f"Assistant: {response}")


def example_with_configuration():
    """Example: Chatbot with custom configuration."""
    print("\n=== Example 2: Custom Configuration ===")
    chatbot = ConversationalChatbot(
        model_name="gpt-3.5-turbo",
        temperature=0.5,  # More focused responses
        max_tokens=300,
    )

    # Ask technical questions
    response = chatbot.chat("Explain REST APIs in simple terms.")
    print(f"Response: {response}")


def example_context_memory():
    """Example: Demonstrate memory and context."""
    print("\n=== Example 3: Context Memory ===")
    chatbot = ConversationalChatbot()

    # First message
    print("User: My name is Alex and I love Python programming.")
    response1 = chatbot.chat("My name is Alex and I love Python programming.")
    print(f"Assistant: {response1}")

    # Second message - chatbot should remember
    print("\nUser: What would be good projects for me?")
    response2 = chatbot.chat("What would be good projects for me?")
    print(f"Assistant: {response2}")


def example_history_management():
    """Example: Manage conversation history."""
    print("\n=== Example 4: History Management ===")
    chatbot = ConversationalChatbot()

    # Have some conversations
    chatbot.chat("Hello! How are you?")
    chatbot.chat("Tell me about artificial intelligence.")
    chatbot.chat("What are some real-world applications?")

    # Get and display history
    history = chatbot.get_conversation_history()
    print("Conversation History:")
    print(history)

    # Save history
    chatbot.save_history("example_history.txt")
    print("\nHistory saved to 'example_history.txt'")


def example_clearing_memory():
    """Example: Clear memory for new session."""
    print("\n=== Example 5: Clearing Memory ===")
    chatbot = ConversationalChatbot()

    # First session
    print("First session - User: Tell me about Python")
    chatbot.chat("Tell me about Python")

    print(f"History length: {len(chatbot.get_conversation_history())}")

    # Clear memory
    print("\nClearing memory...")
    chatbot.clear_memory()
    print(f"History after clear: {len(chatbot.get_conversation_history())}")

    # New session
    print("\nNew session - User: Tell me about Java")
    chatbot.chat("Tell me about Java")


if __name__ == "__main__":
    print("LangChain Conversational AI Chatbot - Examples")
    print("=" * 50)

    # Run examples
    try:
        example_basic_conversation()
        example_with_configuration()
        example_context_memory()
        example_history_management()
        example_clearing_memory()

        print("\n" + "=" * 50)
        print("All examples completed successfully!")
    except Exception as e:
        print(f"\nError running examples: {e}")
        print("Make sure you have:")
        print("1. Set your OPENAI_API_KEY in .env")
        print("2. Installed all requirements: pip install -r requirements.txt")

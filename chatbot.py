import os
from typing import Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()


class ConversationalChatbot:
   
    def __init__(
        self,
        model_name: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 500,
        memory_type: str = "buffer",
    ):
       
        # Initialize the language model
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        # Initialize memory based on type
        if memory_type == "summary":
            self.memory = ConversationSummaryMemory(
                llm=self.llm,
                return_messages=True,
            )
        else:
            self.memory = ConversationBufferMemory(
                return_messages=True,
            )

        # Create custom prompt template for more engaging conversation
        template = """Current conversation:
{history}

Human: {input}
Assistant:"""

        prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=template,
        )

        # Initialize the conversation chain
        self.conversation_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=prompt,
            verbose=False,
        )

    def chat(self, user_input: str) -> str:
        """Process user input and generate a response.
        
        Args:
            user_input: The user's message
            
        Returns:
            The chatbot's response
        """
        response = self.conversation_chain.invoke({"input": user_input})
        return response["response"]

    def get_conversation_history(self) -> str:
        """Get the current conversation history.
        
        Returns:
            The formatted conversation history
        """
        return self.memory.buffer

    def clear_memory(self) -> None:
        
        self.memory.clear()

    def save_history(self, filename: str) -> None:
       
        with open(filename, "w") as f:
            f.write(self.get_conversation_history())
            
def main():
    """Main function to run the chatbot in interactive mode."""
    print("=" * 60)
    print("LangChain Conversational AI Chatbot")
    print("=" * 60)
    print("\nWelcome! I'm your AI assistant. I can have conversations")
    print("with you while maintaining context and memory.")
    print("\nCommands:")
    print("  - Type your message to chat")
    print("  - Type 'history' to see conversation history")
    print("  - Type 'clear' to clear memory")
    print("  - Type 'save' to save conversation")
    print("  - Type 'quit' or 'exit' to end the chat")
    print("=" * 60 + "\n")

    # Initialize the chatbot
    chatbot = ConversationalChatbot(
        model_name=os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
        temperature=float(os.getenv("TEMPERATURE", 0.7)),
        max_tokens=int(os.getenv("MAX_TOKENS", 500)),
    )

    # Main conversation loop
    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit"]:
                print("\nThank you for chatting! Goodbye!")
                break

            if user_input.lower() == "history":
                print("\n--- Conversation History ---")
                print(chatbot.get_conversation_history())
                print("--- End of History ---\n")
                continue

            if user_input.lower() == "clear":
                chatbot.clear_memory()
                print("\nMemory cleared. Starting fresh conversation...\n")
                continue

            if user_input.lower() == "save":
                chatbot.save_history("conversation_history.txt")
                print("\nConversation saved to 'conversation_history.txt'\n")
                continue

            # Get and display the response
            response = chatbot.chat(user_input)
            print(f"\nAssistant: {response}\n")

        except KeyboardInterrupt:
            print("\n\nChat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()

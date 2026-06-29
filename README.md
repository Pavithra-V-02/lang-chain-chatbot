# LangChain Conversational AI Chatbot

A production-ready conversational AI chatbot built with **LangChain** and **OpenAI**, featuring memory management for context-aware conversations.

## Features

✨ **Key Capabilities:**
- 🧠 **Conversational Memory** - Maintains conversation history and context
- 🤖 **AI-Powered** - Uses OpenAI's GPT models for intelligent responses
- 💬 **Multi-turn Conversations** - Engages in extended, coherent discussions
- 🔧 **Configurable** - Adjustable temperature, token limits, and models
- 🌐 **Dual Interfaces** - CLI and Streamlit web interface
- 📝 **History Management** - Save and view conversation histories

## Architecture

```
┌─────────────────────────────────────────┐
│     User Input (CLI/Web Interface)      │
└────────────────┬────────────────────────┘
                 │
         ┌───────▼────────┐
         │  ConversationalAI│
         │    Chatbot      │
         └────────┬────────┘
                  │
       ┌──────────┼──────────┐
       │          │          │
   ┌───▼──┐  ┌───▼──┐  ┌───▼──┐
   │Memory│  │ LLM  │  │Chain │
   │(Hist)│  │(GPT) │  │      │
   └──────┘  └──────┘  └──────┘
       │          │          │
       └──────────┼──────────┘
                  │
        ┌─────────▼─────────┐
        │  Response Output  │
        └───────────────────┘
```

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pavithra-V-02/lang-chain-chatbot.git
   cd lang-chain-chatbot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Option 1: Command-Line Interface

Run the interactive CLI chatbot:

```bash
python chatbot.py
```

**Available commands:**
- `history` - View conversation history
- `clear` - Clear memory and start fresh
- `save` - Save conversation to file
- `quit` or `exit` - End the chat

**Example:**
```
========================================================
LangChain Conversational AI Chatbot
========================================================
You: What is machine learning?
Assistant: Machine learning is a subset of artificial intelligence...

You: Can you give me examples?
Assistant: Sure! Some common examples include...
```

### Option 2: Web Interface (Streamlit)

Run the web-based interface:

```bash
streamlit run streamlit_app.py
```

Then open `http://localhost:8501` in your browser.

**Features:**
- Visual chat interface
- Real-time configuration adjustments
- Save conversation history
- Clean, intuitive UI

## Configuration

You can configure the chatbot by editing the `.env` file or passing parameters:

```python
from chatbot import ConversationalChatbot

chatbot = ConversationalChatbot(
    model_name="gpt-4",          # Model to use
    temperature=0.7,              # Response randomness (0.0-2.0)
    max_tokens=500,               # Max response length
    memory_type="buffer"          # 'buffer' or 'summary'
)
```

## Modes of Memory

### Buffer Memory (Default)
- Stores complete conversation history
- Best for shorter conversations
- Preserves full context

### Summary Memory
- Progressively summarizes conversation
- Better for long conversations
- More token-efficient

## API Reference

### ConversationalChatbot Class

```python
class ConversationalChatbot:
    def __init__(model_name, temperature, max_tokens, memory_type)
    def chat(user_input: str) -> str
    def get_conversation_history() -> str
    def clear_memory() -> None
    def save_history(filename: str) -> None
```

### Example Usage

```python
from chatbot import ConversationalChatbot

# Initialize chatbot
chatbot = ConversationalChatbot()

# Have a conversation
response = chatbot.chat("What is AI?")
print(response)

# Get history
history = chatbot.get_conversation_history()

# Save conversation
chatbot.save_history("my_conversation.txt")

# Clear for new session
chatbot.clear_memory()
```

## Project Structure

```
lang-chain-chatbot/
├── chatbot.py              # Core chatbot implementation
├── streamlit_app.py        # Web interface
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── README.md              # This file
└── conversation_history.txt  # Saved conversations (generated)
```

## Dependencies

- **langchain** - LLM framework
- **langchain-community** - Community integrations
- **langchain-openai** - OpenAI integration
- **python-dotenv** - Environment variable management
- **streamlit** - Web UI framework

## References

- [LangChain Documentation](https://docs.langchain.com/oss/python/langchain/overview)
- [LangChain Memory](https://python.langchain.com/docs/modules/memory/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

## Error Handling

Common issues and solutions:

| Issue | Solution |
|-------|----------|
| `OpenAI API Key Error` | Verify OPENAI_API_KEY in .env |
| `Rate Limit Error` | Wait a moment and retry |
| `Token Limit Exceeded` | Reduce MAX_TOKENS in .env |
| `Memory Issues` | Use 'summary' memory type for long conversations |

## Performance Tips

- 🚀 Use `gpt-3.5-turbo` for faster, cheaper responses
- 💰 Use `gpt-4` for more sophisticated reasoning
- 🧠 Switch to summary memory for conversations > 50 turns
- ⚡ Lower temperature for consistent, focused responses
- 📊 Monitor token usage to manage costs

## Future Enhancements

- [ ] Vector database integration for semantic memory
- [ ] Multi-user support with session management
- [ ] Conversation analysis and insights
- [ ] Custom system prompts
- [ ] Integration with external tools/APIs
- [ ] Voice input/output support
- [ ] RAG (Retrieval Augmented Generation) capabilities

## License

MIT License - Feel free to use this project for learning and development.

## Support

For issues, questions, or suggestions:
1. Check the [FAQ](#faq) section
2. Review [LangChain Documentation](https://docs.langchain.com/)
3. Open an issue on GitHub

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Made with ❤️ for AI Engineering enthusiasts**

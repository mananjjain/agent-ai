# 🎙️ Friday - AI Voice Assistant

Friday is a voice-controlled AI assistant built with Python, LangChain, Ollama, and Qwen3. It listens for a wake word, understands voice commands, and responds using speech synthesis. The assistant can search the web, solve mathematical problems, provide current news updates, and retrieve stock market information using real-time data sources.

The project demonstrates how modern AI frameworks, local language models, and voice technologies can be combined to create a powerful and customizable personal assistant that runs locally on your computer.

## ✨ Features

* 🎤 Wake word activation ("Friday")
* 🗣️ Speech-to-text command recognition
* 🔊 Text-to-speech responses
* 🤖 Local AI model powered by Ollama and Qwen3
* 🔎 Web search using DuckDuckGo
* 🧮 Mathematical calculations
* 📰 Current news and date information
* 📈 Stock market data with Yahoo Finance
* 🔧 LangChain tool-calling agent
* 💻 Fully customizable and extensible

## 🛠️ Tech Stack

* Python
* LangChain
* Ollama
* Qwen3:8B
* SpeechRecognition
* pyttsx3
* DuckDuckGo Search
* Yahoo Finance (yfinance)
* python-dotenv

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/mananjjain/friday-ai-assistant.git
cd friday-ai-assistant
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install langchain
pip install langchain-community
pip install langchain-classic
pip install langchain-ollama
pip install langchain-experimental
pip install speechrecognition
pip install pyttsx3
pip install yfinance
pip install python-dotenv
pip install duckduckgo-search
pip install pyaudio
```

## 🤖 Ollama Setup

Install Ollama and download the Qwen3 model:

```bash
ollama pull qwen3:8b
```

Verify installation:

```bash
ollama list
```

Start Ollama:

```bash
ollama serve
```

## ▶️ Running the Assistant

Run the application:

```bash
python main.py
```

Say the wake word:

```text
Friday
```

Then ask questions such as:

```text
What is the latest news today?
```

```text
Calculate 125 * 45
```

```text
What is the stock price of RELIANCE.NS?
```

```text
Who is the CEO of Tesla?
```

To exit:

```text
exit
```

## 📂 Project Structure

```text
friday-ai-assistant/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## 🔧 Available Tools

### Time Tool

Provides:

* Current date
* Latest news headlines

### Calculator Tool

Provides:

* Arithmetic calculations
* Mathematical expression evaluation

### Search Tool

Provides:

* General web search
* Information lookup

### Stock Tool

Provides:

* Stock prices
* Market information
* Yahoo Finance data

## 🔮 Future Improvements

* Email automation
* Weather updates
* Calendar integration
* Reminders and scheduling
* Conversational memory
* Multi-language support
* GUI dashboard
* Smart home integration
* WhatsApp and Telegram support

## 📖 How It Works

1. The assistant waits for the wake word **"Friday"**.
2. After activation, it listens for voice commands.
3. LangChain analyzes the request and selects the appropriate tool.
4. The selected tool performs the task.
5. The AI generates a response.
6. Friday speaks the result back to the user.

## 👨‍💻 Author

**Manan Jain**

GitHub: https://github.com/mananjjain

---

⭐ If you found this project useful, consider giving the repository a star and contributing to future improvements.

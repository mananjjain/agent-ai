from datetime import date
import os
from dotenv import load_dotenv
import pyttsx3
import speech_recognition as sr
import streamlit as st  # Re-added the missing streamlit import
import yfinance as yf

# Fixed modern import paths (replacing deprecated langchain_classic namespaces)
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

# Set up page styling immediately before any other rendering
st.set_page_config(page_title="FRIDAY Terminal", page_icon="🤖", layout="wide")

# Custom injection for a modern sci-fi dark theme with smooth fade-in animations
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    /* Main container styling */
    .reportview-container, .main {
        background-color: #05050a;
        font-family: 'Share Tech Mono', monospace;
    }
    
    /* Sleek card style */
    .metric-card {
        background: rgba(16, 185, 129, 0.03);
        border: 1px solid rgba(16, 185, 129, 0.2);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
        transition: all 0.3s ease-in-out;
    }
    .metric-card:hover {
        border-color: rgba(16, 185, 129, 0.5);
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.1);
    }
    
    /* Glowing status indicator animations */
    .status-glow {
        display: inline-block;
        width: 12px;
        height: 12px;
        background-color: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 10px #10b981;
        animation: pulse 2s infinite;
        margin-right: 8px;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }
    
    /* Chat stream container formatting */
    .terminal-output {
        background-color: #000000;
        border-left: 3px solid #6366f1;
        padding: 15px;
        border-radius: 4px;
        font-family: monospace;
        margin-bottom: 10px;
        animation: fadeIn 0.5s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App structural header
st.markdown(
    '<div style="text-align: center; padding: 20px;"><h1 style="color: white; margin-bottom: 0px; letter-spacing: 2px;">FRIDAY // COGNITIVE CORE</h1><p style="color: #6366f1; font-size: 14px;">AGENT ARCHITECTURE MATRIX</p></div>',
    unsafe_allow_html=True,
)

# Initialize Session State values to persist logs across script cycles
if "messages" not in st.session_state:
    st.session_state.messages = []
if "status" not in st.session_state:
    st.session_state.status = "Awaiting Activation..."

# Load environmental variables
load_dotenv()


@st.cache_resource
def init_agent():
    llm = ChatOllama(model="qwen3:8b", temperature=0)
    s = DuckDuckGoSearchRun()

    @tool
    def time(text: str) -> str:
        """Returns the current date and modern web headlines."""
        c = str(date.today())
        k = s.run(f"latest news of {c}")
        return f"date {c}, news={k}"

    @tool
    def calculator(expression: str) -> str:
        """Calculates algorithmic and classic arithmetic equations."""
        return str(eval(expression))

    @tool
    def stock(text: str) -> str:
        """Fetches modern stock ticks and historical pricing maps."""
        st_ticker = yf.Tickers(text)
        return str(st_ticker.news)

    prompt1 = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are Friday, an enterprise cognitive agent cluster. Always use appropriate tools when needed.",
            ),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    tools = [time, calculator, stock]
    call = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt1)
    return AgentExecutor(agent=call, tools=tools, verbose=True)


ag = init_agent()


# Text-to-speech configuration helper function
def speak(text):
    try:
        e = pyttsx3.init()
        e.say(text)
        e.runAndWait()
    except Exception:
        pass  # Safeguard against sound architecture lockups on web servers


# Grid Dashboard Layout
col1, col2 = st.columns([4, 8])

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown("### 📡 Diagnostics Perimeter")
    st.markdown(
        f'<p><span class="status-glow"></span>System Monitor: <strong style="color: #10b981;">{st.session_state.status}</strong></p>',
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown("**Core Architecture Parameters:**")
    st.info(
        "• Wake keyword: **'friday'**\n• Exit instruction keyword: **'exit'**\n• Processing Unit: **Ollama qwen3:8b**"
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Manual Input Override block
    st.markdown("<br>", unsafe_allow_html=True)
    manual_input = st.text_input("⌨️ Terminal Prompt Override:")
    if manual_input:
        st.session_state.status = "Executing Query Engine..."
        st.session_state.messages.append({"role": "User", "text": manual_input})
        with st.spinner("Processing framework algorithms..."):
            rg = ag.invoke({"input": manual_input})
            output_text = rg["output"]
            st.session_state.messages.append({"role": "Friday", "text": output_text})
        st.session_state.status = "System Idle"
        speak(output_text)
        st.rerun()

with col2:
    st.markdown(
        '<h3 style="color: white; margin-top:0;">📜 Live System Pipeline Feed</h3>',
        unsafe_allow_html=True,
    )

    # Render modern rolling transcript feeds
    chat_container = st.container()
    with chat_container:
        if not st.session_state.messages:
            st.markdown(
                '<p style="color: #4b5563; font-style: italic;">No stream communication entries located inside pipeline memory logs.</p>',
                unsafe_allow_html=True,
            )
        for msg in st.session_state.messages:
            role_color = "#6366f1" if msg["role"] == "User" else "#10b981"
            st.markdown(
                f"""
                <div class="terminal-output">
                    <span style="color: {role_color}; font-weight: bold;">[{msg["role"].upper()}]</span> {msg["text"]}
                </div>
            """,
                unsafe_allow_html=True,
            )

    # Core system Voice Audio Processing Loop Execution Trigger
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎤 Wake Audio Pipeline Engine", use_container_width=True):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.session_state.status = "Syncing Ambient Calibration Noise Levels..."
            r.adjust_for_ambient_noise(source, duration=1)

            st.write("🌌 *Awaiting keyword wake state ('Friday')...*")
            try:
                w = r.listen(source, timeout=8, phrase_time_limit=4)
                wa = r.recognize_google(w).lower()

                if "friday" in wa:
                    st.session_state.status = "Active Session Link Established"
                    speak("hi manan")
                    st.session_state.messages.append(
                        {
                            "role": "Friday",
                            "text": "Hi Manan. Active microphone matrix monitoring pipeline initiated.",
                        }
                    )

                    # Conversational listening sub-processing channel
                    with sr.Microphone() as sub_source:
                        st.write("🟢 *Listening for query...*")
                        a = r.listen(sub_source, timeout=10, phrase_time_limit=10)
                        t = r.recognize_google(a)
                        speak("ok I will work  on that for you ")
                        while True:
                            if t.lower() != "exit":
                                st.session_state.messages.append(
                                    {"role": "User", "text": t}
                                )

                            rg = ag.invoke({"input": t})
                            output_text = rg["output"]
                            st.session_state.messages.append(
                                {"role": "Friday", "text": output_text}
                            )
                            speak(output_text)
                            print(output_text)
                        else:
                            st.session_state.status = (
                                "Session Connection Safely Severed"
                            )
                            st.session_state.messages.append(
                                {
                                    "role": "Friday",
                                    "text": "Terminal loop exited successfully.",
                                }
                            )

            except sr.WaitTimeoutError:
                st.session_state.status = "Wake Sequence Connection Timeout"
            except sr.UnknownValueError:
                st.session_state.status = (
                    "Failed to transcribe audio signal stream properly"
                )
            except Exception as e:
                st.session_state.status = f"System Exception error logged: {str(e)}"

            # Final interface state synchronized rerun
            st.rerun()

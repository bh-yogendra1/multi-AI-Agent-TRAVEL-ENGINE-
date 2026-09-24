# 🌍 AI Travel Planning System using LangGraph

A Real-World Multi-Agent AI Travel Planning System built using **LangGraph**, **LangChain**, **Groq LLMs**, **PostgreSQL Memory**, and **Real-Time APIs**.

This project demonstrates how multiple AI agents can collaborate to automatically generate a complete travel plan including flight information, hotel recommendations, itinerary generation, and final trip planning.

The system follows an **Agentic AI Architecture**, where specialized agents work together to solve a complex travel-planning task.

---

# 🚀 Project Highlights

* Multi-Agent AI Architecture using LangGraph
* Flight Search Agent
* Hotel Search Agent
* Itinerary Planning Agent
* Final Response Agent
* PostgreSQL-based Conversation Memory
* Real-Time Web Search using Tavily
* Flight Data Integration using AviationStack
* Streamlit Interactive Web Interface
* Modular and Scalable Design
* Suitable for Agentic AI and LangGraph Learning

---

# 🧠 System Architecture

The travel planning process is executed through multiple AI agents.

```text
User Query
    │
    ▼
✈️ Flight Agent
    │
    ▼
🏨 Hotel Agent
    │
    ▼
🗓️ Itinerary Agent
    │
    ▼
🤖 Final Response Agent
    │
    ▼
💾 PostgreSQL Memory
```

Each agent performs a dedicated task and passes its output to the next agent in the workflow.

---

# ✨ Features

## ✈️ Flight Search Agent

Responsible for:

* Searching available flights
* Fetching flight information
* Identifying routes and travel options
* Using AviationStack API

---

## 🏨 Hotel Search Agent

Responsible for:

* Searching hotels near destination
* Finding accommodation options
* Retrieving travel-related information

---

## 🗓️ Itinerary Planning Agent

Responsible for:

* Creating day-wise travel plans
* Suggesting attractions and activities
* Optimizing sightseeing schedules

---

## 🤖 Final Response Agent

Responsible for:

* Combining outputs from all agents
* Generating a structured travel plan
* Producing the final response for the user

---

## 💾 PostgreSQL Memory

The system stores conversation history and context using PostgreSQL.

Benefits:

* Persistent memory
* Context retention
* Multi-session support
* Better user experience

---

# 🛠 Technology Stack

| Component              | Technology                 |
| ---------------------- | -------------------------- |
| Agent Framework        | LangGraph                  |
| LLM Framework          | LangChain                  |
| Large Language Model   | Qwen 3.8 27B               |
| LLM Provider           | Groq                       |
| Memory Database        | PostgreSQL                 |
| Frontend               | Streamlit                  |
| Web Search             | Tavily API                 |
| Flight Search          | AviationStack API          |
| Environment Management | Python Virtual Environment |

---

# 📂 Project Structure

```text
AI-Travel-Planner/
│
├── frontend.py
├── main.py
├── graph.py
│
├── agents/
│   ├── flight_agent.py
│   ├── hotel_agent.py
│   ├── itinerary_agent.py
│   └── final_agent.py
│
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Prerequisites

Before running the project, ensure the following are installed:

* Python 3.10 or higher
* PostgreSQL 14+
* Groq API Key
* Tavily API Key
* AviationStack API Key

---

# 🧪 Step 1: Create Python Environment

Open a terminal inside the project directory.

```bash
python -m venv langgraph_env3
```

Activate the environment.

### Windows

```bash
langgraph_env3\Scripts\activate
```

### Linux / macOS

```bash
source langgraph_env3/bin/activate
```

---

# 📦 Step 2: Install Dependencies

Install required packages:

```bash
pip install langgraph langchain langchain-openai langchain-groq langchain-community langchain-tavily psycopg[binary] psycopg_pool python-dotenv tavily-python requests streamlit
```

Install PostgreSQL checkpoint support:

```bash
pip install -U "psycopg[binary,pool]" langgraph-checkpoint-postgres
```

---

# 🐘 Step 3: Install PostgreSQL

Download PostgreSQL:

https://www.postgresql.org/download/

While installing PostgreSQL, remember:

* PostgreSQL Username
* PostgreSQL Password
* PostgreSQL Port Number

You will need these values when configuring the database connection.

---

# 🗄️ Step 4: Create Database

Open PostgreSQL and execute:

```sql
CREATE DATABASE langgraph_memory_demo;
```

---

# 🔐 Step 5: Configure Environment Variables

Create a file named:

```text
.env
```

Add the following values:

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

AVIATIONSTACK_API_KEY=your_aviationstack_api_key

DATABASE_URL=postgresql://postgres:your_password@localhost:5432/langgraph_memory_demo
```

---

# 🔑 Step 6: Obtain API Keys

## Groq API

Create an account and obtain an API key:

https://console.groq.com

---

## Tavily API

Create an account and obtain an API key:

https://tavily.com

---

## AviationStack API

Create an account and obtain an API key:

https://aviationstack.com

---

# ▶️ Step 7: Run the Application

## Run the Multi-Agent System

```bash
python main.py
```

This will execute the LangGraph workflow in the terminal.

---

## Run the Streamlit Web Application

```bash
streamlit run frontend.py
```

This will launch the web interface in your browser.

---

# 💡 Example Prompt

```text
Plan a complete 7-day Japan trip including flights, hotels, sightseeing, and budget optimization under ₹2 lakhs.
```

---

# 🔄 Workflow Execution

### Step 1

Flight Agent searches flight options.

### Step 2

Hotel Agent searches accommodation options.

### Step 3

Itinerary Agent creates a detailed travel schedule.

### Step 4

Final Response Agent combines all outputs.

### Step 5

Conversation data is stored in PostgreSQL memory.

---

# 📈 Future Enhancements

Planned upgrades include:

* Voice-Based Travel Planning
* Interactive Travel Maps
* Flight Price Prediction
* Multi-Currency Support
* Real-Time Hotel Booking APIs
* Travel Cost Analytics Dashboard
* Agentic Workflow Visualization
* Personalized Travel Recommendations
* Advanced Memory and User Profiles

---

# 👨‍💻 Author

## Yogendra Bharadwaj

**M.Tech Artificial Intelligence**
**Indian Institute of Technology Patna**

Research Interests:

* Agentic AI
* Generative AI
* Multi-Agent Systems
* Retrieval-Augmented Generation (RAG)
* AI-Powered Intelligent Applications

GitHub:

https://github.com/bh-yogendra1

---

# 📜 License

This project is intended for educational, research, and learning purposes.

---

# 🙏 Acknowledgements

* LangGraph
* LangChain
* Groq
* Tavily
* AviationStack
* PostgreSQL
* Streamlit

for providing the tools and technologies used in this project.


<img width="1915" height="927" alt="Screenshot 2026-09-24 142147" src="https://github.com/user-attachments/assets/d32720f3-6459-42a5-b16d-291a54f60654" />

<img width="1535" height="715" alt="Screenshot 2026-09-24 142912" src="https://github.com/user-attachments/assets/283016a7-c143-4ce4-8f54-23964e5c59b5" />

<img width="1561" height="900" alt="Screenshot 2026-09-24 142840" src="https://github.com/user-attachments/assets/af92f718-9f11-463b-a985-fb5f88de5d9f" />

<img width="1486" height="931" alt="Screenshot 2026-09-24 142851" src="https://github.com/user-attachments/assets/d340ecf5-c8c2-4848-a1f0-d071e74b5b55" />

<img width="1535" height="715" alt="Screenshot 2026-09-24 142912" src="https://github.com/user-attachments/assets/e86bbbf4-536f-49e8-8c3f-76078739a194" />






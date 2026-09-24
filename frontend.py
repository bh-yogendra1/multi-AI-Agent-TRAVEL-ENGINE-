import os
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from langchain_core.messages import HumanMessage
from main import app

# ── 1. Page Configuration ───────────────────────────────────────────────────
st.set_page_config(
    page_title="AURORA NEON | Interactive AI Travel Engine",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── 2. High-Tech Animated CSS & Text Input Fixes ─────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background: #030712;
    color: #f3f4f6;
}

/* ── Glowing Animated Cards ── */
@keyframes pulseGlow {
    0% { box-shadow: 0 0 15px rgba(0, 242, 254, 0.2); }
    50% { box-shadow: 0 0 30px rgba(0, 242, 254, 0.5); }
    100% { box-shadow: 0 0 15px rgba(0, 242, 254, 0.2); }
}

.hero-box {
    text-align: center;
    padding: 2.5rem 1.5rem;
    background: rgba(17, 24, 39, 0.6);
    border: 1px solid rgba(0, 242, 254, 0.3);
    border-radius: 24px;
    backdrop-filter: blur(16px);
    margin-bottom: 2rem;
    animation: pulseGlow 4s infinite ease-in-out;
}
.hero-badge {
    background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
    color: #030712 !important;
    font-weight: 800;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    padding: 0.4rem 1.2rem;
    border-radius: 50px;
    display: inline-block;
    margin-bottom: 1rem;
}
.hero-title {
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 30%, #00f2fe 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}

/* ── STEXTAREA & TEXTINPUT FIX (Text Na Dikhne Ka Solution) ── */
.stTextArea textarea, .stTextInput input {
    background-color: #0b1329 !important;
    color: #00ffcc !important; /* High contrast text */
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.05rem !important;
    border: 1px solid #1e3a8a !important;
    border-radius: 12px !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: #00f2fe !important;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.4) !important;
    color: #ffffff !important;
}
.stTextArea textarea::placeholder, .stTextInput input::placeholder {
    color: #6b7280 !important;
}
label, .stTextArea label, .stTextInput label {
    color: #00f2fe !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
}

/* ── Architecture Nodes ── */
.node-card {
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(0, 242, 254, 0.2);
    border-radius: 16px;
    padding: 1rem;
    text-align: center;
    transition: all 0.3s ease;
}
.node-card:hover {
    transform: translateY(-5px);
    border-color: #00f2fe;
    box-shadow: 0 10px 25px rgba(0, 242, 254, 0.3);
}

/* ── Primary Action Button ── */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #00f2fe 0%, #3b82f6 50%, #8b5cf6 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 1rem 2.5rem !important;
    font-size: 1.1rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.05em !important;
    width: 100% !important;
    box-shadow: 0 10px 30px rgba(0, 242, 254, 0.35) !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stButton"] > button:hover {
    box-shadow: 0 15px 45px rgba(0, 242, 254, 0.6) !important;
    transform: translateY(-2px) !important;
}

/* ── Output Box ── */
.plan-card {
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(0, 242, 254, 0.3);
    border-left: 5px solid #00f2fe;
    border-radius: 20px;
    padding: 2rem;
    line-height: 1.8;
    color: #e2e8f0;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
}

/* Custom Tabs Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    background-color: rgba(15, 23, 42, 0.8);
    padding: 8px;
    border-radius: 18px;
    border: 1px solid rgba(0, 242, 254, 0.2);
}
.stTabs [data-baseweb="tab"] {
    height: 50px;
    border-radius: 14px;
    color: #94a3b8;
    font-weight: 600;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #00f2fe 0%, #3b82f6 100%) !important;
    color: #ffffff !important;
    font-weight: 800 !important;
}

section[data-testid="stSidebar"] {
    background: #020617 !important;
    border-right: 1px solid rgba(0, 242, 254, 0.15) !important;
}

#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── 3. Sidebar Architecture Visualization ────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚡ System Architecture & Connections")
    st.markdown("---")

    thread_id = st.text_input("👤 Session User ID", value="yogendra Bharadwaj")

    st.markdown("#### 🔗 Connected Infrastructure")
    st.markdown("""
    * 🧠 **LLM Engine**: Groq (qwen3.8-27b)
    * 🔗 **Orchestrator**: LangGraph Checkpointer
    * 🐘 **State Store**: PostgreSQL DB
    * 🔍 **Search Tool**: Tavily Web API
    * ✈️ **Data Tool**: AviationStack / Flight API
    """)

    st.markdown("---")
    st.markdown("#### ⚙️ Trip Preferences")
    travel_mode = st.selectbox("Travel Class", ["Luxury Elite", "Balanced", "Backpacker"])
    currency = st.selectbox("Currency", ["INR (₹)", "USD ($)", "EUR (€)"])
    budget_range = st.slider("Max Budget Limit", 20000, 1000000, 200000, 10000)

# ── 4. Main Hero Banner ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero-box">
    <div class="hero-badge">✦ MULTI-AGENT AUTONOMOUS SYSTEM ✦</div>
    <div class="hero-title">AURORA NEON TRAVEL ENGINE</div>
    <p style="color: #94a3b8; font-size: 1.1rem; margin-top: 0.5rem;">
        Multi-AI agent pipeline rendering live flights, hotels, itineraries, and workflow analytics.
    </p>
</div>
""", unsafe_allow_html=True)

# ── 5. Interactive Rotating 3D Globe Component ─────────────────────────────
globe_html = """
<div style="text-align: center; background: transparent;">
    <canvas id="globeCanvas" width="320" height="320" style="cursor: grab;"></canvas>
</div>
<script>
    const canvas = document.getElementById('globeCanvas');
    const ctx = canvas.getContext('2d');
    let width = canvas.width;
    let height = canvas.height;
    let radius = 120;
    let rotation = 0;

    function drawGlobe() {
        ctx.clearRect(0, 0, width, height);
        
        // Glow gradient
        let grad = ctx.createRadialGradient(width/2, height/2, radius*0.8, width/2, height/2, radius*1.2);
        grad.addColorStop(0, 'rgba(0, 242, 254, 0.15)');
        grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(width/2, height/2, radius*1.2, 0, Math.PI*2);
        ctx.fill();

        // Wireframe Sphere
        ctx.strokeStyle = '#00f2fe';
        ctx.lineWidth = 1;
        
        for (let lat = -80; lat <= 80; lat += 20) {
            ctx.beginPath();
            let r = radius * Math.cos(lat * Math.PI / 180);
            let y = height/2 + radius * Math.sin(lat * Math.PI / 180);
            ctx.ellipse(width/2, y, r, r * 0.3, 0, 0, Math.PI * 2);
            ctx.stroke();
        }

        for (let lon = 0; lon < 360; lon += 30) {
            ctx.beginPath();
            let angle = (lon + rotation) * Math.PI / 180;
            let x1 = width/2 + radius * Math.cos(angle);
            let y1 = height/2 + radius * Math.sin(angle);
            ctx.arc(width/2, height/2, radius, angle, angle + Math.PI/6);
            ctx.strokeStyle = 'rgba(0, 242, 254, 0.4)';
            ctx.stroke();
        }

        rotation += 0.8;
        requestAnimationFrame(drawGlobe);
    }
    drawGlobe();
</script>
"""

col_g1, col_g2 = st.columns([1, 2])
with col_g1:
    components.html(globe_html, height=330)
with col_g2:
    st.markdown("### 🔄 Live Agent Workflow Pipeline")
    
    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 15px;">
        <div class="node-card">
            <h4 style="color: #00f2fe; margin: 0;">① Flight Agent</h4>
            <p style="font-size: 0.8rem; color: #94a3b8; margin: 5px 0 0;">Queries AviationStack & Tavily APIs</p>
        </div>
        <div class="node-card">
            <h4 style="color: #3b82f6; margin: 0;">② Hotel Agent</h4>
            <p style="font-size: 0.8rem; color: #94a3b8; margin: 5px 0 0;">Filters stays within budget limit</p>
        </div>
        <div class="node-card">
            <h4 style="color: #8b5cf6; margin: 0;">③ Itinerary Agent</h4>
            <p style="font-size: 0.8rem; color: #94a3b8; margin: 5px 0 0;">Builds hour-by-hour daily schedule</p>
        </div>
        <div class="node-card">
            <h4 style="color: #ec4899; margin: 0;">④ Finalizer Agent</h4>
            <p style="font-size: 0.8rem; color: #94a3b8; margin: 5px 0 0;">Synthesizes output & persists to Postgres</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── 6. Trip Input Area (Text Visibility Fixed) ──────────────────────────────
st.markdown("##### 📍 Enter Travel Query:")

user_query = st.text_area(
    "Query Area",
    value="",
    placeholder="e.g. Plan a 5-day trip to Tokyo under ₹1,50,000 including flights, hotel, and sightseeing.",
    height=100,
    label_visibility="collapsed"
)

generate_btn = st.button("⚡ LAUNCH MULTI-AGENT EXECUTION")

# ── 7. Multi-Agent Stream Execution & Results ────────────────────────────────
if generate_btn:
    if not user_query.strip():
        st.warning("⚠️ Please type your destination details above.")
    else:
        full_query = f"{user_query} | Class: {travel_mode} | Budget Limit: {currency} {budget_range:,}"
        config = {"configurable": {"thread_id": thread_id}}

        results = {
            "flight_results": "",
            "hotel_results": "",
            "itinerary": "",
            "final_response": "",
            "llm_calls": 0
        }

        st.markdown("---")
        st.markdown("### 🤖 Pipeline Execution Tracker")
        progress_bar = st.progress(0)
        status_box = st.empty()

        step = 0
        for chunk in app.stream(
            {
                "messages": [HumanMessage(content=full_query)],
                "user_query": full_query,
                "flight_results": "",
                "hotel_results": "",
                "itinerary": "",
                "llm_calls": 0,
            },
            config=config,
            stream_mode="updates",
        ):
            for node_name, state_update in chunk.items():
                step += 1
                progress_bar.progress(step * 25)
                status_box.info(f"⚡ Currently Executing Node: `{node_name}`")

                if node_name == "flight_agent":
                    results["flight_results"] = state_update.get("flight_results", "")
                elif node_name == "hotel_agent":
                    results["hotel_results"] = state_update.get("hotel_results", "")
                elif node_name == "itinerary_agent":
                    results["itinerary"] = state_update.get("itinerary", "")
                elif node_name == "final_agent":
                    msgs = state_update.get("messages", [])
                    results["final_response"] = msgs[-1].content if msgs else ""

                results["llm_calls"] = state_update.get("llm_calls", results["llm_calls"])

        status_box.success("✅ Multi-Agent Orchestration Completed!")

        # Detailed Output Display Tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "🧠 Master Synthesis", 
            "✈️ Live Flights Data", 
            "🏨 Hotel Options", 
            "🗓️ Day-Wise Itinerary"
        ])

        with tab1:
            st.markdown("#### Complete Travel Package Proposal")
            st.markdown(f"<div class='plan-card'>{results['final_response']}</div>", unsafe_allow_html=True)

        with tab2:
            st.markdown("#### Flight Search Output")
            st.markdown(results["flight_results"] or "_No flight data found._")

        with tab3:
            st.markdown("#### Hotel Search Output")
            st.markdown(results["hotel_results"] or "_No hotel data found._")

        with tab4:
            st.markdown("#### Schedule Breakdown")
            st.markdown(results["itinerary"] or "_No itinerary generated._")

        # Save Markdown File
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"aurora_neon_plan_{timestamp}.md"
        save_dir = os.path.join(os.path.dirname(__file__), "travel_plans")
        os.makedirs(save_dir, exist_ok=True)

        file_content = f"""# AURORA NEON Travel Plan
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**User ID:** {thread_id}
**Query:** {full_query}

---
## 🧠 Final Response
{results['final_response']}

---
## ✈️ Flights
{results['flight_results']}

---
## 🏨 Hotels
{results['hotel_results']}

---
## 🗓️ Itinerary
{results['itinerary']}
"""
        with open(os.path.join(save_dir, filename), "w", encoding="utf-8") as f:
            f.write(file_content)

        st.markdown("---")
        d_col1, d_col2 = st.columns([1, 3])
        with d_col1:
            st.download_button(
                label="⬇️ Download Markdown Plan",
                data=file_content,
                file_name=filename,
                mime="text/markdown",
                use_container_width=True
            )
        with d_col2:
            st.info(f"📁 Auto-saved session output to `travel_plans/{filename}`")
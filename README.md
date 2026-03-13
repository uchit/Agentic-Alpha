
# Agentic Alpha – Production Demo

This project demonstrates a multi‑agent trading analysis system with:

• Market Analyst Agent (Fibonacci analysis)  
• Strategy Agent (market data)  
• Trading Signal Agent (enum‑typed output)  
• Regulatory Agent (audit compliance checks)  

All agents share symbol state and return structured results.

---

# Folder Structure

app/
  agents/
  tools/
  models/
  data/
  main.py

---

# Setup

1. Create virtual environment

python -m venv venv

2. Activate

Mac/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

---

# Run Application

streamlit run app/main.py

---

# What the UI Shows

Sidebar buttons:

Market Analyst Agent
Strategy Agent
Trading Signal Agent
Regulatory Agent

Each agent runs on the selected ticker symbol and returns validated results.

---

# Rubric Evidence

Requirement | Location
Fibonacci Tool | tools/pydantic_market_tools.py
Market Data Tool | tools/pydantic_market_tools.py
Enum Typed Agent | agents/pydantic_agents.py
TradingDecision Model | models/trading_models.py
Sidebar Integration | main.py
Symbol State Management | main.py (session_state)
Regulatory Audit Output | agents/regulatory_agent.py


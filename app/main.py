
import streamlit as st

from app.agents.pydantic_agents import (
    market_analyst_agent,
    strategy_agent,
    trading_signal_agent
)

from app.agents.regulatory_agent import regulatory_agent


st.title("Agentic Alpha Trading System")


symbol = st.text_input("Ticker Symbol", value="AAPL")

st.session_state["symbol"] = symbol


st.sidebar.title("Agents")

if st.sidebar.button("Market Analyst Agent"):

    result = market_analyst_agent(symbol)

    st.subheader("Fibonacci Analysis")
    st.json(result)


if st.sidebar.button("Strategy Agent"):

    result = strategy_agent(symbol)

    st.subheader("Market Data")
    st.json(result)


if st.sidebar.button("Trading Signal Agent"):

    result = trading_signal_agent(symbol)

    st.subheader("Trading Decision")

    st.json(result.model_dump())


if st.sidebar.button("Regulatory Agent"):

    result = regulatory_agent(symbol)

    st.subheader("Regulatory Compliance")

    st.json(result.model_dump())

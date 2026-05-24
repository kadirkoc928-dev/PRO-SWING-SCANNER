import streamlit as st
from scanner import scan_market
import pandas as pd

st.set_page_config(page_title="PRO Swing Scanner", layout="wide")

st.title("📊 PRO Swing Trading Scanner")

min_score = st.slider("Minimum Swing Score", 0, 100, 60)

limit = st.slider("Universe Size", 50, 500, 200)

if st.button("🚀 RUN SCAN"):

    with st.spinner("Scanning market..."):
        results = scan_market(limit)

    df = pd.DataFrame(results)
    df = df[df["score"] >= min_score]

    st.success(f"{len(df)} Swing Candidates Found")

    st.dataframe(df, use_container_width=True)

    st.bar_chart(df.set_index("symbol"))

    st.markdown("## 📈 Top Pick Chart")

    if len(df) > 0:
        symbol = df.iloc[0]["symbol"]

        st.components.v1.html(f"""
        <iframe
            src="https://s.tradingview.com/widgetembed/?symbol={symbol}&interval=D"
            width="100%"
            height="500">
        </iframe>
        """, height=500)

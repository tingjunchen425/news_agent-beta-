import streamlit as st
from NEWS_agnet import news_agent
import time

agent = news_agent()
st.title("news today")
if st.button("產生今日新聞"):
    status = st.empty()
    status.write("正在收集新聞...")
    agent.search()
    status.write("正在撰寫...")
    agent.write()
    status.success("新聞已生成！")
    with open("news.md", "r", encoding="utf-8") as f:
        content = f.read()
    st.markdown(content)


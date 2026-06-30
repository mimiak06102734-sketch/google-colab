import streamlit as st
import pandas as pd

st.title("インターン管理システム")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["企業名","選考状況","志望度"]
    )

company = st.text_input("企業名")

status = st.selectbox(
    "選考状況",
    ["未応募","ES提出","WEBテスト","面接","結果待ち"]
)

motivation = st.slider("志望度",1,5,3)

if st.button("追加"):
    new_row = pd.DataFrame(
        [[company,status,motivation]],
        columns=["企業名","選考状況","志望度"]
    )

    st.session_state.data = pd.concat(
        [st.session_state.data,new_row],
        ignore_index=True
    )

st.subheader("応募企業一覧")
st.dataframe(st.session_state.data)

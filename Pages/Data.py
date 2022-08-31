import pandas as pd
import streamlit as st
import sys
sys.path.append("../")
import app #app.pyをimport

st.title("Your Record")
df = pd.read_csv("~/Practice/python/musle/record.csv")
st.dataframe(df)
#例外処理(DataFrameが空の場合)
try:
    #st.dataframe(df)
    if len(df) > 0:
        btn_reload = st.button("Reload")
        btn_delete = st.button("Delete")
        #st.text("最後の記録が削除されます")
        if btn_reload:
            #st.dataframe(df)
            st.text("")
        if btn_delete:
            df = df.drop(df.index[-1])
            st.header("変更後")
            df.to_csv("~/Practice/python/musle/record.csv", index=False)
            if len(df) > -1:
                st.dataframe(df)    
except pd.errors.EmptyDataError or NameError:
    st.header("Your Record is not exist")


#
#数字入力ボタンを作り、入力された数字の行を削除する機能

#st.dataframe(df)
#if len(df) == 1:
#    df = pd.DataFrame()
#    df.to_csv("~/Practice/python/musle/record.csv", index=False)
#    st.dataframe(df)

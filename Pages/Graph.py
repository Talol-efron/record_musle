import streamlit as st
import pandas as pd
import matplotlib as plt

df = pd.read_csv("~/Practice/python/musle/record.csv")
#Graph描画がむずい.matplotlibが有望
#matplotlibを使うにはst.pylot()が必要
df_columns = df.columns
st.markdown("#### 入力データ")
st.dataframe(df.style.highlight_max(axis=0))
#matplotlibで可視化。X軸,Y軸を選択できる
st.markdown("### 可視化 単変量")
#データフレームのカラムを選択オプションに設定する
x = st.selectbox("X軸", df_columns)
y = st.selectbox("Y軸", df_columns)
#選択した変数を用いてmtplotlibで可視化
fig = plt.figure(figsize= (12,8))
plt.scatter(df[x],df[y])
plt.xlabel(x,fontsize=18)
plt.ylabel(y,fontsize=18)
st.pyplot(fig)

"""
df_columns = df.columns
#データフレームを表示
st.markdown("### 入力データ")
st.dataframe(df.style.highlight_max(axis=0))
#matplotlibで可視化。X軸,Y軸を選択できる
st.markdown("### 可視化 単変量")
#データフレームのカラムを選択オプションに設定する
x = st.selectbox("X軸", df_columns)
y = st.selectbox("Y軸", df_columns)
#選択した変数を用いてmtplotlibで可視化
fig = plt.figure(figsize= (12,8))
plt.scatter(df[x],df[y])
plt.xlabel(x,fontsize=18)
plt.ylabel(y,fontsize=18)
st.pyplot(fig)
"""

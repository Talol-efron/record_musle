import pandas as pd
import streamlit as st
from datetime import date

#筋トレの記録webapp
#3ページ構成
#1ページ目: 記録ページ
#2パージ目: データページ(ここからデータの削除可能)
#3ページ目: グラフページ

st.title("Welcome musle Memo")
st.header("Let's recode this !")

df = pd.DataFrame(columns=["日付", "部位", "重さ", "回数", "セット数"])
Count = sum(1 for line in open("record.csv", "rb"))

with st.form(key="memory"):
    #date
    dates = st.date_input("日付", date.today())
    #selectbox
    training_category = st.selectbox("部位", 
    ("胸", "背中", "腕", "肩", "脚"))

    #slider
    weight = st.slider("重さ", min_value=5, max_value=100)
    reps = st.slider("回数", min_value=1, max_value=20)
    sets = st.slider("セット数", min_value=1, max_value=20)
    #button
    btn_save = st.form_submit_button("Save")
    btn_calcel = st.form_submit_button("Cancel")

    if btn_save:
        #csvかDataframeに記録して、データ蓄積を行う
        #蓄積したデータでグラフで可視化し、１週間で部位別の強度を測る
        #違うページに誘導(ボタン？)    
        df = df.append({"日付": dates, "部位": training_category, 
                        "重さ": weight, "回数": reps, "セット数": sets}, 
                        ignore_index=True)
        if (Count == 0):
            df.to_csv("record.csv", mode="a", index=False)
        else:
            df.to_csv("record.csv", mode="a", index=False, header=False)
    elif btn_calcel:
        #一個前に間違えて送信した内容を取り消せるように実装
        #データが記録されている場所(csvかDataFrame)を表示してGUIで削除できるようにする
        st.text("キャンセルなんかできません。今はね")

if btn_save:
    st.text("本日もお疲れ様でした！")
    st.text(
        f"{dates}は、{training_category}のトレーニングを{weight}kgで{reps}回、{sets}セット数、行いました。")
    st.subheader("追加した内容")
    st.dataframe(df)

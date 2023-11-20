import streamlit as st
import time
from PIL import Image


st.title('20代の体力測定の点数')
st.write('どうも。ここでは20代の体力テストの結果を教えてもらえばその判定を出そうというアプリです（年齢の区別をつけるとめちゃくちゃやばいことになるから20歳限定にしました。悪しからず）。さて早速ですが自分のデータを打ち込んで見てくださいな。')
text = st.text_input('あなたの名前を教えてください')
gender = st.radio('まずは性別選択してね',["男","女"])

st.write('あなたの名前は'+text+'でございましゅ')
condition = st.slider('あなたの今の調子は？',0,100,50)
option = st.selectbox('好きな数字を教えてちょ',list(['1','2','3','4']))
'あなたが選択したのは、',option,'です'
st.sidebar.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty() #空コンテンツと一緒に変数を作成
bar = st.progress(0)#プログレスを作る 値は0

for i in range(100):latest_iteration.text(f'Iteration{i+1}')#空のIterationにテキストを入れていく
bar.progress(i +1)#barの中身をぐいぐい増やしていく
time.sleep(0.1)

'Done!!!'
left_column, right_column = st.columns(2)
button = left_column.button('コラムはこちら')
if button:right_column.write('バーカ')
img = Image.open('スクリーンショット 2023-11-13 170501.png')
st.image(img, caption='生活空間', use_column_width=True)
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],
                  columns = ['lat','lon'])
st.map(df)
df = pd.DataFrame(
np.random.rand(20,3), #20行3列
columns = ['a','b','c']
)
#表として表示する
st.table(df.style.highlight_max(axis=0))
#表からグラフ化 bar line area

st.bar_chart(df)
import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image


st.title('streamlit Test')

st.write('Interactive Widets')

st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'interation{i+1}')
    bar.progress(i * 1)
    time.sleep(0.1)

'Done!!!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button :
    right_column.write('Hello World')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容3')

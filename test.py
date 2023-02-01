import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.title(':polar_bear: This is :orange[july-ya] page :polar_bear:')
#st.sidebar.success("Select a demo above.")

def plotting_demo():
  
  #uploaded_file = st.file_uploader("Choose a file")
  
  #money = pd.read_csv(uploaded_file)
  money = pd.read_csv("money_data7.csv")
  
  option = st.selectbox('How would you like to choice year ?', ('2020', '2021', '2022'))
  option2 = int(option)
  st.write('You selected:', option)

  money = money[:] [money['A_YEAR']== option2]

  fig, ax = plt.subplots(2,2, figsize=(12,8))

  plt.subplot(221)
  plt.plot( list(money['A_MONTH']), list(money['A_RATE']), color = 'salmon', marker = 'o' )
  plt.xticks(tuple(money['A_MONTH']))
  plt.title("America Rate", size = 15, color = 'salmon')

  plt.subplot(222)
  plt.plot( list(money['A_MONTH']), list(money['K_RATE']), color = 'lightskyblue', marker = 'o' )
  plt.xticks(tuple(money['A_MONTH']))
  plt.title("Korea Rate", size = 15, color = 'lightskyblue')

  plt.subplot(223)
  plt.plot( list(money['A_MONTH']), list(money['KOSPI']), color = 'lightgreen', marker = 'o' )
  plt.xticks(tuple(money['A_MONTH']))
  plt.title("KOSPI", size = 15, color = 'lightgreen')

  plt.subplot(224)
  plt.plot( list(money['A_MONTH']), list(money['HOUSE_PRICE']), color = 'lightpink', marker = 'o' )
  plt.xticks(tuple(money['A_MONTH']))
  plt.title("House Price", size = 15, color = 'lightpink')

  st.snow()
  st.pyplot(fig)
  st.dataframe(money)

def bar_chart():
  url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="
  years = ['2015', '2016','2017', '2018', '2019', '2020', '2021', '2022' ]

  df = pd.DataFrame([]) 

  for i in years:
    df1 = pd.read_html( url + i  )[0]
    df1['년도'] =  i 
    df = pd.concat([df, df1], axis=0)
        
  baseball = df    

  baseball.팀.replace({'두산':'Dusan','삼성':'SS','키움':'KU','한화': 'HH','롯데':'Lotte','넥센':'NecSen'}, inplace=True)
    
  option = st.selectbox('How would you like to choice year ?', ('2015', '2016','2017', '2018', '2019', '2020', '2021', '2022'))

  option2 = option

  st.write('You selected:', option)

  df7  =  baseball[:] [ baseball.년도==option2 ]
  x = df7.팀
  y = df7.승률
    
  fig, ax = plt.subplots(figsize=(12,8))

  colors = ['plum', 'cornflowerblue', 'lightgreen', 'khaki', 'salmon', 'springgreen', 'lightblue' ,'lightcoral', 'orchid', 'chocolate' ]
  plt.bar(x, y, color= colors) 

  for num, v in enumerate(y):
    plt.text (num -0.4, v + 0.01, v)

  plt.title( "year korea baseball winrate data", position=(0.5,1.1))
  
  st.balloons()
  st.pyplot(fig)
  st.dataframe(df7)  

#st.set_page_config(layout = "centered")
  
with st.form(key = 'Form1'):
  with st.sidebar:
    select_language = st.sidebar.radio('데이터 분석 결과 확인 ?', ('금리와 집 값 빠르게 파악하기',
                                                              '야구 순위와 승률 빠르게 파악하기',
                                                              '다른 데이터 분석(진행중)'))

if select_language == '금리와 집 값 빠르게 파악하기':
  try:
    plotting_demo()
  except:
    pass

elif select_language == '야구 순위와 승률 빠르게 파악하기':
  bar_chart()

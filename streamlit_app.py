import streamlit
streamlit.title('Hello streamlit, you just got a new buddy')
streamlit.header('My Name is Sneha 👸🏻')
streamlit.text('🖥️ I am a software engineer')
streamlit.text('🤓 i love data and I love to work with data...')

streamlit.header('🥭 🍍My fav Fruits 🥑 🍓')
streamlit.text('🥭 mango is the most fav fruit of mine')
streamlit.text('🍓 strawberry is the seasonal fruit which I like')
streamlit.text('🍍 pinaaple is one of my fav tangy fruit')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

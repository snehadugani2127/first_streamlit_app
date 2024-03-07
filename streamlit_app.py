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

my_fruit_list= my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

# adding input box for fruit selection
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the response and normalise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as the table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

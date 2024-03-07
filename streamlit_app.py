import streamlit

import pandas

import requests

import snowflake.connector

from urllib.error import URLError

#import streamlit
streamlit.title('Hello streamlit, you just got a new buddy')
streamlit.header('My Name is Sneha 👸🏻')
streamlit.text('🖥️ I am a software engineer')
streamlit.text('🤓 i love data and I love to work with data...')

streamlit.header('🥭 🍍My fav Fruits 🥑 🍓')
streamlit.text('🥭 mango is the most fav fruit of mine')
streamlit.text('🍓 strawberry is the seasonal fruit which I like')
streamlit.text('🍍 pinaaple is one of my fav tangy fruit')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list= my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#create he repeatable code block(called as function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#new section to display fruityvice app response
streamlit.header("Fruityvice Fruit Advice!")
try:

fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
  streamlit.error("please select a fruit to get information.")
else:
  back_from_function = get_fruityvice_data(fruit_choice)
  streamlit.dataframe(back_from_function)

except URLError as e:
streamlit.error()
#dont run anything past this line
streamlit.stop()

#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)

#allow the end user to add a fruit of their choice
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.write('thanks for adding', add_my_fruit )

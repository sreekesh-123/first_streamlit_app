import streamlit
import snowflake.connector

streamlit.title('Hotel Aadikuttan')
streamlit.header('🥣🍞Shaapaadu')
streamlit.text('🥗Thengakola')
streamlit.text('🥑Mangatholi')

streamlit.header('🍌🥭 Inn rakkam, nale kadam 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# writing it
streamlit.dataframe(fruityvice_normalized)

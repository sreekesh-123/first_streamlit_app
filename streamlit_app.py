import streamlit

streamlit.title('Hotel Aadikuttan')
streamlit.header('🥣🍞Shaapaadu')
streamlit.text('🥗Thengakola')
streamlit.text('🥑Mangatholi')

streamlit.header('🍌🥭 Inn rakkam, nale kadam 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

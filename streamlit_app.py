import streamlit

streamlit.title('Hotel Aadikuttan')
streamlit.header('🥣🍞Shaapaadu')
streamlit.text('🥗Thengakola')
streamlit.text('🥑Mangatholi')

streamlit.header('🍌🥭 Inn rakkam, nale kadam 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

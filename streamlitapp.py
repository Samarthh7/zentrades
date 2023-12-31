import os
import requests
import pandas as pd
import json
import streamlit as st
import matplotlib.pyplot as plt

st.markdown(
    """ this website parses the data from the API and stores the information in pandas Dataframe"""
)
st.title("**Amazon Products**")

data = requests.get("https://s3.amazonaws.com/open-to-cors/assignment.json")
data = json.loads(data.content)
list = []
for i in data:
    list.append(data["products"])
for i in range(len(list)):
    df = pd.DataFrame(list[i])
df2 = df.T
st.dataframe(df2)
count = df2.groupby(by="subcategory").agg("count")
st.write("**count of the subcategories of products sold**")
st.dataframe(count)
# count.index = count
# fig = plt.figure(figsize=(4, 3))
# plt.bar(count.subcategory, count.title)
# plt.xlabel("Items", fontweight="bold")
# plt.ylabel("Count", fontweight="bold")
# plt.xticks(rotation=45)
# st.pyplot(fig)

price_total = df2.groupby(by="subcategory").agg({"price": "sum"})
highest_price = df2.sort_values("price", ascending=False)
aggfunc = df2.pivot_table(
    index="subcategory", values="price", aggfunc=["count", "sum", "mean"]
)
st.dataframe(aggfunc)
highest_price.head(10)
st.write("**top 10 products**")
st.dataframe(highest_price)
df2 = df2.sort_values(by=["popularity", "price"], ascending=False)
st.write("**products based on popularity and price**")
st.dataframe(df2)

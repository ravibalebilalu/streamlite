import streamlit as st 

import numpy as np
 
import matplotlib.pyplot as plt
import pandas as pd

st.title("Streamlit Charts")

chart_data = pd.DataFrame(np.random.randn(20,3),columns=["A","B","C"])

st.subheader("Area Chart")

st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)
st.subheader('Scatter Chart')
st.scatter_chart(pd.DataFrame({
    "x":np.random.randn(100),
    "y":np.random.randn(100)
})
)

st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100,2)/[50,50] + [37.76,-122.4],columns=["lat","lon"]

)
st.map(map_data)

st.subheader("Pyplot chart")

fig,ax =  plt.subplots()
ax.plot(chart_data["A"],label="A")
ax.plot(chart_data["B"],label="B")
ax.plot(chart_data["C"],label="C")
ax.set_title("Pyplot Line chart")
ax.legend()
st.pyplot(fig)
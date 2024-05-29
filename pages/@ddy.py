import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
#import folium
#from folium.plugins import HeatMap
#import seaborn as sns
st.title("SLAY!")

if st.button("Click for Taylor"):
    st.image(image="./resources/taylor.png",width=600)

if st.button("YouTube"):
    st.page_link(page="https://www.youtube.com/",width=200)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
import streamlit.components.v1 as components

st.title("Your Brain, Electricity, Some Stuff Called 'Myelin', and Getting Better at Stuff")
col1, col2 = st.columns(2)
with col2:
        st.image(image="./resources/myelin_sheath.jpg",width=400)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/resistance-in-a-wire/latest/resistance-in-a-wire_en.html"
        components.iframe(iframe_src,height=500)


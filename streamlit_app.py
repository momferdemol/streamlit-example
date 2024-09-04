import altair as alt
import numpy as np
import pandas as pd
import logging
import streamlit as st
from boto3 import client
from botocore.expections import ClientError
from mypy_boto3_ssm import SSMClient

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


def get_parameter_from_store(name: str) -> str:
    try:
        response = ssm.get_parameter(Name=name)
        value = response["Parameter"]["Value"]
        return value
    except ClientError as err:
        msg = f"{err}{name}"
        logging.error(msg)
        raise SystemError from err


num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame(
    {
        "x": x,
        "y": y,
        "idx": indices,
        "rand": np.random.randn(num_points),
    }
)

st.altair_chart(
    alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    )
)

secret = get_parameter_from_store("/streamlit/app/survey/api-key")
st.write(secret)

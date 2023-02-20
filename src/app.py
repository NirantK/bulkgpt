"""
Ecomm Rewriter

Takes an input description and rewrites it using a GPT3 model.
"""

import streamlit as st
from rewriter import rewrite
import pandas as pd

# Main page
st.title("Ecomm Rewriter")
st.write("Rewrite your product descriptions using GPT3")

# Prompt for user to enter description
with st.form("description"):
    # description = st.text_area("Enter your description")
    submit = st.form_submit_button("Rewrite")
    uploaded_file = st.file_uploader("upload a .csv file with a column called 'text'")

    if uploaded_file is not None:
        # Reading the uploaded file
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

    if submit:
        # Call OpenAI API
        st.write("Calling OpenAI. This can take a while...")
        dataframe["rewritten"] = dataframe["text"].apply(rewrite)

        st.write("Rewritten descriptions:")
        st.write("\n\n\n".join(dataframe["rewritten"].tolist()))

        # Write to CSV
        st.write("Writing to CSV")
        dataframe.to_csv("rewritten.csv", index=False)

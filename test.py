
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
st.title("Email/SMS Spam Classifier")
# Custom CSS for vertical line
vertical_line = """
<style>
.vertical-line {
  border-left: 2px solid black;
  height: 1000px;
  position: absolute;
  left: 15%;
  top: 2;
}
</style>
"""

st.markdown(vertical_line, unsafe_allow_html=True)

# HTML for vertical line
st.markdown("<hr style='border:1px solid black'>", unsafe_allow_html=True)
st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)
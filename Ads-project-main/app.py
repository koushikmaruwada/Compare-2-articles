import streamlit as st
import re
from textblob import TextBlob
st.title("Compare Bias — AI Tool")

article1 = st.text_area("Article A")
article2 = st.text_area("Article B")

BIAS_WORDS = [
    "corrupt", "corruption", "scandal", "disaster",
    "shameful", "outrageous", "heroic", "failure",
    "biased", "propaganda", "unfair", "incompetent",
    "dangerous", "radical", "extreme"
]



def analyze(text):
    # text_lower = text.lower()
    # count = 0
    polarity = TextBlob(text).sentiment.polarity
    return round(abs(polarity) * 10)

    for word in BIAS_WORDS:
        matches = re.findall(rf"\b{word}\b", text_lower)
        count += len(matches)

    return count

if st.button("Compare"):
    score1 = analyze(article1)
    score2 = analyze(article2)

    st.write("### Results")
    st.write("Article A Score:", score1)
    st.write("Article B Score:", score2)

    if score1 > score2:
        st.success("Article A appears more biased.")
    elif score2 > score1:
        st.success("Article B appears more biased.")
    else:
        st.info("Both articles appear equally biased.")

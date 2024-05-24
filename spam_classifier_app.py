import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk 
from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(lemma.lemmatize(i))
    return " ".join(y)

tfidf = pickle.load(open('Spam_email_classifier/vectorizer.pkl','rb'))
model = pickle.load(open('Spam_email_classifier/model.pkl','rb'))

st.title("Email/Sms spam classifier")
input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    transform_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transform_sms])
    result = model.predict(vector_input)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
    




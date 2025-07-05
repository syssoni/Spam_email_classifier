# Spam_email_classifier
## About the project
---
This project is an SMS/E-mail spam classifier that classifies user-input messages as spam or not spam. It utilises machine learning and natural language processing techniques to clean and extract features from the text corpus. It uses a Naive Bayes classifier for multivariate Bernoulli for classification.

**Project Structure**<br/>
- `spam_email.ipynb` - main notebook for classifying messages into spam or not spam
- `spam_classifier_app.py` - web interface made using streamlit
- `SMSSpamCollection.txt` - Dataset used<br/>

**Machine learning Pipeline**<br/>
1. **Data collection**<br/>

2. **Text preprocessing**   
   Remove punctuation, special characters, stopwords, and lemmatization<br/>
   
3. **Feature engineering**<br/>
   Label Encoder - Encoding spam and not spam messages to numerical values<br/>
   TF-IDF Vectorizer used to convert preprocessed text into numerical vectors that represent the importance of words<br/>

4. **Model Training and saving**<br/>
   Here, I used a Naive Bayes classifier for training a model<br/>
   The trained model and TF-IDF vectorizer are serialized using pickle and saved as:
    model.pkl<br/>
    vectorizer.pkl<br/>

**About the data**<br/>
- The dataset is obtained from Kaggle
- The dataset contains two columns:- <br/>
  `messages` - The original message<br/>
  `label` - Whether the message is spam or not spam(ham)<br/>

**Classification, Naive Bayes classifier for multivariate Bernoulli, Label encoder, Data preprocessing, Natural language processing(Tokenization, stop word removal, vectorization), Pickling, Wordcloud, Tfidf vectorizer, lemmatization** 

## Installation and running 
---
**Dependencies for the project**<br/>
  - python=3.13.5
  - pandas=2.2.3
  - scikit-learn=1.6.1
  - matplotlib=3.10.0
  - numpy=2.3.1
  - seaborn=0.13.2
  - nltk=3.9.1
  - streamlit=1.46.1<br/>
  
  (Note: All the dependencies are installed in the yaml file)<br/>

**Steps for running the project**<br/> 
1. Create and Activate Environment<br/>
   conda env create -f environment.yml<br/>
   conda activate spam_classifier<br/>
   
2. Add the required data files<br/>
   If not yet created, run spam_email.ipynb.ipynb to generate them<br/>
   vectorizer.pkl<br/>
   model.pkl<br/>
   
3. Run the App<br/>
   streamlit run spam_classifier_app.py<br/>
   
## Application
---
<img src="https://raw.githubusercontent.com/syssoni/Spam_email_classifier/main/Web_app/web_app.png" alt="Web application" width="70%">

**Feel free to suggest changes :)**



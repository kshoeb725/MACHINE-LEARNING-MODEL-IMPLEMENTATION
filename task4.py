import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

# Load data
data = pd.read_csv("spam.csv", encoding='latin-1')  # Specify encoding if required
data = data[['Category', 'Message']]  # Select relevant columns
data.drop_duplicates(inplace=True)
data['Category'] = data['Category'].replace(['ham', 'spam'], ['Not Spam', 'Spam'])

# Split data
mess = data['Message']
cat = data['Category']
mess_train, mess_test, cat_train, cat_test = train_test_split(mess, cat, test_size=0.2, random_state=42)

# Vectorize messages
cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

# Train model
model = MultinomialNB()
model.fit(features, cat_train)

# Test model
features_test = cv.transform(mess_test)

# Predict function
def predict(message):
    input_message = cv.transform([message])
    result = model.predict(input_message)
    return result[0]

# Streamlit app
st.header('Spam Detection')

input_mess = st.text_input('Enter Message Here')

if st.button('Validate'):
    output = predict(input_mess)
    st.markdown(f"**Result:** {output}")


# write in terminal streamlit run filename to open the web 
    
#try using this example for spam email  : Congratulations, you won a lottery

**COMPANY**: CODETECH IT SOLUTIONS

**Name**: SHOEB KHAN

**INTERN ID**: CT0806HU

**Domain**: Python Programming

**BATCH Duration**: 12th December to 12th January

**Mentor**: Neela Santhosh Kumar

**PROJECT**: MACHINE LEARNING MODEL IMPLEMENTATION

###  Overview of the Code

This script demonstrates the implementation of a machine learning-based **spam detection application** using Python. It integrates various libraries and frameworks such as Pandas, Scikit-learn, and Streamlit to create an end-to-end solution. Key functionalities include:  

---

### OUPUT OF THE TASK

![task44](https://github.com/user-attachments/assets/c84a1762-1f44-499c-8450-2ed1e7031936)

---

![task4](https://github.com/user-attachments/assets/c9567518-2d0d-45ef-9ee3-42559abf2cdb)

---

1. **Data Preparation**:  
   - Loads a CSV dataset of labeled messages (`spam.csv`) with relevant columns (`Category` and `Message`).  
   - Cleans the data by removing duplicates and standardizing the target labels (`Spam` and `Not Spam`).  

2. **Data Splitting**:  
   - Divides the dataset into training and testing sets using an 80-20 split for robust model evaluation.  

3. **Feature Extraction**:  
   - Converts textual data into numerical form using `CountVectorizer` with stop words removed to enhance model performance.  

4. **Model Training**:  
   - Utilizes a **Multinomial Naive Bayes** model, which is well-suited for text classification tasks, to train on the vectorized messages.  

5. **Prediction Function**:  
   - A function that takes user input, vectorizes it, and predicts whether the message is "Spam" or "Not Spam."  

6. **Web Interface**:  
   - A simple interface built using **Streamlit** allows users to input messages and validate predictions dynamically.  

---

###  Conclusion  

This script effectively demonstrates the integration of machine learning techniques with real-world applications in text classification. The use of **Multinomial Naive Bayes** ensures a computationally efficient solution for spam detection, while **Streamlit** enhances accessibility by providing an intuitive interface.  

Key highlights of the script include:  
- A structured pipeline for data preprocessing, feature extraction, and classification.  
- A modular design enabling ease of extension, such as supporting other text classification tasks or incorporating additional data preprocessing steps (e.g., stemming or lemmatization).  
- Practical application of machine learning in real-time message classification.  

This implementation showcases how to bridge the gap between technical machine learning workflows and user-facing applications, making it a valuable prototype for production-ready spam detection systems.

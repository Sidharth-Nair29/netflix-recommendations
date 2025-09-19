# 🎬 Netflix Movie Recommendation System  

## 📌 Project Overview  
This project is a content-based movie recommendation system built using the Netflix dataset.  
The goal is to recommend movies that are similar to a user’s choice by analyzing metadata such as genres, descriptions, and release year.  

The project is divided into two main parts:  
1. Exploratory Data Analysis (EDA):  
   - Cleaning and preprocessing the dataset.  
   - Analyzing trends in genres, release years, and content distribution.  
   - Visualizing insights with Python libraries.  

2. Recommendation Engine:  
   - Implemented TF-IDF vectorization on movie descriptions.  
   - Used cosine similarity to calculate similarity between movies.    
   - Added explainability (showing why a movie was recommended).  

An interactive Streamlit app is also included, allowing users to input a movie title and receive tailored recommendations.  

---

## ⚙️ Tech Stack  
- **Languages/Tools:** Python, Pandas, NumPy, Scikit-learn, Streamlit  
- **Visualization:** Matplotlib, Seaborn  
- **Environment:** Jupyter Notebook (Google Colab), VS Code  

---

## 🚀 Features  
- Content-based recommendations using TF-IDF and cosine similarity.  
- User-friendly Streamlit app for real-time recommendations.  
- Filters by genre and release year.  
- EDA with meaningful insights about Netflix content.  

---

## 📂 Project Structure  
```
netflix-recommendation/
│
├── notebooks/
│   └── Netflix_EDA.ipynb
│
├── app/
│   └── app.py
│
├── requirements.txt
└── README.md
```  

---

## 📊 Sample Output  
*(Insert screenshot of Streamlit app or EDA graphs here)*  

---

## 🔮 Future Enhancements  
- Hybrid recommendations (content + collaborative filtering).  
- Improved explainability with keyword highlights.  
- Deployment on cloud platforms (Heroku/Streamlit Cloud).  

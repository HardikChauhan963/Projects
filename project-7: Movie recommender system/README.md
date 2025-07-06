# 🎬 Movie Recommendation App using Streamlit

Welcome to the **Movie Recommendation System**! This project is a simple yet powerful **content-based recommender** built with **Python**, **Streamlit**, and **TMDB movie metadata**.

> 🔍 Find your next favorite movie based on your selected title using **natural language processing** and **cosine similarity**.

---

## 🚀 Features

✅ Content-Based Recommendation System  
✅ Uses **Cosine Similarity** to recommend top 5 similar movies  
✅ Select a movie from a list of 4800+ films  
✅ View posters fetched dynamically via **TMDB API**  
✅ NLP-based feature engineering with **Bag-of-Words**  
✅ Streamlit-powered interactive UI  
✅ Integrated with Kaggle dataset using Kaggle API

---

## 🧠 How It Works

This is a **Content-Based Movie Recommendation System**. It works as follows:

1. **Data Source**: TMDB 5000 Movie & Credit Datasets
2. **Feature Engineering**:
    - Extracted genres, keywords, top 5 cast, and director
    - Combined all into a single `all_info` text column
    - Applied stemming to normalize similar words
3. **Vectorization**:
    - Transformed `all_info` into numeric vectors using `CountVectorizer`
    - Limited to top 6000 features, removed stopwords
4. **Similarity Calculation**:
    - Computed **Cosine Similarity** between movie vectors
    - Lower distance → higher similarity
5. **Recommendation**:
    - Given a movie, it returns 5 most similar movies based on content
6. **Display**:
    - Recommended titles and posters shown in a sleek Streamlit UI

---

## 🛠️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/HardikChauhan963/movie-recommender-streamlit.git
cd movie-recommender-streamlit

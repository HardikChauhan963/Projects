# 🎬 Movie Recommendation App using Streamlit

Welcome to the **Movie Recommendation System**! This project is a simple yet powerful **content-based recommender** built with **Python**, **Streamlit**, and **TMDB movie metadata**.

> 🔍 Find your next favorite movie based on your selected title using **natural language processing** and **cosine similarity**.
<img width="728" alt= "app_photo" src = "https://github.com/user-attachments/assets/9979721b-2a61-428b-8e67-f8e5e74242fa" />
<img width="728" alt="Screenshot 2025-07-06 at 21 48 03" src="https://github.com/user-attachments/assets/f1d5fa9c-5f98-4c6f-b278-2cf513675042" />



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

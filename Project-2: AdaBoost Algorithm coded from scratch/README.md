# 🧠 AdaBoost Algorithm from Scratch

> Dive into the inner workings of one of the most powerful ensemble learning techniques – built step-by-step, from the ground up!

---

## 🎯 Objective

To implement the **AdaBoost Classifier** algorithm manually using basic machine learning and data manipulation libraries to gain deep intuition of how it really works—beyond the black-box of `scikit-learn`.

### 🧾 What is AdaBoost?

**AdaBoost** (short for *Adaptive Boosting*) is an ensemble learning algorithm that combines multiple weak learners (typically simple decision stumps) into a single strong classifier. It works by assigning weights to training examples, emphasizing those that were previously misclassified, and giving more influence to better-performing models through calculated importance weights (alphas).

---

## 🔍 Scope

This project emphasizes **understanding the logic** behind AdaBoost rather than optimizing for performance or accuracy.

---

## ⚙️ Algorithm Breakdown

1. **Data Preparation**
2. **Weight Initialization** – Uniform weights for all samples
3. **Train Weak Learners** – Using decision stumps (`max_depth = 1`)
4. **Make Predictions**
5. **Calculate Alpha** – The importance of each model
6. **Update Sample Weights** – Focus more on misclassified samples
7. **Resample Data** – Based on updated weights
8. **Repeat** – Re-train for `n` models (e.g. 2 in this example)

# 📊 Central Limit Theorem – Visualized with Python

> A hands-on demonstration of how sample means from different distributions converge to a normal distribution. Built for clarity. Backed by theory.

---

## 🎯 Objective

This Python program empirically demonstrates the **Central Limit Theorem (CLT)** by analyzing the distribution of sample means derived from various probability distributions, including **binomial**, **Poisson**, **uniform**, and **Pareto**.

Through repeated sampling and visualization, the code showcases the convergence of sample mean distributions towards a **normal distribution**, regardless of the underlying population distribution—validating the fundamental principles of CLT.

---

## 🧾 What is the Central Limit Theorem?

The **Central Limit Theorem** states that, given a sufficiently large sample size from a population with a finite level of variance, the **mean of all samples** from the same population will be **approximately normally distributed**.

This holds true even if the original data is **not normally distributed**.

---

## 🧪 Distributions Analyzed

1. **Binomial Distribution** – Success/failure outcomes
2. **Uniform Distribution** – Equal probability between a range
3. **Poisson Distribution** – Count-based events in time or space
4. **Pareto Distribution** – Heavy-tailed distribution (e.g., 80/20 rule)

---

## 🧰 Technologies Used

- Python 3
- NumPy
- Seaborn
- Matplotlib

---

## 🧠 What the Code Does

- Generates 10,000 random values for each distribution
- Randomly draws 1,000 samples of size 100 from each population
- Calculates the mean of each sample
- Plots both:
  - Original population distribution
  - Sampling distribution of the mean

Each subplot shows:
- A histogram of the values
- Kernel Density Estimation (KDE) overlay
- Mean and variance annotations

---

## 📸 Output Example

The program displays **8 plots**:
- 4 original distributions (binomial, uniform, Poisson, Pareto)
- 4 sampling distributions of the sample means

You’ll observe that:
> While the original distributions vary in shape, their sample means consistently approximate a **normal bell curve**—a powerful visual proof of the CLT.

---

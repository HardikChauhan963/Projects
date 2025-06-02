
---

## 📌 Objective

The goal is to predict the **credit approval flag** (`Approved_Flag`) using customer financial and demographic features. The problem is treated as a **multiclass classification** task using the following models:

- 🌲 Random Forest
- ⚡ XGBoost
- 🌳 Decision Tree

---

## 📁 Dataset Description

Two datasets are used:

- `case_study1.xlsx` – contains demographic and transaction history
- `case_study2.xlsx` – contains detailed credit history

Merged on the `PROSPECTID` column to form a unified dataset.

---
## 🔄 Workflow Summary

### 🧼 Step 1: Data Cleaning & Merging

- **Datasets Used**:
  - `case_study1.xlsx`: Demographic and transaction history
  - `case_study2.xlsx`: Credit history

- **Cleaning Steps**:
  - Replaced `-99999` with null-equivalent logic
  - Dropped rows from `case_study1` where `Age_Oldest_TL == -99999`
  - In `case_study2`:
    - Dropped columns with more than 20% missing values
    - Dropped remaining rows with missing values

- **Merging**:
  - Merged both datasets on the `PROSPECTID` column using an inner join

---

### 📊 Step 2: Feature Selection

#### Categorical Features

- **Selected Columns**: `MARITALSTATUS`, `EDUCATION`, `GENDER`, `last_prod_enq2`, `first_prod_enq2`
- **Statistical Test**: Chi-Square Test with target variable `Approved_Flag`
- **Outcome**: All features retained (p-value ≤ 0.05)

#### Numerical Features

- **Step 1 - VIF (Variance Inflation Factor)**:
  - Removed multicollinear features (threshold: VIF > 6)

- **Step 2 - ANOVA Test**:
  - Retained features with p-value ≤ 0.05

---

### 🧾 Step 3: Encoding

#### 🎓 Label Encoding for `EDUCATION`

| Education Level     | Encoded Value |
|---------------------|---------------|
| SSC                 | 1             |
| 12TH                | 2             |
| GRADUATE            | 3             |
| UNDER GRADUATE      | 3             |
| PROFESSIONAL        | 3             |
| POST-GRADUATE       | 4             |
| OTHERS              | 1             |

#### 🔢 One-Hot Encoding Applied To:
- `MARITALSTATUS`
- `GENDER`
- `last_prod_enq2`
- `first_prod_enq2`

---

### 🧠 Step 4: Model Training & Evaluation

#### 🔀 Data Split
- **Training Set**: 80%
- **Test Set**: 20%

#### 🤖 Models Used

| Model           | Parameters                                       |
|-----------------|--------------------------------------------------|
| Random Forest   | `n_estimators=200`                               |
| XGBoost         | `objective='multi:softmax'`, `num_class=4`       |
| Decision Tree   | `max_depth=20`, `min_samples_split=10`           |

#### 📈 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score

**Metrics are reported for each class**: `P1`, `P2`, `P3`, `P4`


## 🛠️ Technologies & Libraries

| Category       | Tools / Libraries                                  |
|----------------|----------------------------------------------------|
| Programming    | Python                                              |
| Data Handling  | `pandas`, `numpy`, `openpyxl`                      |
| Visualization | `matplotlib`                                       |
| ML Models      | `sklearn`, `xgboost`                               |
| Stats Tests    | `scipy`, `statsmodels`                             |

Install dependencies using:

```bash
pip install numpy pandas matplotlib scikit-learn statsmodels scipy xgboost openpyxl

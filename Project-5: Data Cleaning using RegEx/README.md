# ⚽ FIFA 21 Data Cleaning & Transformation Project

## 🧼 Objective

The goal of this project is to **clean and transform** a messy FIFA 21 player dataset using Python and Pandas. The dataset originally contains inconsistent, incomplete, and mixed-format entries. This project demonstrates how to handle real-world dirty data by converting it into a structured and analysis-ready format.

---

## 📂 Dataset

- **Source**: [Kaggle - FIFA 21 Messy Raw Dataset](https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring)
- **Files Used**:
  - `fifa21_raw_data.csv`
  - `fifa21 raw data v2.csv`

---

## 🔧 Tools & Libraries

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `re` (regex)

---

## 🧱 Key Cleaning Steps

### 🔄 Dataset Merging
- Analyzed differences in column structures between `df1` and `df2`
- Extracted relevant values like `Club`, `Contract_start`, and `Contract_end` from combined text columns
- Renamed inconsistent column names to ensure schema alignment
- Concatenated both datasets into one unified dataframe

### 🧹 Data Normalization
- Dropped columns with **over 50% missing values**
- Removed **duplicate rows**
- Cleaned and standardized:
  - **Height**: Converted feet/inches and cm to consistent **cm format**
  - **Weight**: Converted lbs and kg to consistent **kg format**
  - **Value, Wage, Release Clause**: Converted K/M values to **millions (float)**
  - **W/F, SM, IR, Hits**: Extracted numeric values from string fields like `"5 ★"` or `"3*"`
  
### 📊 Key Transformations
| Column                  | Transformation                                                                 |
|-------------------------|----------------------------------------------------------------------------------|
| `Height`                | Converted mixed units (ft/in & cm) → cm                                         |
| `Weight`                | Converted lbs & kg → kg                                                         |
| `Value`, `Wage`, `Release Clause` | Normalized currency values (€K, €M) → millions (float)                      |
| `W/F`, `IR`, `SM`, `Hits`        | Extracted only the numeric rating (e.g., from "5 ★" to 5)                         |

---

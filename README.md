 Letter Recognition – Data Preprocessing & Visualization

Welcome to my mini-project on **Letter Recognition**!  
This project focuses on cleaning, transforming, and visualizing the popular *Letter Recognition Dataset* using Python.

It’s a simple but important part of any ML pipeline—because clean data is smart data.

---

Project Structure

elevate-task/
├── clean_data.py ~ Code to load, clean, scale & visualize the dataset
├── letter-recognition.csv ~The dataset used for the task
├── README.md 


---

Dataset Overview

- **Source**: UCI Machine Learning Repository  
- **Samples**: 20,000  
- **Target column**: `letter` (A-Z)  
- **Features**: 16 numerical columns describing pixel edge counts, width, height, etc.

Each row is a visual representation of an alphabet letter in numeric form.

---

What the Script Does

`clean_data.py` performs:

-  Loads the dataset  
-  Cleans column names (removes trailing spaces)  
-  Displays dataset info and head  
-  Scales numeric features using `StandardScaler`  
- Visualizes frequency of each letter using Seaborn countplot

---

Sample Output (What You’ll See)

- DataFrame structure (rows, columns, types)  
- Cleaned column names  
- Scaled features  
- A colorful bar chart showing how often each letter appears

---

How to Run

1. Activate your environment (if using one):

```bash
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate.bat  # Windows

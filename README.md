# Student Performance Analyzer (Python & Streamlit)

A professional, interactive Data Science dashboard built using Python, Streamlit, and Pandas. This application allows users to upload student datasets and instantly generate actionable academic insights through automated grading and ranking.

---

## Project Overview

The Student Performance Analyzer automates the manual process of calculating grades and identifying student performance trends. It demonstrates a complete data science workflow—from dynamic data ingestion and cleaning to interactive visualization.

**Key focuses include:**

- Dynamic Data Processing using **Pandas**
- Interactive Dashboarding with **Streamlit**
- Defensive Programming (input validation for numeric vs. text columns)
- Data-Driven Logic (automated grading using Pandas binning)
- Modern UI/UX Design with a high-contrast cinematic theme

---

## Key Features

- **Universal File Support:** Upload any CSV or Excel dataset.
- **Dynamic Column Mapping:** Automatically detects and filters numeric subject columns and text-based name columns.
- **Automated Grading:** Assigns letter grades (A–F) based on averages using Pandas `cut()`.
- **Performance Tracking:**
  - **Top 10 Performers:** Real-time leaderboard using `.nlargest()`.
  - **Failing Students Detector:** Instantly flags students requiring academic attention.
- **Class Metrics:** Summary cards for Total Students, Class Average, and Fail Count.
- **Sleek UI:** "Royal Black & White" professional aesthetic for enhanced readability.

---

## Tech Stack

- **Python**
- **Streamlit** (Web Interface)
- **Pandas** (Data Manipulation)
  
---

## Project Structure
```
Student-Performance-Analyzer/
│
├── .streamlit/
│   └── config.toml        # Custom Black & White Theme settings
│
├── main.py                # Core application logic and UI
├── requirements.txt       # List of dependencies
│
└── data/
    └── student_sample.csv # Sample dataset for testing
```


- `main.py` → Handles file uploads, sidebar configuration, and UI rendering
- `config.toml` → Defines the royal dark mode aesthetic (Background: #000000, Accent: #F0F0F0)
- `requirements.txt` → Ensures consistent environment setup, including optional openpyxl for Excel files

---

## Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/Student-Performance-Analyzer.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the application:
```bash
streamlit run main.py
```
---

## Purpose of This Project

This project demonstrates my ability to:

- Build robust, end-to-end Data Science dashboards
- Implement flexible logic that handles varied user inputs
- Turn raw data into actionable visual insights
- Apply data cleaning and feature engineering in real-world scenarios

It reflects my focus on building **data-driven solutions that provide immediate value** to users.

---

## Developer
**Muhammad Bazil**

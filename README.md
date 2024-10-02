# Bike Sharing System Data Analysis Dashboard 🚴‍♂️📊

Welcome to the **Bike Sharing System Data Analysis Dashboard**! This project analyzes historical bike rental data and provides a comprehensive visualization dashboard using **Streamlit**. The dataset includes bike-sharing records from **Capital Bikeshare System** in **Washington D.C.** for the years 2011 and 2012.

## ✨ Project Overview
The goal of this project is to uncover patterns and insights from the bike rental data, such as:
- Trends in bike rentals by year, month, season, and weather conditions 🌤️.
- Rental behavior across working days, weekends, and holidays 📅.
- Peak rental hours during the day ⏰.
- Distribution of rentals between registered users and casual users 👥.

The dashboard allows users to interactively explore these trends and derive insights for improving the bike-sharing service.

---

## ⚙️ Setup Environment

This section outlines two methods for setting up the environment—**Anaconda** or **Shell/Terminal**. Choose the method that best fits your system configuration.

### Setup Environment - Anaconda

Follow these steps to set up your environment using **Anaconda**:
```
conda create --name main-ds python=3.11
conda activate main-ds
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal

Alternatively, use the following steps to set up the environment using **Shell/Terminal**:
```
mkdir submission
cd submission
pipenv install
pipenv shell
pip install -r requirements.txt
```

## 🚀 Running the Dashboard

Once the environment is set up, you can run the **Streamlit** app to explore the bike-sharing data:
```
streamlit run dashboard.py
```

After running the command, the dashboard will open in your default web browser, where you can interactively explore the data.

---

## 📁 Project Structure
```
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───day.csv
| └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

---

## 📊 Data Source
The data used in this project is sourced from **Capital Bikeshare**, a publicly available dataset that logs bike rentals in Washington D.C. for the years 2011 and 2012.

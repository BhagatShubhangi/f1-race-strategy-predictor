<div align="center">

# 🏎️ F1 Race Strategy Prediction System

### AI-Powered Race Engineering with Machine Learning

</div>

---

## 📖 Overview

An end-to-end Machine Learning project that predicts Formula 1 race strategy decisions such as **pit stop count**, **pit stop timing**, and **next tire compound** using historical F1 race data.

This project simulates a **virtual F1 race engineer** and demonstrates how data science and ML can assist strategic decision-making in motorsports.

### 🎯 Why This Matters

In Formula 1, race strategy is critical:
- ❌ A poorly timed pit stop can cost **10–20 seconds**
- ❌ Wrong tire choice can lose multiple positions
- ✅ Machine Learning can learn patterns from **thousands of historical races**
- ✅ Provides data-driven strategy recommendations instantly

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| **🔮 Pit Stop Count Prediction** | Recommends 1-stop or 2-stop strategy |
| **⏱️ Pit Stop Timing** | Predicts optimal lap for pit stop (e.g., Lap 18-22) |
| **🛞 Tire Compound Selection** | Suggests Soft / Medium / Hard compound |
| **🌐 Interactive Web Interface** | Flask-based UI for easy strategy generation |
| **📊 Historical Data Analysis** | Trained on real Formula 1 race datasets |

---

## 🧠 Machine Learning Approach

The system breaks down race strategy into **three ML problems**:

### 1️⃣ Pit Stop Count (Classification)
```python
Model: Random Forest Classifier
Input: Circuit, Year, Driver, Grid Position
Output: 1 stop or 2 stops
Accuracy: ~79%
```

### 2️⃣ Pit Stop Lap (Regression)
```python
Model: Random Forest Regressor
Input: Race length, Driver position, Current lap
Output: Predicted pit lap (e.g., Lap 21)
```

### 3️⃣ Next Tire Compound (Classification)
```python
Model: Random Forest Classifier
Input: Track type, Weather, Previous compound
Output: Soft / Medium / Hard
```

---

## 📊 Dataset

Historical Formula 1 race data sourced from [Kaggle F1 Dataset](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020):

| File | Description |
|------|-------------|
| `circuits.csv` | Circuit information (name, country, location) |
| `drivers.csv` | Driver details and identifiers |
| `driverGrid.csv` | Starting grid positions |
| `constructors.csv` | Team information |
| `f1_strategy_base.csv` | Cleaned and merged race data |
| `f1_strategy_with_target.csv` | Final dataset with target variables |

> **Note:** Pit lap and tire compound data are simulated to demonstrate the full ML pipeline.

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Languages** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **ML/Data Science** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white) |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat) ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat) |
| **Web Framework** | ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) |

</div>

---

## 📁 Project Structure
```
F1_RACE_STRATEGY_ML/
│
├── 📂 data/                          # Raw and processed datasets
│   ├── circuits.csv
│   ├── constructors.csv
│   ├── driverGrid.csv
│   ├── drivers.csv
│   ├── f1_strategy_base.csv
│   └── f1_strategy_with_target.csv
│
├── 📂 notebooks/                     # Jupyter notebooks for analysis
│   └── 03_merge_clean.ipynb
│
├── 📂 models/                        # Trained ML models
│   ├── pit_stop_count_model.pkl
│   ├── pit_lap_model.pkl
│   └── tire_compound_model.pkl
│
├── 📂 templates/                     # HTML templates
│   └── index.html
│
├── 📂 static/                        # CSS, JS, images
│   └── style.css
│
├── app.py                            # Flask application
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
├── .gitignore                        # Git ignore file
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/f1-race-strategy-predictor.git
cd f1-race-strategy-predictor
```

### 2️⃣ Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn flask
```

---

## 🚀 Usage

### 1️⃣ Start the Flask Application
```bash
python app.py
```

### 2️⃣ Open in Your Browser
```
http://127.0.0.1:5000/
```

### 3️⃣ Input Race Parameters
- **Circuit Name:** e.g., "Silverstone Circuit"
- **Country:** e.g., "UK"
- **Year:** e.g., 2024
- **Driver ID:** e.g., 1

### 4️⃣ Get AI Strategy Recommendation
Click **"GENERATE STRATEGY"** to receive predictions for:
- Number of pit stops
- Optimal pit lap
- Recommended tire compound

---

## 📈 Results & Model Performance

| Model | Metric | Score |
|-------|--------|-------|
| **Pit Stop Count** | Accuracy | ~79% |
| **Pit Lap Prediction** | MAE (Mean Absolute Error) | ~2.5 laps |
| **Tire Compound** | Accuracy | ~75% |

### Key Learnings
✅ Built complete ML pipeline from raw data to deployment  
✅ Implemented feature engineering and encoding techniques  
✅ Integrated ML models with interactive web interface  
✅ Learned model evaluation and performance optimization  

---

## 🔮 Future Enhancements

- [ ] Add weather data integration
- [ ] Implement safety car prediction
- [ ] Real-time race strategy updates
- [ ] Driver comparison analytics
- [ ] Mobile-responsive design improvements
- [ ] Deploy on cloud (AWS/Heroku)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with 🏎️ by [Shubhangi Bhagat]

</div>


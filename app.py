from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# --- 1️⃣ Load and prepare real F1 dataset ---
driver_grid = pd.read_csv("data/driverGrid.csv")
circuits = pd.read_csv("data/circuits.csv")

# Merge relevant columns
driver_grid = driver_grid[["raceId", "driverId", "position"]]
circuits = circuits[["raceId", "circuit_name", "circuit_country", "year", "race_round"]]
merged_df = pd.merge(driver_grid, circuits, on="raceId", how="inner")

# Add simulated pit stop count (1-stop for short races, 2-stop for longer)
merged_df['pit_stop_count'] = merged_df['race_round'].apply(lambda x: 1 if x < 10 else 2)

# Simulate pit lap based on pit_stop_count
def simulate_pit_lap(row):
    if row['pit_stop_count'] == 1:
        return np.random.randint(15, 26)
    else:  # 2-stop
        return np.random.randint(10, 21)

merged_df['pit_lap'] = merged_df.apply(simulate_pit_lap, axis=1)

# Simulate next tire based on pit_stop_count
def simulate_tire(row):
    if row['pit_stop_count'] == 1:
        return np.random.choice(['Medium', 'Hard'])
    else:
        return np.random.choice(['Soft', 'Medium', 'Hard'])

merged_df['next_tire'] = merged_df.apply(simulate_tire, axis=1)

# Prepare features and targets
X = pd.get_dummies(merged_df[["circuit_name", "circuit_country", "year", "driverId"]])
y_count = merged_df["pit_stop_count"]
y_lap = merged_df["pit_lap"]
y_tire = LabelEncoder().fit_transform(merged_df["next_tire"])
le_tire = LabelEncoder().fit(merged_df["next_tire"])

# Train simple models
rf_count = RandomForestClassifier(n_estimators=50, random_state=42)
rf_count.fit(X, y_count)

rf_lap = RandomForestRegressor(n_estimators=50, random_state=42)
rf_lap.fit(X, y_lap)

rf_tire = RandomForestClassifier(n_estimators=50, random_state=42)
rf_tire.fit(X, y_tire)

# --- 2️⃣ Flask Routes ---
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Get input values
        circuit = request.form["circuit"]
        country = request.form["country"]
        year = int(request.form["year"])
        driver = int(request.form["driverId"])
        
        # Create input dataframe
        input_df = pd.DataFrame({
            "circuit_name": [circuit],
            "circuit_country": [country],
            "year": [year],
            "driverId": [driver]
        })
        
        input_encoded = pd.get_dummies(input_df)
        
        # Align with training columns
        input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)
        
        # Predictions
        pit_count = int(rf_count.predict(input_encoded)[0])
        pit_lap = int(rf_lap.predict(input_encoded)[0])
        tire = le_tire.inverse_transform(rf_tire.predict(input_encoded))[0]

        prediction = {
            "Pit Stop Count": pit_count,
            "Pit Stop Lap": pit_lap,
            "Next Tire": tire
        }
        
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

# Student Placement Predictor

A machine learning web application that predicts whether a student is likely to be placed based on academic and skill-related inputs. The app trains a Random Forest classifier on historical placement data and serves predictions through a Flask API, with optional Docker deployment.

---

## Features

- Predict placement outcome from five input features
- Random Forest classifier trained on `student_placement_data.csv`
- Simple web form for real-time predictions
- Docker support for consistent local and cloud deployment

---

## Tech Stack

| Layer | Technology |
| --- | --- |
| Language | Python 3.10 |
| Web framework | Flask |
| ML | scikit-learn, pandas, NumPy |
| Production server | Gunicorn |
| Containerization | Docker |

---

## Project Structure

```text
Student-Placement_Predictor_App/
├── app.py                      # Flask app and prediction routes
├── train.py                    # Model training script
├── placement_model.pkl         # Serialized trained model
├── student_placement_data.csv  # Training dataset
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container build configuration
├── static/
│   └── style.css               # UI styles
└── templates/
    └── index.html              # Prediction form
```

---

## Input Features

| Field | Type | Range |
| --- | --- | --- |
| CGPA | Float | 0.00 – 10.00 |
| Communication Skills | Float | 0.0 – 10.0 |
| Resume Score | Float | 0.0 – 10.0 |
| Coding Score | Float | 0.0 – 10.0 |
| Placement Attendance | Float | 0.0% – 100.0% |

**Output**

- `1` — Placed
- `0` — Not Placed

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Local setup

```bash
# Navigate to the project folder
cd Student-Placement_Predictor_App

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train the model (generates placement_model.pkl)
python train.py

# Run the development server
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### Docker

```bash
docker build -t student-placement-app .
docker run -p 10000:10000 student-placement-app
```

Open [http://localhost:10000](http://localhost:10000).

---

## Deployment

The included `Dockerfile` runs the app with Gunicorn on port `10000`. You can deploy the container to any platform that supports Docker (Render, Railway, AWS, Azure, Google Cloud, etc.).

---

## Author

**Shrishkd**

---

## License

This project is open source and available for educational and personal use.

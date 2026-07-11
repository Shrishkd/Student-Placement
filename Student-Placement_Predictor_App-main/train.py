import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

FEATURE_COLUMNS = [
    "cgpa",
    "communication_skills",
    "resume_score",
    "coding_score",
    "attendance_placement",
]
TARGET_COLUMN = "placed"


def main():
    data = pd.read_csv("student_placement_data.csv")
    X = data[FEATURE_COLUMNS]
    y = data[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Model trained. Test accuracy: {accuracy:.2%}")

    with open("placement_model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)

    print("Saved model to placement_model.pkl")


if __name__ == "__main__":
    main()

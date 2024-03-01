# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import joblib


df = pd.read_csv('c:\\Users\\Frances\\Desktop\\PolarityPredictorApp\\data\\IMDB Dataset.csv')
X = df['review']
y = df['sentiment']

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with CountVectorizer and Decision Tree classifier
model = make_pipeline(CountVectorizer(), DecisionTreeClassifier())

# Train the model
model.fit(X_train, y_train)

# Save the trained model with the full path
joblib.dump(model, 'c:\\Users\\Frances\\Desktop\\PolarityPredictorApp\\data\\decision_tree_model.joblib')

# Evaluate the model on the validation set (optional)
val_predictions = model.predict(X_val)
accuracy = accuracy_score(y_val, val_predictions)
print(f"Validation Accuracy: {accuracy}")



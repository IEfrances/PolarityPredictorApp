# predict_sentiment.py

import joblib

# Load the trained model
model_path = 'c:\\Users\\Frances\\Desktop\\PolarityPredictorApp\\data\\decision_tree_model.joblib'
model = joblib.load(model_path)

# Function to predict sentiment for a given review
def predict_sentiment(review):
    # Use the trained model to predict sentiment
    prediction = model.predict([review])[0]
    return prediction

if __name__ == "__main__":
    # Input a review
    user_review = input("Enter a movie review: ")

    # Predict sentiment
    result = predict_sentiment(user_review)

    # Display the result
    print(f"Predicted Sentiment: {result}")

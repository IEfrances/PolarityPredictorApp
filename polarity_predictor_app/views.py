from django.shortcuts import render
from .models import MovieReview
from django.http import HttpResponse
from joblib import load 
import requests
import random

def project_info(request):
    return render(request, 'project_info.html') 

def get_random_movie_image(api_key):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc"
    response = requests.get(url)
    data = response.json()
    if data.get('results'):
        movie = random.choice(data['results'])  # Choose a random movie from the results
        poster_path = movie.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/original{poster_path}"
    return None

def predict_sentiment(review_text):
    # Load the trained model
    model = load('c:\\Users\\Frances\\Desktop\\PolarityPredictorApp\\data\\decision_tree_model.joblib')

    # Make predictions
    sentiment_prediction = model.predict([review_text])[0]

    return sentiment_prediction

def index(request):

    tmdb_api_key = '42ce80845529796cc18957014e223094'
    image_url = get_random_movie_image(tmdb_api_key)

    if request.method == 'POST':
        review_text = request.POST.get('review_text', '')
        image_url = request.POST.get('image_url', '')
        
        # Predict sentiment
        sentiment_prediction = predict_sentiment(review_text)

        # Save the review and prediction to the database
        MovieReview.objects.create(image_url = image_url, review = review_text, predicted_sentiment  = sentiment_prediction)

        return render(request, 'result.html', {'review_text': review_text, 'sentiment_prediction': sentiment_prediction,'image_url': image_url})
    
    return render(request, 'index.html',{'image_url': image_url})

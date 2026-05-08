import requests
import json


def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Custom header specifying the model ID
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parsing the JSON response from the API
    formatted_response = response.json()
    
    # Extract emotion scores from the response (adjust keys as per actual response structure)
    anger_score = formatted_response.get('anger', 0)
    disgust_score = formatted_response.get('disgust', 0)
    fear_score = formatted_response.get('fear', 0)
    joy_score = formatted_response.get('joy', 0)
    sadness_score = formatted_response.get('sadness', 0)
    
    # Create a dictionary of emotion scores
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Find the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the results including the dominant emotion
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
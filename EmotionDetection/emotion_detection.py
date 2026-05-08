import requests
import json

def emotion_detector(text_to_analyze):
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
    
    # Sending a POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    if response.status_code == 200:
        formatted_response = response.json()
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        desired_object = {
            'anger': emotion_scores.get('anger', 0),
            'disgust': emotion_scores.get('disgust', 0),
            'fear': emotion_scores.get('fear', 0),
            'joy': emotion_scores.get('joy', 0),
            'sadness': emotion_scores.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        desired_object = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Handle other unexpected responses
        desired_object = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    return desired_object
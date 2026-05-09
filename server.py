"""
Flask application for detecting emotions in text.
"""


from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")




@app.route("/emotionDetector")
def detect_emotions():
    """
    Endpoint to detect emotions from the given text.
    Returns a formatted string with emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Error: No text provided to analyze.", 400


    try:
        response = emotion_detector(text_to_analyze)


        anger = response.get('anger', 0)
        disgust = response.get('disgust', 0)
        fear = response.get('fear', 0)
        joy = response.get('joy', 0)
        sadness = response.get('sadness', 0)
        dominant_emotion = response.get('dominant_emotion')


        if dominant_emotion is None:
            return "Invalid text! Please try again!", 400


        response_text = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
        )
        return response_text


    except KeyError as key_err:
        return f"Missing expected key in response: {key_err}", 500
    except ValueError as val_err:
        return f"Value error: {val_err}", 500
    except Exception as err:  # Broad catch as fallback
        return f"An unexpected error occurred: {err}", 500




@app.route("/")
def render_index_page():
    """Render index.html page."""
    return render_template('index.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector") 

@app.route("/emotionDetector")
def detect_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze') 

    if not text_to_analyze:
        return "Error: No text provided for analysis.", 400

    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion and its score from the response
    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text, please try again!.", 400

    # Return a formatted string with the dominant emotion and its score
    return (
        "For the given statement, the system response is anger: {}, disgust: {}, fear: {}, joy: {} and sadness: {}. "
        "The dominant emotion is {}."
        .format(
            response['emotion_scores'].get('anger', 0),
            response['emotion_scores'].get('disgust', 0),
            response['emotion_scores'].get('fear', 0),
            response['emotion_scores'].get('joy', 0),
            response['emotion_scores'].get('sadness', 0),
            dominant_emotion
        ), 
        200
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
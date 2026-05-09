from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector") 

@app.route("/emotionDetector")
def detect_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the function and store the response 
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion and its score from the response
    dominant_emotion = response['dominant_emotion']
    score = response['emotion_scores'].get(dominant_emotion, 0)

    # Return a formatted string with the dominant emotion and its score
    return "The dominant emotion has been identified as {} with a score of {:.2f}.".format(dominant_emotion, score)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector") 

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    scores = response['emotion_scores']

    return (
        "For the given statement, the system response is anger: {:.6f}, disgust: {:.6f}, fear: {:.6f}, joy: {:.6f} and sadness: {:.6f}. "
        "The dominant emotion is {}."
        .format(
            scores.get('anger', 0),
            scores.get('disgust', 0),
            scores.get('fear', 0),
            scores.get('joy', 0),
            scores.get('sadness', 0),
            response['dominant_emotion']
        ), 
        200
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
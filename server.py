from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def detect_emotions():
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

    except Exception as err:
        return f"An error occurred: {err}", 500


@app.route("/")
def render_index_page():
    """Render the index.html page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
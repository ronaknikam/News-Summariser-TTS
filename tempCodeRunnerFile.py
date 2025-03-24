from flask import Flask, request, jsonify, send_file
from utils import fetch_news
from sentiment_analysis import analyze_sentiment
from comparative_analysis import comparative_analysis
from tts import generate_tts

app = Flask(__name__)

@app.route("/get_news", methods=["GET"])
def get_news():
    company = request.args.get("company", "")
    news = fetch_news(company)
    
    if "error" in news:
        return jsonify({"error": news["error"]})
    
    for article in news:
        article["sentiment"] = analyze_sentiment(article["title"])

    sentiment_data = comparative_analysis([a["sentiment"] for a in news])
    
    return jsonify({"company": company, "articles": news, "sentiment_summary": sentiment_data})

@app.route("/generate_tts", methods=["POST"])
def tts():
    text = request.json.get("text", "कोई जानकारी उपलब्ध नहीं है।")
    audio_path = generate_tts(text)
    return send_file(audio_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)


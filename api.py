from flask import Flask, request, jsonify, send_file
from utils import fetch_news, summarize_text
from sentiment_analysis import analyze_sentiment
from comparative_analysis import comparative_analysis
from tts import generate_tts
import os

app = Flask(__name__)

@app.route("/get_news", methods=["GET"])
def get_news():
    company = request.args.get("company", "")
    news = fetch_news(company)
    
    if "error" in news:
        return jsonify({"error": news["error"]})
    
    for article in news:
        article["summary"] = summarize_text(article["title"])  # Summarizing title (better: full text if available)
        article["sentiment"] = analyze_sentiment(article["summary"])

        # Generate Hindi TTS for the summary
        tts_path = f"tts_{hash(article['summary'])}.mp3"
        article["tts_path"] = generate_tts(article["summary"], tts_path)

    sentiment_data = comparative_analysis([a["sentiment"] for a in news])
    
    return jsonify({"company": company, "articles": news, "sentiment_summary": sentiment_data})

@app.route("/play_tts", methods=["GET"])
def play_tts():
    """Serve the generated TTS file for an article."""
    file_path = request.args.get("file")
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

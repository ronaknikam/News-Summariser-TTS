import streamlit as st
import requests

st.title("📢 News Summarizer & Sentiment Analysis")

company = st.text_input("Enter a Company Name")

if st.button("Fetch News"):
    response = requests.get(f"http://127.0.0.1:5000/get_news?company={company}")
    
    if response.status_code == 200:
        data = response.json()
        st.write(f"### 🏢 Company: {data['company']}")

        # Comparative Analysis
        st.subheader("📊 Sentiment Analysis Summary")
        st.write(data["sentiment_summary"])

        # Filter options
        filter_sentiment = st.selectbox("Filter by Sentiment", ["All", "Positive", "Negative", "Neutral"])

        for article in data["articles"]:
            if filter_sentiment != "All" and article["sentiment"] != filter_sentiment:
                continue  # Skip articles that don't match the filter
            
            st.subheader(article["title"])
            st.write(f"🔗 [Read More]({article['link']})")
            st.write(f"🗞 Sentiment: **{article['sentiment']}**")
            st.write(f"📖 Summary: {article['summary']}")

            # Play TTS
            tts_url = f"http://127.0.0.1:5000/play_tts?file={article['tts_path']}"
            st.audio(tts_url, format="audio/mp3")

    else:
        st.error("Error fetching news")

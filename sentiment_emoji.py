from transformers import pipeline
import emoji
from emoji_sentiment import classify_emoji

# Load model sentiment Bahasa Indonesia
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="taufiqdp/indonesian-sentiment"
)

label_map = {
    "positif": "positive",
    "negatif": "negative",
    "netral": "neutral",
    "positive": "positive",
    "negative": "negative",
    "neutral": "neutral"
}

def detect_emojis(text):
    return [char for char in text if char in emoji.EMOJI_DATA]

def sentiment_analysis(text):
    result = sentiment_pipeline(text)[0]
    raw_label = result['label'].lower()
    label = label_map.get(raw_label, "neutral")
    
    emojis = detect_emojis(text)
    emoji_sentiments = {e: classify_emoji(e) for e in emojis}
    
    return {
        "text": text,
        "sentiment": label,
        "emojis_found": emojis,
        "emoji_sentiments": emoji_sentiments
    }

# Contoh komentar
comments = [
    "Saya sangat senang dengan produk ini! 😍",
    "Layanan pelanggan buruk sekali 😡",
    "Biasa saja, tidak terlalu bagus 🤔",
    "Mantap sekali 👍👍",
    "Menarik"
]

for c in comments:
    analysis = sentiment_analysis(c)
    print(f"Teks: {analysis['text']}")
    print(f"Sentimen teks: {analysis['sentiment']}")
    print(f"Emoji terdeteksi: {analysis['emojis_found']}")
    print(f"Sentimen emoji: {analysis['emoji_sentiments']}\n")

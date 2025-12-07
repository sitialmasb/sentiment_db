# Custom library untuk klasifikasi emoji
emoji_sentiment_map = {
    # Positif
    "😊": "positive",
    "😍": "positive",
    "👍": "positive",
    "✨": "positive",
    "😁": "positive",
    "🥳": "positive",
    
    # Negatif
    "😡": "negative",
    "💔": "negative",
    "👎": "negative",
    "😢": "negative",
    "😭": "negative",
    "😠": "negative",
    
    # Netral
    "😐": "neutral",
    "🤔": "neutral",
    "😶": "neutral",
    "🙄": "neutral"
}

def classify_emoji(emoji_char):
    """Kembalikan kategori sentimen dari emoji"""
    return emoji_sentiment_map.get(emoji_char, "neutral")

# This script performs sentiment analysis on a list of text comments using the TextBlob library.
# For each comment, it calculates a polarity score (ranging from -1 to +1) and classifies it as:
# - Positive — polarity above 0.1
# - Negative — polarity below -0.1
# - Neutral — polarity between -0.1 and 0.1
# Results are printed in a formatted table showing the (truncated) text, sentiment label, and absolute polarity score.

# 1. Activate the virtual environment: python3 -m venv venv && source venv/bin/activate
# 2. Ensure textblob and corpora are installed: pip install textblob && python - m textblob.download_corpora
# 3. Run the script (using 'python', which points to the correct version in venv): python text_mood_analyzer.py

from textblob import TextBlob


def analyze_mood(comments):
    # Improved header alignment for better readability
    print(f"\n{'Text':<65} | {'Sentiment':<10} | {'Score'}")
    print("-" * 100)

    for comment in comments:
        analysis = TextBlob(comment)
        # polarity: from -1 (negative) to 1 (positive)
        polarity = analysis.sentiment.polarity
        threshold = 0.1

        if polarity > threshold:
            sentiment = "Positive"
        elif polarity < -threshold:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Using absolute value for the score to show intensity
        score = f"{abs(polarity):.2f}"

        # Truncate long strings to prevent breaking the table layout
        display_text = (comment[:62] + '..') if len(comment) > 65 else comment
        print(f"{display_text:<65} | {sentiment:<10} | {score}")


# Example usage
feedback_list = [
    "I love this product, it works perfectly!",
    "This is the worst experience I have ever had.",
    "Roses are red.",
    "The delivery was okay, but the box was damaged.",
    "Absolutely brilliant customer service!",
    "I don't like this product, it's too expensive.",
    "My name is Przemyslaw and I am pretty good Python developer.",
    "I am writing code."
]

if __name__ == "__main__":
    analyze_mood(feedback_list)
    print("")


# ==========================================
# TextBlob
# ==========================================

# TextBlob is a simple Python library for Natural Language Processing (NLP).
# It provides easy-to-use tools for tasks such as:
# - sentiment analysis (detecting if text is positive or negative)
# - tokenization (splitting text into words or sentences)
# - part-of-speech tagging (identifying nouns, verbs, etc.)
# - translation and spell correction
#

# ==========================================
# Corpora
# ==========================================

# Corpora (singular: corpus) are collections of text data used by NLP tools.
# In the context of TextBlob, corpora include dictionaries, language models,
# and datasets required for text analysis.
#
# TextBlob relies on external data (mainly from NLTK) to function properly,
# so these corpora often need to be downloaded separately using:
#     python -m textblob.download_corpora

# ==========================================
# In short:
# ==========================================

# - TextBlob = the tool/library
# - Corpora = the data it uses to analyze language

import nltk
import re
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Make sure you have these resources
nltk.download("punkt")
nltk.download("stopwords")

def extractive_summary(text, num_sentences=3):
    # Step 1: Clean text
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    
    # Step 2: Split into sentences
    sentences = sent_tokenize(text)
    
    # Step 3: Tokenize words & filter stopwords
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    
    # Step 4: Calculate word frequencies
    freq = {}
    for word in words:
        if word.isalnum() and word not in stop_words:
            freq[word] = freq.get(word, 0) + 1
    
    # Normalise frequencies
    max_freq = max(freq.values()) if freq else 1
    for word in freq:
        freq[word] = freq[word] / max_freq
    
    # Step 5: Score sentences
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]
    
    # Step 6: Select top N sentences
    best_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    # Step 7: Preserve original order
    summary = [s for s in sentences if s in best_sentences]
    
    return " ".join(summary)

# -------------------------
# Example usage:
text = """Climate change is one of the biggest challenges facing the world today. 
Rising global temperatures are causing more extreme weather events. 
Governments are working together to reduce carbon emissions. 
Scientists warn that urgent action is needed to prevent irreversible damage."""

print("Summary:\n", extractive_summary(text, num_sentences=2))
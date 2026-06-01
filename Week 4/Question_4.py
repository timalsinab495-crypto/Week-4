text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""
 
def word_frequency(text):
    words = text.lower().split()
    counts = {}
 
    for word in words:
        word = word.strip(".,!?;:'\"")
        if word:
            counts[word] = counts.get(word, 0) + 1
 
    top3 = sorted(counts, key=counts.get, reverse=True)[:3]
    return [(word, counts[word]) for word in top3]
 
print("\n---- Word Frequency ----")
print("Top 3 words:")
for word, count in word_frequency(text):
    print(f"{word} — {count} times")

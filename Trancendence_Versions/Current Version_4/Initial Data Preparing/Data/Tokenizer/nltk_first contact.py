from collections import Counter
import nltk

# Ensure that 'punkt' tokenizer is downloaded
nltk.download('punkt')


def main():
    """Calculate top term frequencies for a single document (text file)."""

    # Set n-gram size to 3
    n = 4
    # Set file path to the previous directory
    filepath = "../v4_step1_cleaned_diary.txt"

    print("Loading data...")

    # Load and process the text file
    corpus = load_data(filepath)

    # Compute n-grams
    ngrams = Counter(nltk.ngrams(corpus, n))

    # Print the most common n-grams
    for ngram, freq in ngrams.most_common(10):
        print(f"{freq}: {ngram}")


def load_data(filepath):
    """Load and tokenize text from a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        contents = [
            word.lower() for word in nltk.word_tokenize(f.read())
            if any(c.isalpha() for c in word)
        ]
    return contents


if __name__ == "__main__":
    main()

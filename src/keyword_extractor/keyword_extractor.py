from keybert import KeyBERT


class SentenceBert:
    def __init__(self):
        self.kw_model = KeyBERT()

    def extract_keywords(self, sentence, top_n: int = 5) -> list:
        keywords = self.kw_model.extract_keywords(
            sentence,
            keyphrase_ngram_range=(1, 1),
            stop_words="english",
            top_n=top_n,
            use_mmr=True,
            diversity=0.7,
        )

        keywords = [word[0] for word in keywords]

        return keywords

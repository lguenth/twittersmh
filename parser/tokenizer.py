import spacy
from tqdm.notebook import (
    tqdm,
)  # See: https://stackoverflow.com/questions/45595689/how-to-fix-tqdm-progress-apply-for-pandas-in-jupyter

tqdm.pandas()
nlp = spacy.load("de_dep_news_trf")


def cleaner(string):
    doc = nlp(string)
    lemmas = [token.lemma_ for token in doc]  # Remove tokens that are not alphabetic
    a_lemmas = [
        lemma for lemma in lemmas if lemma.isalpha() or lemma == "-PRON-"
    ]  # Print string after text cleaning
    return " ".join(a_lemmas)


de["text_cleaned"] = de["text"].progress_apply(cleaner)

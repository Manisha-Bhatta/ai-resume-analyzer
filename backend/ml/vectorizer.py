from sklearn.feature_extraction.text import TfidfVectorizer

class ResumeVectorizer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def vectorize(self, resume, job_description):
        vectors = self.vectorizer.fit_transform([resume, job_description])
        return vectors
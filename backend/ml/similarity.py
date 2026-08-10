from sklearn.metrics.pairwise import cosine_similarity

class ResumeMatcher:

    def similarity(self, vectors):
        score = cosine_similarity(vectors[0], vectors[1])
        return float(score[0][0]) * 100
from utils.pdf_parser import PDFParser
from utils.preprocess import TextPreprocessor
from utils.skill_extractor import SkillExtractor

from ml.vectorizer import ResumeVectorizer
from ml.similarity import ResumeMatcher

# -----------------------------
# STEP 1 : Read Resume PDF
# -----------------------------
parser = PDFParser()

resume_text = parser.extract_text("ResumeCloudKaptan2.pdf")

print("=" * 50)
print("RAW RESUME TEXT")
print("=" * 50)
print(resume_text)

# -----------------------------
# STEP 2 : Preprocess Resume
# -----------------------------
processor = TextPreprocessor()

tokens = processor.clean_text(resume_text)

print("\n")
print("=" * 50)
print("TOKENS")
print("=" * 50)
print(tokens)

# -----------------------------
# STEP 3 : Extract Skills
# -----------------------------
extractor = SkillExtractor()

skills = extractor.extract(tokens)

print("\n")
print("=" * 50)
print("DETECTED SKILLS")
print("=" * 50)
print(skills)

# -----------------------------
# STEP 4 : Sample Job Description
# -----------------------------
job_description = """
We are looking for a Software Engineer.

Required Skills:

Python
React
SQL
Docker
AWS
Git
Machine Learning
"""

# -----------------------------
# STEP 5 : TF-IDF Vectorization
# -----------------------------
vectorizer = ResumeVectorizer()

vectors = vectorizer.vectorize(
    resume_text,
    job_description
)

# -----------------------------
# STEP 6 : Cosine Similarity
# -----------------------------
matcher = ResumeMatcher()

score = matcher.similarity(vectors)

print("\n")
print("=" * 50)
print("MATCH SCORE")
print("=" * 50)
print(f"{score:.2f}%")
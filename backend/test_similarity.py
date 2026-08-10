from utils.preprocess import TextPreprocessor
from utils.skill_extractor import SkillExtractor
from ml.vectorizer import ResumeVectorizer
from ml.similarity import ResumeMatcher


# -----------------------------------
# Initialize components
# -----------------------------------

processor = TextPreprocessor()
extractor = SkillExtractor()
vectorizer = ResumeVectorizer()
matcher = ResumeMatcher()


# -----------------------------------
# Sample resume
# -----------------------------------

resume = """
Software Engineer with experience in Python, React, Spring Boot,
MySQL and Git. Built REST API applications using Spring Boot.
"""


# -----------------------------------
# Job description
# -----------------------------------

job_description = """
We are looking for a Software Engineer with experience in:
Python React Spring Boot Docker AWS MySQL Git REST APIs
"""


# -----------------------------------
# Preprocessing
# -----------------------------------

resume_tokens = processor.clean_text(resume)
job_tokens = processor.clean_text(job_description)


# -----------------------------------
# Skill extraction
# -----------------------------------

resume_skills = extractor.extract(resume_tokens)
job_skills = extractor.extract(job_tokens)


print("RESUME SKILLS:")
print(resume_skills)

print("\nJOB SKILLS:")
print(job_skills)


# -----------------------------------
# Missing skills
# -----------------------------------

missing_skills = sorted(
    set(job_skills) - set(resume_skills)
)

print("\nMISSING SKILLS:")
print(missing_skills)


# -----------------------------------
# TF-IDF
# -----------------------------------

resume_skill_text = " ".join(resume_skills)
job_skill_text = " ".join(job_skills)


vectors = vectorizer.vectorize(
    resume_skill_text,
    job_skill_text
)


print("\nTF-IDF VECTOR SHAPE:")
print(vectors.shape)


# -----------------------------------
# Cosine Similarity
# -----------------------------------

match_score = matcher.similarity(vectors)


print("\nMATCH SCORE:")
print(match_score)
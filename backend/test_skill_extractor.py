from utils.skill_extractor import SkillExtractor
from utils.preprocess import TextPreprocessor


processor = TextPreprocessor()
extractor = SkillExtractor()


job_description = """
We are looking for a Software Engineer with experience in:
Python React Spring Boot Docker AWS MySQL Git REST APIs
"""


tokens = processor.clean_text(job_description)

print("TOKENS:")
print(tokens)

skills = extractor.extract(tokens)

print("\nDETECTED SKILLS:")
print(skills)
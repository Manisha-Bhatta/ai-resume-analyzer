from utils.preprocess import TextPreprocessor

processor = TextPreprocessor()

text = "I have worked with Python, React and Spring Boot."

tokens = processor.clean_text(text)

print(tokens)
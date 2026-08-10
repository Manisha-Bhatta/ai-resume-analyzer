from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from utils.pdf_parser import PDFParser
from utils.preprocess import TextPreprocessor
from utils.skill_extractor import SkillExtractor

from ml.vectorizer import ResumeVectorizer
from ml.similarity import ResumeMatcher
from ml.ats_scorer import ATSScorer


app = FastAPI(
    title="AI Resume Analyzer",
    description="Resume Analyzer using NLP and Machine Learning",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://ai-resume-analyzer-three-cyan.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is Running 🚀"
    }


@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    try:

        # ==========================================
        # 1. Create uploads directory
        # ==========================================

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            file.filename
        )


        # ==========================================
        # 2. Save uploaded PDF
        # ==========================================

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        # ==========================================
        # 3. Extract text from PDF
        # ==========================================

        parser = PDFParser()

        resume_text = parser.extract_text(
            file_path
        )


        # ==========================================
        # 4. NLP preprocessing
        # ==========================================

        processor = TextPreprocessor()

        resume_tokens = processor.clean_text(
            resume_text
        )

        job_tokens = processor.clean_text(
            job_description
        )


        # ==========================================
        # 5. Extract skills
        # ==========================================

        extractor = SkillExtractor()

        resume_skills = extractor.extract(
            resume_tokens
        )

        job_skills = extractor.extract(
            job_tokens
        )


        # ==========================================
        # 6. Find missing skills
        # ==========================================

        missing_skills = sorted(
            set(job_skills) - set(resume_skills)
        )


        # ==========================================
        # 7. Prepare text for TF-IDF
        # ==========================================

        resume_skill_text = " ".join(
            resume_skills
        )

        job_skill_text = " ".join(
            job_skills
        )


        # ==========================================
        # 8. TF-IDF Vectorization
        # ==========================================

        vectorizer = ResumeVectorizer()

        vectors = vectorizer.vectorize(
            resume_skill_text,
            job_skill_text
        )


        # ==========================================
        # 9. Cosine Similarity
        # ==========================================

        matcher = ResumeMatcher()

        match_score = matcher.similarity(
            vectors
        )


        # ==========================================
        # 10. ATS Score
        # ==========================================

        ats = ATSScorer().calculate_score(
            resume_text,
            resume_skills,
            job_skills
        )


        # ==========================================
        # 11. Return final result
        # ==========================================

        return {

            "filename": file.filename,

            "match_score": round(
                match_score,
                2
            ),

            "ats_score": ats["ats_score"],

            "ats_breakdown": ats["breakdown"],

            "resume_skills": resume_skills,

            "job_skills": job_skills,

            "missing_skills": missing_skills,

            "resume_text": resume_text

        }


    except Exception as e:

        return {
            "error": str(e)
        }
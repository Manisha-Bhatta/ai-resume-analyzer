class ATSScorer:

    def calculate_score(
        self,
        resume_text,
        resume_skills,
        job_skills
    ):

        resume_lower = resume_text.lower()

        # --------------------------
        # Skill Match (50)
        # --------------------------
        matched = len(set(resume_skills) & set(job_skills))
        total = max(len(set(job_skills)), 1)

        skill_score = (matched / total) * 50

        # --------------------------
        # Contact Information (5)
        # --------------------------
        contact_score = 0

        if "@" in resume_text:
            contact_score += 2

        if "linkedin" in resume_lower:
            contact_score += 1

        if "github" in resume_lower:
            contact_score += 1

        if "phone" in resume_lower:
            contact_score += 1

        # --------------------------
        # Education (10)
        # --------------------------
        education_score = 0

        education_keywords = [
            "bachelor",
            "b.tech",
            "computer science",
            "engineering",
            "university"
        ]

        for word in education_keywords:
            if word in resume_lower:
                education_score += 2

        education_score = min(education_score, 10)

        # --------------------------
        # Projects (15)
        # --------------------------
        project_score = 0

        if "projects" in resume_lower:
            project_score += 5

        project_keywords = [
            "react",
            "spring boot",
            "mysql",
            "api",
            "github"
        ]

        for word in project_keywords:
            if word in resume_lower:
                project_score += 2

        project_score = min(project_score, 15)

        # --------------------------
        # Experience (10)
        # --------------------------
        experience_score = 0

        experience_keywords = [
            "internship",
            "experience",
            "campus ambassador"
        ]

        for word in experience_keywords:
            if word in resume_lower:
                experience_score += 3

        experience_score = min(experience_score, 10)

        # --------------------------
        # Certifications (10)
        # --------------------------
        certification_score = 0

        certification_keywords = [
            "certificate",
            "certification",
            "cisco",
            "credly"
        ]

        for word in certification_keywords:
            if word in resume_lower:
                certification_score += 2.5

        certification_score = min(certification_score, 10)

        # --------------------------
        # Final ATS Score
        # --------------------------
        final_score = round(

            skill_score

            + contact_score

            + education_score

            + project_score

            + experience_score

            + certification_score,

            2

        )

        return {

            "ats_score": final_score,

            "breakdown": {

                "skill_match": round(skill_score, 2),

                "contact_information": contact_score,

                "education": education_score,

                "projects": project_score,

                "experience": experience_score,

                "certifications": certification_score

            }

        }
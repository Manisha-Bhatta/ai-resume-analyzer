from data.skills import SKILLS
import re


class SkillExtractor:

    def extract(self, tokens):
        """
        Extract technical skills from preprocessed tokens.
        """

        detected = set()

        tokens = [
            str(token).lower().strip()
            for token in tokens
            if token
        ]

        token_string = " ".join(tokens)

        # -----------------------------------------
        # Single-word skills
        # -----------------------------------------

        for skill in SKILLS:

            skill = skill.lower().strip()

            if not skill:
                continue

            if " " not in skill:

                if skill in tokens:
                    detected.add(skill)

        # -----------------------------------------
        # Multi-word skills
        # -----------------------------------------

        for skill in SKILLS:

            skill = skill.lower().strip()

            if not skill or " " not in skill:
                continue

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, token_string):
                detected.add(skill)

        # -----------------------------------------
        # REST API normalization
        # -----------------------------------------

        if "rest" in tokens:

            if "api" in tokens or "apis" in tokens:
                detected.add("rest api")

        # Remove plural variation
        detected.discard("rest apis")

        # -----------------------------------------
        # Spring Boot normalization
        # -----------------------------------------

        if "spring boot" in detected:
            detected.discard("spring")

        return sorted(detected)
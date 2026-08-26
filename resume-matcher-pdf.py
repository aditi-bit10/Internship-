import streamlit as st
import re
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📄 Resume Matcher")

resume_file = st.file_uploader("Upload Resume", type="pdf")

job = st.text_area("Enter Job Description")

def get_resume_text(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def clean(text):
    text = text.lower()
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text


if st.button("Match Resume"):

    if resume_file is None:
        st.error("Please upload your resume.")

    elif job.strip() == "":
        st.error("Please enter job description.")

    else:

        resume = get_resume_text(resume_file)

        resume = clean(resume)
        job = clean(job)

        # Convert text into numbers
        vectorizer = TfidfVectorizer(stop_words="english")

        vectors = vectorizer.fit_transform([
            resume,
            job
        ])

        # Calculate similarity
        score = cosine_similarity(
            vectors[0],
            vectors[1]
        )[0][0]

        percentage = score * 100

        st.subheader("📊 Match Result")

        st.metric(
            "Resume Match Score",
            f"{percentage:.0f}%"
        )

        if score >= 0.70:
            st.success("🎉 Excellent Match!")

        elif score >= 0.50:
            st.warning("👍 Good Match!")

        else:
            st.error("❌ Low Match")

        # Find missing keywords
        words = vectorizer.get_feature_names_out()

        resume_words = set(resume.split())

        missing = []

        for word in words:
            if word not in resume_words:
                missing.append(word)

        st.subheader("🔍 Missing Keywords")

        if missing:
            st.write(", ".join(missing))
        else:
            st.success("No missing keywords!")
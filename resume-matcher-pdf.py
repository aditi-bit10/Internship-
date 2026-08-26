import streamlit as st
import re
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0B3D2E,
        #145A32,
        #8A6D1D,
        #D4AF37
    );
    color: white;
    min-height: 100vh;
}

/* Main Title */
h1 {
    color: #FFD700;
    text-align: center;
    font-weight: bold;
}

/* Headings */
h2, h3 {
    color: #FFD700;
}

/* Normal text */
p, label {
    color: white !important;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background-color: rgba(0, 0, 0, 0.25);
    border: 2px solid #D4AF37;
    border-radius: 12px;
    padding: 15px;
}

/* Text Area */
textarea {
    background-color: rgba(0, 0, 0, 0.35) !important;
    color: white !important;
    border: 2px solid #D4AF37 !important;
    border-radius: 10px !important;
}

/* Button */
.stButton > button {
    background-color: #D4AF37;
    color: #0B3D2E;
    border: 2px solid #FFD700;
    border-radius: 10px;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    background-color: #FFD700;
    color: #0B3D2E;
}

/* Metric */
[data-testid="stMetric"] {
    background-color: rgba(0, 0, 0, 0.35);
    border: 2px solid #D4AF37;
    border-radius: 12px;
    padding: 15px;
}

[data-testid="stMetricValue"] {
    color: #FFD700;
}

/* Divider */
hr {
    border-color: #D4AF37;
}

</style>
""", unsafe_allow_html=True)

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
import streamlit as st

from api import upload_resume
from api import upload_job
from api import match

st.set_page_config(page_title="Candidate Evaluation AI")

st.title("🤖 Candidate Evaluation AI")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job = st.file_uploader(
    "Upload Job Description",
    type=["txt"]
)

if st.button("Evaluate Candidate"):

    if resume and job:

        resume_result = upload_resume(resume)

        job_result = upload_job(job)

        result = match(
            resume_result["candidate_id"],
            job_result["job_id"]
        )

        st.success("Evaluation Complete!")

        st.json(result)

    else:

        st.warning("Upload both files.")
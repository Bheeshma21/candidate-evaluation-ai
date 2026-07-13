import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_resume(file):
    files = {
        "file": (
            file.name,
            file,
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BASE_URL}/resume/upload",
        files=files
    )

    return response.json()


def upload_job(file):
    files = {
        "file": (
            file.name,
            file,
            "text/plain"
        )
    }

    response = requests.post(
        f"{BASE_URL}/job/upload",
        files=files
    )

    return response.json()



def match(candidate_id, job_id):
    response = requests.post(
        f"{BASE_URL}/ai/match",
        params={
            "candidate_id": candidate_id,
            "job_id": job_id
        }
    )

    return response.json()
console.log("script loaded");

const scheduleBtn = document.getElementById("scheduleInterview");
const sendEmailBtn = document.getElementById("sendEmail");
const analyzeBtn = document.getElementById("analyzeBtn");
const startInterviewBtn = document.getElementById("startInterview");
const downloadBtn = document.getElementById("downloadReport");

let latestResult = null;
let latestResume = null;

/* ============================
   ANALYZE RESUME
============================ */

analyzeBtn.addEventListener("click", async () => {

    const resumeFile = document.getElementById("resume").files[0];
    const jobDescription = document.getElementById("jobDescription").value;

    if (!resumeFile) {
        alert("Please upload resume.");
        return;
    }

    if (!jobDescription.trim()) {
        alert("Please enter Job Description.");
        return;
    }

    analyzeBtn.disabled = true;
    analyzeBtn.innerText = "Analyzing...";
    document.getElementById("loading").style.display = "block";

    try {

        /* Resume Upload */

        const formData = new FormData();
        formData.append("file", resumeFile);

        const resumeResponse = await fetch(
            "http://127.0.0.1:8000/resume/upload",
            {
                method: "POST",
                body: formData
            }
        );

        latestResume = await resumeResponse.json();

        /* Job Upload */

        const jobResponse = await fetch(
            "http://127.0.0.1:8000/job/create",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    job_description: jobDescription
                })
            }
        );

        const jobData = await jobResponse.json();

        /* AI Match */

        const matchResponse = await fetch(
            "http://127.0.0.1:8000/ai/match",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    candidate_id: latestResume.candidate_id,
                    job_id: jobData.job_id
                })
            }
        );

        latestResult = await matchResponse.json();

        console.log(latestResult);

        /* SCORE */

        document.getElementById("score").innerText =
            latestResult.match_score + "%";

        const progress =
            document.getElementById("progressBar");

        progress.style.width =
            latestResult.match_score + "%";

        progress.innerText =
            latestResult.match_score + "%";

        if (latestResult.match_score >= 80)
            progress.style.background = "#16a34a";
        else if (latestResult.match_score >= 60)
            progress.style.background = "#eab308";
        else
            progress.style.background = "#dc2626";

        /* Recommendation */

        document.getElementById("recommendation").innerText =
            latestResult.recommendation;

        document.getElementById("ready").innerText =
            latestResult.match_score >= 70 ? "YES" : "NO";

        /* Matched Skills */

        const matched =
            document.getElementById("matchedSkills");

        matched.innerHTML = "";

        (latestResult.match_result?.matched_skills || []).forEach(skill => {

            matched.innerHTML +=
                `<span class="skill-chip matched">✓ ${skill}</span>`;

        });

        /* Missing Skills */

        const missing =
            document.getElementById("missingSkills");

        missing.innerHTML = "";

        (latestResult.match_result?.missing_skills || []).forEach(skill => {

            missing.innerHTML +=
                `<span class="skill-chip missing">✗ ${skill}</span>`;

        });

        downloadBtn.disabled = false;

        startInterviewBtn.disabled =
            latestResult.match_score < 70;

    }

    catch (err) {

        console.error(err);

        alert("Something went wrong.");

    }

    finally {

        analyzeBtn.disabled = false;

        analyzeBtn.innerText = "Analyze Resume";

        document.getElementById("loading").style.display = "none";

    }

});


/* ============================
   START INTERVIEW
============================ */

startInterviewBtn.addEventListener("click", async () => {

    try {

        await fetch(
            "http://127.0.0.1:8000/voice/start",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    job_description:
                        document.getElementById("jobDescription").value
                })
            }
        );

        window.location.href =
            "http://127.0.0.1:8501/interview";

    }

    catch (err) {

        console.error(err);

        alert("Unable to start interview.");

    }

});


/* ============================
   DOWNLOAD REPORT
============================ */

downloadBtn.addEventListener("click", () => {

    if (!latestResult)
        return;

    const report = `
AI Candidate Evaluation Report

Match Score:
${latestResult.match_score}%

Recommendation:
${latestResult.recommendation}

Matched Skills:
${(latestResult.match_result?.matched_skills || []).join(", ")}

Missing Skills:
${(latestResult.match_result?.missing_skills || []).join(", ")}

Interview Ready:
${latestResult.match_score >= 70 ? "YES" : "NO"}
`;

    const blob =
        new Blob([report], { type: "text/plain" });

    const url =
        URL.createObjectURL(blob);

    const a =
        document.createElement("a");

    a.href = url;

    a.download = "AI_Evaluation_Report.txt";

    a.click();

    URL.revokeObjectURL(url);

});


/* ============================
   SEND EMAIL
============================ */

sendEmailBtn.addEventListener("click", async () => {

    const email =
        document.getElementById("candidateEmail").value;

    if (!email) {

        alert("Enter Candidate Email");

        return;

    }

    const response = await fetch(
        "http://127.0.0.1:8000/email/send",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                candidate_name: latestResume.name,
                score: latestResult.match_score
            })
        }
    );

    const data = await response.json();

    alert(data.message);

});


/* ============================
   SCHEDULE INTERVIEW
============================ */

scheduleBtn.addEventListener("click", async () => {

    const response = await fetch(
        "http://127.0.0.1:8000/interview/send",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({

                email:
                    document.getElementById("candidateEmail").value,

                candidate_name:
                    latestResume.name,

                interview_date:
                    document.getElementById("interviewDate").value,

                interview_time:
                    document.getElementById("interviewTime").value,

                interviewer:
                    document.getElementById("interviewer").value,

                meeting_link:
                    document.getElementById("meetingLink").value

            })
        }
    );

    const data = await response.json();

    alert(data.message);

});
async function startInterview() {

    // Read the job role from the textbox
    const job =
        document.getElementById("job").value || "Python Developer";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/voice/start",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    job_description: job
                })
            }
        );

        const result = await response.json();

        console.log("Interview Started:", result);

        document.getElementById("status").innerText =
            "Interview Status: Interview Started";

    }

    catch (err) {

        console.error("Start Interview Error:", err);

        document.getElementById("status").innerText =
            "Interview Status: Failed to start";

    }

}

async function updateInterview() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/voice/live"
        );

        const data = await response.json();

        console.log("LIVE DATA:", data);

        document.getElementById("question").innerText =
            data.question && data.question.trim() !== ""
                ? data.question
                : "Waiting for interview...";

        document.getElementById("answer").innerText =
            data.answer && data.answer.trim() !== ""
                ? data.answer
                : "Waiting for candidate...";

        document.getElementById("status").innerText =
            "Interview Status: " +
            (data.status || "Waiting...");

    }

    catch (err) {

        console.error("Live Update Error:", err);

        document.getElementById("status").innerText =
            "Interview Status: Connection Error";

    }

}

// Start polling immediately
updateInterview();

// Refresh every second
setInterval(updateInterview, 1000);
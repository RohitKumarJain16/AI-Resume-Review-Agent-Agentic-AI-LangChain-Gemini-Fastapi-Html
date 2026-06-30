const analyzeBtn = document.getElementById("analyzeBtn");
const fileInput = document.getElementById("resume");
const fileName = document.getElementById("fileName");
const loading = document.getElementById("loading");
const results = document.getElementById("results");
const overallScore = document.getElementById("overallScore");
const scoreBar = document.getElementById("scoreBar");
const atsResult = document.getElementById("atsResult");
const skillsResult = document.getElementById("skillsResult");
const projectResult = document.getElementById("projectResult");
const hrResult = document.getElementById("hrResult");
const downloadBtn = document.getElementById("downloadBtn");
const errorMessage = document.getElementById("errorMessage");
const apiStatus = document.getElementById("apiStatus");

let reportContent = "";

function setError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.toggle("hidden", !message);
}

function markdownToHtml(markdown) {
    return markdown
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/^### (.*)$/gm, "<h3>$1</h3>")
        .replace(/^## (.*)$/gm, "<h2>$1</h2>")
        .replace(/^# (.*)$/gm, "<h1>$1</h1>")
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/^- (.*)$/gm, "<li>$1</li>")
        .replace(/(<li>.*<\/li>)/gs, "<ul>$1</ul>")
        .replace(/\n{2,}/g, "<br><br>")
        .replace(/\n/g, "<br>");
}

async function checkApiStatus() {
    try {
        const response = await fetch("/health");

        if (!response.ok) {
            throw new Error("API returned an error");
        }

        apiStatus.textContent = "API online";
        apiStatus.classList.add("online");
        apiStatus.classList.remove("offline");
    } catch (error) {
        apiStatus.textContent = "API offline";
        apiStatus.classList.add("offline");
        apiStatus.classList.remove("online");
    }
}

fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    fileName.textContent = file ? file.name : "Choose a resume PDF";
    setError("");
});

analyzeBtn.addEventListener("click", async () => {
    const file = fileInput.files[0];

    if (!file) {
        setError("Please upload a PDF resume.");
        return;
    }

    if (file.type !== "application/pdf" && !file.name.toLowerCase().endsWith(".pdf")) {
        setError("Only PDF files are supported.");
        return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    analyzeBtn.disabled = true;
    loading.classList.remove("hidden");
    results.classList.add("hidden");
    setError("");

    try {
        const response = await fetch("/analyze-resume", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Server error while analyzing resume.");
        }

        const score = Number(data.overall_score || 0);
        overallScore.textContent = score;
        scoreBar.style.width = `${Math.max(0, Math.min(score, 100))}%`;

        atsResult.innerHTML = markdownToHtml(data.ats || "No ATS feedback returned.");
        skillsResult.innerHTML = markdownToHtml(data.skills || "No skills feedback returned.");
        projectResult.innerHTML = markdownToHtml(data.projects || "No project feedback returned.");
        hrResult.innerHTML = markdownToHtml(data.hr || "No HR feedback returned.");

        reportContent = data.report || "";
        results.classList.remove("hidden");
    } catch (error) {
        setError(error.message || "Something went wrong.");
    } finally {
        analyzeBtn.disabled = false;
        loading.classList.add("hidden");
    }
});

downloadBtn.addEventListener("click", () => {
    if (!reportContent) {
        setError("No report is available yet.");
        return;
    }

    const blob = new Blob([reportContent], {
        type: "text/markdown",
    });

    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");

    a.href = url;
    a.download = "Resume_Report.md";
    a.click();

    window.URL.revokeObjectURL(url);
});

checkApiStatus();

const API_URL = "http://127.0.0.1:5000";

async function analyzeSymptoms() {

    const age = document.getElementById("age").value;
    const symptom = document.getElementById("symptoms").value.trim();

    const result = document.getElementById("result");
    const button = document.getElementById("analyzeBtn");

    if (!age || !symptom) {
        alert("Please enter age and symptoms!");
        return;
    }

    button.disabled = true;
    button.innerText = "Analysing...";

    try {

        const response = await fetch(API_URL + "/api/symptoms", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                age: age,
                symptom: symptom
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong");
        }

        result.style.display = "block";

        result.innerHTML = `
            <h3>Assessment Result</h3>
            <p><strong>Status:</strong> ${escapeHTML(data.status)}</p>
            <p><strong>Guidance:</strong> ${escapeHTML(data.message)}</p>
        `;

    } catch (error) {

        result.style.display = "block";
        result.textContent = "Error: " + error.message;

    } finally {

        button.disabled = false;
        button.innerText = "Analyse Symptoms";

    }
}


async function savePatient() {

    const age = document.getElementById("age").value;
    const symptoms = document.getElementById("symptoms").value.trim();

    if (!age || !symptoms) {
        alert("Please enter age and symptoms!");
        return;
    }

    try {

        const response = await fetch(API_URL + "/save", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                age: age,
                symptoms: symptoms
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to save details");
        }

        alert(data.message);

    } catch (error) {

        alert("Error: " + error.message);

    }
}


function escapeHTML(value) {

    return String(value).replace(/[&<>"']/g, char => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[char]);

}

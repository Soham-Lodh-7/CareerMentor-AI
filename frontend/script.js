document.getElementById("careerForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const interests = document.getElementById("interests").value;
    const skills = document.getElementById("skills").value;
    const dream = document.getElementById("dream").value;

    const payload = { name, interests, skills, dream };

    try {
        const response = await fetch("http://127.0.0.1:5000/recommend", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        console.log("Backend response:", result);

        if (result.recommendations) {
            result.name = name;
            localStorage.setItem("career_results", JSON.stringify(result));
            window.location.href = "result.html";
        } else {
            alert("Something went wrong!");
        }
    } catch (error) {
        console.error(error);
        alert("Error connecting to backend.");
    }
});

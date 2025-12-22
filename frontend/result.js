const data = JSON.parse(localStorage.getItem("career_results"));
const container = document.getElementById("results-container");

if (!data || !data.recommendations || data.recommendations.length === 0) {
    container.innerHTML = "<p>No recommendations found.</p>";
} else {
    const greeting = document.createElement("h2");
    greeting.textContent = `Hi ${data.name}, here are your career recommendations:`;
    container.appendChild(greeting);

    data.recommendations.forEach(item => {
        const card = document.createElement("div");
        card.classList.add("card");
        card.innerHTML = `<h3>${item.title}</h3><p>${item.reason}</p>`;
        container.appendChild(card);
    });
}

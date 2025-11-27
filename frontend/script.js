function displayResults(results) {
    const container = document.getElementById("resultsContainer");
    container.innerHTML = "";

    results.forEach(item => {
        const card = document.createElement("div");
        card.className = "result-card";

        card.innerHTML = `
            <div class="title">${item.title}</div>
            <div class="link">${item.url}</div>
            <div class="snippet">${item.snippet}</div>
        `;

        container.appendChild(card);
    });
}

document.addEventListener("DOMContentLoaded", function () {

    // 1. Mobile Menu Toggle
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", function () {
            navLinks.classList.toggle("show");
        });
    }

    // 2. Prediction Form Submission
    const form = document.getElementById("predictionForm");
    const resultDiv = document.getElementById("result");

    if (form) {
        form.addEventListener("submit", async function (e) {
            e.preventDefault();

            const data = {};
            new FormData(form).forEach((value, key) => {
                data[key] = value;
            });

            let apiURL = "";
            if (data.area) {
                apiURL = "/predict/chennai";
            } else if (data.sqft) {
                apiURL = "/predict/bengaluru";
            }

            const btn = document.getElementById("predictBtn") || form.querySelector("button[type='submit']");
            const originalBtnText = btn ? btn.textContent : "Predict Price";

            try {
                if (btn) {
                    btn.disabled = true;
                    btn.textContent = "Calculating...";
                }

                const response = await fetch(apiURL, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                if (resultDiv) {
                    resultDiv.style.display = "block";
                    resultDiv.className = "result-success";
                    resultDiv.innerHTML = `Estimated Price: <strong>₹ ${result.predicted_price} ${result.unit}</strong>`;
                }

            } catch (error) {
                if (resultDiv) {
                    resultDiv.style.display = "block";
                    resultDiv.className = "result-error";
                    resultDiv.innerHTML = "Prediction Failed. Please check inputs and try again.";
                }
                console.error(error);
            } finally {
                if (btn) {
                    btn.disabled = false;
                    btn.textContent = originalBtnText;
                }
            }
        });
    }

});
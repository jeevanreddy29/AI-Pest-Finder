const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const previewArea = document.getElementById("previewArea");
const placeholder = document.querySelector(".preview-placeholder");

const analyzeBtn = document.getElementById("analyzeBtn");
const loading = document.getElementById("loading");
const resultCard = document.getElementById("resultCard");


/* IMAGE UPLOAD */

imageInput.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) {
        return;
    }

    if (!file.type.startsWith("image/")) {
        alert("Please select a valid image.");
        return;
    }

    if (file.size > 10 * 1024 * 1024) {
        alert("Image size must be less than 10MB.");
        return;
    }

    const reader = new FileReader();

    reader.onload = function (event) {

        previewImage.src = event.target.result;

        previewImage.style.display = "block";

        placeholder.style.display = "none";

        resultCard.style.display = "none";
    };

    reader.readAsDataURL(file);
});


/* DRAG AND DROP */

const uploadArea = document.getElementById("uploadArea");

uploadArea.addEventListener("dragover", function (event) {

    event.preventDefault();

    uploadArea.style.borderColor = "#218838";
});

uploadArea.addEventListener("dragleave", function () {

    uploadArea.style.borderColor = "#a9c9ad";
});

uploadArea.addEventListener("drop", function (event) {

    event.preventDefault();

    uploadArea.style.borderColor = "#a9c9ad";

    const file = event.dataTransfer.files[0];

    if (!file || !file.type.startsWith("image/")) {

        alert("Please drop a valid image.");

        return;
    }

    imageInput.files = event.dataTransfer.files;

    const reader = new FileReader();

    reader.onload = function (event) {

        previewImage.src = event.target.result;

        previewImage.style.display = "block";

        placeholder.style.display = "none";
    };

    reader.readAsDataURL(file);
});


/* AI ANALYSIS */

async function analyzeImage() {

    if (!imageInput.files.length) {
        alert("Please upload a crop image first.");
        return;
    }

    analyzeBtn.style.display = "none";
    loading.style.display = "block";
    resultCard.style.display = "none";

    const file = imageInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    try {

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (!result.success) {

    if (result.type === "not_supported") {

        alert(
            "Image Not Supported\n\n" +
            result.message
        );

    } else {

        throw new Error(
            result.error || "Prediction failed."
        );
    }

    return;
}

        document.getElementById("pestName").textContent =
            result.pest;

        document.getElementById("pestResult").textContent =
            result.pest;

        document.querySelector(".confidence").textContent =
            result.confidence + "% Confidence";

        const levelEl = document.getElementById("infestationLevel");
        if (levelEl && result.confidence_level) {
            levelEl.textContent = result.confidence_level;
        }

        document.querySelector(".treatment p").textContent =
            result.management;

        resultCard.style.display = "block";

        resultCard.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

    } catch (error) {

        console.error("Prediction error:", error);

        alert(
            "Unable to analyze the image.\n\n" +
            "Please make sure the AI backend is running."
        );

    } finally {

        loading.style.display = "none";
        analyzeBtn.style.display = "block";
    }
}


/* SCROLL */

function scrollToDetector() {

    document.getElementById("detect").scrollIntoView({
        behavior: "smooth"
    });

}
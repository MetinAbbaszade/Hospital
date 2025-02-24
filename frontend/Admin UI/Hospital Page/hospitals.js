 document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal");
    const addHospitalLeft = document.getElementById("addHospitalLeft");
    const addHospitalRight = document.getElementById("addHospitalRight");
    const closeModal = document.querySelector(".close");
    const saveHospital = document.getElementById("saveHospital");
    const hospitalList = document.getElementById("hospitalList");
    const searchInput = document.getElementById('hospitalSearch');
    const hospitalCards = document.querySelectorAll('.hospital-card');

    addHospitalLeft.addEventListener("click", () => {
        modal.style.display = "block";
    });

    addHospitalRight.addEventListener("click", () => {
        alert('New hospital addition feature coming soon!');
    });

    closeModal.addEventListener("click", () => {
        modal.style.display = "none";
    });

    saveHospital.addEventListener("click", () => {
        const name = document.getElementById("hospitalName").value;
        const location = document.getElementById("hospitalLocation").value;
        const hours = document.getElementById("hospitalHours").value;

        if (name && location && hours) {
            const hospitalCard = document.createElement("div");
            hospitalCard.classList.add("hospital-card");
            hospitalCard.innerHTML = `
                <h2>${name}</h2>
                <p>📍 Location: ${location}</p>
                <p>🕒 Working Hours: ${hours}</p>
            `;

            hospitalList.appendChild(hospitalCard);

            document.getElementById("hospitalName").value = "";
            document.getElementById("hospitalLocation").value = "";
            document.getElementById("hospitalHours").value = "";

            modal.style.display = "none";
        } else {
            alert("Please fill in all fields!");
        }
    });

    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();

        hospitalCards.forEach(card => {
            const hospitalName = card.querySelector('h2').textContent.toLowerCase();
            const hospitalAddress = card.querySelector('p').textContent.toLowerCase();
            
            if (hospitalName.includes(searchTerm) || hospitalAddress.includes(searchTerm)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    });

    window.addEventListener("click", (event) => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
});
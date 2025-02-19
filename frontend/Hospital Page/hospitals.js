 document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal");
    const addHospitalLeft = document.getElementById("addHospitalLeft");
    const addHospitalRight = document.getElementById("addHospitalRight");
    const closeModal = document.querySelector(".close");
    const saveHospital = document.getElementById("saveHospital");
    const hospitalList = document.getElementById("hospitalList");

    
    addHospitalLeft.addEventListener("click", () => {
        modal.style.display = "block";
    });

    addHospitalRight.addEventListener("click", () => {
        modal.style.display = "block";
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

    
    window.addEventListener("click", (event) => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
});
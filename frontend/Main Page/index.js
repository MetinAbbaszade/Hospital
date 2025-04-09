document.addEventListener('DOMContentLoaded', () => {
    if (isAuthenticated()) {
        document.querySelector('#login-button').style.display = 'none';
        document.querySelector('#register-button').style.display = 'none';
    }
    loadHospitals();
    loadDoctors();
});

async function loadDoctors() {
    try {
        const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/`);
        const doctors = await response.json();
        displayDoctors(doctors);
    } catch {
        console.error('Error loading doctors:', error);
    }
}

async function displayDoctors(doctors) {
    const container = document.querySelector('#doctors-container');
    container.innerHTML = '';
    let count = 0;
    for (const doctor of doctors) {
        if (count != 4) {
            const div = document.createElement('div');
            div.className = 'col-md-6';
            div.classList.add('mb-4');
            div.classList.add('col-lg-4');
            const hospital = await loadHospitalDetails(doctor.hospital_id)
            const specializations = await fetchDoctorSpecialization(doctor.id)
            div.innerHTML = `
            <div class="doctor-card">
                <div class="card-badge">
                    <i class="fas fa-star"></i>Top Rated
                </div>
                <img src="https://img.freepik.com/free-photo/pleased-young-female-doctor-wearing-medical-robe-stethoscope-around-neck-standing-with-closed-posture_409827-254.jpg"
                alt="Doctor" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">
                        <i class="fas fa-user-md"></i>Dr. ${doctor.fname} ${doctor.lname}
                    </h5>
                    <p class="card-text">
                        <i class="fas fa-stethoscope"></i>${await fetchDoctorSpecialization(doctor.id)}
                    </p>
                    <div class="doctor-features">
                        <span><i class="fas fa-hospital"></i>${hospital.name}</span>
                        <span><i class="fas fa-clock"></i>${doctor.experience} Years</span>
                    </div>
                    <p class="doctor-description">${aboutDoctors['cardiologist']}</p>
                    <a href="#appointment" class="btn btn-primary">
                        <i class="fas fa-calendar-check"></i>Book Appointment
                    </a>
                </div>
            </div>
        </div>`;
            container.appendChild(div);
            count++;
        }
        else {
            break;
        }
    }

}

async function loadHospitals() {
    try {
        const response = await fetch(`http://0.0.0.0:8000/api/v1/hospital/`);
        const hospitals = await response.json();
        displayHospitals(hospitals);
    } catch (error) {
        console.error('Error loading hospitals:', error);
    }
}

async function loadHospitalDetails(hospitalId) {
    try {
        const response = await fetch(`http://0.0.0.0:8000/api/v1/hospital/${hospitalId}`);
        const hospital = await response.json();
        return hospital;
    } catch (error) {
        console.error('Error loading hospital details:', error);
    }
}

async function fetchDoctorSpecialization(doctorId) {
    try {
        const response = await fetch(`http://0.0.0.0:8000/api/v1/doctorspecialization/doctor/${doctorId}`);
        const doctorSpecializations = await response.json();
        const specializations = [];
        for (const doctorSpecialization of doctorSpecializations) {
            const response2 = await fetch(`http://0.0.0.0:8000/api/v1/specialization/${doctorSpecialization.specialization_id}`);
            const specialization = await response2.json();
            specializations.push(specialization.name);
        }
        return specializations.join(', ');
    } catch {
        console.error('Error loading doctor specialization:', error);
    }
}

async function displayHospitals(hospitals) {
    const container = document.getElementById('hospitals-container');
    container.innerHTML = '';

    for (const hospital of hospitals) {
        const card = document.createElement('div');
        card.className = 'col-md-4';
        card.innerHTML = `
            <div class="card hospital-card">
                        <div class="card-badge"><i class="fas fa-check-circle"></i> Premium</div>
                        <!-- <img src="Admin UI/Hospital Page/Hospital 2.jpg" class="card-img-top" alt="Modern Hospital Baku"> -->
                        <div class="card-body">
                            <h5 class="card-title"><i class="fas fa-hospital-alt me-2"></i>${hospital.name}</h5>
                            <p class="card-text"><i class="fas fa-map-marker-alt me-2"></i>${hospital.state}, ${hospital.city}</p>
                            <p class="card-text"><i class="fas fa-phone me-2"></i>${formatPhoneNumber(hospital.phone_number)}</p>
                            <div class="hospital-features">
                                <span><i class="fas fa-user-md"></i> ${await fetchDoctorCounts(hospital.id)} Doctors</span>
                                <span><i class="fas fa-star"></i> 5.0</span>
                                <span><i class="fas fa-procedures"></i> 200 Beds</span>
                            </div>
                            <div class="hospital-actions">
                                <button class="btn btn-info btn-sm hospital-details">
                                    <i class="fas fa-info-circle"></i>
                                </button>
                                <button class="btn btn-primary btn-sm book-appointment" onclick="bookAppointment()">
                                    <i class="fas fa-calendar-check"></i>
                                </button>
                            </div>
                        </div>
                    </div>
        `;
        container.appendChild(card);
    }
}

async function bookAppointment() {
    window.location.href = "http://127.0.0.1:5506/frontend/Admin%20UI/User%20UI/user_ui.html";
}

function checkAuthAndRedirect() {
    if (!isAuthenticated()) {
        console.log('User not authenticated, redirecting to login page');
        window.location.href = 'Login Page/login_sign.html';
        return false;
    }
    return true;
}


function getCurrentPageName() {
    const path = window.location.pathname;
    const pageName = path.split('/').pop();
    return pageName;
}

document.querySelector('#logoutLink').addEventListener('click', (e) => {
    e.preventDefault();
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = 'http://127.0.0.1:5506/frontend/Login%20Page/login_sign.html';
});

const isAuthenticated = () => localStorage.getItem('access_token');

function formatPhoneNumber(number) {
    return number.replace(/^(\+\d{3})(\d{2})(\d{3})(\d{2})(\d{2})$/, '$1 $2 $3 $4 $5');
}

const fetchDoctorCounts = async (hospital_id) => {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/hospital/${hospital_id}`);
    const data = await response.json();
    return data.length ? data.length : 0;
}

const aboutDoctors = {
    cardiologist: "Cardiologists specialize in diagnosing and treating diseases of the heart and blood vessels, such as hypertension, arrhythmias, and heart failure.",
    neurologist: "Neurologists focus on disorders of the nervous system, including the brain, spinal cord, and nerves. They treat conditions like epilepsy, migraines, and multiple sclerosis.",
    dermatologist: "Dermatologists treat conditions related to the skin, hair, and nails, including acne, eczema, psoriasis, and skin cancer.",
    pediatrician: "Pediatricians care for the health and development of children from birth through adolescence, handling everything from routine checkups to childhood illnesses.",
    orthopedic: "Orthopedic doctors diagnose and treat issues related to the musculoskeletal system, such as broken bones, joint problems, arthritis, and sports injuries.",
    gynecologist: "Gynecologists specialize in women’s reproductive health, including menstruation, fertility, pregnancy, and menopause.",
    ophthalmologist: "Ophthalmologists diagnose and treat eye conditions and perform eye surgeries. They deal with issues like cataracts, glaucoma, and vision correction.",
    psychiatrist: "Psychiatrists are medical doctors who diagnose and treat mental health disorders, such as depression, anxiety, and schizophrenia. They can prescribe medication.",
    oncologist: "Oncologists specialize in the diagnosis and treatment of cancer, including chemotherapy, immunotherapy, and palliative care.",
    general_practitioner: "General practitioners (GPs) provide routine health care, treat common illnesses, and guide patients on preventive care and health education."
}
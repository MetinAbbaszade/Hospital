document.addEventListener('DOMContentLoaded', async () => {
    const headerUsername = document.getElementById('headerUsername');
    const userId = getUserIdFromLocalStorage();
    const data = await fetchUserData(userId);
    headerUsername.textContent = data.fname.charAt(0).toUpperCase() + data.fname.slice(1) + " " + data.lname.charAt(0).toUpperCase() + data.lname.slice(1);

    document.querySelector('.value.email').textContent = getEmailfromLocalStorage();
    document.querySelector('.value.full-name').textContent = data.fname.charAt(0).toUpperCase() + data.fname.slice(1) + " " + data.lname.charAt(0).toUpperCase() + data.lname.slice(1);

    makeAppointSection();
});

function getUserIdFromLocalStorage() {
    const token = localStorage.getItem('access_token');
    const payload = token.split('.')[1];
    const decodedPayload = JSON.parse(atob(payload));
    const userId = decodedPayload['sub'];
    return userId;
}

function getEmailfromLocalStorage() {
    const token = localStorage.getItem('access_token');
    const payload = token.split('.')[1];
    const decodedPayload = JSON.parse(atob(payload));
    const email = decodedPayload['email'];
    return email;
}

async function fetchUserData(userId) {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/patient/${userId}`)
    const data = await response.json();
    return data;
}

const fileInput = document.getElementById('file-input');
const profileImage = document.querySelector('.profile-image-container img');
const headerProfileImage = document.getElementById('headerProfileImage');

fileInput.addEventListener('change', function (e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            profileImage.src = e.target.result;
            headerProfileImage.src = e.target.result;
        }
        reader.readAsDataURL(file);
    }
});


const modal = document.getElementById('editProfileModal');
const editBtn = document.querySelector('.edit-profile-btn');
const closeBtn = document.querySelector('.close-modal');
const editForm = document.getElementById('editProfileForm');

editBtn.addEventListener('click', () => {
    document.getElementById('editName').value = document.querySelector('.info-item:nth-child(1) .value').textContent;
    document.getElementById('editEmail').value = document.querySelector('.info-item:nth-child(2) .value').textContent;
    document.getElementById('editPhone').value = document.querySelector('.info-item:nth-child(3) .value').textContent;
    document.getElementById('editAddress').value = document.querySelector('.info-item:nth-child(4) .value').textContent;

    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
});

closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
});

editForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const obj = {
        fname: document.getElementById('editName').value.split(' ')[0],
        lname: document.getElementById('editName').value.split(' ')[1]
    }
    console.log(obj);
    document.querySelector('.info-item:nth-child(4) .value').textContent = document.getElementById('editAddress').value || "N/A";

    await updateUserProfile(obj);
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
    showAlert('Profile updated successfully!');
});

async function updateUserProfile(obj) {
    const userId = getUserIdFromLocalStorage();
    for (const key in obj) {
        if (obj[key] === "") {
            delete obj[key];
        }
    }
    const response = await fetch(`http://0.0.0.0:8000/api/v1/patient/${userId}`, {
        method: 'PUT',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ ...obj })
    });
    const data = await response.json();
    if (response.ok) {
        console.log('Profile updated successfully:', data);
    } else {
        console.error('Error updating profile:', data);
    }
    window.location.reload();
}

function showAlert(message) {
    const alertBox = document.createElement('div');
    alertBox.className = 'alert';
    alertBox.textContent = message;
    document.body.appendChild(alertBox);
    setTimeout(() => {
        alertBox.remove();
    }, 3000);
}
function showSuccessMessage(message) {
    const successBox = document.createElement('div');
    successBox.className = 'success';
    successBox.textContent = message;
    document.body.appendChild(successBox);
    setTimeout(() => {
        successBox.remove();
    }, 3000);
}

const makeAppointSection = async () => {
    const hospitalDatas = await fetchHospitalDatas();
    const hospitalSelect = document.querySelector('.hospital-select');

    hospitalDatas.forEach(hospital => {
        const option = document.createElement('option');
        option.setAttribute('hospitalid', hospital.id);
        option.textContent = hospital.name;
        hospitalSelect.appendChild(option);
    });
}

const fetchHospitalDatas = async () => {
    const response = await fetch('http://0.0.0.0:8000/api/v1/hospital/');
    const data = await response.json();
    return data;
}

const fetchDoctorDatas = async () => {
    const response = await fetch('http://0.0.0.0:8000/api/v1/doctor/');
    const data = await response.json();
    return data;
}

const fetchDoctorData = async (doctorId) => {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/${doctorId}`, {
        method: 'GET',
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    return data;
}

const appointmentForm = document.querySelector('.appointment-form');
appointmentForm.addEventListener('submit', async (e) => {
    const patientId = getUserIdFromLocalStorage();
    e.preventDefault();
    const doctorId = document.querySelector('.doctor-select').value;
    const date = document.querySelector('.date-input').value;
    const time = document.querySelector('.time-input').value;
    const problem = document.querySelector('.problem-input').value;
    if (!date || !time) {
        alert("Please select both date and time.");
        return null;
    }
    const localDateTime = new Date(`${date}T${time}`);
    const isoDateTime = localDateTime.toISOString();
    const hospitalId = document.querySelector('.hospital-select').value;
    const doctorData = await fetchDoctorData(doctorId);
    if(doctorData.hospital_id !== hospitalId) {
        alert("The correct hospital is not selected.");
        return null;
    }
    const appointmentData = {
        patient_id: patientId,
        doctor_id: doctorId,
        date_time: isoDateTime,
        problem: problem
    };
    await createAppointment(appointmentData);
    window.location.reload();
})

async function createAppointment(appointmentData) {
    if (!appointmentData) {
        console.error('Invalid appointment data');
        return;
    }
    for (const key in appointmentData) {
        if (appointmentData[key] === "") {
            delete appointmentData[key];
        }
    }

    const response = await fetch('http://0.0.0.0:8000/api/v1/appointment/', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({...appointmentData})
    })
    const data = await response.json();
    if (response.ok) {
        alert('Appointment created successfully:');
    } else {
        console.error('Error creating appointment:', data);
        showAlert('Error creating appointment');
    }
}

const hospitalSelect = document.querySelector('#hospital-select');

hospitalSelect.addEventListener('change', async (event) => {
    const selectedOption = event.target.selectedOptions[0];
    const hospitalId = selectedOption.getAttribute('hospitalid');
    const doctorSelect = document.querySelector('.doctor-select');
    if (!hospitalId) {
        console.warn('No hospitalId found in selected option');
        return;
    }

    try {
        const datas = await fetchDoctorDatasByHospital(hospitalId);
        doctorSelect.innerHTML = '<option value="">Select a doctor</option>'; 
        datas.forEach((data) => {
            const option = document.createElement('option');
            option.setAttribute('doctor-id', data.id);
            option.textContent = data.fname.charAt(0).toUpperCase() + data.fname.slice(1) + " " + data.lname.charAt(0).toUpperCase() + data.lname.slice(1)
            doctorSelect.appendChild(option);
        })

    } catch (error) {
        console.error('Error fetching doctor data:', error);
    }
});


const fetchDoctorDatasByHospital = async (hospitalId) => {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/hospital/${hospitalId}`);
    const data = await response.json();
    return data;
}
async function getDoctorData() {
    const doctorId = await getDoctorIdFromLocalStorage();
    const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/${doctorId}`)
    if (!response.ok) {
        console.error("Failed to fetch doctor data:", response.statusText);
        return;
    }
    const data = await response.json()
    return data;
}

async function getHospitalName(id) {
    const hospitalName = await fetch(`http://0.0.0.0:8000/api/v1/hospital/${id}`);
    if (!hospitalName.ok) {
        console.error("Failed to fetch hospital data:", hospitalName.statusText);
        return;
    }
    const data = await hospitalName.json();
    return data;
}

async function getDoctorSpecialization(id) {
    const doctorSpecialization = await fetch(`http://0.0.0.0:8000/api/v1/doctorspecialization/doctor/${id}`);
    if (!doctorSpecialization.ok) {
        console.error("Failed to fetch doctor specialization data:", doctorSpecialization.statusText);
        return;
    }
    const doctorSpecializationDatas = await doctorSpecialization.json();
    return doctorSpecializationDatas;
}

async function loadDoctorProfile() {
    const doctorId = await getDoctorIdFromLocalStorage();
    if (!doctorId) {
        console.error("No doctor ID found in localStorage.");
        return;
    }
    const data = await getDoctorData();
    if (!data) {
        console.error("No doctor data found.");
        return;
    }
    document.getElementById('doctorName').textContent = toCapitalize(data)
    document.getElementById('fullName').textContent = toCapitalize(data)
    document.getElementById('email').textContent = await getDoctorEmailFromLocalStorage();
    document.getElementById('phone').textContent = data.phone_num;
    document.getElementById('experience').textContent = data.experience;
    document.getElementById('licenseNo').textContent = (data.id).slice(0, 4);


    const doctorSpecializationDatas = await getDoctorSpecialization(doctorId);
    const count = 0;
    for (const specialization of doctorSpecializationDatas) {
        const response = await fetch(`http://0.0.0.0:8000/api/v1/specialization/${specialization.specialization_id}`);
        if (!response.ok) {
            console.error("Failed to fetch specialization data:", response.statusText);
            return;
        }
        const specializationData = await response.json();
        if ((count + 1) === doctorSpecializationDatas.length) {
            document.getElementById('specializationInfo').textContent += specializationData.name;
        } else {
            document.getElementById('specializationInfo').textContent += specializationData.name + ", ";
        }
    }
    const hospitalData = await getHospitalName(data.hospital_id);
    document.getElementById('hospitalName').textContent = hospitalData.name;
}



async function loadAppointments() {
    const appointmentsList = document.getElementById('appointmentsList');
    appointmentsList.innerHTML = '';
    const doctorId = await getDoctorIdFromLocalStorage();
    if (!doctorId) {
        console.error("No doctor ID found in localStorage.");
        return;
    }
    const appointments = await fetch(`http://0.0.0.0:8000/api/v1/appointment/doctor/${doctorId}`);
    if (!appointments.ok) {
        console.error("Failed to fetch appointments:", appointments.statusText);
        return;
    }
    const appointmentsData = await appointments.json();
    for (const appointment of appointmentsData) {
        const row = document.createElement('tr');
        row.className = 'appointment-row';
        const patientName = await fetch(`http://0.0.0.0:8000/api/v1/patient/${appointment.patient_id}`);
        if (!patientName.ok) {
            console.error("Failed to fetch patient data:", patientName.statusText);
            return;
        }
        const patientData = await patientName.json();
        row.innerHTML = `
            <td>${patientData.fname + " " + patientData.lname}</td>
            <td>${(appointment.date_time).slice(0, 10)}</td>
            <td>${(appointment.date_time).slice(11)}</td>
            <td>
            <span class="badge text-white ${appointment.status === 'confirmed' ? 'bg-success' : appointment.status === 'pending' ? 'bg-warning' : 'bg-danger'}">${appointment.status}</span></td>
            <td>
                <button class="btn btn-primary" onclick="viewDetails(${appointment.id})">
                    <span class="las la-eye"></span>
                </button>
                ${appointment.status === 'pending' ? `
                    <button class="btn btn-success" onclick="confirmAppointment('${appointment.id}')">
                        <span class="las la-check"></span>
                    </button>
                ` : ''}
                ${appointment.status === 'pending' ? `
                     <button class="btn btn-danger" onclick="cancelAppointment(this, '${appointment.id}')">
                    <span class="las la-times"></span>
                </button>
                ` : ''}
               
            </td>
        `;
        appointmentsList.appendChild(row);
    }
    loadStats();
}

function loadStats() {
    const rows = document.querySelectorAll('.appointment-row');
    const totalAppointments = document.getElementById('totalAppointments');
    const todaysAppointmentWrapper = document.getElementById('todayAppointments');
    const today = new Date().toISOString().split('T')[0];
    totalAppointments.textContent = rows.length;
    let todaysAppointments = 0;
    rows.forEach(row => {
        const appointmentDate = row.cells[1].textContent;
        if (appointmentDate === today) {
            todaysAppointments++;
        }
    });
    todaysAppointmentWrapper.textContent = todaysAppointments;
}

async function confirmAppointment(appointmentId) {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/appointment/${appointmentId}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                status: 'confirmed',
            })
        }
    )
    if (!response.ok) {
        console.error("Failed to fetch appointment data:", response.statusText);
        return;
    }
}


async function cancelAppointment(appointmentId) {
    if (confirm('Bu görüşü silmək istədiyinizə əminsiniz?')) {
        const response = await fetch(`http://0.0.0.0:8000/api/v1/appointment/${appointmentId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ status: 'canceled' })
        });

        if (!response.ok) {
            console.error("Failed to cancel appointment:", response.statusText);
            return;
        }
    }
}

async function editProfile() {
    const doctorData = await getDoctorData();
    if (!doctorData) {
        console.error("No doctor data found.");
        return;
    }
    const hospitalName = await getHospitalName(doctorData.hospital_id);
    document.getElementById('editHospital').value = hospitalName.name;
    document.getElementById('editLicense').value = (doctorData.id).slice(0, 4);
    document.getElementById('editEmail').value = await getDoctorEmailFromLocalStorage();
    document.getElementById('editModal').style.display = 'block';
}

async function saveProfile() {
    const obj = {
        fname: document.getElementById('editFirstName').value,
        lname: document.getElementById('editLastName').value,
        phone_num: document.getElementById('editPhone').value,
        experience: document.getElementById('editExperience').value
    }
    console.log(obj);
    await updateDoctorProfile(obj);
    document.getElementById('editModal').style.display = 'none';
    alert('Profile updated successfully!');
}

async function updateDoctorProfile(obj) {
    for (const key in obj) {
        if(obj[key] === "") {
            delete obj[key];
        }
    }
    if (Object.keys(obj).length === 0) {
        console.error("No fields to update.");
        return;
    }
    const doctorId = await getDoctorIdFromLocalStorage();
    const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/${doctorId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({...obj})
    })
    if (!response.ok) {
        console.error(`${response.json}`)
        return;
    }
    window.location.reload();
}

function closeModal() {
    document.getElementById('editModal').style.display = 'none';
}

// Close modal when clicking outside
window.onclick = (event) => {
    if (event.target === document.getElementById('editModal')) {
        closeModal();
    }
};

// Close modal when clicking X
document.querySelector('.close').onclick = closeModal;

window.addEventListener('DOMContentLoaded', () => {
    loadDoctorProfile();
    loadAppointments();
});

async function getDoctorIdFromLocalStorage() {
    const token = localStorage.getItem("token");
    if (!token) {
        console.error("No token found in localStorage.");
        return null;
    }

    try {
        const payloadBase64 = token.split('.')[1];
        const payloadJson = atob(payloadBase64);
        const payload = JSON.parse(payloadJson);
        return payload.sub;
    } catch (error) {
        console.error("Error decoding token:", error);
        return null;
    }
}

async function getDoctorEmailFromLocalStorage() {
    const token = localStorage.getItem("token");
    if (!token) {
        console.error("No token found in localStorage.");
        return null;
    }

    try {
        const payloadBase64 = token.split('.')[1];
        const payloadJson = atob(payloadBase64);
        const payload = JSON.parse(payloadJson);
        return payload.email;
    } catch (error) {
        console.error("Error decoding token:", error);
        return null;
    }
}


const toCapitalize = (data) => (data.fname).replace(data.fname[0], data.fname[0].toUpperCase()) + " " + (data.lname).replace(data.lname[0], data.lname[0].toUpperCase());
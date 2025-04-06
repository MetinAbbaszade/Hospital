const doctorData = {
    fullName: "Dr. John Doe",
    specialization: "Cardiologist",
    email: "john.doe@hospital.com",
    phone: "+994 50 123 45 67",
    experience: "15 years",
    license: "AZ12345",
    hospital: {
        name: "City Central Hospital",
        workingHours: "Mon-Fri: 09:00-18:00"
    },
    stats: {
        totalAppointments: 24,
        todayAppointments: 8,
        rating: 4.8
    }
};

const appointments = [
    {
        id: 1,
        patientName: "Alice Smith",
        date: "2025-03-08",
        time: "10:00",
        status: "Confirmed"
    },
    {
        id: 2,
        patientName: "Bob Johnson",
        date: "2025-03-08",
        time: "11:00",
        status: "Pending"
    },
    {
        id: 3,
        patientName: "Carol Williams",
        date: "2025-03-08",
        time: "14:00",
        status: "Confirmed"
    }
];

function loadDoctorProfile() {
    document.getElementById('doctorName').textContent = doctorData.fullName;
    document.getElementById('specialization').textContent = doctorData.specialization;
    document.getElementById('fullName').textContent = doctorData.fullName;
    document.getElementById('email').textContent = doctorData.email;
    document.getElementById('phone').textContent = doctorData.phone;
    document.getElementById('specializationInfo').textContent = doctorData.specialization;
    document.getElementById('experience').textContent = doctorData.experience;
    document.getElementById('license').textContent = doctorData.license;
    document.getElementById('workingHours').textContent = doctorData.hospital.workingHours;
    document.getElementById('hospitalName').textContent = doctorData.hospital.name;
}

function loadAppointments() {
    const appointmentsList = document.getElementById('appointmentsList');
    appointmentsList.innerHTML = '';

    appointments.forEach(appointment => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${appointment.patientName}</td>
            <td>${appointment.date}</td>
            <td>${appointment.time}</td>
            <td><span class="badge ${appointment.status === 'Confirmed' ? 'bg-success' : 'bg-warning'}">${appointment.status}</span></td>
            <td>
                <button class="btn btn-primary" onclick="viewDetails(${appointment.id})">
                    <span class="las la-eye"></span>
                </button>
                ${appointment.status === 'Pending' ? `
                    <button class="btn btn-success" onclick="confirmAppointment(${appointment.id})">
                        <span class="las la-check"></span>
                    </button>
                ` : ''}
                <button class="btn btn-danger" onclick="deleteAppointment(${appointment.id})">
                    <span class="las la-times"></span>
                </button>
            </td>
        `;
        appointmentsList.appendChild(row);
    });
}

function loadStats() {
    document.getElementById('totalAppointments').textContent = doctorData.stats.totalAppointments;
    document.getElementById('todayAppointments').textContent = doctorData.stats.todayAppointments;
    document.getElementById('rating').textContent = doctorData.stats.rating;
}

function viewDetails(appointmentId) {
    const appointment = appointments.find(a => a.id === appointmentId);
    if (appointment) {
        alert(`Viewing details for appointment with ${appointment.patientName}`);
    }
}

function confirmAppointment(appointmentId) {
    const appointment = appointments.find(a => a.id === appointmentId);
    if (appointment) {
        appointment.status = 'Confirmed';
        loadAppointments();
        alert(`Appointment with ${appointment.patientName} has been confirmed`);
    }
}

function deleteAppointment(appointmentId) {
    if (confirm('Bu görüşü silmək istədiyinizə əminsiniz?')) {
        const index = appointments.findIndex(a => a.id === appointmentId);
        if (index !== -1) {
            appointments.splice(index, 1);
            loadAppointments();
            // Update stats
            doctorData.stats.totalAppointments--;
            if (appointments.filter(a => a.date === new Date().toISOString().split('T')[0]).length < doctorData.stats.todayAppointments) {
                doctorData.stats.todayAppointments--;
            }
            loadStats();
        }
    }
}

function editProfile() {
    document.getElementById('editFullName').value = doctorData.fullName;
    document.getElementById('editEmail').value = doctorData.email;
    document.getElementById('editPhone').value = doctorData.phone;
    document.getElementById('editSpecialization').value = doctorData.specialization;
    document.getElementById('editExperience').value = doctorData.experience;
    document.getElementById('editLicense').value = doctorData.license;
    document.getElementById('editWorkingHours').value = doctorData.hospital.workingHours;
    document.getElementById('editHospital').value = doctorData.hospital.name;
    
    document.getElementById('editModal').style.display = 'block';
}

function saveProfile() {
    doctorData.fullName = document.getElementById('editFullName').value;
    doctorData.email = document.getElementById('editEmail').value;
    doctorData.phone = document.getElementById('editPhone').value;
    doctorData.specialization = document.getElementById('editSpecialization').value;
    doctorData.experience = document.getElementById('editExperience').value;
    doctorData.license = document.getElementById('editLicense').value;
    doctorData.hospital.workingHours = document.getElementById('editWorkingHours').value;
    doctorData.hospital.name = document.getElementById('editHospital').value;

    loadDoctorProfile();
    document.getElementById('editModal').style.display = 'none';
    alert('Profile updated successfully!');
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

// Initialize
window.addEventListener('DOMContentLoaded', () => {
    loadDoctorProfile();
    loadAppointments();
    loadStats();
});

document.addEventListener('DOMContentLoaded', async () => {
    const userId = getUserIdFromLocalStorage();
    const adminData = await getAdminData(userId);
    const userData = await getAllUsers();
    const hospitalData = await getAllHospitals();
    const appointmentData = await getAllAppoints();

    document.querySelector('.user-wrapper h4').textContent = toCapitalize(adminData);
    document.querySelector('#user-count').textContent = userData.length;
    document.querySelector('#hospital-count').textContent = hospitalData.length;
    document.querySelector('#appointment-count').textContent = appointmentData.length;
    configureAppointBody(10);
    showUsers();
});


const toCapitalize = (data) => (data.fname).replace(data.fname[0], data.fname[0].toUpperCase()) + " " + (data.lname).replace(data.lname[0], data.lname[0].toUpperCase());

function showAlert(message) {
    const alertBox = document.createElement('div');
    alertBox.className = 'alert';
    alertBox.textContent = message;

    document.body.appendChild(alertBox);

    setTimeout(() => {
        alertBox.remove();
    }, 3000);
}

function showError(message) {
    const errorBox = document.createElement('div');
    errorBox.className = 'error';
    errorBox.textContent = message;

    document.body.appendChild(errorBox);

    setTimeout(() => {
        errorBox.remove();
    }, 3000);
}

function getUserIdFromLocalStorage() {
    const token = localStorage.getItem('access_token');
    if (!token) {
        showError('User ID not found in local storage.');
        return null;
    }
    const payload = token.split('.')[1];
    const decodedPayload = JSON.parse(atob(payload));
    const userId = decodedPayload.sub;
    return userId;
}

async function getAdminData(id) {
    try {
        const response = await fetch(`http://0.0.0.0:8000/api/v1/admin/${id}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch admin data');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        showError(error.message);
    }
}

async function getAllUsers() {
    const response = await fetch('http://0.0.0.0:8000/api/v1/patient/')
    const data = await response.json();
    return data;
}

async function getAllHospitals() {
    const response = await fetch('http://0.0.0.0:8000/api/v1/hospital/');
    const data = await response.json();
    return data;
}

async function getAllAppoints() {
    const response = await fetch('http://0.0.0.0:8000/api/v1/appointment/');
    const data = await response.json();
    return data;
}

async function getHospitalName(id) {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/${id}`);
    const data = await response.json();
    const hospitalId = data.hospital_id;
    const hospitalResponse = await fetch(`http://0.0.0.0:8000/api/v1/hospital/${hospitalId}`)
    const hospitalData = await hospitalResponse.json();
    return hospitalData.name;
}
async function getPatient(id) {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/patient/${id}`);
    const data = await response.json();
    return data;
}

async function configureAppointBody(appointCount) {
    const appointData = await getAllAppoints();
    const appointBody = document.querySelector('.appoint-body');
    let count = 0;
    for (const appoint of appointData) {
        if (count < appointCount) {
            const appointRow = document.createElement('tr');
            const patientData = await getPatient(appoint.patient_id);
            const hospitalData = await getHospitalName(appoint.doctor_id);
            appointRow.innerHTML = `
                <td>${patientData.fname + " " + patientData.lname}</td>
                <td>${hospitalData}</td>
                <td>${appoint.date_time.slice(0, 10) + " " + appoint.date_time.slice(11)}</td>
                <td>${appoint.status}</td>
            `;
            appointBody.appendChild(appointRow);
            count++;
            continue;
        }
        break;
    }
}

async function showUsers() {
    userData = await getAllUsers();
    const userBody = document.querySelector('#card-body');
    userData.forEach((row) => {
        const customer = document.createElement('div');
        customer.className = 'customer';
        customer.innerHTML = `
        <div class="info">
            <img src="Profil Photo.webp" width="40px" height="40px">
            <div>
                <h4>${row.fname + " " + row.lname}</h4>
                <small>User</small>
            </div>
        </div>
        <div class="contact">
            <span class="las la-user-circle"></span>
            <span class="las la-comment"></span>
            <span class="las la-phone"></span>
        </div>
        `;
        userBody.appendChild(customer);
    });
}
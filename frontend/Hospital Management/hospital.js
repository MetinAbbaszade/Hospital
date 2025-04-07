document.addEventListener('DOMContentLoaded', function () {

    async function loadHospitals() {
        const ownerId = getOwnerId();
        const hospitals = await fetchHospitalsByOwner(ownerId);
        const container = document.getElementById('hospitalCardsContainer');
        const hospitalCount = document.querySelector('.card-single>div>h1');
        hospitalCount.textContent = hospitals.length;
        if (hospitals.length === 0) {
            container.innerHTML = '<p class="no-hospitals">No hospitals found. Add a new hospital to get started.</p>';
            return;
        }

        container.innerHTML = '';
        hospitals.forEach(hospital => {
            container.appendChild(createHospitalCard(hospital));
        });
        getDoctorCounts();
        return hospitals;
    }

    async function fetchHospitalsByOwner(ownerId) {
        try {
            const response = await fetch(`http://0.0.0.0:8000/api/v1/hospital/owner/${ownerId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch hospitals');
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching hospitals:', error);
            return [];
        }
    }

    function createHospitalCard(hospitalData) {
        const card = document.createElement('div');
        card.className = 'hospital-card';
        card.dataset.id = hospitalData.id;

        card.innerHTML = `
            <div class="card">
                <div class="card-header">
                    <h3>${hospitalData.name}</h3>
                    <button class="edit-hospital-btn" data-id="${hospitalData.id}">Edit <span class="las la-edit"></span></button>
                </div>
                <div class="card-body">
                    <div class="hospital-details">
                        <div class="detail-item">
                            <span class="las la-hospital"></span>
                            <div class="info">
                                <h4 class="HospitalNameClass">${hospitalData.name}</h4>
                                <small>Name</small>
                            </div>
                        </div>
                        <div class="detail-item">
                            <span class="las la-map-marker"></span>
                            <div class="info">
                                <h4>${hospitalData.state}</h4>
                                <small>Address</small>
                            </div>
                        </div>
                        <div class="detail-item">
                            <span class="las la-phone"></span>
                            <div class="info">
                                <h4>${hospitalData.phone_number}</h4>
                                <small>Contact</small>
                            </div>
                        </div>
                        <div class="detail-item">
                            <span class="las la-envelope"></span>
                            <div class="info">
                                <h4>${hospitalData.email}</h4>
                                <small>Email</small>
                            </div>
                        </div>
                        <div class="detail-item">
                            <span class="las la-bed"></span>
                            <div class="info">
                                <h4>${hospitalData.capacity || '250'} Beds</h4>
                                <small>Capacity</small>
                            </div>
                        </div>
                        <div class="detail-item">
                            <span class="las la-certificate"></span>
                            <div class="info">
                                <h4>${hospitalData.specialities?.join(', ') || 'General'}</h4>
                                <small>Specializations</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

        card.querySelector('.edit-hospital-btn').addEventListener('click', function () {
            populateHospitalModal(hospitalData);
            handleModal('hospitalModal', true);
        });

        return card;
    }

    loadHospitals();
    const hospitalOwnerWrapper = document.querySelector('.user-wrapper>div');
    const hospitalOwnerName = document.createElement('h3');
    hospitalOwnerName.textContent = getOwnerName();
    hospitalOwnerWrapper.appendChild(hospitalOwnerName);


    const addDoctorForm = document.getElementById('addDoctorForm');

    addDoctorForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        const fname = document.getElementById('doctorName').value;
        const lname = document.getElementById('doctorSurName').value;
        const specialization = document.getElementById('specialization').value;
        const experience = document.getElementById('experience').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const hospitalId = getHospitalId(document.getElementById('hospitalName').value);

        const doctorData = {
            email: email,
            hospital_id: hospitalId,
            specialities: [specialization],
            fname: fname,
            lname: lname,
            phone_num: phone,
            experience: experience,
            password: `${fname}@1234`,
        };

        try {
            const response = await addDoctor(doctorData);
            if (response) {
                showAlert("Doctor added successfully", "success");
                addDoctorForm.reset();
            }
        } catch (error) {
            showAlert(`Failed to add doctor: ${error.message}`, "error");
        }
    });


    async function addDoctor(doctorData) {
        try {
            const response = await fetch('http://0.0.0.0:8000/api/v1/doctor/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(doctorData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Failed to add doctor');
            }

            return await response.json();
        } catch (error) {
            console.error('Error adding doctor:', error);
            throw error;
        }
    }

    function showAlert(message, type) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type}`;
        alertDiv.textContent = message;

        document.body.appendChild(alertDiv);

        setTimeout(() => {
            alertDiv.remove();
        }, 3000);
    }

    function getOwnerId() {
        const token = localStorage.getItem("access_token");
        if (!token) {
            console.error("No token found in localStorage.");
            return;
        }

        try {
            const payloadBase64 = token.split('.')[1];
            const decodedPayload = JSON.parse(atob(payloadBase64));

            const id = decodedPayload['sub'];
            if (id) {
                return id
            } else {
                console.warn("Role not found or not recognized:", role);
                alert("Unauthorized role or destination.");
            }
        } catch (error) {
            console.error("Failed to decode token:", error);
        }
    }

    function getOwnerName() {
        const token = localStorage.getItem("access_token");
        if (!token) {
            console.error("No token found in localStorage.");
            return;
        }
        try {
            const payloadBase64 = token.split('.')[1];
            const decodedPayload = JSON.parse(atob(payloadBase64));
            const name = decodedPayload['email'].slice(0, decodedPayload['email'].indexOf('@')).replace(decodedPayload['email'][0], decodedPayload['email'][0].toUpperCase());
            if (name) {
                return name;
            }
        } catch (error) {
            console.error("Failed to decode token:", error);
        }
    }

    function getHospitalId(hospitalName) {
        const hospitals = document.querySelectorAll('.hospital-card');
        for (const hospital of hospitals) {
            if (hospital.querySelector('h3').textContent === hospitalName) {
                return hospital.dataset.id;
            }
        }
        return null;
    }

    async function getDoctorCounts() {
        const hospitals = document.querySelectorAll('.hospital-card');
        const doctorCountsWrapper = document.querySelector('.doctor-count h1');
        let doctorCount = 0;
        for (const hospital of hospitals) {
            const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/hospital/${hospital.dataset.id}`);
            if (!response.ok) {
                throw new Error('Failed to fetch hospitals');
            }
            const data = await response.json();
            doctorCount += data.length;
            doctorCountsWrapper.textContent = doctorCount;
        }
    }
});
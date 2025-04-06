document.addEventListener('DOMContentLoaded', function() {
    let hospitalInfo = {
        name: "City Central Hospital",
        address: "123 Medical Street, City Center",
        contact: "+1 234 567 8900",
        email: "info@cityhospital.com",
        workingHours: "24/7",
        beds: "250 Beds",
        established: "Since 1995",
        certification: "ISO 9001:2015"
    };

    function handleModal(modalId, show = true) {
        const modal = document.getElementById(modalId);
        modal.style.display = show ? 'block' : 'none';
    }

    const doctorModal = document.getElementById('doctorModal');
    const doctorEditList = doctorModal.querySelector('.doctor-edit-list');

    function createDoctorItem(data = {}) {
        const item = document.createElement('div');
        item.className = 'doctor-edit-item';
        item.innerHTML = `
            <input type="text" class="doctor-name" value="${data.name || ''}" placeholder="Doctor Name">
            <input type="text" class="doctor-department" value="${data.department || ''}" placeholder="Department">
            <input type="text" class="doctor-rating" value="${data.rating || ''}" placeholder="Rating (⭐)">
            <input type="text" class="doctor-experience" value="${data.experience || ''}" placeholder="Years of Experience">
            <button class="delete-btn" ${data.id ? `data-id="${data.id}"` : ''}>Delete</button>
        `;

        item.querySelector('.delete-btn').onclick = () => item.remove();
        return item;
    }

    function loadDoctorsToModal() {
        doctorEditList.innerHTML = '';
        document.querySelectorAll('.doctor').forEach(doctor => {
            const data = {
                name: doctor.querySelector('h4').textContent,
                department: doctor.querySelector('small').textContent,
                rating: doctor.querySelector('.rating').textContent,
                experience: doctor.querySelector('.experience').textContent,
                id: doctor.dataset.id
            };
            doctorEditList.appendChild(createDoctorItem(data));
        });
    }

    function saveDoctors() {
        const doctorsList = document.getElementById('doctorsList');
        doctorsList.innerHTML = '';

        doctorEditList.querySelectorAll('.doctor-edit-item').forEach((item, index) => {
            const data = {
                name: item.querySelector('.doctor-name').value,
                department: item.querySelector('.doctor-department').value,
                rating: item.querySelector('.doctor-rating').value || '⭐⭐⭐⭐⭐',
                experience: item.querySelector('.doctor-experience').value || '10 years experience'
            };

            if (data.name && data.department) {
                const doctorDiv = document.createElement('div');
                doctorDiv.className = 'doctor';
                doctorDiv.setAttribute('data-id', index + 1);
                doctorDiv.innerHTML = `
                    <div class="info">
                        <img src="../Profil Photo.webp" width="50px" height="50px" alt="Doctor">
                        <div>
                            <h4>${data.name}</h4>
                            <small>${data.department}</small>
                            <p class="rating">${data.rating}</p>
                            <p class="experience">${data.experience}</p>
                        </div>
                    </div>
                    <div class="contact">
                        <span class="las la-user-circle" title="View Profile"></span>
                        <span class="las la-comment" title="Send Message"></span>
                        <span class="las la-phone" title="Call"></span>
                    </div>
                `;
                doctorsList.appendChild(doctorDiv);
            }
        });
        handleModal('doctorModal', false);
    }

    function updateHospitalInfo() {
        const items = [
            { icon: 'hospital', label: 'Name', value: hospitalInfo.name },
            { icon: 'map-marker', label: 'Address', value: hospitalInfo.address },
            { icon: 'phone', label: 'Contact', value: hospitalInfo.contact },
            { icon: 'envelope', label: 'Email', value: hospitalInfo.email },
            { icon: 'clock', label: 'Working Hours', value: hospitalInfo.workingHours },
            { icon: 'bed', label: 'Capacity', value: hospitalInfo.beds },
            { icon: 'calendar', label: 'Established', value: hospitalInfo.established },
            { icon: 'certificate', label: 'Certification', value: hospitalInfo.certification }
        ];

        document.querySelector('.hospital-details').innerHTML = items.map(item => `
            <div class="detail-item">
                <span class="las la-${item.icon}"></span>
                <div class="info">
                    <h4>${item.value}</h4>
                    <small>${item.label}</small>
                </div>
            </div>
        `).join('');
    }

    function fillModalInputs() {
        const inputs = {
            'hospitalName': hospitalInfo.name,
            'hospitalAddress': hospitalInfo.address,
            'hospitalContact': hospitalInfo.contact,
            'hospitalEmail': hospitalInfo.email,
            'hospitalHours': hospitalInfo.workingHours,
            'hospitalBeds': hospitalInfo.beds.replace(' Beds', ''),
            'hospitalEstablished': hospitalInfo.established.replace('Since ', ''),
            'hospitalCertification': hospitalInfo.certification
        };

        Object.entries(inputs).forEach(([id, value]) => {
            document.getElementById(id).value = value;
        });
    }

    function saveHospitalInfo() {
        const beds = document.getElementById('hospitalBeds').value;
        const established = document.getElementById('hospitalEstablished').value;
        
        hospitalInfo = {
            name: document.getElementById('hospitalName').value,
            address: document.getElementById('hospitalAddress').value,
            contact: document.getElementById('hospitalContact').value,
            email: document.getElementById('hospitalEmail').value,
            workingHours: document.getElementById('hospitalHours').value,
            beds: beds + (beds.includes('Beds') ? '' : ' Beds'),
            established: 'Since ' + established,
            certification: document.getElementById('hospitalCertification').value
        };

        updateHospitalInfo();
        handleModal('hospitalModal', false);
    }

    async function fetchHospitalsByOwner(ownerId) {
        try {
            const response = await fetch(`/api/v1/hospital/owner/${ownerId}`);
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
                                <h4>${hospitalData.name}</h4>
                                <small>Name</small>
                            </div>
                        </div>
                        <div class="detail-item">
                            <span class="las la-map-marker"></span>
                            <div class="info">
                                <h4>${hospitalData.address}</h4>
                                <small>Address</small>
                            </div>
                        </div>
                        <div class="detail-item">
                            <span class="las la-phone"></span>
                            <div class="info">
                                <h4>${hospitalData.phone}</h4>
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

        card.querySelector('.edit-hospital-btn').addEventListener('click', function() {
            populateHospitalModal(hospitalData);
            handleModal('hospitalModal', true);
        });

        return card;
    }

    function populateHospitalModal(hospitalData) {
        document.getElementById('hospitalName').value = hospitalData.name || '';
        document.getElementById('hospitalAddress').value = hospitalData.address || '';
        document.getElementById('hospitalContact').value = hospitalData.phone || '';
        document.getElementById('hospitalEmail').value = hospitalData.email || '';
        document.getElementById('hospitalHours').value = hospitalData.working_hours || '24/7';
        document.getElementById('hospitalBeds').value = hospitalData.capacity || '250';
        document.getElementById('hospitalEstablished').value = hospitalData.established_year || '1995';
        document.getElementById('hospitalCertification').value = hospitalData.certification || 'ISO 9001:2015';
        
        document.getElementById('saveHospital').dataset.hospitalId = hospitalData.id;
    }

    async function loadHospitals() {
        const ownerId = 'your-owner-id-here';
        const hospitals = await fetchHospitalsByOwner(ownerId);
        const container = document.getElementById('hospitalCardsContainer');
        
        if (hospitals.length === 0) {
            container.innerHTML = '<p class="no-hospitals">No hospitals found. Add a new hospital to get started.</p>';
            return;
        }
        
        container.innerHTML = '';
        hospitals.forEach(hospital => {
            container.appendChild(createHospitalCard(hospital));
        });
    }

    loadHospitals();

    document.getElementById('editDoctors').onclick = () => {
        handleModal('doctorModal', true);
        loadDoctorsToModal();
    };

    document.getElementById('closeModal').onclick = () => handleModal('doctorModal', false);
    document.getElementById('addNewDoctor').onclick = () => doctorEditList.appendChild(createDoctorItem());
    document.getElementById('saveDoctors').onclick = saveDoctors;

    document.getElementById('editHospital').onclick = () => {
        fillModalInputs();
        handleModal('hospitalModal', true);
    };

    document.getElementById('closeHospital').onclick = () => handleModal('hospitalModal', false);
    document.getElementById('saveHospital').onclick = function() {
        const hospitalId = this.dataset.hospitalId;
        
        if (hospitalId) {
            // Code to update existing hospital
        } else {
            saveHospitalInfo();
        }
        
        loadHospitals();
        handleModal('hospitalModal', false);
    };

    window.onclick = (event) => {
        if (event.target.classList.contains('modal')) {
            handleModal(event.target.id, false);
        }
    };

    updateHospitalInfo();

    // Add Doctor Form Submission
    const addDoctorForm = document.getElementById('addDoctorForm');
    addDoctorForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const doctorName = document.getElementById('doctorName').value;
        const specialization = document.getElementById('specialization').value;
        const experience = document.getElementById('experience').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        
        // Get current hospital ID - assuming we're working with a selected hospital
        const currentHospitalId = getCurrentHospitalId();
        
        if (!currentHospitalId) {
            showAlert("Please select a hospital first", "error");
            return;
        }
        
        // Prepare data in the format backend expects
        const doctorData = {
            email: email,
            hospital_id: currentHospitalId,
            specialities: [specialization], // Backend expects an array of specialities
            name: doctorName,
            phone: phone,
            experience: experience + " years",
            password: "defaultPassword123", // You may want to generate this or handle it differently
            role: "doctor"
        };
        
        try {
            const response = await addDoctor(doctorData);
            if (response) {
                showAlert("Doctor added successfully", "success");
                addDoctorForm.reset();
                // You might want to fetch and display the updated doctor list here
                await loadDoctors(currentHospitalId);
            }
        } catch (error) {
            showAlert(`Failed to add doctor: ${error.message}`, "error");
        }
    });
    
    // Function to get the current hospital ID
    function getCurrentHospitalId() {
        // This could come from a selected hospital card, URL parameter, or session storage
        // For now, return a hardcoded value or check for a selected hospital
        const selectedHospital = document.querySelector('.hospital-card.selected');
        return selectedHospital ? selectedHospital.dataset.id : null;
    }
    
    // Function to add a doctor via API
    async function addDoctor(doctorData) {
        try {
            const response = await fetch('/api/v1/doctor/', {
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
    
    // Function to load doctors for a specific hospital
    async function loadDoctors(hospitalId) {
        try {
            const response = await fetch(`/api/v1/doctor/hospital/${hospitalId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch doctors');
            }
            
            const doctors = await response.json();
            displayDoctors(doctors);
        } catch (error) {
            console.error('Error loading doctors:', error);
            showAlert('Failed to load doctors', 'error');
        }
    }
    
    // Function to display doctors in the UI
    function displayDoctors(doctors) {
        const doctorsList = document.getElementById('doctorsList') || createDoctorsList();
        
        doctorsList.innerHTML = '';
        
        if (doctors.length === 0) {
            doctorsList.innerHTML = '<p class="no-doctors">No doctors found for this hospital.</p>';
            return;
        }
        
        doctors.forEach(doctor => {
            const doctorDiv = document.createElement('div');
            doctorDiv.className = 'doctor';
            doctorDiv.setAttribute('data-id', doctor.id);
            doctorDiv.innerHTML = `
                <div class="info">
                    <img src="../Profil Photo.webp" width="50px" height="50px" alt="Doctor">
                    <div>
                        <h4>${doctor.name}</h4>
                        <small>${doctor.specialities.join(', ')}</small>
                        <p class="experience">${doctor.experience || 'N/A'}</p>
                    </div>
                </div>
                <div class="contact">
                    <span class="las la-user-circle" title="View Profile"></span>
                    <span class="las la-comment" title="Send Message"></span>
                    <span class="las la-phone" title="Call"></span>
                </div>
            `;
            doctorsList.appendChild(doctorDiv);
        });
    }
    
    // Function to create doctors list container if it doesn't exist
    function createDoctorsList() {
        const container = document.createElement('div');
        container.id = 'doctorsList';
        container.className = 'doctors-list';
        
        // Find where to append this in your DOM structure
        const main = document.querySelector('main');
        main.appendChild(container);
        
        return container;
    }
    
    // Function to show alerts/notifications
    function showAlert(message, type) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type}`;
        alertDiv.textContent = message;
        
        document.body.appendChild(alertDiv);
        
        // Remove after 3 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 3000);
    }
});
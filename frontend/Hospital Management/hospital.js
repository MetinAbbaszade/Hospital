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
    document.getElementById('saveHospital').onclick = saveHospitalInfo;

    window.onclick = (event) => {
        if (event.target.classList.contains('modal')) {
            handleModal(event.target.id, false);
        }
    };

    updateHospitalInfo();
});

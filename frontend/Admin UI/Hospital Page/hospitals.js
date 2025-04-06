document.addEventListener("DOMContentLoaded", () => {
    // Get DOM elements
    const modal = document.getElementById('addHospitalModal');
    const addBtn = document.getElementById('addHospitalBtn');
    const closeBtn = document.querySelector('.close');
    const cancelBtn = document.querySelector('.cancel-btn');
    const addHospitalForm = document.getElementById('addHospitalForm');
    const is24HoursCheckbox = document.getElementById('is24Hours');
    const openTimeInput = document.getElementById('openTime');
    const closeTimeInput = document.getElementById('closeTime');
    const hospitalList = document.querySelector('.hospital-list');

    // Open modal
    addBtn.onclick = function() {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }

    // Close modal functions
    function closeModal() {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
        addHospitalForm.reset();
    }

    closeBtn.onclick = closeModal;
    cancelBtn.onclick = closeModal;

    // Close modal when clicking outside
    window.onclick = function(event) {
        if (event.target == modal) {
            closeModal();
        }
    }

    // Handle 24/7 checkbox
    is24HoursCheckbox.onchange = function() {
        const isChecked = this.checked;
        openTimeInput.disabled = isChecked;
        closeTimeInput.disabled = isChecked;
        if (isChecked) {
            openTimeInput.value = '';
            closeTimeInput.value = '';
        }
    }

    // Handle form submission
    addHospitalForm.onsubmit = async function(e) {
        e.preventDefault();

        // Get form data
        const formData = new FormData(this);
        
        // Create hospital data object
        const hospitalData = {
            name: formData.get('hospitalName'),
            address: formData.get('address'),
            district: formData.get('district'),
            workingHours: formData.get('is24Hours') ? '24/7' : 
                `${formData.get('openTime')} - ${formData.get('closeTime')}`,
            phone: formData.get('phone')
        };

        // Handle image file
        const imageFile = formData.get('hospitalImage');
        if (imageFile) {
            try {
                const imageUrl = await readFileAsDataURL(imageFile);
                const card = createHospitalCard(hospitalData, imageUrl);
                hospitalList.insertBefore(card, hospitalList.firstChild); // Add to the beginning of the list
                closeModal();
            } catch (error) {
                console.error('Error processing image:', error);
                alert('Şəkil yüklənərkən xəta baş verdi. Yenidən cəhd edin.');
            }
        }
    }

    // Function to read file as Data URL
    function readFileAsDataURL(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result);
            reader.onerror = () => reject(new Error('Şəkil oxuna bilmədi'));
            reader.readAsDataURL(file);
        });
    }

    // Create hospital card function
    function createHospitalCard(data, imageUrl) {
        const card = document.createElement('div');
        card.className = 'hospital-card';
        
        card.innerHTML = `
            <img src="${imageUrl}" alt="${data.name}">
            <h2>${data.name}</h2>
            <p><span class="las la-map-marker"></span>${data.address}, ${data.district} rayonu, Bakı</p>
            <p><span class="las la-clock"></span>İş saatları: ${data.workingHours}</p>
            <p><span class="las la-phone"></span>${data.phone}</p>
        `;
        
        return card;
    }

    // Search functionality
    const searchInput = document.getElementById('hospitalSearch');
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const hospitals = document.querySelectorAll('.hospital-card');
        
        hospitals.forEach(hospital => {
            const hospitalName = hospital.querySelector('h2').textContent.toLowerCase();
            const hospitalAddress = hospital.querySelector('p').textContent.toLowerCase();
            
            if (hospitalName.includes(searchTerm) || hospitalAddress.includes(searchTerm)) {
                hospital.style.display = 'block';
            } else {
                hospital.style.display = 'none';
            }
        });
    });
});
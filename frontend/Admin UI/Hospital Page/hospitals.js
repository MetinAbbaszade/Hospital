const hospitalImg = [
    './img/Hospital 1.jpg',
    './img/Hospital 2.jpg',
    './img/Hospital 3.jpg',
    './img/Hospital 4.jpg',
    'https://media.gettyimages.com/id/1312706413/photo/modern-hospital-building.jpg?s=612x612&w=0&k=20&c=oUILskmtaPiA711DP53DFhOUvE7pfdNeEK9CfyxlGio=',
    'https://media.gettyimages.com/id/1453876840/photo/hospital-sign.jpg?s=612x612&w=0&k=20&c=r1s1eCKhK4jprX4HodUDOZ32H_x5rK0xIASqTx1lwVs=',
    'https://media.gettyimages.com/id/1312706504/photo/modern-hospital-building.jpg?s=612x612&w=0&k=20&c=DT6YDRZMH5G5dL-Qv6VwPpVDpIDxJqkAY4Gg0ojGi58=',
    'https://media.gettyimages.com/id/1191945461/photo/modern-hospital-building.jpg?s=612x612&w=0&k=20&c=FtoTkJB1BTa1yu4qqHJN_RHAkZiB9ZNJ0B8LunTpRXs=',
    'https://media.gettyimages.com/id/173799627/photo/study-of-architectural-form-05.jpg?s=612x612&w=0&k=20&c=rrHldo5akJRAeGjm_5ICkzZrTooEYLcww1BkMeCc7Y0=',
    'https://media.gettyimages.com/id/182344359/photo/hospital.jpg?s=612x612&w=0&k=20&c=uRc1SKUdsXgpz-H4NdTtlvLOo5_dftXalm4j_CmIssI=',
    'https://media.gettyimages.com/id/157187378/photo/modern-building.jpg?s=612x612&w=0&k=20&c=uv2GYmOUDRpAL2vEnrdNxnlerEvC3K2OXTk3nyP6V64=',
    'https://media.gettyimages.com/id/183239497/photo/modern-hospital-building-exterior.jpg?s=612x612&w=0&k=20&c=AOR5m5SnHGB4ximhe06fgbTfrrgb9XCJLmCck_hLiz0=',
    'https://media.gettyimages.com/id/157525237/photo/modern-scottsdale-medical-business-building.jpg?s=612x612&w=0&k=20&c=my_e3_RjUAn21TmBKW_h-xrrCxzFMmwxDk8xindOtmY=',
    'https://media.gettyimages.com/id/2170018550/photo/post-cancer-check-up.jpg?s=612x612&w=0&k=20&c=cfVQGT4htRKg2nTI-wfmiadL2tFw4RtreXMJYCYmO60=',
    'https://media.gettyimages.com/id/157643948/photo/large-teaching-research-hospital.jpg?s=612x612&w=0&k=20&c=ovp3oGamE8OgthkfH045kg4zp0J7j7SHH0YHICmp1_A=',
    'https://media.gettyimages.com/id/171308566/photo/hospital.jpg?s=612x612&w=0&k=20&c=xmmW_3wc4-qpjZk2aJfHgVMuQYRtmP_bnh-G7hf02lM=',
    'https://media.gettyimages.com/id/626386896/photo/the-siriraj-hospital-in-bangkok-at-sunset.jpg?s=612x612&w=0&k=20&c=8OrZg785sPAwa9Lxlh_CGGeXbyC8c2Pa9Uzw5VcaypM=',
    'https://media.gettyimages.com/id/935715504/photo/netcare-hospital-in-rosebank-johannesburg.jpg?s=612x612&w=0&k=20&c=QFT53OtVBzyvus928LSB-S_1r2dpINio522g0eAwB4o='
]

const districtsByCity = {
    'Bakı': [
        'Nəsimi', 'Yasamal', 'Nərimanov', 'Binəqədi', 'Səbail',
        'Suraxanı', 'Xətai', 'Xəzər', 'Sabunçu', 'Nizami', 'Qaradağ'
    ],
    'Gəncə': [
        'Kəpəz', 'Nizami'
    ],
    'Sumqayıt': [
        '1-ci mikrorayon', '2-ci mikrorayon', '3-cü mikrorayon',
        'Corat', 'Kimyaçılar'
    ],
    'Mingəçevir': [
        'Energetiklər', 'Yevlax yolu', 'Yeni şəhər'
    ],
    'Şəki': [
        'Şəki mərkəz', 'Oxud', 'Baş Göynük'
    ],
    'Lənkəran': [
        'Lənkəran şəhər', 'Liman', 'Vel'
    ],
    'Naftalan': [
        'Naftalan mərkəz'
    ],
    'Quba': [
        'Quba şəhər', 'Qonaqkənd', 'Qırız'
    ],
    'Qusar': [
        'Qusar şəhər', 'Hil', 'Xuray'
    ],
    'Xaçmaz': [
        'Xaçmaz şəhər', 'Nabran', 'Xudat'
    ],
    'Zaqatala': [
        'Zaqatala şəhər', 'Mazıx', 'Yuxarı Tala'
    ],
    'Qax': [
        'Qax şəhər', 'Əlibəyli', 'Qaxbaş'
    ],
    'Ağcabədi': [
        'Ağcabədi şəhər', 'Avşar', 'Qiyaməddinli'
    ],
    'Ağdam': [
        'Ağdam şəhər', 'Gülablı', 'Quzanlı'
    ],
    'Bərdə': [
        'Bərdə şəhər', 'Əmirli', 'Uğurbəyli'
    ],
    'Tərtər': [
        'Tərtər şəhər', 'Seydimli', 'Azadqaraqoyunlu'
    ],
    'Yevlax': [
        'Yevlax şəhər', 'Havarlı', 'Qaramanlı'
    ],
    'Şamaxı': [
        'Şamaxı şəhər', 'Çuxuryurd', 'Göylər'
    ],
    'Salyan': [
        'Salyan şəhər', 'Şorsulu', 'Xalac'
    ],
    'Astara': [
        'Astara şəhər', 'Pensər', 'Archivan'
    ],
    'Masallı': [
        'Masallı şəhər', 'Boradigah', 'Təzə Alvadı'
    ],
    'Lerik': [
        'Lerik şəhər', 'Anbu', 'Cəngəmiran'
    ],
    'İmişli': [
        'İmişli şəhər', 'Məmmədli', 'Xubyarlı'
    ],
    'Sabirabad': [
        'Sabirabad şəhər', 'Nizami', 'Qaragüney'
    ],
    'Zərdab': [
        'Zərdab şəhər', 'Alıcanlı', 'Dəkkəoba'
    ]
};
const modal = document.getElementById('addHospitalModal');
const addBtn = document.getElementById('addHospitalBtn');
const closeBtn = document.querySelector('.close');
const cancelBtn = document.querySelector('.cancel-btn');
const addHospitalForm = document.getElementById('addHospitalForm');
const is24HoursCheckbox = document.getElementById('is24Hours');
const openTimeInput = document.getElementById('openTime');
const closeTimeInput = document.getElementById('closeTime');

const citySelect = document.getElementById('city');
const districtSelect = document.getElementById('district');


document.addEventListener("DOMContentLoaded", async () => {
    const hospitalData = await fetchHospitalDatas();
    const hospitalWrapper = document.querySelector('.hospital-list');

    hospitalWrapper.innerHTML = '';

    if (hospitalData.length === 0) {
        const noDataMessage = document.createElement('p');
        noDataMessage.className = 'no-hospitals-message';
        noDataMessage.textContent = 'No hospitals found.';
        hospitalWrapper.appendChild(noDataMessage);
    } else {
        hospitalData.forEach((hospital, index) => {
            const card = document.createElement('div');
            card.className = 'hospital-card';
            card.innerHTML = `
            <img src="${hospitalImg[index+1]}" alt="${hospital.name}">
            <h2>${hospital.name}</h2>
            <p><span class="las la-map-marker"></span>Address: ${hospital.street} ${hospital.state}, ${hospital.city} city</p>
            <p><span class="las la-clock"></span>Working Hours: 08:00 - 20:00</p>
            <p><span class="las la-phone"></span>${formatPhoneNumber(hospital.phone_number)}</p>
        `;
            hospitalWrapper.appendChild(card);
        });
    }

    const selectHospitalOwnerWrapper = document.querySelector('#hospital-owner');
    const hospitaOwnersData = await fetchHospitalOwners();
    hospitaOwnersData.forEach(owner => {
        const option = document.createElement('option');
        option.value = owner.id;
        option.textContent = `${toCapitalize(owner)}`;
        selectHospitalOwnerWrapper.appendChild(option);
    })

});

const fetchHospitalDatas = async () => {
    const response = await fetch('http://0.0.0.0:8000/api/v1/hospital/');
    const data = await response.json();
    return data;
}

function formatPhoneNumber(number) {
    return number.replace(/^(\+\d{3})(\d{2})(\d{3})(\d{2})(\d{2})$/, '$1 $2 $3 $4 $5');
}

const addHospital = async (hospitalData) => {
    const response = await fetch('http://0.0.0.0:8000/api/v1/hospital/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ...hospitalData })
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    } else {
        alert('Xəstəxana məlumatları uğurla yükləndi.');
    }
    window.location.reload();
}

const fetchHospitalOwners = async () => {
    const response = await fetch('http://0.0.0.0:8000/api/v1/owner/')
    const data = await response.json();
    return data;
}

addBtn.onclick = function () {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
    addHospitalForm.reset();
}

closeBtn.onclick = closeModal;
cancelBtn.onclick = closeModal;

window.onclick = function (event) {
    if (event.target == modal) {
        closeModal();
    }
}

is24HoursCheckbox.onchange = function () {
    const isChecked = this.checked;
    openTimeInput.disabled = isChecked;
    closeTimeInput.disabled = isChecked;
    if (isChecked) {
        openTimeInput.value = '';
        closeTimeInput.value = '';
    }
}

addHospitalForm.onsubmit = async function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    const hospitalData = {
        name: formData.get('hospitalName'),
        email: formData.get('hospitalEmail'),
        city: formData.get('city'),
        street: formData.get('address'),
        state: formData.get('district'),
        phone_number: formData.get('phone'),
        zipcode: formData.get('hospitalZipCode'),
        owner_id: formData.get('hospital-owner')
    };
    console.log('Hospital Data:', hospitalData);
    const hospitalList = document.querySelector('.hospital-list');

    try {
        addHospital(hospitalData);
        closeModal();
    } catch (error) {
        console.error('Error processing image:', error);
        alert('Xəstəxana məlumatları yüklənərkən xəta baş verdi. Yenidən cəhd edin.');
    }
}

function readFileAsDataURL(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = () => reject(new Error('Şəkil oxuna bilmədi'));
        reader.readAsDataURL(file);
    });
}


const searchInput = document.getElementById('hospitalSearch');
searchInput.addEventListener('input', function () {
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

const toCapitalize = (data) => (data.fname).replace(data.fname[0], data.fname[0].toUpperCase()) + " " + (data.lname).replace(data.lname[0], data.lname[0].toUpperCase());

citySelect.addEventListener('change', function () {
    const selectedCity = this.value;
    const districts = districtsByCity[selectedCity] || [];

    districtSelect.innerHTML = '<option value="">Rayon seçin</option>';

    districts.forEach(district => {
        const option = document.createElement('option');
        option.value = district;
        option.textContent = district;
        districtSelect.appendChild(option);
    });

    districtSelect.disabled = districts.length === 0;
});
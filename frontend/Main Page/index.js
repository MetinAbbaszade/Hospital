document.addEventListener('DOMContentLoaded', () => {
    if (isAuthenticated()) {
        document.querySelector('#login-button').style.display = 'none';
        document.querySelector('#register-button').style.display = 'none';
    }
    loadHospitals();
    loadDoctors();

    initChatbot();

    const quickActions = document.querySelector('.quick-actions');
    if (quickActions) {
        const hasHorizontalScroll = quickActions.scrollWidth > quickActions.clientWidth;
        const scrollIndicator = document.querySelector('.scroll-indicator');

        if (!hasHorizontalScroll && scrollIndicator) {
            scrollIndicator.style.display = 'none';
        }

        quickActions.addEventListener('scroll', function () {
            if (this.scrollLeft > 30) {
                scrollIndicator.style.opacity = '0';
                setTimeout(() => {
                    scrollIndicator.style.display = 'none';
                }, 300);
            }
        });

        quickActions.addEventListener('keydown', function (e) {
            if (e.key === 'ArrowRight') {
                this.scrollLeft += 100;
            } else if (e.key === 'ArrowLeft') {
                this.scrollLeft -= 100;
            }
        });
    }
});

const chatbotResponses = {
    "Ən yaxın xəstəxana?": "Sizə ən yaxın xəstəxana Mərkəzi Klinikadır. Ünvan: Rəşid Behbudov küç. 87, Bakı. Telefon: +994 12 310 10 10",
    "Həkim növləri?": "Bizim sistemdə aşağıdakı həkim növləri var: Kardioloq, Nevroloq, Dermatoloq, Pediatr, Ortoped, Ginekoloq, Oftalmoloq, Psixiatr, Onkoloq və Ümumi həkim.",
    "Qiymətlər?": "Müayinə qiymətləri həkim ixtisasından asılı olaraq 30-120 AZN arasında dəyişir. Dəqiq məlumat üçün xəstəxana ilə əlaqə saxlayın.",
    "İş saatları?": "Xəstəxanalarımız Bazar ertəsi-Cümə günləri 08:00-20:00, Şənbə 09:00-18:00 saatlarında fəaliyyət göstərir. Bazar günü 10:00-16:00 saatlarında yalnız təcili yardım şöbəsi işləyir.",
    "Təcili yardım?": "Təcili tibbi yardım üçün 103 və ya 112 nömrələri ilə əlaqə saxlaya bilərsiniz. Həmçinin MedAze tətbiqindən də təcili yardım çağıra bilərsiniz.",
    "Sığorta?": "Bizim xəstəxanalar şəbəkəsi Paşa Sığorta, Atəşgah Sığorta, AXA Mbask və digər əsas sığorta şirkətləri ilə əməkdaşlıq edir. Xidmət göstərilməzdən əvvəl sığorta kartınızı təqdim edin.",
    "Başım ağrıyır və başgicəllənmə hiss edirəm. Nə etməliyəm?": "Baş ağrısı və başgicəllənmə bir çox səbəbdən ola bilər. Əgər simptomlar kəskindirsə və ya qəflətən başlayıbsa, təcili tibbi yardıma müraciət edin. Digər hallarda Nevroloq və ya Ümumi həkimə müraciət etməyiniz məsləhətdir. Bol su için və dincəlin.",
    "Yüksək qızdırmam var və boğazım ağrıyır. Hansı həkimə müraciət etməliyəm?": "Qızdırma və boğaz ağrısı virus və ya bakterial infeksiyalara işarə ola bilər. Ümumi həkim və ya infeksionist həkimə müraciət etməyiniz tövsiyə olunur. Çox su için, parasetamol qəbul edin və dincəlin.",
    "Dərimdə səpkilər var və qaşınır. Bu nə ola bilər?": "Dəri səpkisi və qaşınma allergiya, dəri infeksiyası və ya digər dəri xəstəliklərindən ola bilər. Dermatoloqa müraciət etməyiniz tövsiyə olunur. Dəri səpkisinə toxunmamağa çalışın və hidratlaşdırıcı krem istifadə edin.",
    "Ürək döyüntülərim sürətlənib və nəfəs almaqda çətinlik çəkirəm. Təcili yardım lazımdır?": "Əgər kəskin nəfəs darlığı və sürətli ürək döyüntüsü yaşayırsınızsa, bu təcili tibbi vəziyyət ola bilər. Dərhal 103 və ya 112 ilə əlaqə saxlayın. Kardioloq müayinəsi tövsiyə olunur.",
    "Qarın ağrısı və ürəkbulanma hiss edirəm. Nə etməliyəm?": "Qarın ağrısı və ürəkbulanma həzm sistemində problem ola bilər. Qastroenteroloq və ya ümumi həkimə müraciət edin. Yağlı və ağır yeməklərdən uzaq durun, bol su için və yüngül qidalar qəbul edin.",
    "Oynaqlarda ağrı və şişkinlik var. Hansı həkimə getməliyəm?": "Oynaq ağrısı və şişkinlik revmatizm, artrit və ya travma əlaməti ola bilər. Revmatoloq və ya ortopedə müraciət edin. İsti kompres və ağrıkəsici kremlər müvəqqəti rahatlıq verə bilər.",
    "Göz qızartısı və qaşınma hiss edirəm. Allergiya ola bilər?": "Göz qızartısı və qaşınma allergik reaksiya, göz infeksiyası və ya quruluq səbəbi ilə ola bilər. Oftalmoloqa müraciət edin. Gözlərinizi ovuşdurmaqdan çəkinin və təmiz su ilə yuyun.",
    "Uşağımın səpgisi və yüksək hərarəti var. Təcili müdaxilə lazımdır?": "Uşaqlarda səpgi və yüksək hərarət müxtəlif infeksiyaların əlaməti ola bilər. Pediatra müraciət edin. Əgər uşaq 3 aydan kiçikdirsə və ya hərarət 39°C-dən yüksəkdirsə, dərhal tibbi yardım alın. Parasetamol uşaq dozasında və çox su vermək tövsiyə olunur."
};

function initChatbot() {
    const quickActionButtons = document.querySelectorAll('.quick-action-btn');
    const chatMessages = document.getElementById('chatMessages');

    quickActionButtons.forEach(button => {
        button.addEventListener('click', function () {
            const question = this.getAttribute('data-question');
            addUserMessage(question);

            quickActionButtons.forEach(btn => btn.disabled = true);

            // Add a small delay to simulate processing
            setTimeout(() => {
                addBotMessage(chatbotResponses[question]);

                quickActionButtons.forEach(btn => btn.disabled = false);
            }, 1000);
        });
    });
}

function addUserMessage(message) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user';
    messageDiv.innerHTML = `
        <i class="fas fa-user"></i>
        <div class="message-content">
            ${message}
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function addBotMessage(message) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot';
    messageDiv.innerHTML = `
        <i class="fas fa-robot"></i>
        <div class="message-content">
            ${message}
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function scrollToBottom() {
    const chatMessages = document.getElementById('chatMessages');
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

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
                        <i class="fas fa-stethoscope"></i>${specializations[0]}
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
        return specializations;
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
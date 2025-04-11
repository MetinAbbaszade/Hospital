const hospitalImg = [
    './hospitalImg/Bakı Mərkəzi Klinikası.jpg',
    './hospitalImg/Gəncə Şəhər Xəstəxanası.jpg',
    './hospitalImg/Mingəçevir Regional Xəstəxanası.jpg',
    './hospitalImg/New Hospital.jpg',
    './hospitalImg/Qəbələ Rayon Xəstəxanası.jpg',
    './hospitalImg/Şəfa Tibb Mərkəzi.jpg',
    'hospitalImg/Şəki Rayon Xəstəxanası.jpg',
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



const aboutDoctors = {
    "kardiologiya": "Kardioloqlar ürək və qan damarları xəstəliklərinin, o cümlədən hipertoniya, aritmiya və ürək çatışmazlığının diaqnostika və müalicəsində ixtisaslaşırlar.",
    "ortopediya": "Ortopedlər sümük, oynaqlar və əzələ sistemi ilə bağlı problemlərin, o cümlədən sınıqlar, artrit və idman xəsarətlərinin müalicəsi ilə məşğul olurlar.",
    "təcili_yardım": "Təcili yardım həkimləri qəfil və həyati təhlükə yaradan tibbi hallarda sürətli və effektiv tibbi yardım göstərirlər.",
    "nevrologiya": "Nevroloqlar beyin, onurğa beyni və sinirlər daxil olmaqla sinir sistemi pozuntularının diaqnostikası və müalicəsini aparırlar.",
    "onkologiya": "Onkoloqlar xərçəng və şiş xəstəliklərinin diaqnostika və müalicəsində ixtisaslaşırlar; kimyaterapiya, immunoterapiya və palyativ baxımı həyata keçirirlər.",
    "pediatriya": "Pediatrlar doğuşdan yeniyetməlik dövrünə qədər uşaqların sağlamlığı və inkişafına nəzarət edir, xəstəliklərin müalicəsini həyata keçirirlər.",
    "dermatologiya": "Dermatoloqlar dəri, saç və dırnaqlarla bağlı xəstəliklərin, o cümlədən sızanaq, ekzema və dəri xərçəngi kimi problemlərin müalicəsi ilə məşğul olurlar.",
    "cərrahiyyə": "Cərrahlar müxtəlif xəstəlik və zədələrin müalicəsi üçün əməliyyatlar həyata keçirirlər – həm açıq, həm də minimal invaziv prosedurlar şəklində.",
    "radiologiya": "Radioloqlar rentgen, KT, MRT kimi görüntüləmə üsullarından istifadə edərək diaqnoz qoyurlar və bəzən müalicə də edirlər.",
    "endokrinologiya": "Endokrinoloqlar hormon balanssızlıqları və şəkərli diabet, qalxanabənzər vəzi xəstəlikləri kimi hormonal problemlərin müalicəsində ixtisaslaşırlar.",
    "psixiatriya": "Psixiatrlar zehni pozuntular, o cümlədən depressiya, narahatlıq, şizofreniya kimi xəstəliklərin diaqnostika və müalicəsini həyata keçirirlər və dərman yaza bilirlər.",
    "daxili_xəstəliklər": "Terapevtlər (daxili xəstəliklər üzrə həkimlər) orqan sistemlərinin müxtəlif xəstəliklərini aşkarlayır və müalicə edirlər.",
    "nefrologiya": "Nefroloqlar böyrəklərlə bağlı xəstəliklərin, o cümlədən xroniki böyrək çatışmazlığı və dializ müalicəsinin aparılması ilə məşğul olurlar.",
    "qastroenterologiya": "Qastroenteroloqlar həzm sistemi xəstəliklərinin – mədə, bağırsaq, qaraciyər və mədəaltı vəzi pozuntularının müalicəsi ilə məşğul olurlar.",
    "pulmonologiya": "Pulmonoloqlar tənəffüs sistemi xəstəliklərinin, o cümlədən astma, KOAH və sətəlcəm kimi problemlərin diaqnostika və müalicəsini həyata keçirirlər.",
    "allergologiya": "Allerqoloqlar allergik reaksiyalar, o cümlədən toz, yemək və dərman allergiyalarının və immun sistem pozuntularının müalicəsi ilə məşğul olurlar.",
    "revmotologiya": "Revmotoloqlar oynaq və əzələ xəstəlikləri, məsələn revmatoid artrit və digər autoimmun xəstəlikləri müalicə edirlər.",
    "ağrı_müalicəsi": "Ağrı mütəxəssisləri xroniki və kəskin ağrıların idarə edilməsi və müalicəsi ilə məşğul olurlar.",
    "geriatriya": "Geriatriya həkimləri yaşlı insanların sağlamlıq problemlərinin diaqnostika və müalicəsi ilə məşğul olurlar.",
    "infeksion_xəstəliklər": "İnfeksionistlər bakterial, virus və digər yoluxucu xəstəliklərin, məsələn hepatit və COVID-19-un müalicəsini həyata keçirirlər.",
    "plastik_cərrahiyyə": "Plastik cərrahlar estetik və rekonstruktiv əməliyyatlar apararaq görünüşü yaxşılaşdırır və ya deformasiyaları aradan qaldırırlar.",
    "lor": "LOR (qulaq, burun, boğaz) həkimləri bu orqanlarla bağlı xəstəliklərin müalicəsini həyata keçirirlər – məsələn, sinusit, otit və səs problemləri.",
    "infeksion xəstəliklər": "İnfeksionistlər bakterial, virus və digər yoluxucu xəstəliklərin, məsələn hepatit və COVID-19-un müalicəsini həyata keçirirlər."
  };
  

document.addEventListener('DOMContentLoaded', () => {
    if (isAuthenticated()) {
        document.querySelector('#login-button').style.display = 'none';
        document.querySelector('#register-button').style.display = 'none';
    }
    if(!isAuthenticated()){
        document.querySelector('#profileDropdown').style.display = 'none';
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

        console.log(doctor.fname)
        if (count != 6) {
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
                <img src="doctorImg/${doctor.fname}.webp"
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
                    <p class="doctor-description">${aboutDoctors[specializations[0].toLowerCase()]}</p>
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
    let count = 0;
    for (const hospital of hospitals) {
        if (count != 6) {
            const card = document.createElement('div');
            card.className = 'col-md-4';
            card.innerHTML = `
                <div class="card hospital-card">
                            <div class="card-badge"><i class="fas fa-check-circle"></i> Premium</div>
                            <img src="${hospitalImg[count + 1]}" class="card-img-top" alt="${hospital.name}">
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
            count++;
        }else{
            return;
        }
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

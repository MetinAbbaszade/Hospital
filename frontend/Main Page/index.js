// API endpoint for hospitals
const API_URL = 'http://localhost:8000/api/v1';

// Load hospitals when the page loads
document.addEventListener('DOMContentLoaded', loadHospitals);

async function loadHospitals() {
    try {
        const response = await fetch(`${API_URL}/hospitals/`);
        const hospitals = await response.json();
        displayHospitals(hospitals);
    } catch (error) {
        console.error('Error loading hospitals:', error);
    }
}

function displayHospitals(hospitals) {
    const container = document.getElementById('hospitals-container');
    container.innerHTML = '';

    hospitals.forEach(hospital => {
        const card = document.createElement('div');
        card.className = 'col-md-4';
        card.innerHTML = `
            <div class="card hospital-card">
                <img src="${hospital.image || 'Admin UI/Hospital Page/Hospital 1.jpg'}" class="card-img-top" alt="${hospital.name}">
                <div class="card-body">
                    <h5 class="card-title">${hospital.name}</h5>
                    <p class="card-text">${hospital.address}</p>
                    <p class="card-text">
                        <small class="text-muted">
                            <i class="fas fa-phone"></i> ${hospital.phone}
                        </small>
                    </p>
                    <button class="btn btn-primary" onclick="bookAppointment(${hospital.id})">
                        Book Appointment
                    </button>
                </div>
            </div>
        `;
        container.appendChild(card);
    });
}

function bookAppointment(hospitalId) {
    // Redirect to login if user is not authenticated
    if (!isAuthenticated()) {
        window.location.href = 'Login Page/login_sign.html';
        return;
    }
    // Otherwise redirect to appointment page
    window.location.href = `Admin UI/Appoints Page/appoints.html?hospital=${hospitalId}`;
}

function isAuthenticated() {
    // Check if user has valid token in localStorage
    return localStorage.getItem('token') !== null;
}

function scrollToHospitals() {
    document.getElementById('hospitals').scrollIntoView({ behavior: 'smooth' });
}

// Chatbot functionality
let isChatbotMinimized = false;

function toggleChatbot() {
    const chatbotBody = document.getElementById('chatbot-body');
    const minimizeBtn = document.querySelector('.minimize-btn i');
    
    if (isChatbotMinimized) {
        chatbotBody.style.display = 'flex';
        minimizeBtn.className = 'fas fa-minus';
    } else {
        chatbotBody.style.display = 'none';
        minimizeBtn.className = 'fas fa-plus';
    }
    
    isChatbotMinimized = !isChatbotMinimized;
}

function sendMessage() {
    const input = document.getElementById('chatbot-input');
    const message = input.value.trim();
    
    if (message) {
        addMessage('user', message);
        input.value = '';
        
        // Process the message and get bot response
        processMessage(message);
    }
}

function addMessage(sender, text) {
    const messages = document.getElementById('chatbot-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.textContent = text;
    messages.appendChild(messageDiv);
    messages.scrollTop = messages.scrollHeight;
}

function processMessage(message) {
    // Simple response logic - can be expanded with more sophisticated AI/API integration
    const responses = {
        'hello': 'Hi! How can I help you today?',
        'hi': 'Hello! What can I do for you?',
        'appointment': 'To book an appointment, please select a hospital from the list above and click "Book Appointment".',
        'help': 'I can help you with: \n- Finding hospitals\n- Booking appointments\n- General information',
        'default': 'I\'m here to help! You can ask about hospitals, appointments, or any other healthcare related questions.'
    };

    const lowercaseMsg = message.toLowerCase();
    let response = responses.default;

    for (const [key, value] of Object.entries(responses)) {
        if (lowercaseMsg.includes(key)) {
            response = value;
            break;
        }
    }

    // Simulate typing delay
    setTimeout(() => {
        addMessage('bot', response);
    }, 500);
}

// Handle Enter key in chatbot input
document.getElementById('chatbot-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Chat functionality
document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chatMessages');
    const searchInput = document.getElementById('searchInput');
    const sendButton = document.getElementById('sendButton');

    const addMessage = (message, isUser = false) => {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
        
        const icon = document.createElement('i');
        icon.className = isUser ? 'fas fa-user' : 'fas fa-robot';
        
        const content = document.createElement('div');
        content.className = 'message-content';
        content.textContent = message;
        
        messageDiv.appendChild(icon);
        messageDiv.appendChild(content);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    const processQuestion = (question) => {
        // Sample responses - in a real app, this would be connected to a backend
        const responses = {
            'ən yaxın xəstəxana': 'Sizə ən yaxın xəstəxana Central Hospital-dır. Ünvan: Bakı şəhəri, Nərimanov rayonu.',
            'həkim növləri': 'Bizim xəstəxanalarda müxtəlif ixtisaslar var: Kardioloq, Nevroloq, Pediatr, Dermatoloq, Ortoped və s.',
            'qiymətlər': 'Qiymətlər həkim və xəstəxanaya görə dəyişir. Ümumi müayinə: 30-50 AZN, Mütəxəssis müayinəsi: 50-100 AZN.',
            'default': 'Üzr istəyirəm, bu sual haqqında məlumatım yoxdur. Zəhmət olmasa, daha dəqiq sual verin və ya +994 12 345 67 89 nömrəsi ilə əlaqə saxlayın.'
        };

        const questionLower = question.toLowerCase();
        let response = responses.default;

        for (const [key, value] of Object.entries(responses)) {
            if (questionLower.includes(key)) {
                response = value;
                break;
            }
        }

        addMessage(response);
    };

    const handleSend = () => {
        const message = searchInput.value.trim();
        if (message) {
            addMessage(message, true);
            searchInput.value = '';
            setTimeout(() => processQuestion(message), 500);
        }
    };

    sendButton.addEventListener('click', handleSend);
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleSend();
        }
    });
});

// Function for quick action buttons
function askQuestion(question) {
    const searchInput = document.getElementById('searchInput');
    searchInput.value = question;
    document.getElementById('sendButton').click();
}

// Language translations
const translations = {
    az: {
        hospitals: "Xəstəxanalar",
        doctors: "Həkimlər",
        about: "Haqqımızda",
        contact: "Əlaqə",
        register: "Qeydiyyat",
        login: "Daxil ol",
        language: "Dil",
        welcome: "MedAze-yə xoş gəlmisiniz",
        findHospitals: "Xəstəxanaları tap",
        description: "Ən yaxşı xəstəxanaları tapın, görüş təyin edin və dərhal tibbi yardım alın.",
        quickLinks: "Sürətli Keçidlər",
        services: "Xidmətlər",
        contactInfo: "Əlaqə Məlumatları",
        bookAppointment: "Görüş təyin et",
        findDoctor: "Həkim tap",
        emergencyCare: "Təcili Yardım",
        insurance: "Sığorta",
        ourDoctors: "Həkimlərimiz",
        topRated: "Ən Yaxşı",
        certified: "Sertifikatlı",
        experience: "il təcrübə",
        specializes: "İxtisaslaşıb:",
        cardiology: "Kardioloq",
        neurology: "Nevroloq",
        pediatrics: "Pediatr",
        centralHospital: "Mərkəzi Xəstəxana",
        medicalCenter: "Tibb Mərkəzi",
        childrensHospital: "Uşaq Xəstəxanası",
        doctorDescriptions: {
            sarah: "Ürək xəstəlikləri və kardiovaskulyar sağlamlıq üzrə ixtisaslaşıb. Mürəkkəb kardiak prosedurlar üzrə təcrübəlidir.",
            michael: "Nevroloji pozuntular və beyin sağlamlığı üzrə ekspert. Hərtərəfli nevroloji qayğı göstərir.",
            emily: "Uşaq sağlamlığı və inkişafına həsr olunub. Pediatrik qayğı və müalicədə təcrübəlidir."
        }
    },
    en: {
        hospitals: "Hospitals",
        doctors: "Doctors",
        about: "About",
        contact: "Contact",
        register: "Register",
        login: "Login",
        language: "Language",
        welcome: "Welcome to MedAze",
        findHospitals: "Find Hospitals",
        description: "Find the best hospitals, book appointments, and get instant medical assistance.",
        quickLinks: "Quick Links",
        services: "Services",
        contactInfo: "Contact Info",
        bookAppointment: "Book Appointment",
        findDoctor: "Find Doctor",
        emergencyCare: "Emergency Care",
        insurance: "Insurance",
        ourDoctors: "Our Doctors",
        topRated: "Top Rated",
        certified: "Certified",
        experience: "Years Experience",
        specializes: "Specializes in:",
        cardiology: "Cardiologist",
        neurology: "Neurologist",
        pediatrics: "Pediatrician",
        centralHospital: "Central Hospital",
        medicalCenter: "Medical Center",
        childrensHospital: "Children's Hospital",
        doctorDescriptions: {
            sarah: "Specializes in heart diseases and cardiovascular health. Experienced in complex cardiac procedures.",
            michael: "Expert in neurological disorders and brain health. Provides comprehensive neurological care.",
            emily: "Dedicated to children's health and development. Experienced in pediatric care and treatment."
        }
    },
    ru: {
        hospitals: "Больницы",
        doctors: "Врачи",
        about: "О нас",
        contact: "Контакты",
        register: "Регистрация",
        login: "Вход",
        language: "Язык",
        welcome: "Добро пожаловать в MedAze",
        findHospitals: "Найти больницы",
        description: "Найдите лучшие больницы, записывайтесь на прием и получайте мгновенную медицинскую помощь.",
        quickLinks: "Быстрые ссылки",
        services: "Услуги",
        contactInfo: "Контактная информация",
        bookAppointment: "Записаться на прием",
        findDoctor: "Найти врача",
        emergencyCare: "Экстренная помощь",
        insurance: "Страхование",
        ourDoctors: "Наши врачи",
        topRated: "Лучший",
        certified: "Сертифицированный",
        experience: "лет опыта",
        specializes: "Специализация:",
        cardiology: "Кардиолог",
        neurology: "Невролог",
        pediatrics: "Педиатр",
        centralHospital: "Центральная больница",
        medicalCenter: "Медицинский центр",
        childrensHospital: "Детская больница",
        doctorDescriptions: {
            sarah: "Специализируется на заболеваниях сердца и сердечно-сосудистой системы. Имеет опыт проведения сложных кардиологических процедур.",
            michael: "Эксперт по неврологическим расстройствам и здоровью мозга. Предоставляет комплексную неврологическую помощь.",
            emily: "Посвятила себя здоровью и развитию детей. Имеет опыт в педиатрическом уходе и лечении."
        }
    }
};

// Set default language
let currentLang = 'az';

// Function to update content
function updateContent(lang) {
    currentLang = lang;
    
    // Update navigation items
    document.querySelector('a[href="#hospitals"]').innerHTML = `<i class="fas fa-hospital me-1"></i>${translations[lang].hospitals}`;
    document.querySelector('a[href="#doctors"]').innerHTML = `<i class="fas fa-user-md me-1"></i>${translations[lang].doctors}`;
    document.querySelector('a[href="#about"]').innerHTML = `<i class="fas fa-info-circle me-1"></i>${translations[lang].about}`;
    document.querySelector('a[href="#contact"]').innerHTML = `<i class="fas fa-envelope me-1"></i>${translations[lang].contact}`;
    
    // Update login/register buttons
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.innerHTML.includes('Register')) {
            link.innerHTML = `<i class="fas fa-user-plus me-1"></i>${translations[lang].register}`;
        }
        if (link.innerHTML.includes('Login')) {
            link.innerHTML = `<i class="fas fa-sign-in-alt me-1"></i>${translations[lang].login}`;
        }
        if (link.innerHTML.includes('Language')) {
            link.innerHTML = `<i class="fas fa-globe me-1"></i>${translations[lang].language}`;
        }
    });
    
    // Update hero section
    document.querySelector('.hero h1').innerHTML = translations[lang].welcome;
    document.querySelector('.hero p').textContent = translations[lang].description;
    document.querySelector('.hero .btn-primary').innerHTML = `<i class="fas fa-hospital-user me-2"></i>${translations[lang].findHospitals}`;
    
    // Update doctors section
    document.querySelector('.doctors-section h2').innerHTML = `<i class="fas fa-user-md me-2"></i>${translations[lang].ourDoctors}`;
    
    // Update doctor cards
    const doctorCards = document.querySelectorAll('.doctor-card');
    doctorCards.forEach((card, index) => {
        const badges = card.querySelectorAll('.card-badge');
        badges.forEach(badge => {
            if (badge.innerHTML.includes('Top Rated')) {
                badge.innerHTML = `<i class="fas fa-star"></i>${translations[lang].topRated}`;
            }
            if (badge.innerHTML.includes('Certified')) {
                badge.innerHTML = `<i class="fas fa-certificate"></i>${translations[lang].certified}`;
            }
        });

        const features = card.querySelectorAll('.doctor-features span');
        features.forEach(feature => {
            if (feature.innerHTML.includes('Central Hospital')) {
                feature.innerHTML = `<i class="fas fa-hospital"></i>${translations[lang].centralHospital}`;
            }
            if (feature.innerHTML.includes('Medical Center')) {
                feature.innerHTML = `<i class="fas fa-hospital"></i>${translations[lang].medicalCenter}`;
            }
            if (feature.innerHTML.includes('Children')) {
                feature.innerHTML = `<i class="fas fa-hospital"></i>${translations[lang].childrensHospital}`;
            }
            if (feature.innerHTML.includes('Years')) {
                const years = feature.innerHTML.match(/\d+/)[0];
                feature.innerHTML = `<i class="fas fa-clock"></i>${years} ${translations[lang].experience}`;
            }
        });

        const specialty = card.querySelector('.card-text');
        if (specialty.innerHTML.includes('Cardiologist')) {
            specialty.innerHTML = `<i class="fas fa-stethoscope"></i>${translations[lang].cardiology}`;
        }
        if (specialty.innerHTML.includes('Neurologist')) {
            specialty.innerHTML = `<i class="fas fa-stethoscope"></i>${translations[lang].neurology}`;
        }
        if (specialty.innerHTML.includes('Pediatrician')) {
            specialty.innerHTML = `<i class="fas fa-stethoscope"></i>${translations[lang].pediatrics}`;
        }

        const description = card.querySelector('.doctor-description');
        if (description.innerHTML.includes('Sarah')) {
            description.textContent = translations[lang].doctorDescriptions.sarah;
        }
        if (description.innerHTML.includes('Michael')) {
            description.textContent = translations[lang].doctorDescriptions.michael;
        }
        if (description.innerHTML.includes('Emily')) {
            description.textContent = translations[lang].doctorDescriptions.emily;
        }

        const appointmentBtn = card.querySelector('.btn-primary');
        appointmentBtn.innerHTML = `<i class="fas fa-calendar-check"></i>${translations[lang].bookAppointment}`;
    });
    
    // Update footer sections
    document.querySelectorAll('.footer h5').forEach(h5 => {
        if (h5.innerHTML.includes('Quick Links')) {
            h5.innerHTML = `<i class="fas fa-link me-2"></i>${translations[lang].quickLinks}`;
        }
        if (h5.innerHTML.includes('Services')) {
            h5.innerHTML = `<i class="fas fa-stethoscope me-2"></i>${translations[lang].services}`;
        }
        if (h5.innerHTML.includes('Contact Info')) {
            h5.innerHTML = `<i class="fas fa-phone-alt me-2"></i>${translations[lang].contactInfo}`;
        }
    });
    
    // Update footer links
    document.querySelectorAll('.footer a').forEach(link => {
        if (link.innerHTML.includes('Book Appointment')) {
            link.innerHTML = `<i class="fas fa-chevron-right"></i>${translations[lang].bookAppointment}`;
        }
        if (link.innerHTML.includes('Find Doctor')) {
            link.innerHTML = `<i class="fas fa-chevron-right"></i>${translations[lang].findDoctor}`;
        }
        if (link.innerHTML.includes('Emergency Care')) {
            link.innerHTML = `<i class="fas fa-chevron-right"></i>${translations[lang].emergencyCare}`;
        }
        if (link.innerHTML.includes('Insurance')) {
            link.innerHTML = `<i class="fas fa-chevron-right"></i>${translations[lang].insurance}`;
        }
        if (link.innerHTML.includes('Hospitals')) {
            link.innerHTML = `<i class="fas fa-chevron-right"></i>${translations[lang].hospitals}`;
        }
        if (link.innerHTML.includes('Doctors')) {
            link.innerHTML = `<i class="fas fa-chevron-right"></i>${translations[lang].doctors}`;
        }
        if (link.innerHTML.includes('About')) {
            link.innerHTML = `<i class="fas fa-chevron-right"></i>${translations[lang].about}`;
        }
        if (link.innerHTML.includes('Contact')) {
            link.innerHTML = `<i class="fas fa-chevron-right"></i>${translations[lang].contact}`;
        }
    });
}

// Add click event listeners to language options
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.dropdown-item').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const lang = e.target.closest('.dropdown-item').getAttribute('data-lang');
            updateContent(lang);
        });
    });
});

// Initialize with default language
updateContent(currentLang);

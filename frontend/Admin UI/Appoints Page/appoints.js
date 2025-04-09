const obj = {
    'pending': 'pending',
    'confirmed': 'confirmed',
    'canceled': 'canceled',
}
document.addEventListener('DOMContentLoaded', async function () {
    const appointmentWrapper = document.querySelector('.appointment-timeline');
    const appointmentDatas = await fetchAppointmentData();

    for (const appointment of appointmentDatas) {
        const appointmentItem = document.createElement('div');
        appointmentItem.classList.add('timeline-item');
        const doctorData = await fetchDoctorData(appointment.doctor_id);
        const hospitalData = await fetchHospitalData(doctorData.hospital_id);
        appointmentItem.innerHTML = `
        <div class="appointment-time">${(appointment.date_time).slice(0, 10)} ${(appointment.date_time).slice(11, 16)}</div>
                    <div class="appointment-info">
                        <div class="info-item">
                            <i class="las la-hospital"></i>
                            <div>
                                <div class="info-label">Hospital</div>
                                <div class="info-value">${hospitalData.name}</div>
                            </div>
                        </div>
                        <div class="info-item">
                            <i class="las la-user-md"></i>
                            <div>
                                <div class="info-label">Doctor</div>
                                <div class="info-value">${toCapitalize(doctorData)}</div>
                            </div>
                        </div>
                        <div class="info-item">
                            <i class="las la-stethoscope"></i>
                            <div>
                                <div class="info-label">Problem</div>
                                <div class="info-value">${appointment.problem}</div>
                            </div>
                        </div>
                        <div class="info-item">
                            <i class="las la-clock"></i>
                            <div>
                                <div class="info-label">Duration</div>
                                <div class="info-value">30 minutes</div>
                            </div>
                        </div>
                    </div>
                    <div class="appointment-status">
                        <span class="status ${obj[appointment.status]}">${appointment.status}</span>
                    </div>
                    <div class="appointment-actions">
                        <button class="action-btn reschedule-btn">
                            <i class="las la-calendar"></i>
                            Reschedule
                        </button>
                        ${appointment.status === 'pending' ? `<button class="action-btn cancel-btn">
                            <i class="las la-times"></i>
                            Cancel
                        </button>` : ''}
                    </div>`
        appointmentWrapper.append(appointmentItem);
    }

    const appointmentsCount = appointmentDatas.length;
    document.querySelector('#appointmentCount').innerText = appointmentsCount;
    const pendingCount = appointmentDatas.filter(appointment => appointment.status === 'pending').length;
    document.querySelector('#pendingAppointmentCount').innerText = pendingCount;
    const confirmedCount = appointmentDatas.filter(appointment => appointment.status === 'confirmed').length;
    document.querySelector('#confirmedAppointmentCount').innerText = confirmedCount;

    // const timelineItems = document.querySelectorAll('.timeline-item');
    // timelineItems.forEach((item, index) => {
    //     setTimeout(() => {
    //         item.style.opacity = '1';
    //         item.style.transform = 'translateX(0)';
    //     }, 100 * index);
    // });
});

const fetchAppointmentData = async () => {
    const response = await fetch('http://0.0.0.0:8000/api/v1/appointment/');
    const data = await response.json();
    return data;
}

const fetchHospitalData = async (hospitalId) => {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/hospital/${hospitalId}`);
    const data = await response.json();
    return data;
}

const fetchDoctorData = async (doctorId) => {
    const response = await fetch(`http://0.0.0.0:8000/api/v1/doctor/${doctorId}`);
    const data = await response.json();
    return data;
}


const toCapitalize = (data) => (data.fname).replace(data.fname[0], data.fname[0].toUpperCase()) + " " + (data.lname).replace(data.lname[0], data.lname[0].toUpperCase());

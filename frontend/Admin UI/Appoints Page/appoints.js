document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchInput = document.getElementById('appointSearch');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const appointments = document.querySelectorAll('.timeline-item');
            
            appointments.forEach(appointment => {
                const text = appointment.textContent.toLowerCase();
                if (text.includes(searchTerm)) {
                    appointment.style.display = 'block';
                } else {
                    appointment.style.display = 'none';
                }
            });
        });
    }

    // Add new appointment button
    const addAppointBtn = document.getElementById('addAppointBtn');
    if (addAppointBtn) {
        addAppointBtn.addEventListener('click', function() {
            // Show modal or form for new appointment
            alert('Add New Appointment clicked');
        });
    }

    // Handle appointment actions (Reschedule/Cancel)
    const actionButtons = document.querySelectorAll('.action-btn');
    actionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const appointmentItem = this.closest('.timeline-item');
            if (this.classList.contains('reschedule-btn')) {
                alert('Reschedule appointment clicked');
            } else if (this.classList.contains('cancel-btn')) {
                if (confirm('Are you sure you want to cancel this appointment?')) {
                    appointmentItem.remove();
                }
            }
        });
    });

    // Initialize animations
    const timelineItems = document.querySelectorAll('.timeline-item');
    timelineItems.forEach((item, index) => {
        setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'translateX(0)';
        }, 100 * index);
    });
});
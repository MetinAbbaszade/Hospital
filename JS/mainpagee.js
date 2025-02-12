const navToggle = document.getElementById('nav-toggle');
const sidebar = document.querySelector('.sidebar');

navToggle.addEventListener('change', () => {
    if (navToggle.checked) {
        sidebar.style.transform = 'translateX(0)';
    } else {
        sidebar.style.transform = 'translateX(-250px)';
    }
});

const searchInput = document.querySelector('input[type="search"]');
const appointsRows = document.querySelectorAll('.recent-grid .projects .card-body table tbody tr');
const usersRows = document.querySelectorAll('.customers .card-body .customer');

searchInput.addEventListener('input', (event) => {
    const query = event.target.value.toLowerCase();

    appointsRows.forEach(row => {
        const title = row.querySelector('td:first-child').textContent.toLowerCase();
        const hospital = row.querySelector('td:nth-child(2)').textContent.toLowerCase();

        if (title.includes(query) || hospital.includes(query)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });

    usersRows.forEach(user => {
        const name = user.querySelector('.info h4').textContent.toLowerCase();
        const role = user.querySelector('.info small').textContent.toLowerCase();

        if (name.includes(query) || role.includes(query)) {
            user.style.display = '';
        } else {
            user.style.display = 'none';
        }
    });
});

const navToggle = document.getElementById('nav-toggle');
const sidebar = document.querySelector('.sidebar');

navToggle.addEventListener('change', () => {
    sidebar.style.transform = navToggle.checked ? 'translateX(0)' : 'translateX(-250px)';
});

const seachInput = document.querySelector('input[type="search"]');
const appointsRows = document.querySelectorAll('.recent-grid .projects .card-body table tbody tr');
const usersRows = document.querySelectorAll('.customers .card-body .customer');

searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();

    appointsRows.forEach(row => {
        const title = row.children[0].textContent.toLowerCase();
        const hospital = row.children[1].textContent.toLowerCase();

        row.style.display = (title.includes(query) || hospital.includes(query)) ? '' : 'none';
    });

    usersRows.forEach(user => {
    
        const role = user.querySelector('.info small').textContent.toLowerCase();

        user.style.display = (name.includes(query) || role.includes(query)) ? '' : 'none';
    });
});

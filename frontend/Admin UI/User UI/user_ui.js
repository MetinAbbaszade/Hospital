// Profile Image Upload
const fileInput = document.getElementById('file-input');
const profileImage = document.querySelector('.profile-image-container img');
const headerProfileImage = document.getElementById('headerProfileImage');

fileInput.addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            // Update both profile images
            profileImage.src = e.target.result;
            headerProfileImage.src = e.target.result;
        }
        reader.readAsDataURL(file);
    }
});

// Edit Profile Modal
const modal = document.getElementById('editProfileModal');
const editBtn = document.querySelector('.edit-profile-btn');
const closeBtn = document.querySelector('.close-modal');
const editForm = document.getElementById('editProfileForm');
const headerUsername = document.getElementById('headerUsername');

// Set initial values when opening modal
editBtn.addEventListener('click', () => {
    document.getElementById('editName').value = document.querySelector('.info-item:nth-child(1) .value').textContent;
    document.getElementById('editEmail').value = document.querySelector('.info-item:nth-child(2) .value').textContent;
    document.getElementById('editPhone').value = document.querySelector('.info-item:nth-child(3) .value').textContent;
    document.getElementById('editAddress').value = document.querySelector('.info-item:nth-child(4) .value').textContent;
    
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
});

closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
});

window.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});

editForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Get the new name value
    const newName = document.getElementById('editName').value;
    
    // Update profile information
    document.querySelector('.info-item:nth-child(1) .value').textContent = newName;
    document.querySelector('.info-item:nth-child(2) .value').textContent = document.getElementById('editEmail').value;
    document.querySelector('.info-item:nth-child(3) .value').textContent = document.getElementById('editPhone').value;
    document.querySelector('.info-item:nth-child(4) .value').textContent = document.getElementById('editAddress').value;
    
    // Update header username
    headerUsername.textContent = newName;
    
    // Close modal
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';

    // Show success message
    alert('Profile updated successfully!');
});


const signupBtn = document.getElementById('signup-btn');
const signinBtn = document.getElementById('signin-btn');
const signupForm = document.querySelector('.signup-form');
const signinForm = document.querySelector('.signin-form');
const signupIntro = document.querySelector('.signup-intro');
const signinIntro = document.querySelector('.signin-intro');


signupBtn.addEventListener('click', () => {
   
    signupForm.style.display = 'block';
    signupIntro.style.display = 'block';
    signinForm.style.display = 'none';
    signinIntro.style.display = 'none';
});

signinBtn.addEventListener('click', () => {
    signinForm.style.display = 'block';
    signinIntro.style.display = 'block';
    signupForm.style.display = 'none';
    signupIntro.style.display = 'none';
});

signinForm.style.display = 'block';
signinIntro.style.display = 'block';
signupForm.style.display = 'none';
signupIntro.style.display = 'none';

const signupBtn = document.getElementById("signup-btn");
const signinBtn = document.getElementById("signin-btn");
const mainContainer = document.querySelector(".container");
const signInForm = document.querySelector("#signin-form");
const signUpForm = document.querySelector("#signup-form");

signupBtn.addEventListener("click", () => {
  mainContainer.classList.toggle("change");
});
signinBtn.addEventListener("click", () => {
  mainContainer.classList.toggle("change");
});

signInForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.querySelector("#sign-in-email").value;
  const password = document.querySelector("#sign-in-password").value;

  try {
    const response = await fetch('/api/v1/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    })
    .then(res => res.json())
    .then(data => {
      window.localStorage.setItem("token", data.token);
    });
  }
  catch (error) {
    console.error('Error:', error);
  }
})

signUpForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const fname = document.querySelector("#sign-up-fname").value;
  const lname = document.querySelector("#sign-up-lname").value;
  const email = document.querySelector("#sign-up-email").value;
  const password = document.querySelector("#sign-up-password").value;

  try {
    const response = await fetch('/api/v1/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ fname, lname, email, password }),
    })
    .then(res => res.json())
    .then(data => {
      window.localStorage.setItem("token", data.token);
    });
  }
  catch (error) {
    console.error('Error:', error);
  }
})
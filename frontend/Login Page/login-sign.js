document.addEventListener("DOMContentLoaded", () => {
  const signupBtn = document.getElementById("signup-btn");
  const signinBtn = document.getElementById("signin-btn");
  const mainContainer = document.querySelector(".container");
  const togglePasswordBtns = document.querySelectorAll(".toggle-password");
  const inputs = document.querySelectorAll(".input-field input");

  // Add placeholder attribute to all inputs to work with the floating label
  inputs.forEach(input => {
    input.setAttribute("placeholder", " ");
  });

  // Toggle password visibility
  togglePasswordBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const input = btn.previousElementSibling;
      if (input.type === "password") {
        input.type = "text";
        btn.classList.remove("fa-eye");
        btn.classList.add("fa-eye-slash");
      } else {
        input.type = "password";
        btn.classList.remove("fa-eye-slash");
        btn.classList.add("fa-eye");
      }
    });
  });

  // Switch between login and signup forms
  if (signupBtn && signinBtn && mainContainer) {
    signupBtn.addEventListener("click", () => {
      mainContainer.classList.toggle("change");
    });

    signinBtn.addEventListener("click", () => {
      mainContainer.classList.toggle("change");
    });
  }

  // Login form submission
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('sign-in-email').value.trim();
      const password = document.getElementById('sign-in-password').value.trim();

      const formData = new URLSearchParams();
      formData.append("email", email);
      formData.append("password", password);

      try {
        const response = await fetch("http://0.0.0.0:8000/api/v1/auth/login", {
          method: "POST",
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: formData
        });

        const data = await response.json();
        if (response.ok) {
          console.log("Login Successful", data);
          // You could redirect user or show success message
        } else {
          console.error("Login Failed:", data);
          alert("Error: " + (data.detail || response.statusText));
        }
      } catch (error) {
        console.error("Fetch failed:", error);
        alert("An unexpected error occurred.");
      }
    });
  }

  // Signup form submission
  const signupForm = document.getElementById('signup-form');
  if (signupForm) {
    signupForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const fname = document.getElementById('sign-up-fname').value;
      const lname = document.getElementById('sign-up-lname').value;
      const email = document.getElementById('sign-up-email').value;
      const password = document.getElementById('sign-up-password').value;

      try {
        const response = await fetch("http://0.0.0.0:8000/api/v1/auth/signup", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            fname: fname,
            lname: lname,
            email: email,
            password: password,
          }),
        });

        if (response.ok) {
          const user = await response.json();
          console.log("Signup successful:", user);
          alert("Signup successful!");
          // You could redirect the user or automatically log them in
        } else {
          const error = await response.json();
          console.error("Error response:", error);
          alert("Signup failed: " + (error.detail || response.statusText));
        }
      } catch (error) {
        console.error("Fetch failed:", error);
        alert("An unexpected error occurred.");
      }
    });
  }
});
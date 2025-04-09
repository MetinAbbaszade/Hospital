document.addEventListener("DOMContentLoaded", () => {
  const signupBtn = document.getElementById("signup-btn");
  const signinBtn = document.getElementById("signin-btn");
  const mainContainer = document.querySelector(".container");
  const togglePasswordBtns = document.querySelectorAll(".toggle-password");
  const inputs = document.querySelectorAll(".input-field input");

  inputs.forEach(input => {
    input.setAttribute("placeholder", " ");
  });

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

  if (signupBtn && signinBtn && mainContainer) {
    signupBtn.addEventListener("click", () => {
      mainContainer.classList.toggle("change");
    });

    signinBtn.addEventListener("click", () => {
      mainContainer.classList.toggle("change");
    });
  }

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
          // Store both tokens
          localStorage.setItem("access_token", data.access_token);
          localStorage.setItem("refresh_token", data.refresh_token);
          redirectToPage();
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
          const data = await response.json();
          alert("Signup successful!");
          // Store both tokens
          localStorage.setItem("access_token", data.access_token);
          localStorage.setItem("refresh_token", data.refresh_token);
          redirectToPage();
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

// Add token refresh functionality
async function refreshToken() {
  const refreshToken = localStorage.getItem("refresh_token");
  if (!refreshToken) {
    console.error("No refresh token found");
    return false;
  }

  try {
    const response = await fetch("http://0.0.0.0:8000/api/v1/auth/refresh", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        refresh_token: refreshToken
      }),
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem("access_token", data.access_token);
      localStorage.setItem("refresh_token", data.refresh_token);
      return true;
    } else {
      console.error("Token refresh failed", await response.json());
      return false;
    }
  } catch (error) {
    console.error("Token refresh error:", error);
    return false;
  }
}

function redirectToPage() {
  const redirectionToPage = {
    'patient': 'http://127.0.0.1:5506/frontend/Admin%20UI/User%20UI/user_ui.html',
    'doctor': 'http://127.0.0.1:5506/frontend/Doctor%20Panel/doctor.html',
    'admin': 'http://127.0.0.1:5506/frontend/Admin%20UI/Hospital%20Page/hospitals.html',
    'owner': 'http://127.0.0.1:5506/frontend/Hospital%20Management/hospital.html'
  };
  const token = localStorage.getItem("access_token");
  if (!token) {
    console.error("No access token found in localStorage.");
    return;
  }

  try {
    const payloadBase64 = token.split('.')[1];
    const decodedPayload = JSON.parse(atob(payloadBase64));

    const role = decodedPayload['role'];

    if (role && redirectionToPage[role]) {
      window.location.href = redirectionToPage[role];
    } else {
      console.warn("Role not found or not recognized:", role);
      alert("Unauthorized role or destination.");
    }
  } catch (error) {
    console.error("Failed to decode token:", error);
  }
}

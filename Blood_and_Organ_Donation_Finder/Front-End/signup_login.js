let role="user";

function setRole(selected) {
  role = selected;

  document.querySelectorAll(".role-btn").forEach(btn =>
    btn.classList.remove("active")
  );
  event.target.classList.add("active");

  // Toggle signup sections
  document.getElementById("userSignup")
    .classList.toggle("hidden", role === "hospital");

  document.getElementById("hospitalSignup")
    .classList.toggle("hidden", role !== "hospital");
}

function showLogin(){
  document.getElementById("loginForm").classList.remove("hidden");
  document.getElementById("signupForm").classList.add("hidden");
  document.querySelectorAll(".nav-link")[0].classList.add("active");
  document.querySelectorAll(".nav-link")[1].classList.remove("active");
}

function showSignup(){
  document.getElementById("signupForm").classList.remove("hidden");
  document.getElementById("loginForm").classList.add("hidden");
  document.querySelectorAll(".nav-link")[1].classList.add("active");
  document.querySelectorAll(".nav-link")[0].classList.remove("active");
}

function login(e){
  e.preventDefault();
  localStorage.setItem("isLoggedIn","true");
  localStorage.setItem("role",role);
  alert(role+" logged in successfully");
  window.location.href="index.html";
}

function signup(e){
  e.preventDefault();
  alert("Signup successful! Please login.");
  showLogin();
}
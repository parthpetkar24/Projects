let requestType = "blood";

function selectType(type, btn) {
  emergency_request_type = type;
  document.getElementById("emergency_request_type").value = type;

  document.getElementById("bloodSection")
    .classList.toggle("hidden", type !== "blood");

  document.getElementById("organSection")
    .classList.toggle("hidden", type !== "organ");

  document.querySelectorAll(".tab-btn")
    .forEach(b => b.classList.remove("active"));

  btn.classList.add("active");
}

function calculateAge() {
  const dob = document.getElementById("dob").value;
  if (!dob) return;

  const birth = new Date(dob);
  const today = new Date();
  let age = today.getFullYear() - birth.getFullYear();

  if (
    today.getMonth() < birth.getMonth() ||
    (today.getMonth() === birth.getMonth() &&
     today.getDate() < birth.getDate())
  ) age--;

  document.getElementById("age").value = age;
}

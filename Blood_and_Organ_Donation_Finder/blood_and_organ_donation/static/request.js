let requestType = "blood";

function selectType(type, btn) {
  requestType = type;
  document.getElementById("requestType").value = type;

  // Toggle sections
  document.getElementById("bloodSection")
    .classList.toggle("hidden", type !== "blood");

  document.getElementById("organSection")
    .classList.toggle("hidden", type !== "organ");

  // Required fields
  document.querySelector('[name="blood_group"]').required = (type === "blood");
  document.querySelector('[name="organ"]').required = (type === "organ");

  // Active tab styling
  document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
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

function nextStep(step) {
  /* Hide only actual steps */
  for (let i = 1; i <= 4; i++) {
    document.getElementById(`step${i}`).classList.add("hidden");
  }

  document.getElementById(`step${step}`).classList.remove("hidden");
  const weight = document.querySelector('[name="weight"]');
  if (step === 3) {
    weight.required = true;     // visible step
  } else {
    weight.required = false;    // hidden step
  }
  /* Reset indicators safely */
  for (let i = 1; i <= 4; i++) {
    document.getElementById(`s${i}`).classList.remove("active");
  }

  document.getElementById(`s${step}`).classList.add("active");
}

let donationType = "blood";

function selectType(type, btn) {
  donationType = type;
  document.getElementById("donationType").value = type;

  document.getElementById("bloodSection")
    .classList.toggle("hidden", type !== "blood");

  document.getElementById("organSection")
    .classList.toggle("hidden", type !== "organ");

  document.querySelectorAll(".tab-btn").forEach(b => {
    b.classList.remove("active")
  });
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

function enableSubmit(step) {
  const btn = document.getElementById(`step${step}SubmitBtn`);
  if (btn) btn.disabled = false;
}

function nextStep(step) {
  // hide all steps
  document.querySelectorAll('[id^="step"]').forEach(div => {
    div.classList.add("hidden");
  });

  // show current step
  document.getElementById("step" + step).classList.remove("hidden");

  // reset all indicators
  document.querySelectorAll('[id^="s"]').forEach(span => {
    span.classList.remove("active");
  });

  // activate current indicator
  document.getElementById("s" + step).classList.add("active");
}

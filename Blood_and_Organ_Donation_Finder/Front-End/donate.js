let donationType="";

function selectType(type){
  donationType=type;
  document.getElementById("bloodField").classList.toggle("hidden",type!=="blood");
  document.getElementById("organField").classList.toggle("hidden",type!=="organ");
}

function nextStep(step){
  ["step1","step2","step3"].forEach(s=>document.getElementById(s).classList.add("hidden"));
  document.getElementById("step"+step).classList.remove("hidden");
  ["s1","s2","s3"].forEach(s=>document.getElementById(s).classList.remove("active"));
  document.getElementById("s"+step).classList.add("active");
}

function submitForm(){
  alert("Thank you for becoming a donor ❤️");
  window.location.href="index.html";
}
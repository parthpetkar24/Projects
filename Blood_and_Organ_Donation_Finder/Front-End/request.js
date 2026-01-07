let requestType="";

function selectType(type){
  requestType=type;
  document.getElementById("bloodField").classList.toggle("hidden",type!=="blood");
  document.getElementById("organField").classList.toggle("hidden",type!=="organ");
}

function nextStep(step){
  ["step1","step2","step3"].forEach(s=>document.getElementById(s).classList.add("hidden"));
  document.getElementById("step"+step).classList.remove("hidden");

  ["r1","r2","r3"].forEach(s=>document.getElementById(s).classList.remove("active"));
  document.getElementById("r"+step).classList.add("active");
}
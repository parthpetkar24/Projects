function increaseUnit(type) {
  const display = document.getElementById(type + "_display");
  const store = document.getElementById(type + "_store");

  let value = parseInt(display.textContent) || 0;
  value++;

  display.textContent = value;
  store.value = value;
}

function decreaseUnit(type) {
  const display = document.getElementById(type + "_display");
  const store = document.getElementById(type + "_store");

  let value = parseInt(display.textContent) || 0;

  if (value > 0) value--;

  display.textContent = value;
  store.value = value;
}

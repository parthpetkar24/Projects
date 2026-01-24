function increaseUnit(id) {
  const cell = document.getElementById(id);
  const store = document.getElementById(id + "_store");
  let value = parseInt(cell.textContent);
  value=value+1;
  cell.textContent = value;
  store.value = value;
}

function decreaseUnit(id) {
  const cell = document.getElementById(id);
  let value = parseInt(cell.textContent);

  if (value > 0) {
    cell.textContent = value - 1;
  }
}

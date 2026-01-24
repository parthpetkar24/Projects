function increaseUnit(id) {
  const cell = document.getElementById(id);
  let value = parseInt(cell.textContent);
  cell.textContent = value + 1;
}

function decreaseUnit(id) {
  const cell = document.getElementById(id);
  let value = parseInt(cell.textContent);

  if (value > 0) {
    cell.textContent = value - 1;
  }
}

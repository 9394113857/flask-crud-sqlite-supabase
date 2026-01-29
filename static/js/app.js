function editRow(btn) {
  const row = btn.closest("tr");
  row.querySelectorAll("input, select").forEach(el => el.disabled = false);

  btn.classList.add("d-none");
  row.querySelector(".btn-success").classList.remove("d-none");
}

function saveRow(btn) {
  if (!confirm("Do you want to update all values for this user?")) {
    return;
  }

  const row = btn.closest("tr");
  const id = row.dataset.id;

  const inputs = row.querySelectorAll("input, select");

  const data = {
    full_name: inputs[0].value,
    email: inputs[1].value,
    phone: inputs[2].value,
    age: inputs[3].value || null,
    gender: inputs[4].value
  };

  fetch(`/users/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(() => {
    inputs.forEach(el => el.disabled = true);
    btn.classList.add("d-none");
    row.querySelector(".btn-warning").classList.remove("d-none");
  });
}

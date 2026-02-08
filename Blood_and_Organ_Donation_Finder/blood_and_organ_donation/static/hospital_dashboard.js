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
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function approveWithAppointment(appType, formId) {
    const date = document.getElementById(`date-${formId}`).value;
    const time = document.getElementById(`time-${formId}`).value;

    if (!date || !time) {
        alert("Appointment date and time are required");
        return;
    }

    fetch("/approve_application/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": csrftoken
        },
        body: `app_type=${appType}&form_id=${formId}&date=${date}&time=${time}`
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            window.location.href = data.pdf_url;
        } else {
            alert(data.error);
        }
    });
}


// Handle rejection of application
function handleRejection(appType, formId) {
    if (!confirm(`Are you sure you want to reject application ${formId}?`)) {
        return;
    }

    fetch('/reject_application/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken
        },
        body: `app_type=${appType}&form_id=${formId}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(`Application ${formId} rejected`);
            const appCard = document.getElementById(`app-${appType}-${formId}`);
            if (appCard) appCard.remove();
            location.reload();
        } else {
            alert('Error: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while rejecting the application');
    });
}

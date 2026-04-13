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
function getCSRFToken() {
    const tokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
    if (tokenInput) return tokenInput.value;

    // Fallback to cookie
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, 'csrftoken'.length + 1) === 'csrftoken=') {
                cookieValue = decodeURIComponent(cookie.substring('csrftoken='.length));
                break;
            }
        }
    }
    return cookieValue;
}

function approveWithAppointment(appType, formId) {
    const date = document.getElementById(`date-${formId}`).value;
    const time = document.getElementById(`time-${formId}`).value;

    if (!date || !time) {
        alert("Appointment date and time are required");
        return;
    }

    const csrftoken = getCSRFToken();

    fetch("/hospital_dashboard/approve_application/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": csrftoken
        },
        body: `app_type=${appType}&form_id=${formId}&date=${date}&time=${time}`
    })
    .then(res => {
        if (!res.ok) {
            throw new Error(`Server responded with ${res.status}`);
        }
        return res.json();
    })
    .then(data => {
        if (data.success) {
            window.location.href = data.pdf_url;
        } else {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Approve error:', error);
        alert('An error occurred while approving the application');
    });
}


// Handle rejection of application
function handleRejection(appType, formId) {
    if (!confirm(`Are you sure you want to reject application ${formId}?`)) {
        return;
    }

    const csrftoken = getCSRFToken();

    fetch('/hospital_dashboard/reject_application/', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken
        },
        body: `app_type=${appType}&form_id=${formId}`
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server responded with ${response.status}`);
        }
        return response.json();
    })
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

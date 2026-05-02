setTimeout(() => {
  console.log("New donor attempting contact");
}, 3000);

function getCSRFToken() {
    const tokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
    if (tokenInput) return tokenInput.value;

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

function clearApplication(appType, formId, btn) {
    if (!confirm(`Are you sure you want to permanently delete application ${formId}? This action cannot be undone.`)) {
        return;
    }

    const csrftoken = getCSRFToken();

    fetch("/user_dashboard/clear-application/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": csrftoken
        },
        body: `app_type=${appType}&form_id=${formId}`
    })
    .then(res => {
        if (!res.ok) throw new Error(`Server responded with ${res.status}`);
        return res.json();
    })
    .then(data => {
        if (data.success) {
            // Remove the row from the table
            const row = btn.closest('tr');
            if (row) {
                row.style.transition = 'opacity 0.3s ease';
                row.style.opacity = '0';
                setTimeout(() => row.remove(), 300);
            }
        } else {
            alert('Error: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Clear error:', error);
        alert('An error occurred while deleting the application.');
    });
}

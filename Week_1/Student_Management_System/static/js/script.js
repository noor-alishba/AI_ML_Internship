// script.js
// ---------
// Small helper script for the Student Management System web pages.
// Right now it just auto-hides flash messages (success/error alerts)
// after a few seconds, so the page stays clean.

document.addEventListener("DOMContentLoaded", function () {
    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {
        setTimeout(function () {
            // Use Bootstrap's built-in way of closing an alert, if available
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 4000); // hide after 4 seconds
    });
});
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".alert[data-timeout]").forEach(function (alert) {
    const timeout = parseInt(alert.dataset.timeout, 10);

    setTimeout(function () {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert.close();
    }, timeout);
  });
});

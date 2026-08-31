document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menuToggle");
    const mainNav = document.getElementById("mainNav");
    if (menuToggle && mainNav) {
        menuToggle.addEventListener("click", function () {
            mainNav.classList.toggle("open");
        });
    }
    document.querySelectorAll(".main-nav a").forEach(function (link) {
        link.addEventListener("click", function () {
            if (mainNav) mainNav.classList.remove("open");
        });
    });
    document.querySelectorAll(".message").forEach(function (message) {
        setTimeout(function () {
            message.style.opacity = "0";
            setTimeout(function () { message.remove(); }, 400);
        }, 5000);
    });
});

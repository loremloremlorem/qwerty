document.addEventListener("DOMContentLoaded", () => {
    const logoutButton = document.getElementById("logout");
    const cartLink = document.getElementById("cart");
    const ordersLink = document.getElementById("orders");

    // Highlight active page
    const activePage = window.location.pathname;
    if (activePage.includes("cart")) {
        cartLink.style.backgroundColor = "var(--main-color)";
        cartLink.style.color = "#fff";
    } else if (activePage.includes("orders")) {
        ordersLink.style.backgroundColor = "var(--main-color)";
        ordersLink.style.color = "#fff";
    }

    // Logout functionality
    logoutButton.addEventListener("click", () => {
        sessionStorage.removeItem("csrfToken");
        window.location.href = "/";
    });
});
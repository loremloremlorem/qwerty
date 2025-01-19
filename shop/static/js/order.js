const openModalButton = document.getElementById("openModalButton");
const closeModalButton = document.getElementById("closeModalButton");
const modal = document.getElementById("modal");

// Открыть модальное окно
openModalButton.addEventListener("click", () => {
    modal.style.display = "flex";
});

// Закрыть модальное окно
closeModalButton.addEventListener("click", () => {
    modal.style.display = "none";
});

// Дополнительно: закрыть модальное окно при отправке формы
const orderForm = document.getElementById("orderForm");
orderForm.addEventListener("submit", (e) => {
    e.preventDefault();
    modal.style.display = "none";
    alert("Order placed successfully!");
});
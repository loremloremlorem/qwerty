document.addEventListener("DOMContentLoaded", () => {
    const price = document.getElementById("price").textContent; // Получаем текущую цену из элемента
    const formattedPrice = Number(price).toLocaleString('en-US'); // Форматируем число
    document.getElementById("price").textContent = formattedPrice; // Устанавливаем отформатированное значение
});
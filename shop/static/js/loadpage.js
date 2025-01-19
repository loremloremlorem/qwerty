// Отслеживаем изменения в hash (например, при переходе по якорным ссылкам)
window.addEventListener('hashchange', () => {
    window.scrollTo(0, 0); // Прокрутка в начало страницы
});

// Прокрутка в начало страницы при загрузке
window.addEventListener('load', () => {
    window.scrollTo(0, 0);
});
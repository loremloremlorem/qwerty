// Получаем элементы
const playButton = document.getElementById('playButton');
const videoModal = document.getElementById('videoModal');
const closeButton = document.getElementById('closeButton'); // Изменено на новый id
const videoElement = document.getElementById('videoElement');

// Открытие модального окна
playButton.addEventListener('click', () => {
    videoModal.classList.add('active'); // Добавляем класс active
    videoElement.play(); // Начинаем воспроизведение видео
});

// Закрытие модального окна
closeButton.addEventListener('click', () => {
    videoModal.classList.remove('active'); // Удаляем класс active
    videoElement.pause(); // Останавливаем видео
    videoElement.currentTime = 0; // Перематываем на начало
});

// Закрытие модального окна при клике вне контента
videoModal.addEventListener('click', (e) => {
    if (e.target === videoModal) {
        videoModal.classList.remove('active');
        videoElement.pause();
        videoElement.currentTime = 0;
    }
});

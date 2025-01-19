const openModal = document.getElementById('openModal');
const closeModal = document.getElementById('closeModal');
const modal = document.getElementById('modal');
const loginForm = document.getElementById('loginForm');
const error = document.getElementById('error');

openModal.addEventListener('click', () => {
    modal.style.display = 'flex';
    error.textContent = '';
});

closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
});

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;

    if (!login || !password) {
        error.textContent = 'Please fill all inputs!';
    } else {
        error.textContent = 'Login successful!';
        modal.style.display = 'none';
    }
});
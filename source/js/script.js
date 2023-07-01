// Get the modal elements
var registerModal = document.getElementById('registerModal');
var loginModal = document.getElementById('loginModal');

// Get the button elements that open the modals
var openRegisterModalBtn = document.getElementById('openRegisterModal');
var openLoginModalBtn = document.getElementById('openLoginModal');

// Get the close button elements within the modals
var closeButtons = document.getElementsByClassName('close');

// Function to open the register modal
function openRegisterModal() {
  registerModal.style.display = 'block';
}

// Function to open the login modal
function openLoginModal() {
  loginModal.style.display = 'block';
}

// Function to close the modals
function closeModal() {
  registerModal.style.display = 'none';
  loginModal.style.display = 'none';
}

// Function to switch to the login modal from the register modal
function goToLoginModal() {
  registerModal.style.display = 'none';
  loginModal.style.display = 'block';
}

// Function to switch to the register modal from the login modal
function goToRegisterModal() {
  loginModal.style.display = 'none';
  registerModal.style.display = 'block';
}

// Add event listeners to open the modals
openRegisterModalBtn.addEventListener('click', openRegisterModal);
openLoginModalBtn.addEventListener('click', openLoginModal);

// Add event listeners to close the modals
for (var i = 0; i < closeButtons.length; i++) {
  closeButtons[i].addEventListener('click', closeModal);
}

// Add event listeners to switch between modals
document.getElementById('goToLogin').addEventListener('click', goToLoginModal);
document.getElementById('goToRegister').addEventListener('click', goToRegisterModal);

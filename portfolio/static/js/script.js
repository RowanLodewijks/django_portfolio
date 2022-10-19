// Toggle Menu
window.addEventListener("load",function(){
  var button = document.querySelector('.menu_toggle');
  var menu = document.querySelector('.menu');

  button.addEventListener('click', function(){
    menu.classList.toggle('hidden');
  });
});

// Stops Scrolling When In Menu
function lockScroll() {
  document.body.classList.toggle('lock-scroll');
}

// Open Modal
const btnOpenModal = document.querySelector(".for-modal");
const btnOpenDialog = document.querySelector(".for-dialog");
const btnClose = document.querySelectorAll(".close-modal");
const dialog = document.querySelector("example-dialog");

btnOpenModal.addEventListener("click", () => {
  btnOpenModal.nextElementSibling.showModal();
});

btnClose.forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.parentElement.close();
  });
});
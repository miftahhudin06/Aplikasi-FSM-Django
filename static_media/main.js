function showMenu() {
  let toggle = document.querySelector(".toggle");
  let main = document.querySelector(".main");
  let navigation = document.querySelector(".nav");
  toggle.classList.toggle("active");
  main.classList.toggle("active");
  navigation.classList.toggle("active");
}

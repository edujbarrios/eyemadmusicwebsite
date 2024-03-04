// JavaScript code from the original <script> tags
document.getElementById('menuToggle').addEventListener('click', function() {
    const menu = document.getElementById('menu');
    if (menu.classList.contains('hidden')) {
      menu.classList.remove('hidden');
      menu.classList.add('show');
    } else {
      menu.classList.remove('show');
      menu.classList.add('hidden');
    }
  });
  const mobileMenuButton = document.getElementById("mobile-menu");
  const navList = document.querySelector("nav ul");
  
  mobileMenuButton.addEventListener("click", () => {
    navList.classList.toggle("active");
  });
  
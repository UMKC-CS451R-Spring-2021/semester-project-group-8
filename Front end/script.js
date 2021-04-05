const burger = document.querySelector(".burger-menu");
      const navMenu = document.querySelector(".navlinks");
      const shop = document.querySelector(".shop");
      const accordian = document.querySelector(".accordian");
      const arrow = document.querySelector(".arrow");

      burger.addEventListener("click", () => {
        burger.classList.toggle("toggle");
        navMenu.classList.toggle("show");
      });

      shop.addEventListener("click", () => {
        accordian.classList.toggle("show");
        arrow.classList.toggle("down");
      });
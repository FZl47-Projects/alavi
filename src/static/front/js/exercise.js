
//-------دکمه و محتوای آن---------------//
let btns = document.querySelectorAll(".btn-item")
let content_table = document.querySelectorAll(".tables-content")
btns.forEach((item, index) => {
    item.addEventListener("click", () => {
        btns.forEach((item) => {
        item.classList.remove("active");
      });
      content_table.forEach((item) => {
        item.classList.remove("active");
      });
      btns[index].classList.add("active");
      content_table[index].classList.add("active");
    });
  });
//-------دکمه و محتوای آن---------------//
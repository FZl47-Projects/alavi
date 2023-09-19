

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
// --------نمایش پاپ آپ افزودن موادغذایی----------//

let btnsShowModal = document.querySelectorAll(".btn-material-add");
let modals = document.querySelector(".moda-add-material");
let overalyModals = document.querySelector(".moda-add-material .inner-modal");
btnsShowModal.forEach((item , index) => {
    item.addEventListener("click", () => {
        modals.classList.add("active");
      });
})

    overalyModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal"){
      modals.classList.remove("active");
    }
  });
  // --------نمایش پاپ آپ افزودن موادغذایی----------//
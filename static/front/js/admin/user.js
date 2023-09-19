/*------------------show and close modal comment user ------------------- */
let btnsShowModal = document.querySelectorAll(".add-btn");
let modals = document.querySelector("#add-modal");
let overalyModals = document.querySelector("#add-modal .inner-modal");
// let closemodal = document.querySelectorAll("#close");

btnsShowModal.forEach((item,index)=>{
  item.addEventListener("click", () => {
   
    modals.classList.add("active");
  });
});

    overalyModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal"){
      modals.classList.remove("active");
    }
  });

// closemodal.forEach((item,index)=>{
//     item.addEventListener("click", () => {
     
//       modals[index].classList.remove("active");
//     });
//   });
/*------------------show and close modal comment user ------------------- */


/*------------------show and close modal comment user ------------------- */
let btnsShowModal = document.querySelectorAll(".add-btn");
let modals = document.querySelectorAll(".add-modal");
let overalyModals = document.querySelectorAll(".add-modal .inner-modal");
// let closemodal = document.querySelectorAll("#close");

for (let el of btnsShowModal) {

    el.addEventListener("click", () => {
        let modal_id = el.getAttribute('modal-id')
        document.querySelector(`#add-modal-${modal_id}`).classList.add("active");
    });

}


for (let el of overalyModals) {
    el.addEventListener("click", (e) => {
        if (e.target.className === "inner-modal") {
            hideAllModal()
        }
    });
}

function hideAllModal() {
    for (let el of modals) {
        el.classList.remove('d-none')
    }
}

// closemodal.forEach((item,index)=>{
//     item.addEventListener("click", () => {

//       modals[index].classList.remove("active");
//     });
//   });
/*------------------show and close modal comment user ------------------- */


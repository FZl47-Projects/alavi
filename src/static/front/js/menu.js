
// Open/Close Sidebar menu
function openCloseSidebar() {
    const sidebar = document.querySelector('.menu-fixed-right');
    const sidebarBtn = document.querySelector('.sidebar-btn');

    if(sidebar.style.right === '0px') {
        sidebar.style.right = '-240px';
        sidebarBtn.style.right = '0';
    } else {
        sidebar.style.right = '0';
        sidebarBtn.style.right = '230px';
    }
}

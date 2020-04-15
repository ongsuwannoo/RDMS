function click_side_bar(event) {
    var len = document.getElementById("hover_sidebar").getElementsByClassName("box-side-sub");
    for (let i = 0; i < len.length; i++) {
        len[i].classList.remove("is-active-sidebar");
        if (event.target.className.includes("box-side-sub")) {
            event.target.classList.add("is-active-sidebar");
        }
    }
}

function out_hover_side_bar(event) {
    // if (event.target.className.includes("box-side-sub")) {
    //     event.target.style.backgroundColor = '#090A0E';
    // }
}

function hide_sidebar(event) {
    document.getElementById("side_bar").style.marginLeft = "-19%";
    // document.getElementById("side_bar").style.display = "none";
    document.getElementById("hamburger").style.display = "block";
}

function show_sidebar(event) {
    document.getElementById("side_bar").style.marginLeft = "0";
    document.getElementById("hamburger").style.display = "none";
}

window.onload = function() {
    document.getElementById("hover_sidebar").addEventListener("click", click_side_bar);
    document.getElementById("hide_sidebar_btn").addEventListener("click", hide_sidebar);
    document.getElementById("hamburger").addEventListener("click", show_sidebar);
}
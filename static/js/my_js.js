var pages = {
    '/camp/': 'overview'
}

function click_side_bar(event) {
    var page = event.target.getAttribute("href");
    if (page != null){
        window.location = page;
    }
    console.log(pages[window.location.pathname])
    
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
    document.getElementById("side_bar").style.marginLeft = "-20%";
    setTimeout(() => { document.getElementById("side_bar").style.display = "none" }, 500);
    // document.getElementById("hamburger2").style.display = "none";
    document.getElementById("hamburger1").style.display = "block";
    document.getElementById("hamburger1").style.zIndex = "1";
    document.getElementById("hamburger1").style.position = "inherit";
}

function show_sidebar(event) {
    document.getElementById("side_bar").style.display = "block";
    document.getElementById("side_bar").style.marginLeft = "0";
    document.getElementById("hamburger1").style.display = "none";
    // document.getElementById("hamburger2").style.display = "block";
}

window.onload = function () {
    document.getElementById("hover_sidebar").addEventListener("click", click_side_bar);
    document.getElementById("hide_sidebar_btn").addEventListener("click", hide_sidebar);
    document.getElementById("hamburger1").addEventListener("click", show_sidebar);
    // const fileInput = document.querySelector('#file-js-example input[type=file]');
    // fileInput.onchange = () => {
    //     if (fileInput.files.length > 0) {
    //         const fileName = document.querySelector('#file-js-example .file-name');
    //         fileName.textContent = fileInput.files[0].name;
    //     }
    // }
}


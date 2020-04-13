function hover_side_bar(event) {
    if (event.target.className.includes("box-side-sub")) {
        event.target.style.backgroundColor = '#924BE7';
    }
}

function out_hover_side_bar(event) {
    if (event.target.className.includes("box-side-sub")) {
        event.target.style.backgroundColor = '#090A0E';
    }
}

window.onload = function() {
    document.getElementById("hover_sidebar").addEventListener("mouseover", hover_side_bar);
    document.getElementById("hover_sidebar").addEventListener("mouseout", out_hover_side_bar);
}

var pages = {
    '/campers/': 'campers',
    '/flow/': 'flow',
    '/locations/': 'locations',
    '/staffs/': 'staffs',
    '/camp/': 'camp',
    'camp': 'overview'
}
$(function () {
    $('.material-tooltip-main').tooltip({
        template: '<div class="tooltip md-tooltip-main"><div class="tooltip-arrow md-arrow"></div><div class="tooltip-inner md-inner-main"></div></div>'
    });

})

function hamburger(x) {
    if (x.matches) {
        document.getElementById('menu-toggle2').style.display = 'block';
        $("#main-content").addClass("toggled");
    }
    else {
        document.getElementById('menu-toggle2').style.display = 'none';
        $("#main-content").removeClass("toggled");
    }
        
}

window.onload = function () {
    for (let key in pages) {
        if (window.location.pathname.includes(key)){
            if (isNaN(parseInt(window.location.pathname.split("/")[2])) && key != '/locations/')
                document.getElementById("overview").classList.add("active");
            else
                document.getElementById(pages[key]).classList.add("active");
            break;
        }
    }

    var x = window.matchMedia("(max-width: 768px)")
    hamburger(x)
    x.addListener(hamburger)
}



var pages = {
    '/camp/': 'overview',
    '/camp/campers/': 'campers',
    '/camp/flow/': 'flow',
    '/locations/': 'locations',
    '/camp/staffs/': 'staffs'
}

window.onload = function () {
    document.getElementById(pages[window.location.pathname]).classList.add("active")
}


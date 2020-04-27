
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
        if (window.location.pathname.includes(key)) {
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
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHerderName = 'X-CSRFTOKEN'
}



function getDepartment(id) {
    axios.get('/api/getDepartment/' + id)
        .then(function (response) {
            // handle success
            data = response.data
            console.log(data);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
            document.getElementById('name_modal_department').innerHTML = 'ฝ่าย' + data.name;
            document.getElementById('desc_modal_department').innerHTML = data.desc;
            // document.getElementById('head_modal_department')
        });
}

function getStaffsDetail(id_staff) {
    axios.get('/api/getStaffsDetail/' + id_staff)
        .then(function (response) {
            // handle success
            data = response.data
            console.log(data);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
            var lis = ['staff_name', 'staff_nickname', 'staff_sex', 'staff_sid', 'staff_religion', 'staff_disease', 'staff_foodallergy',
                'staff_sirstsize', 'staff_birthday', 'staff_department', 'staff_position', 'staff_MC', 'staff_phone', 'staff_email'];
            for (let key in data) { // ข้อมูลที่เหลือ (camp, personal, **position, group**, depart)
                console.log(key, data[key]);
                try {
                    if (key == 'personal') {
                        for (let key in data.personal) { // ข้อมูลเฉพาะใน personal ส่วนใหญ่
                            try {
                                if (key == 'profile_pic' && data.personal[key] == '') {
                                    data.personal[key] = 'profile.png'
                                }
                                document.getElementById('staff_' + key).innerHTML = data.personal[key];
                            } catch (err) { }
                        }
                    }
                    if (key == 'department')
                        document.getElementById('staff_' + key).innerHTML = data.department['name'];
                    else
                        document.getElementById('staff_' + key).innerHTML = '-';
                } catch (err) { }
            }
            document.getElementById('modal_pic').src = '/media/' + data.personal.profile_pic;
        });
}

function getFlow(id_camp) {
    axios.get('/api/flow_api/' + id_camp)
        .then(function (response) {
            // handle success
            data = response.data
            console.log(data);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed

        });
}

function addFlow() {
    axios
    .post('/api/addFlow/', {
      email : "test@gmail.com",
      username : 'test'
    })
    .then(response => (this.info = response.data))


    // axios.post('/api/addFlow/', {
    //     text: 'test'

    // })
    //     .then(function (response) {
    //         console.log(response);
    //     })
    //     .catch(function (error) {
    //         console.log(error);
    //     });
}
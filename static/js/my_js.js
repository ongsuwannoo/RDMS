
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
}

function getDepartment(id) {
    axios.get('/api/getDepartment/', {
        params: {
            text: 'test',
            id_department: id
        }
    })
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

function getLocation(id) {
    axios.get('/api/getLocation/', {
        params: {
            id_location: id
        }
    })
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
        document.getElementById('name').value = data.name
        document.getElementById('desc').value = data.desc
        document.getElementById('img_profile').src = '/media/'+data.logo
        document.getElementById('id').value = data.id
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
    console.log('getFlow')
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
            for (let i = 0; i < data.length; i++) {
                data[i].department = data[i].department || { 'name': 'ทุกคน' }
                data[i].location = data[i].location || { 'name': 'ทั่วคณะ' }
                // data[i].department.name = 'ทุกฝ่าย'
                $('#tbl > tbody:last-child').append(
                    '<tr>' +
                    '<td class="text-center">' +
                    (data[i].time_start).slice(0, 5) + ' - ' +
                    (data[i].time_end).slice(0, 5) +
                    '</td>' +
                    '<td class="text-center">' + data[i].activity + '</td>' +
                    '<td class="text-center">' + (data[i].sub_time).slice(0, 5) + '</td>' +
                    '<td>' + data[i].desc + '</td>' +
                    '<td class="text-center">' + data[i].department.name + '</td>' +
                    '<td class="text-center">' + data[i].location.name + '</td>' +
                    '<td>' + data[i].note + '</td>' +
                    '<th scope="col">' +
                    '<span onclick="' + data[i].id + '" style="cursor:pointer;" class="m-1">' +
                    '<a class="material-tooltip-main" data-toggle="tooltip" data-placement="top" title="Edit">' +
                    '<i class="fas fa-edit fa-sm"></i>' +
                    '</a>' +
                    '</span>' +
                    '<span onclick="' + data[i].id + '" style="cursor:pointer;">' +
                    '<a class="material-tooltip-main" data-toggle="tooltip" data-placement="top" title="Delete">' +
                    '<i class="fas fa-times fa-sm"></i>' +
                    '</a>' +
                    '</span>' +
                    '</th>' +
                    '</tr>'
                );
            }
        });
}
function addFlow(id) {
    console.log('addFlow');
    var time_start, time_end, activity, sub_time, desc, camp, department, mc, location, note;
    // Send AJAX resuest to create in the DB
    console.log('/api/flow_api/' + id)
    axios.post('/api/flow_api/' + id, {
        time_start: document.getElementById('time_start').value,
        time_end: document.getElementById('time_end').value,
        activity: document.getElementById('activity').value,
        sub_time: document.getElementById('sub_time').value,
        desc: document.getElementById('desc').value,
        camp: document.getElementById('camp').value,
        department: document.getElementById('department').value,
        mc: '',
        location: document.getElementById('location').value,
        note: document.getElementById('note').value
    })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}
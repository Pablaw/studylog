console.log('연결 확인');

function getContributions() {
    $('#cards-box').empty()
        $.ajax({
            type: 'GET',
            url: '/githublog',
            data: {},
            success: function (response) {
                const date = Object.values(response)[0][0]
                const work = Object.values(response)[0][1]
                console.log(date, work);

            $('#today').append(date);
            $('#work_today').append(work);
            }
        })
}

$(document).ready(function () {
            getContributions();
        });
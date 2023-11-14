window.addEventListener('resize', function () {
    let width = window.innerWidth

    if (width < 1250) {
        $('header>div').css('padding', '0 10px');
        $('body>div').css('padding', '0 10px');
    } else {
        $('body>div').css('padding', '');
        $('header>div').css('padding', '');
    }
})

$(document).ready(function() {
    $('#active_user_dropdown').click(function(){
        console.log("a")
        $('.account_dropdown').slideToggle();
    })
});
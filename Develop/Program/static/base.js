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
    cart = Cookies.get('cart')
    if (!(typeof cart === 'undefined')){
        cart = JSON.parse(cart)
        console.log(cart)

        if (!(Object.keys(cart).length === 0)) {
            $('.icon_and_word>badge').text(sumObjectValues(cart))
            $('.icon_and_word>badge').show()
        }
    }

    $('#active_user_dropdown').click(function(){
        $('.account_dropdown').slideToggle();
    })

    $('.have-urls').click(function(){
        window.location.href = $(this).attr('href')
    })
});

function getValueOrDefault(obj, key, defaultValue) {
    if (obj.hasOwnProperty(key)) {
        return obj[key];
    } else {
        return defaultValue;
    }
}

function sumObjectValues(obj) {
    return Object.values(obj).reduce((total, value) => total + value, 0);
  }
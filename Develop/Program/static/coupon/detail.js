$(document).ready(function() {
    $('#image_list > :first-child').addClass('-selected');

    $('#image_list>div').on('click', function() {
        if ($(this).hasClass('-selected')){
            return
        }

        // get new image src
        var imgSrc = $(this).find('img').attr('src');

        // remove default -selected, and change
        $('.-selected').removeClass('-selected')
        $(this).addClass('-selected')

        // change to new image
        $('#iamge_preview>img').attr('src', imgSrc)
    });

    $("#buttons>button:nth-child(2)").click(function() {
        addCookie(this.value, $('#quantity').val())
        window.location.href = $(this).attr('href')
    });

    $("#buttons>button:nth-child(3)").click(function() {
        addCookie(this.value, $('#quantity').val())
        alert('The product has been added to your cart.')
        location.reload();
    });
});

function addCookie(product_id, quantity) {
    cart = Cookies.get('cart')
    if (typeof cart === 'undefined'){
        tmp = {}
    } else {
        tmp = JSON.parse(cart)
    }

    current_quantity = getValueOrDefault(tmp, product_id, 0)
    tmp[product_id] = Number(current_quantity) + Number(quantity)
    
    Cookies.set('cart', JSON.stringify(tmp), { expires: 7, path: '/' })
}

function getValueOrDefault(obj, key, defaultValue) {
    if (obj.hasOwnProperty(key)) {
        return obj[key];
    } else {
        return defaultValue;
    }
}
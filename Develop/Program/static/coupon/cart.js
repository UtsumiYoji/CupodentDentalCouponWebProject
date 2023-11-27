$(document).ready(function() {
    $(".coupon_info>div:nth-child(2)>span").click(function() {
        removeProduct($(this).attr('product_id'))
        location.reload();
    });

    $(".quantity>").change(function() {
        changeQuantity($(this).attr('product_id'), $(this).val())        
        location.reload();
    });
});

function removeProduct(product_id){
    cart = Cookies.get('cart')
    tmp = JSON.parse(cart)
    delete tmp[product_id]

    Cookies.set('cart', JSON.stringify(tmp), { expires: 7, path: '/' })
}

function changeQuantity(product_id, quantity){
    cart = Cookies.get('cart')
    tmp = JSON.parse(cart)

    tmp[product_id] = Number(quantity)
    Cookies.set('cart', JSON.stringify(tmp), { expires: 7, path: '/' })
}

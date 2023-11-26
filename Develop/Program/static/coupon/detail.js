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
});
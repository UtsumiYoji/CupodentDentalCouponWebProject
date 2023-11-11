window.addEventListener('resize', function () {
    let width = window.innerWidth

    if (width < 1250) {
        $('header>div').css('padding', '0 10px');
    } else {
        $('header>div').css('padding', '');
    }
  })
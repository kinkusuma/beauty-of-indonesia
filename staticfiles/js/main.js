AOS.init();

$(window).scroll(function() {
    if ($(window).scrollTop() >= 500) {
        $('.navbarhome').css('background', '#004F2D');
        $('.navbar-brand').css('font-size', '2em');
    } else {
        $('.navbarhome').css('background', 'rgba(0, 0, 0, 0)');
        $('.navbar-brand').css('font-size', '2.5em');
    }
});
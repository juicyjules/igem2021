const spypad = 400
$(document).ready(function () {
    // Bootstrap animated dropdown
    $("#scrollspy").css("top", Math.max(0, spypad));
    $('.navbar .dmenu').hover(function () {
            $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
        }, function () {
            $(this).find('.sm-menu').first().stop(true, true).slideUp(105)
        });

    // Keep Scrollspy fixed
    $(window).scroll(function(){
        $("#scrollspy").css("top", Math.max(0, spypad - $(this).scrollTop()));
    });

    $('[data-spy="scroll"]').on('activate.bs.scrollspy', function () {
        console.log("Mmhh Monke")
      })
});
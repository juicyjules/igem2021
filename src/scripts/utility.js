function vh(v) {
    var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
    return (v * h) / 100;
}
function vw(v) {
    var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    return (v * w) / 100;
}
const fadeScrollLimit = vh(100)
const half=vh(50)
$(document).ready(function () {
    const spypad = $("#header").outerHeight() + $("#navigation").outerHeight() + 30;
    const spypadH = half - ($("#scrollspy").outerHeight()/ 2);
    // Bootstrap animated dropdown
    $("#scrollspy").css("top", Math.max(spypadH, spypad));
    $('.navbar .dmenu').hover(function () {
            $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
        }, function () {
            $(this).find('.sm-menu').first().stop(true, true).slideUp(105)
        });
    $("#go-up").on("click" ,function(){
        window.scrollTo(0, 0)
    });
    // Keep Scrollspy fixed
    $(window).scroll(function(){
        $("#scrollspy").css("top", Math.max(spypadH, spypad - $(this).scrollTop()));
        if (window.scrollY > fadeScrollLimit){
            $("#go-up").css("opacity",1);
        } else {
            $("#go-up").css("opacity",0);
        }
    });

    $('[data-spy="scroll"]').on('activate.bs.scrollspy', function () {
        console.log("Mmhh Monke")
      })

    
});
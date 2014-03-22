
s3_url = "http://s3-ap-northeast-1.amazonaws.com/setsuhi-tokyo/";


// Making her name vertical, oh this is janky.
(function( $ ){
    $.fn.insertBreaks = function() {
        moji = $(this).text().trim().split('');
        $(this).html( moji.join("<br>") );
    }; 
})( jQuery );

$(".vertical-text").insertBreaks();


//=================================================================
// Source: http://css-tricks.com/snippets/jquery/smooth-scrolling/
$(function() {
    $('a.smooth-page-scroll[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });
});


//======================================
// galleria.io
if( Galleria && $(".galleria").length ){
    Galleria.loadTheme(s3_url + "static/galleria/themes/classic/galleria.classic.min.js");
    Galleria.configure({
        debug: !isProduction
    });
    Galleria.run('.galleria');

    // This should make any gallerias visible.
    $(".galleria.preload").removeClass("preload");
}

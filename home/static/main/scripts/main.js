//$(".navigation-button").smoothHover();

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

//$(".navigation-button").smoothHover();

(function( $ ){
    $.fn.insertBreaks = function() {
        moji = $(this).text().trim().split('');
        $(this).html( moji.join("<br>") );
    }; 
})( jQuery );


$(".vertical-text").insertBreaks();

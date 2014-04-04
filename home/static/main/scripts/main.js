
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
    Galleria.loadTheme(s3_url + "static/galleria/themes/twelve/galleria.twelve.min.js");
    Galleria.configure({
        debug: !isProduction,
        imageCrop: false,
        preload: 'all',
        autoplay: false,
        variation: 'light'
    });
    Galleria.run('.galleria');

    // This should make any gallerias visible.
    $(".galleria.preload").removeClass("preload");
}



//=======================================================
// Make sure all nav buttons are accessible!
(function( $ ){
    $.fn.navHide = function() {
        $(this).removeClass("navitem-on")
               .addClass("navitem-off");
    }; 
    $.fn.navShow = function() {
        $(this).removeClass("navitem-off")
               .addClass("navitem-on");
    };
    $.fn.navSpilcount = function() {
        overage = $(this).height() + $(this).offset().top - $(window).height();
        b = $(".navigation-button");
        bh = b.height() + parseInt(b.css("margin-top"));
        spilcount = Math.ceil(overage / bh);
        return spilcount;
    };
})( jQuery );

nav = $("#main-navigation");
spilmenuButton = $("#nav-spilmenu-wrapper");
spilmenu = $("#navspilmenu");

updateNavItems = function() {
    spilcount = nav.navSpilcount();
    if( spilcount > 0 ) {
        spilmenuButton.navShow();
        spilcount = nav.navSpilcount();
        onlist = $(".navigation-button.navitem-on");
        spilfrom = onlist.length - spilcount;
        onlist.slice(spilfrom).navHide();
        spilitems = $(".spilmenuitem.navitem-off");
        toshow = spilitems.slice(spilfrom);
        toshow.navShow();
    } else if( spilcount < 0 ) {
        showcount = -spilcount;
        offlist = $(".navigation-button.navitem-off");
        if( offlist.length > 0 ) {
            if( offlist.length == showcount )
                spilmenuButton.navHide();
            oncount = Math.min( offlist.length, showcount );
            toshow = offlist.slice( 0, oncount )
            toshow.navShow();
            tohide = $(".spilmenuitem.navitem-on").slice( 0, oncount );
            tohide.navHide();
        }
    }
    h = $(".navigation-button.navitem-off");
    if( spilmenuButton.hasClass("navitem-on") && h.length == 1 ) {
        spilmenuButton.navHide();
        h.navShow();
        $(".spilmenuitem.navitem-on").navHide();
    }
};

$(window).on('ready load resize orientationChanged', updateNavItems);


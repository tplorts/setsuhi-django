
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
})( jQuery );

nav = $("#main-navigation");
spillMenu = $("#navigation-spill-menu-wrapper");

updateNavigationSpill = function() {
    buttons = nav.find(".navigation-button");
    buttonCount = buttons.length;
    spillItems = spillMenu.find(".spill-menu-item");

    // The height of each button and the inter-button space
    buttonsh = buttons.height() + parseInt(buttons.css("margin-top"));

    // How much vertical space there is for navigation
    // buttons, in terms of how many buttons could be fit into
    // the visible navigation area.
    spaceCount = Math.floor( $(window).height() / buttonsh );

    // How many buttons can be shown
    showCount = Math.min( spaceCount, buttonCount );

    // If there is not enough room for all buttons...
    if( showCount < buttonCount ) {
        // Turn on the spill menu button
        spillMenu.navShow();

        // Since we activated the menu button, there is
        // now less space for navigation buttons.
        if(showCount > 0) showCount -= 1;
    }

    // But if there is enough room for all buttons...
    else {
        // Turn off the spill menu button
        spillMenu.navHide();
    }

    // Show up to 'showCount'; hide the rest.
    buttons.slice(0, showCount).navShow();
    buttons.slice(showCount).navHide();

    // In the spill menu, show only starting at 'showCount'.
    spillItems.slice(0, showCount).navHide();
    spillItems.slice(showCount).navShow();
};

$(window).on('ready load resize orientationChanged', updateNavigationSpill);



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
spillMenuButton = $("#navigation-spill-menu-wrapper");

navSpillCount = function() {
    // How many pixels of the navigation have gone out of view?
    overage = nav.height() + nav.offset().top - $(window).height();

    b = $(".navigation-button");

    // The height of each button and the inter-button space
    bh = b.height() + parseInt(b.css("margin-top"));

    return Math.ceil(overage / bh);
};

updateNavigationSpill = function() {
    spillCount = navSpillCount();

    // negative of spillCount --> how much space for buttons
    spaceCount = -spillCount;

    // If there are buttons spilling into the invisible region
    if( spillCount > 0 ) {
        // Turn on the spill menu button
        spillMenuButton.navShow();

        // Recalculate how much room there is now that the
        // spill menu button was inserted.
        spillCount = navSpillCount();

        // Gather all buttons which are turned on.
        onlist = $(".navigation-button.navitem-on");

        // Get the button index from which we will spill
        spillFrom = onlist.length - spillCount;

        // Turn off all turned-on buttons starting at 'spillFrom'
        onlist.slice(spillFrom).navHide();
        
        // Turn on all turned-off spill menu items starting at 'spillFrom'
        $(".spill-menu-item.navitem-off").slice(spillFrom).navShow();
    }         
    // If there is now room to insert more buttons
    else if( spaceCount > 0 ) {
        // Gather all turned off buttons
        offlist = $(".navigation-button.navitem-off");

        // The minimum of the spilled buttons count and how much
        // room we have tells us how many buttons to insert.
        // (There may be more space than buttons, or vice-versa)
        oncount = Math.min( offlist.length, spaceCount );

        // Turn on the first 'oncount' buttons that were off
        offlist.slice(0, oncount).navShow();

        // Turn off the first 'oncount' menu items that were on
        $(".spill-menu-item.navitem-on").slice( 0, oncount ).navHide();
    }

    // If only one button remains in the spil menu, then
    // the spil menu is not necessary, so put that button back
    // into main navigation.
    h = $(".navigation-button.navitem-off");
    if( spillMenuButton.hasClass("navitem-on") && h.length == 1 ) {
        h.navShow();
        $(".spill-menu-item.navitem-on").navHide();
    }
    
    // If the spill menu is empty, then hide that button.
    if( $(".spill-menu-item.navitem-on").length == 0 )
        spillMenuButton.navHide();
};

$(window).on('ready load resize orientationChanged', updateNavigationSpill);


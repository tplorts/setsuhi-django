
s3_url = "http://s3-ap-northeast-1.amazonaws.com/setsuhi-tokyo/";


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




// Activate different groups of sakuhin in the galleria
$("button.section-button").click( function() {
    if( typeof galleriaDataSets === 'undefined' )
        return;
    groupName = $(this).attr('data-sakuhin-group');
    Galleria.get(0).load( galleriaDataSets[groupName] );
    activeSakuhinGroup = groupName;
    //TODO: use the below function instead
});

function setActiveSakuhinGroup( groupName ) {
    if( groupName == activeSakuhinGroup )
        return;
    activeSakuhinGroup = groupName;
    //TODO: code from above to update galleria + button visual active
}

//======================================
// galleria.io
$(window).ready( function() {
    if( !Galleria || $(".galleria").length == 0 )
        return;

    themePath = "static/galleria/themes/twelve/galleria.twelve.min.js";
    Galleria.loadTheme(s3_url + themePath);
    Galleria.configure({
        debug: !isProduction,
        imageCrop: false,
        preload: 'all',
        autoplay: false,
        variation: 'light'
    });

    if( typeof galleriaDataSets !== 'undefined' 
        && typeof activeSakuhinGroup !== 'undefined' )
    {
        Galleria.run(".galleria", {
            dataSource: galleriaDataSets[activeSakuhinGroup]
        });
        setActiveSakuhinGroup( activeSakuhinGroup );
    } else if( typeof galleriaData !== 'undefined' ) {
        Galleria.run('.galleria', {
            dataSource: galleriaData
        });
    } else {
        Galleria.run('.galleria');
    }

    // This should make any gallerias visible.
    $(".galleria.preload").removeClass("preload");
});




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

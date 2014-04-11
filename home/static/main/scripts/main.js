

s3_url = "http://s3-ap-northeast-1.amazonaws.com/setsuhi-tokyo/";



//=============================================================
// http://www.codeproject.com/Articles/462209/Using-custom-font-without-slowing-down-page-load
// http://css-tricks.com/preventing-the-performance-hit-from-custom-fonts/
/*
takaoFontFile = s3_url + "TakaoMincho.ttf";
takaoCSS = "\
@font-face {\
    font-family: 'TakaoMincho';\
    font-style: normal;\
    font-weight: 300;\
    src: url('"+takaoFontFile+"');\
}\
[lang='ja'] {\
    font-family: 'TakaoMincho' !important;\
}\
";
$(document).ready(function(){
    $.ajax({
        url: takaoFontFile,
        beforeSend: function ( xhr ) {
            xhr.overrideMimeType("application/octet-stream");
        },
        success: function(data) {
            style = $('<style type="text/css" />');
            style.append( takaoCSS );
            style.appendTo('head');
        }
    });
});
*/




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
    groupName = $(this).attr('data-sakuhin-group');
    setActiveSakuhinGroup( groupName );
});

function setActiveSakuhinGroup( groupName ) {
    buttonBin = $("#sakuhin-section-buttons");
    activeButtons = buttonBin.find(".active-group");
    activeButtons.removeClass("active-group");

    if( typeof galleriaDataSets === 'undefined' )
        return;

    b = buttonBin.find(".section-button[data-sakuhin-group='"+groupName+"']");
    b.addClass("active-group");

    if( groupName != activeSakuhinGroup ) {
        Galleria.get(0).load( galleriaDataSets[groupName] );
        activeSakuhinGroup = groupName;
    }
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
        autoplay: false
    });

    if( typeof galleriaDataSets !== 'undefined' 
        && typeof activeSakuhinGroup !== 'undefined' )
    {
        Galleria.run(".galleria", {
            dataSource: galleriaDataSets[activeSakuhinGroup],
            extend: function(options) {

                //Galleria.log(this) // the gallery instance
                //Galleria.log(options) // the gallery options

                // listen to when an image is shown
                this.bind('image', function(e) {
                    editform = $("#sakuhin-info-form");
                    if( editform.length == 0 ) return;
                    info = e.galleriaData;
                    editform.find("[name='dbpk']").val(info.dbpk);
                    editform.find("[name='title']").val(info.title);
                    editform.find("[name='brief']").val(info.description);
                    editform.find("[name='lengthy']").val(info.long_description);
                });
            }
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

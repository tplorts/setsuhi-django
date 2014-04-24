

s3_url = "http://s3-ap-northeast-1.amazonaws.com/setsuhi-tokyo/";



//=================================================================
// LONG PRESS DETECTION
// For opening a login menu without an explicit login button.

var pressTimer = null;
var signature = $("#signature");
var didLongPress = false;

signature.click( function() {
    var toGo = !didLongPress;
    if( didLongPress ) {
        window.location.href = '/workroom/';
    }
    didLongPress = false;
    return toGo;
});

var longPressed = function() {
    didLongPress = true;
    signature.addClass("secret-activated");
};

signature.mouseup(function(){
    clearTimeout(pressTimer);
    pressTimer = null;
    return false;
}).mousedown(function(){
    pressTimer = window.setTimeout(longPressed, 2000);
    didLongPress = false;
    return false; 
});

$(document).mouseup(function() {
    if( signature.hasClass("secret-activated") )
        signature.removeClass("secret-activated");
});

//=================================================================
//                            \\\\|////
//                             \\|||//
//                              |||||
//                             //|||\\
//                            ////|\\\\
//=================================================================
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



  /* Select the group listed at the top */
  var activeSakuhinGroup = $("#sakuhin-group-buttons .on").first().find("button").attr("data-sakuhin-group");

// Activate different groups of sakuhin in the galleria
$(".sakuhin-group-button").click( function() {
    groupName = $(this).attr('data-sakuhin-group');
    setActiveSakuhinGroup( groupName );
});

function setActiveSakuhinGroup( groupName ) {
    buttonBin = $("#sakuhin-group-buttons");
    activeButtons = buttonBin.find(".active-group");
    activeButtons.removeClass("active-group");

    if( typeof galleriaDataSets === 'undefined' )
        return;

    b = buttonBin.find(".sakuhin-group-button[data-sakuhin-group='"+groupName+"']");
    b.addClass("active-group");

    if( groupName != activeSakuhinGroup ) {
        var gal = Galleria.get(0);
        gal.load( galleriaDataSets[groupName] );
        activeSakuhinGroup = groupName;
    }
}

var presentImageData = null;
updateImageEditor = function (e) {
    editform = $("#sakuhin-info-form");

    //todo: when in fullscreen an error shows up on the
    //      log but it seems to be inconsequential.
    var isFullscreen = $(".galleria-container").hasClass("fullscreen");

    // Don't do anything if this element does
    // not exist (user is not logged in).
    if( editform.length == 0 )
        return;

    // Get the data Galleria's structure.
    info = e.galleriaData;
    presentImageData = info;

    // Insert the values originally from the database
    editform.find("[name='dbpk']").val(info.dbpk);
    editform.find("[name='title']").val(info.title);
    editform.find("[name='brief']").val(info.description);
    editform.find("[name='lengthy']").val(info.long_description);

    // Reset the result area
    $("#sakuhin-edit-result").empty();
};

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
//        preload: 'all',
        autoplay: false
    });

    if( typeof galleriaDataSets !== 'undefined' 
        && typeof activeSakuhinGroup !== 'undefined' )
    {
        Galleria.run(".galleria", {
            dataSource: galleriaDataSets[activeSakuhinGroup],
            extend: function(options) {
                // listen to when an image is shown
                this.bind('loadfinish', updateImageEditor);
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

var infoForm = $('#sakuhin-info-form');

$("#edit-toggle").click( function() {
    if( infoForm.hasClass("on") ) {
        infoForm.removeClass("on").addClass("off");
        $(this).text("show editor");
    } else if( infoForm.hasClass("off") ) {
        infoForm.removeClass("off").addClass("on");
        $(this).text("hide editor");
    }
});


// Submit the edits for the image info without
// triggering a page reload.
infoForm.submit(function () {
    d = infoForm.serialize();
    console.log("data to POST:"+d);
    $.ajax({
        type: infoForm.attr('method'),
        url: infoForm.attr('action'),
        data: d,
        success: function (data) {
            $("#sakuhin-edit-result").html(data);
            // Put the new data into the Galleria
            // structure so that navigating back to 
            // this image renders the new info data.
            presentImageData.title = infoForm.find("[name='title']").val();
            presentImageData.description = infoForm.find("[name='brief']").val();
            presentImageData.long_description = infoForm.find("[name='lengthy']").val();
        },
        error: function(data) {
            $("#sakuhin-edit-result").html(data);
        }
    });
    return false;
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

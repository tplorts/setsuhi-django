mlWidget = $(".ml-widget");
mlIndicator = mlWidget.find(".ml-active-indicator");

(function( $ ){
   $.fn.mlFindLocal = function( languageCode ) {
       return this.find("[lang='" + languageCode + "']");
   }; 
})( jQuery );


function mlButton( lang ) {
    return mlWidget.find( ".ml-language[lang='" + lang + "']" );
}


function setTitleLanguage( languageCode ) {
    titles = $("#ml-titles .ml");
    if( titles ) {
        localTitleElement = titles.mlFindLocal( languageCode );
        if( localTitleElement ) {
            document.title = localTitleElement.text();
        }
    }
}


function moveIndicator( lang, animated ) {
    langButton = mlButton( lang );
    if( !langButton ) return;

    newProperties = {
        left: langButton.position().left + "px", 
        width: (langButton.width() + 14) + "px",
        height: (langButton.height() + 8) + "px"
    };
    if( animated ) {
        mlIndicator.animate(newProperties, 600);
    } else {
        mlIndicator.css( newProperties );
    }

    mlWidget.find(".selected").removeClass("selected");
    langButton.addClass("selected");
}


function setLanguage( lang, animated ) {
    langButton = mlButton( lang );
    if( !langButton ) return;

    moveIndicator( lang, animated );
    setTitleLanguage(lang);

    $.removeCookie("ml-language-selection");
    $.cookie("ml-language-selection", lang, {path: '/', expires: 3650});

    ml_elements = $(".ml");
    former = ml_elements.find(".ml-on");
    latter = ml_elements.mlFindLocal( lang );

    if( former && latter ) {

        if( animated ) {
            former.fadeOut(400, function() {
                former.removeClass("ml-on").addClass("ml-off");
                latter.fadeIn(400, function() {
                    latter.removeClass("ml-off").addClass("ml-on");
                });
            });
        } else {
            former.removeClass("ml-on").addClass("ml-off");
            latter.removeClass("ml-off").addClass("ml-on");
        }

    }
}

// Attach click-handlers to each ml language button
mlWidget.find(".ml-language").click( function() {
    if( $(this).hasClass("selected") )
        return;
    setLanguage( $(this).attr("lang"), true );
});


priorSelection = $.cookie("ml-language-selection");
if( priorSelection ) {
    langButton = mlButton( priorSelection );
    if( langButton ) {
        moveIndicator( priorSelection, false );
        setTitleLanguage( priorSelection );
    } else {
        $.removeCookie("ml-language-selection");
    }
}

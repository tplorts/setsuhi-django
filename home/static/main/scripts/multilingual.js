mlWidget = $(".ml-widget");

(function( $ ){
   $.fn.mlFindLocal = function( languageCode ) {
       return this.find(">[lang='" + languageCode + "']");
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


function indicateActive( langButton ) {
    mlWidget.find(".ml-language.active").removeClass("active");
    langButton.addClass("active");
}


function setLanguage( lang, animated ) {
    langButton = mlButton( lang );
    if( !langButton ) return;

    setTitleLanguage(lang);
    indicateActive( langButton );

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
if( !priorSelection ) {
    priorSelection = "ja";
}
langButton = mlButton( priorSelection );

// We take the presence of a button for a particular language
// to mean that this website has that language available.
// Therefore, only set to that language if it's available.
if( langButton ) {
    setLanguage( priorSelection, false );
}

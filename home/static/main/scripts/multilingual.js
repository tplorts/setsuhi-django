
(function( $ ){
   $.fn.mlFindLocal = function( languageCode ) {
       return this.find(">[lang='" + languageCode + "']");
   }; 
})( jQuery );

function Multilingual() {
    this.COOKIE_KEY = "ml-language-selection";
    this.widgets = null;
    this.activeLanguage = null;
}

Multilingual.prototype.cookied = function() {
    return $.cookie(this.COOKIE_KEY);
}

Multilingual.prototype.cookie = function( lang ) {
    $.removeCookie(this.COOKIE_KEY);
    $.cookie(this.COOKIE_KEY, lang, {path: '/', expires: 3650});    
}

Multilingual.prototype.button = function( lang ) {
    return this.widgets.find( ".ml-language[lang='" + lang + "']" );
}

Multilingual.prototype.applyTitle = function( languageCode ) {
    titles = $("#ml-titles .ml");
    if( titles && titles.length > 0 ) {
        local = titles.mlFindLocal( languageCode );
        if( local && local.length > 0 ) {
            document.title = local.text();
        }
    }
}


Multilingual.prototype.indicateActiveButton = function( langButton ) {
    this.widgets.find(".ml-language.active").removeClass("active");
    langButton.addClass("active");
}


Multilingual.prototype.activate = function( lang, animated ) {
    langButton = this.button( lang );

    // Check that the button for the new language exists,
    // implicitly meaning that the language is available.
    if( !langButton ) return;

    this.activeLanguage = lang;

    // Apply this language's title and visually change the buttons.
    this.applyTitle( lang );
    this.indicateActiveButton( langButton );

    // Update the cookie
    this.cookie( lang );

    // Update all multilingual content
    allMultilingualBlocks = $(".ml");
    this.update( allMultilingualBlocks );
}

Multilingual.prototype.update = function( mlBlocks ) {
    // Pass if no content
    if( mlBlocks.length == 0 )
        return;

    if( typeof animated === 'undefined' )
        animated = false;

    former = mlBlocks.find(".ml-on");
    latter = mlBlocks.mlFindLocal( this.activeLanguage );

    if( animated && false ) {
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


Multilingual.prototype.initialise = function() {
    this.widgets = $(".ml-widget");

    var mlthis = this;
    // Attach click-handlers to each ml language button
    this.widgets.find(".ml-language").click( function() {
        if( $(this).hasClass("active") )
            return;
        mlthis.activate( $(this).attr("lang"), true );
    });

    // Check for a previously selected language
    savedLang = this.cookied();
    if( !savedLang ) {
        // Default to Japanese
        savedLang = "ja";
    }
    langButton = this.button( savedLang );

    // We take the presence of a button for a particular language
    // to mean that this website has that language available.
    // Therefore, only set to that language if it's available.
    if( langButton ) {
        this.activate( savedLang, false );
    }
}


var multilingual;
$(document).ready( function() {
    multilingual = new Multilingual();
    multilingual.initialise();
});


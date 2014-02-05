
EXPAND = 1, CONTRACT = -1;
LAST_STEP = 5;

function HoverHandler( jqButton ) {
    this.button = jqButton;
    this.direction = EXPAND;
    this.stepIndex = 0;
    this.intervalId = null;
}

HoverHandler.prototype.presentClass = function() {
    return "expand-step-" + this.stepIndex;
}

HoverHandler.prototype.stop = function() {
    if( this.intervalId ) {
        clearInterval( this.intervalId );
        this.intervalId = null;
    }
}

HoverHandler.prototype.step = function() {
    this.button.removeClass( this.presentClass() );
    this.stepIndex += this.direction;
    if( this.stepIndex <= 0 ) {
        this.stop();
        this.stepIndex = 0;
    } else if( this.stepIndex >= LAST_STEP ) {
        this.stop();
        this.stepIndex = LAST_STEP;
    }
    this.button.addClass( this.presentClass() );
}

HoverHandler.prototype.start = function( newDirection ) {
    this.stop();
    this.direction = newDirection;
    var self = this;
    this.intervalId = setInterval( function(){self.step();}, 40 );
}

HoverHandler.prototype.expand = function() {
    this.start( EXPAND );
}

HoverHandler.prototype.contract = function() {
    this.start( CONTRACT );
}



hoverRegistry = [];

function hoverHandler( button ) {
    bid = button.attr("id");
    if( !(bid in hoverRegistry) )
        hoverRegistry[bid] = new HoverHandler( button );
    return hoverRegistry[bid];
}


(function( $ ){
    $.fn.smoothHover = function() {
        $(this).hover( function(event) {
            hoverHandler( $(this) ).expand();
        }, function(event) {
            hoverHandler( $(this) ).contract();
        } );
    }; 
})( jQuery );



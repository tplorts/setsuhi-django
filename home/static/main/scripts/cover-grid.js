grid = $("#photo-collection-grid");
textarea = $("#collection-description-area");

function hidePrior() {
    prior = textarea.find(".collection-description.active");
    if( prior ) prior.removeClass("active");
}

grid.find(".cover-image").hover(
    function() {
        hidePrior();
        n = parseInt( $(this).attr("id").slice(11) );
        textarea.find("#description-"+n).addClass("active");
    },
    function() {
        hidePrior();
    }
);

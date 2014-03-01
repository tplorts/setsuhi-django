grid = $(".phota-grid");
textarea = $("#photum-brief-area");

function hidePrior() {
    prior = textarea.find(".photum-brief.active");
    if( prior ) prior.removeClass("active");
}

grid.find(".photum-cover").hover(
    function() {
        hidePrior();
        n = parseInt( $(this).attr("id").slice(13) );
        textarea.find("#photum-brief-"+n).addClass("active");
    },
    function() {
        hidePrior();
    }
);

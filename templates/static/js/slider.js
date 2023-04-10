$(function() {
    $("#slider-range" ).slider({
        range: true,
        min: 0,
        max: 24600,
        values: [ 750, 24600 ],
        slide: function( event, ui ) {
            $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] +"/ Year" );
        }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
        " - $" + $( "#slider-range" ).slider( "values", 1 ) + "/ Year");
} );
$("#slider-range").slider({
    range: true,
    min: 0,
    max: 24600,
    values: [750, 24600],
    slide: function(event, ui) {
        $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1] + "/ Year");
    }
});

$("#amount").val("$" + $("#slider-range").slider("values", 0) +
    " - $" + $("#slider-range").slider("values", 1) + "/ Year");
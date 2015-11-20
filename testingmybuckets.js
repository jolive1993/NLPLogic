$.ajaxSetup( { "async": false } );
var data = []
$.getJSON( "relationships.json", function(json) {
    data = json
});

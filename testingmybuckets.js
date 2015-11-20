$.ajaxSetup( { "async": false } );
var data = []
var data2 = []
$.getJSON( "relationships.json", function(json) {
    data = json
});
$.getJSON( "secondrelations.json", function(json) {
    data2 = json
});

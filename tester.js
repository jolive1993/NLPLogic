var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var ObjectId = require('mongodb').ObjectID;
var url = 'mongodb://localhost:27017/wikitext';
var data = []
var findRelationships = function(db, callback) {
    var cursor =db.collection('relationships').find( );
    cursor.each(function(err, doc) {
        assert.equal(err, null);
        if (doc != null) {
            data = doc;
        } else {
            callback();
        }
    });
};
MongoClient.connect(url, function(err, db) {
    assert.equal(null, err);
        findRelationships(db, function() {
        for (x in data){
            console.log(data[x])
        }
        db.close();
    });
});
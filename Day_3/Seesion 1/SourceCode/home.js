var mongoose = require("mongoose");

// 1) Connecting to the Database 

mongoose.connect("mongodb://localhost/gg");

console.log("Sucessfully Connected to MongoDB");

// 2) Creating a Schema

var schema = mongoose.Schema;

var travelSchema = new schema({

    userId : String,
    stationName : String,
    doorType :String,
    timestamp : String
});

// 3) Model the Schema 

var travelModel = mongoose.model("travels",travelSchema);


// 4) Insert Data

var travelData = new travelModel({

    userId : "485",
    stationName : "virar",
    doorType : "exit",
    timestamp :"562345"

});


travelData.save(function(err){
    if(err) throw err;
    console.log("Inserted Data ..");

});


console.log("Function Complete..");


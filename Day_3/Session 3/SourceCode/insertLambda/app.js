var mongoose = require("mongoose");

// 1) Creating a Connection 

mongoose.connect("mongodb://54.255.220.89/testDb");

console.log("Connection Established ....");

// 2) Crating Schema 

var schema = mongoose.Schema;

var userSchema = new schema({

    userId: String,
    stationName:String,
    doorType :String,
    timestamp : String

});

// 3) Creating a MOdel

var userModel = mongoose.model("users", userSchema);

// 4) Insert values

var userData = new userModel({

    userId : "105",
    stationName : "vasai",
    doorType : "entry",
    timestamp :"455789"
});


userData.save(function(err){
    if(err) throw err;
    console.log("Sucessfully Inserted Values")

});

console.log("Function Ended ...");
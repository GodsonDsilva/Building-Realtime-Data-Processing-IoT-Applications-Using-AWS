var mongoose = require("mongoose");

// 1) Connecting to MongoDb
mongoose.connect("mongodb://localhost/gg");

console.log("Sucessfully Connected");

// 2) Creating Schema 
var MySchema = mongoose.Schema;

var userSchema = new MySchema({
    userId : String,
    stationName : String,
    doorType : String,
    timestamp : String

});

console.log("Sucessfully Created a schema");

// 3) Model the Schema 

var userModel = mongoose.model("users", userSchema);

// 4)  Insert data in mongodb
var userData = new userModel({

    userId : "503",
    stationName: "vasai",
    doorType : "entry",
    timestamp : "1890345"
});


userData.save(function(err){
    if(err) throw err;
    console.log("Sucessfully Inserted Data");
});

console.log("Function Ended");
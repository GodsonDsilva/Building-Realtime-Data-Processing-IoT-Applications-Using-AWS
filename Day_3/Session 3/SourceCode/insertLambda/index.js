'use strict';

var mongoose = require("mongoose");

console.log('Loading function');

exports.handler = (event, context, callback) => {
   
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

        var colectionName = event.userId;

        var userModel = mongoose.model(colectionName, userSchema);

        // 4) Insert values

        var userData = new userModel({

            userId : event.userId,
            stationName : event.stationName,
            doorType : event.doorType,
            timestamp :event.timestamp
        });


        userData.save(function(err){
            if(err) throw err;
            console.log("Sucessfully Inserted Values")

        });

        console.log("Function Ended ...");

        callback(null, {
            statusCode: '200',
            body:"success",
            headers: {
            'Content-Type':'application/json',
         }
    });

};

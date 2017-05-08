'use strict';

var mongoose = require('mongoose');
  
exports.handler = (event, context, callback) => 
{

    console.log('Received event:', JSON.stringify(event, null, 2));
    
    //Lets connect to our database using the DB server URL.
     mongoose.connect('mongodb://172.31.20.220/travelDb');

     console.log("Connected Succesfully ...");

      var Schema = mongoose.Schema;

   // Creating Schema 

    var travelSchema = new Schema({
                      usrerId : String,
                      stationName  : String,
                      doorType  : String,
                      timestamp : String
                                 
                       
      });

      console.log("Created the Schema Succesfully ...");

     var travelModel = mongoose.model('Travels', travelSchema);     
     
     var travelData = new travelModel(
      {
                      usrerId : event.usrerId,
                      stationName  : event.stationName,
                      doorType  : event.doorType,
                      timestamp : event.timestamp
     });
  

    travelData.save(function(err) {
      if (err) throw(err);
      //console.dir(trainData);
    });

   
  console.log("Inserted Data Succesfully ...");  

  callback(null, {
    statusCode: '200',
    body:"success",
    headers: {
      'Content-Type':'application/json',
    },

  }); 
}

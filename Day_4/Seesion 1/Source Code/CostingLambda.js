'use strict';

console.log('Loading function');

var mongoose = require('mongoose');
var AWS = require('aws-sdk');  

AWS.config.region = 'ap-southeast-1';

exports.handler = (event, context, callback) => {
   
     mongoose.connect('mongodb://172.31.20.220/testDb');

    console.log("Connected Succesfully ...");

    var Schema = mongoose.Schema;

   // Creating Schema 

    var travelSchema = new Schema({
                      userId : String,
                      stationName  : String,
                      doorType  : String,
                      timestamp : String
                      
      });

      console.log("Created the Schema Succesfully ...");

    var collectionName = event.userId;
    //var collectionName = "101"

    var destinationStation = event.stationName;

    var travelModel = mongoose.model(collectionName, travelSchema);  

    //Lets try to Find a source station
    travelModel.find({doorType: 'entry' }, function (err, userObj) {
    if (err) {
                console.log(err);

    } else if (userObj) {

            // var myJSON = JSON.stringify(userObj);
            console.log('Found:', userObj);
            var sourceStation = userObj[0].stationName;

            console.log("Source Station:",sourceStation);
            console.log("Destination Station:",destinationStation);
            
            calculateCost(sourceStation,destinationStation);
            
            
    } else {
        console.log('User not found!');
    }

});


function calculateCost(source, destination){
    
    console.log('Calculate Cost Function Called ...');
    console.log("Source Station in cost:",source);
    var stationkm = {
                virar:1,
                nallasopara:5,
                vasaiRoad:10,
                naigaon:14,
                bhayander:18,
                miraRoad:23,
                dahisar:28,
                borivali:32,
                andheri:45,
                bandra:53,
                dadar:64,
                mumbaiCentral :72,
                churchgate :80
        };

     var sourceKm = stationkm[source];
     console.log("Source KM:",sourceKm);

     var destinationKm = stationkm[destination];
     console.log("Destination KM:",destinationKm);

      var totalKmTraveled = destinationKm - sourceKm;
      console.log("Total KM Travelled:",totalKmTraveled);

      var travelCost = totalKmTraveled * 3;

      var travelCostSend = travelCost.toString();

      console.log("Total Travel Cost :",travelCostSend);

      sendMessage(travelCostSend);

};

// function sendMessage(payload){
    
//      var sns = new AWS.SNS();
      
//       //var payload = 145;

//       var msg = "The cost of Your travel today is RS"+payload;
      
//       console.log("Sending SMS Msg Data :",msg );
//       var params = {
//         Message: msg,
//         MessageStructure: 'string',
//         PhoneNumber: '+918698877587'
//         };
        
//         console.log("Sending SMS ..");

//      sns.publish(params, function(err, data) {
//         if (err) console.log(err, err.stack); // an error occurred
//         else console.log(data); // successful response
//         });
        
//         console.log("Sucessfully Send SMS ..");
//     // Sending an Email

//      console.log("Sending Email ..");
//       sns.publish({
//             Message:msg ,
//             TopicArn: 'arn:aws:sns:ap-southeast-1:921100090497:TrainTravelCost'
//             }, function(err, data) {
//             if (err) {
//             console.log(err.stack);
//             return;
//             }
//             console.log('push sent');
//             console.log(data);
//            // context.done(null, 'Function Finished!');
//      });
     
//      console.log(" Email SEND..");

//      console.log("Droping a Collection  ..");
//       // Droping the data from the Collection
//     //  travelModel.find('', function(err, user) {
//     //     if (err) throw err;

//     //             // delete the documents
//     //             travelModel.remove(function(err) {
//     //                 if (err) throw err;

//     //                 console.log('Users successfully deleted!');
//     //             });
//     //     });

// };

console.log('Function Ended');
callback(null, {
        statusCode: '200',
        body:"success",
        headers: {
        'Content-Type':'application/json',
          }
     });

};



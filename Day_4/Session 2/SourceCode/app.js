'use strict';

console.log('Loading function');

var AWS = require('aws-sdk');

AWS.config.region = 'ap-southeast-1';

console.log("\n\nLoading handler\n\n");


var sns = new AWS.SNS();
var msg = "Hello mate ..welcome to |RO|ckstar";

sns.publish({
    Message:msg ,
    TopicArn: 'arn:aws:sns:ap-southeast-1:703171350772:lambdaToSNS'
}, function(err, data) {
    if (err) {
        console.log(err.stack);
        return;
    }
    console.log('push sent');
    console.log(data);

 });

console.log("Sucess...");
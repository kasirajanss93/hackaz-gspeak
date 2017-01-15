'use strict';
var http = require('http');
console.log('Loading event');
exports.handler = function(event, context, callback) {
  console.log('"Hello":"World"');
  var req = http.request({
      port:8080,
      hostname:'138.197.222.95',
      method:'GET',
      path:'/'
  },function(res){
      var output = ''
      res.on('data',function(chunk){
          output+=chunk;
      });
      res.on('end',function(){
        callback(null,JSON.parse(output));          
      })
  }).end();
}
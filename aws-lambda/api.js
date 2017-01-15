'use strict';
var http = require('http');
var ip_addr = ''; //IP Address of the Memcached and Controller to be mentioned here
console.log('Loading event');
exports.handler = function(event, context, callback) {
  console.log('"Hello":"World"');
  var req = http.request({
      port:8080,
      hostname:ip_addr,
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

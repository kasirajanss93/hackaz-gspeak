var express = require('express')
var app = express()
var Memcached = require('memcached')
var memcached = new Memcached('127.0.0.1:11211')
var bodyParser = require('body-parser')
var router = express.Router()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use('/',router)
router.get('/',function(req,res){
	memcached.get('data',function(err,data){
		val = { "uid": "urn:uuid:1335c695-cfb8-4ebb-abbd-80da344efa6b",
			"updateDate": new Date().toISOString(),
			"titleText": "Gesture Speak Feed",
			"mainText": data,
			"redirectionUrl": "http://manojsenguttuvan.com"
		}
		res.send(val);
	});
});

router.post('/',function(req,res){
	console.log(req.body.data)
	memcached.set('data',req.body.data,100,function(err){
		res.send("successful")
	});
});

app.listen(8080,function(){
	console.log('server running at 8080');
});

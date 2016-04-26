var bodyParser = require('body-parser');
var express = require('express');
var mongoose = require('mongoose');
var morgan = require('morgan');
var path = require('path');

var app = express();
var port = process.env.PORT || 3000;

var user = require('./app/routes/user')();

var options = {
  server: {
    socketOptions: {
      keepAlive: 1,
      connectTimeoutMS: 30000
    }
  },
  replset: {
    socketOptions: {
      keepAlive: 1,
      connectTimeoutMS: 30000
    }
  }
}

mongoose.connect('mongodb://localhost/user_database', options)
var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error: '));

app.use(morgan('dev'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.text());
app.use(bodyParser.json({type: 'application/json'}));

app.use(express.static(__dirname + '/public'));
app.use('/bower_components', express.static(__dirname + '/bower_components'));

app.route('/user').post(user.post).get(user.getAll);

app.route('/user/:id').get(user.getOne);

app.listen(port);
console.log('listening on port ' + port);

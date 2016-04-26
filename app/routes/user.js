var mongoose = require('mongoose')
var express = require('express')
var User = require('../models/user')

module.exports = function() {
  return {
    getAll: function(req, res){
      var query = User.find({});

      query.exec(function(err, users){
        if(err) res.send(err);
        res.json(users);
      });
    },

    post: function(req, res){
      var newUser = new User(req.body);

      newUser.save(function(err){
        if(err){
          res.send(err);
        }
        res.json(req.body);
      });
    },

    getOne: function(req, res){
      User.findById(req.params.id, function(err, user){
        if(err){
          res.send(err);
        }
        res.json(user);
      });
    }
  }
};

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var UserSchema = new Schema({
  firstName: {type: String, required: true},
  lastName: {type: String, required: true},
  privileges: {type: String, required: true},
  picture: {type: Schema.Types.Mixed, required: true},
  morePictures: Schema.Types.Mixed,
  createdAt: {type: Date, default: Date.now},
});

UserSchema.pre('save', function(next){
  now = new Date();
  if(!this.createdAt) {
    this.createdAt = now;
  }
  next();
});

module.exports = mongoose.model('user', UserSchema);

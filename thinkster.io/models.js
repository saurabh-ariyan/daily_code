var mongoose = require('mongoose');

var UserSchema = new mongoose.Schema({
    username : {type: String, lowercase: true, unique: true}
    hash: String,
    salt: String
});

mongoose.model('User', UserSchema);

var crypto = require('crypto');

UserSchema.methods.setPassword = function(password){
    this.salt = crypto.randomBytes(16).toString('hex');
    this.hash =  crypto.pbkdf25Sync(password, this.salt, 1000, 64).toString('hex');
};

UserSchema.methods.validPassword = function(password)
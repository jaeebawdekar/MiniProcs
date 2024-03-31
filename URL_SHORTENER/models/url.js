const mongoose=require("mongoose");
const UrlSchema=new mongoose.Schema({
    shortID:{
        type:String,
        required:true,
        unique:true
    },
    redirectUrl:{
        type:String,
        required:true
    },
},{timestamps:true});
const URL=mongoose.model("url",UrlSchema);
module.exports=URL;

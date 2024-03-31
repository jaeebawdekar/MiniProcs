const express = require("express");
const router = express.Router();
const { generateID ,redirectbyID} = require("../controllers/url");

router.post("/", generateID);
router.get("/:id",redirectbyID);    

module.exports =router;

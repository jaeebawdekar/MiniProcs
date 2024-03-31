const URL = require("../models/url");
const shortid = require("shortid");

async function generateID(req, res, next) {
    const body = req.body;
    if (!body || !body.url) {
        return res.status(400).json({ "err": "The URL is missing" });
    }
    const shortId = shortid(); 
    try {
        await URL.create({
            shortID: shortId,
            redirectUrl: body.url
        });
        return res.json({"id":shortId})
        
    } catch (err) {
        console.error("Error creating URL:", err);
        return res.status(500).json({ "err": "Internal Server Error" });
    }
}
async function redirectbyID(req,res){
    const generatedID = req.params.id;
    try {
        const result = await URL.findOne({ shortID: generatedID }); 
        if (!result) {
            return res.status(404).json({ "err": "URL not found" });
        }
        res.redirect(result.redirectUrl);
    } catch (err) {
        console.error("Error redirecting:", err);
        return res.status(500).json({ "err": "Internal Server Error" });
    }
}

module.exports = {
    generateID,
    redirectbyID,
};

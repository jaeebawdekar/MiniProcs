const express = require("express");
const app = express();
const PORT = 8000;
const { connectDB } = require("./connection");
const urlRouter= require("./routers/url");

connectDB("mongodb://127.0.0.1:27017/urlShortener").then(() => {
  console.log("The Database is connected");
  app.use(express.json());
  app.use("/url", urlRouter);
  app.listen(PORT, () => {
    console.log("Server started");
  });
});

const http = require("http");
const fs = require("fs");
const clarifai = require("clarifai");

const app = new clarifai.App({
  apiKey: "b8f4339020aa4524bdf092820a486c3f"
});

http.createServer(function(request, response) {
  if (request.url == "/") {
    fs.readFile("test-client.html", (error, data) => {
      response.writeHead("200", {"Content-Type": "text/html"});
      response.write(data);
      response.end();
    });
  } else if (request.url == "/clarifai") {
    if (request.method == "POST") {
      var body = "";
      request.on("data", data => {
        body += data;
        if (body.length > 1e9) {
          request.connection.destroy();
        }
      });
      request.on("end", () => {
        var data = JSON.parse(body).image;
        app.models.predict(clarifai.GENERAL_MODEL, {base64: data}).then(
          predictions => {
            response.writeHead("200", {"Content-Type": "application/json"});
            response.write(JSON.stringify(predictions));
            response.end();
          },
          error => {
            console.log(error);
          }
        );
      });
    } else {
      response.writeHead("405", {"Content-Type": "text/html"});
      response.write("405 Method Not Allowed");
      response.end();
    }
  } else if (request.url == "/jquery") {
    fs.readFile("jquery-3.3.1.min.js", (error, data) => {
      response.writeHead("200", {"Content-Type": "text/javascript"});
      response.write(data);
      response.end();
    })
  }
}).listen(5000);

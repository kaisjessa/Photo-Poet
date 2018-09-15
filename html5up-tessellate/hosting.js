var http = require("http");
var fs = require("fs");
const clarifai = require("clarifai");

const app = new clarifai.App({
  apiKey: "b8f4339020aa4524bdf092820a486c3f"
});

http.createServer(function(request, response) {
  if (request.url == "/clarifai") {
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
            var concepts = predictions.outputs[0].data.concepts;
            response.writeHead("200", {"Content-Type": "application/json"});
            response.write(
              JSON.stringify(
                (concepts.filter(a => a.value > 0.9)
             || [concepts[0]]).map(a => a.name)
              )
            );
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
    return;
  }
  var url = request.url.slice(1) || "index.html";
  fs.readFile(url.split("?")[0], (error, data) => {
    if (data === undefined) {
      response.writeHead(404, {"Content-Type": "text/html"});
      response.write("404 Not Found");
      response.end();
    } else {
      if (request.url.endsWith("css")) {
        response.writeHead(200, {"Content-Type": "text/css"});
      } else if (request.url.endsWith("html")) {
        response.writeHead(200, {"Content-Type": "text/html"});
      } else if (request.url.endsWith("js")) {
        response.writeHead(200, {"Content-Type": "text/js"});
      } else {
        response.writeHead(200, {"Content-Type": "text/html"});
      }
      response.write(data);
      response.end();
    }
  });
}).listen(8000);

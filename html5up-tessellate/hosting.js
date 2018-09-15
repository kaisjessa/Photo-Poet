var http = require("http");
var fs = require("fs");

http.createServer(function(request, response) {
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

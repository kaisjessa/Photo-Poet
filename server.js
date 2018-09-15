var http = require("http");
var fs = require("fs");

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
        var postdata = JSON.parse(body);
        response.writeHead("200", {"Content-Type": "text/html"});
        response.write(JSON.stringify(postdata));
        response.end();
      })
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

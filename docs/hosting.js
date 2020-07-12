(async () => {
  const http = require("http");
  const fs = require("fs");
  const fetch = require("node-fetch");
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
              var filtered = concepts.filter(a => a.value > 0.9);
              if (filtered.length == 0) filtered = [concepts[0]];
              concepts = filtered.slice(0, 5);
              var concept = concepts[0];
              (async () => {
                const answer = await fetch("http://localhost:5000", {
                  method: "POST",
                  headers: {
                    "Accept": "application/json",
                    "Content-Header": "application/json"
                  },
                  body: JSON.stringify({
                    keyword: concept.name
                  })
                });
                const content = await answer.text();
                response.writeHead("200", {"Content-Type": "application/json"});
                response.write(content);
                response.end();
              })();
            },
            error => {
              response.writeHead("500", {"Content-Type": "text/html"});
              response.write(JSON.stringify({
                code: error.data.status.code,
                desc: error.data.status.description,
                outputs: error.data.status.outputs
              }));
              response.end();
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
})();

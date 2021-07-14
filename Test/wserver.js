var http = require('http');
var fs = require('fs');
var app = http.createServer(function (req, res) {
    var url = req.url;
    if (url == '/') {
        url = '/index.html';
    }
    res.writeHead(200);
    res.end(fs.readFileSync(__dirname + url));
}).listen(8080, '127.0.0.1');
console.log('Webserver is running at http://127.0.0.1:8080');
var http = require('http');
var fs = require('fs');
var formidable = require("formidable");
var util = require('util');
const sqlite3 = require('sqlite3').verbose();


let db = new sqlite3.Database('./myinfo.sqlite');
db.run('CREATE TABLE IF NOT EXISTS items (name text, userid integer, medicine text, disease text, remarks text, hourTake integer, minTake integer)');

var server = http.createServer(function (req, res) {
    if (req.method.toLowerCase() == 'get') {
        displayForm(res);
    } else if (req.method.toLowerCase() == 'post') {
        //processAllFieldsOfTheForm(req, res);
        processFormFieldsIndividual(req, res);
    }
});

function displayForm(res) {
    fs.readFile('form.html', function (err, data) {
        res.writeHead(200, {
            'Content-Type': 'text/html',
                'Content-Length': data.length
        });
        res.write(data);
        res.end();
    });
}

function processAllFieldsOfTheForm(req, res) {
    var form = new formidable.IncomingForm();

    form.parse(req, function (err, fields, files) {
        //Store the data from the fields in your data store.
        //The data store could be a file or database or any other store based
        //on your application.
        res.writeHead(200, {
            'content-type': 'text/plain'
        });
        res.write('received the data:\n\n');
        res.end(util.inspect({
            fields: fields,
            files: files
        }));
    });
}

function processFormFieldsIndividual(req, res) {
    //Store the data from the fields in your data store.
    //The data store could be a file or database or any other store based
    //on your application.
    var fields = [];
    var form = new formidable.IncomingForm();
    form.on('field', function (field, value) {
        console.log(field, " ", value);
        fields[field] = value;
    });

    form.on('end', function () {
        res.writeHead(200, {
            'content-type': 'text/plain'
        });
        res.write('received the data:\n\n');
        res.end(util.inspect({
            fields: fields
        }));

	db.run("INSERT INTO items (name, userid , medicine, disease, remarks, hourTake, minTake) VALUES (?,?,?,?,?,?,?)", [fields["name"], fields["userid"], fields["medicine"], fields["disease"], fields["remarks"], fields["hour"], fields["minute"]]);
});
    form.parse(req);
}

server.listen(1185);
console.log("server listening on 1185");

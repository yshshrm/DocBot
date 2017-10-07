function processFormFieldsIndividual(req, res) {
    //Store the data from the fields in your data store.
    //The data store could be a file or database or any other store based
    //on your application.
    var fields = [];
    var form = new formidable.IncomingForm();
    form.on('field', function (field, value) {
        console.log(field);
        console.log(value);
        fields[field] = value;
    });

    form.on('end', function () {
        res.writeHead(200, {'content-type': 'text/plain'});
        res.write('received the data:\n\n');
        res.end(util.inspect({fields: fields}));
    //console.log(fields);
    //console.log(fields.hour);
    //console.log(fields.minute);
    //db.run("INSERT into items(description,owner,hourTake, minTake) VALUES (fields.description,fields.userid,fields.hour, fields.minute)");
	db.run("INSERT INTO items (description,owner,hourTake, minTake) VALUES (?,?,?,?)", [fields["description"], fields["userid"], fields["hour"], fields["minute"]]);
});
    form.parse(req);
    

};
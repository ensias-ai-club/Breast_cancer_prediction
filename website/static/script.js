function loadFile(event) {
    // load csv file
    var csv = event.target.files[0];
    // read csv file
    var reader = new FileReader();
    reader.readAsText(csv);
    reader.onload = function() {
        // split csv file into rows
        var rows = reader.result.split('\n');
        // get the first and second row
        rows = rows.slice(1, 3);
        
        

        console.log(rows);
    };
}
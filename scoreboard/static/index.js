function update(fileName) {
    var newValue = document.getElementById(fileName).value;
    var request = new XMLHttpRequest();
    request.open("GET", '/update/' + fileName + '/' + newValue);
    request.onload = function() {
        document.getElementById(fileName).value = request.responseText;
    };
    request.send('');
}
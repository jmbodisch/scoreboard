function update(fileName) {
    let newValue = document.getElementById(fileName).value;
    let request = new XMLHttpRequest();
    request.open("GET"),'/update/' + fileName + '/' + newValue;
    request.onload = function() {
        document.getElementById(fileName).value = request.responseText;
    };
    request.send('');
}

function increment(fileName) {
    let request = new XMLHttpRequest();
    request.open("GET", '/' + fileName);
    request.onload = function() {
        let num = parseInt(request.responseText);
        num++;
        document.getElementById(fileName).value = num;
        document.getElementById("fields").submit();
    };
    request.send('');
}

function decrement(fileName) {
    let request = new XMLHttpRequest();
    request.open("GET", '/' + fileName);
    request.onload = function() {
        let num = parseInt(request.responseText);
        num--;
        document.getElementById(fileName).value = num;
        document.getElementById("fields").submit();
    };
    request.send('');
}

function saveConfig() {
    let request = new XMLHttpRequest();
    request.open("GET", '/save');
    request.onload = function() {
        if (request.responseText == "200"){
            alert("Save successful");
        }
   }
   request.send('');
}
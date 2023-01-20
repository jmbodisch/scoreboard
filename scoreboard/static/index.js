function update(fileName) {
    let newValue = document.getElementById(fileName).value;
    let request = new XMLHttpRequest();
    request.open("GET"),'/update/' + fileName + '/' + newValue;
    request.onload = function() {
        document.getElementById(fileName).value = this.responseText;
    };
    request.send('');
}

function increment(fileName) {
    let request = new XMLHttpRequest();
    request.open("GET", '/' + fileName);
    request.onload = function() {
        let num = parseInt(this.responseText);
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
        let num = parseInt(this.responseText);
        num--;
        document.getElementById(fileName).value = num;
        document.getElementById("fields").submit();
    };
    request.send('');
}

function moveUp(fileName) {
    let request = new XMLHttpRequest();
    request.open("GET", '/moveup/' + fileName);
    request.onload = function(event) {
        document.body.innerHTML = event.currentTarget.response;
    };
    request.send('');
}

function moveDown(fileName) {
    let request = new XMLHttpRequest();
    request.open("GET", '/movedown/' + fileName);
    request.onload = function(event) {
        document.body.innerHTML = event.currentTarget.response;
    };
    request.send('');
}

function deleteFile(fileName) {
    let request = new XMLHttpRequest();
    request.open("GET",'/delete/' + fileName);
    request.onload = function(event) {
        document.body.innerHTML = event.currentTarget.response;
    };
    request.send('');
}

function saveConfig() {
    let request = new XMLHttpRequest();
    request.open("GET", '/save');
    request.onload = function() {
        if (this.status == "200"){
            alert("Save successful");
        }
   }
   request.send('');
}

function toggleDetails(file) {
    let div = document.getElementById("details-" + file);
    div.classList.toggle('visibleDetails');
}

function updateDetails(name) {
    let request = new XMLHttpRequest();

    request.open("POST", "/details");
    request.setRequestHeader("Content-Type", "application/json");

    newName = document.getElementById('name-'+name).value;
    newPath = document.getElementById('path-'+name).value;
    newLabel = document.getElementById('label-'+name).value;

    let data = {
        'name': name,
        'newName': newName,
        'path': newPath,
        'label': newLabel
    };

    request.onload = function(event) {
        document.body.innerHTML = event.currentTarget.response;
    };

    request.send(JSON.stringify(data));
}
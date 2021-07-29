function updateTeamA() {
    var newName = document.getElementById("teamA").value;
    var request = new XMLHttpRequest();
    request.open("GET", '/teamA/'+newName);
    request.onload = function() {
        document.getElementById("teamA").value = request.responseText;
    };
    request.send('');
}

function updateTeamB() {
    var newName = document.getElementById("teamB").value;
    var request = new XMLHttpRequest();
    request.open("GET", '/teamB/'+newName);
    request.onload = function() {
        document.getElementById("teamB").value = request.responseText;
    };
    request.send('');
}

function updateScoreA() {
    var newName = document.getElementById("scoreA").value;
    var request = new XMLHttpRequest();
    request.open("GET", '/scoreA/'+newName);
    request.onload = function() {
        document.getElementById("scoreA").value = request.responseText;
    };
    request.send('');
}

function updateScoreB() {
    var newName = document.getElementById("scoreB").value;
    var request = new XMLHttpRequest();
    request.open("GET", '/scoreB/'+newName);
    request.onload = function() {
        document.getElementById("scoreB").value = request.responseText;
    };
    request.send('');
}

function incrementScoreA() {
    var request = new XMLHttpRequest();
    request.open("GET", '/scoreA');
    request.onload = function() {
        document.getElementById("scoreA").value = request.responseText;
    };
    request.send('');
}

function incrementScoreB() {
    var request = new XMLHttpRequest();
    request.open("GET", '/scoreB');
    request.onload = function() {
        document.getElementById("scoreB").value = request.responseText;
    };
    request.send('');
}
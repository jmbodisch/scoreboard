function updateTeamA() {
    var newName = document.getElementById("teamA").value;
    var request = new XMLHttpRequest();
    request.open("GET", '/update/teamA/'+newName);
    request.onload = function() {
        document.getElementById("teamA").value = request.responseText;
    };
    request.send('');
}

function updateTeamB() {
    var newName = document.getElementById("teamB").value;
    var request = new XMLHttpRequest();
    request.open("GET", '/update/teamB/'+newName);
    request.onload = function() {
        document.getElementById("teamB").value = request.responseText;
    };
    request.send('');
}

function updateScoreA() {
    var newName = document.getElementById("scoreA").value;
    var request = new XMLHttpRequest();
    request.open("GET", '/update/scoreA/'+newName);
    request.onload = function() {
        document.getElementById("scoreA").value = request.responseText;
    };
    request.send('');
}

function updateScoreB() {
    var newName = document.getElementById("scoreB").value;
    var request = new XMLHttpRequest();
    request.open("GET", '/update/scoreB/'+newName);
    request.onload = function() {
        document.getElementById("scoreB").value = request.responseText;
    };
    request.send('');
}

function incrementScoreA() {
    var request = new XMLHttpRequest();
    request.open("GET", '/update/scoreA');
    request.onload = function() {
        document.getElementById("scoreA").value = request.responseText;
    };
    request.send('');
}

function incrementScoreB() {
    var request = new XMLHttpRequest();
    request.open("GET", '/update/scoreB');
    request.onload = function() {
        document.getElementById("scoreB").value = request.responseText;
    };
    request.send('');
}
function login(){
var username = document.getElementById("username").value;
var pass = document.getElementById("password").value;

Http = new XMLHttpRequest();
url="http://0.0.0.0:80/validate/";
Http.open("POST", url, true);
Http.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
var data = "user=" + username + "&password=" + pass
Http.send(data);

}

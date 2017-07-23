function compile() {
  var http = new XMLHttpRequest();
  var url = "http://localhost:5000";
  var editor = ace.edit("editor");
  var myCode = editor.getSession().getValue();

  http.open("POST", url, true);
  http.setRequestHeader("Content-Type", "application/json");

  http.onload = function() {
    if (http.status == 200) {
      temp = JSON.parse(http.responseText);
      document.getElementById("compilertext").value = temp.result;
    }
    else {
      document.getElementById("compilertext").value = "HTTP Request failed. Check Docker server";
    }
  };

  var obj = { "code": myCode, "lang": "java"};
  http.send(JSON.stringify(obj));
}

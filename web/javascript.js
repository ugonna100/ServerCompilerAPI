function compile() {
  var http = new XMLHttpRequest();
  var url = "http://localhost:5000";
  var editor = ace.edit("editor");
  var myCode = editor.getSession().getValue();
  var lang = document.getElementById("langSel").value;
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

  var obj = { "code": myCode, "lang": lang};
  http.send(JSON.stringify(obj));
}

function changeLang() {
  var editor = ace.edit("editor");
  lang = document.getElementById("langSel").value;
  if (lang == "c++") {
    editor.session.setMode("ace/mode/" + "c_cpp");
  }
  else {
    editor.session.setMode("ace/mode/" + lang);
  }
}

function run() {
  const path = document.getElementById("path").value;
  eel.run(path);
}

function select(){
  eel.selectFolder();
}

eel.expose(result);
function result(r) {
  console.log(r);
  if(r) {
    document.getElementById("result").innerHTML = "Done ✌️";
    document.getElementById("path").value = "";
  } else {
    document.getElementById("result").innerHTML = "Failed 😥";
  }
}

eel.expose(setvalue);
function setvalue(path2) {
  document.getElementById("path").value = path2;
}
// function readfile(url) {

// }

var url = "/assert/repos/docker/docker.run.help"
    //var file_content = readfile(url)
var file_content = "TEST"
var string = "<pre><code>" + file_content + "</pre></code>"
document.getElementById("to_instead").innerHTML(string)
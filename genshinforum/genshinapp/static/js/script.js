

window.onload = () => {
    CKEDITOR.replace("themecontent");
  };

  function sendText() {
    window.parent.postMessage(CKEDITOR.instances.themecontent.getData(), "*");
  };
    themeblock = document.getElementById("themeblock")
    btn = document.getElementById("open")
    cancel = document.getElementById("cancelthemeblock")

  btn.addEventListener("click", function () {
    themeblock.style.display = "block";
    cancel.style.display = "flex"
    btn.style.display = "none"
    });

    cancel.addEventListener("click", function() {
        btn.style.display = "block"
        themeblock.style.display = "none";
        cancel.style.display = "none"
    });

  function cancelDiv(){
    document.getElementById("themeblock").style.display = "none";
    document.getElementById("cancelthemeblock").style.display = "none";
    document.getElementById("open").style.display = "block";
  };




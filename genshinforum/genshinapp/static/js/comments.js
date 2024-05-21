window.onload = () => {
    CKEDITOR.replace("commentcontent");
  };

  function sendText() {
    window.parent.postMessage(CKEDITOR.instances.commentcontent.getData(), "*");
  };
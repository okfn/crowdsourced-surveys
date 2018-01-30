function init_content_monitor() {
  var content = jQuery('#ifrm');

  // The user did navigate away from the currently displayed iframe page. Show an animation
  var content_start_loading = function() {
    alert ('NOW: show the animation');
  }

  // the iframe is done loading a new page. Hide the animation again
  var content_finished_loading = function() {
    alert ('DONE: hide the animation');
  }

  // Listen to messages sent from the content iframe
  var receiveMessage = function receiveMessage(e){
    // Handle the message
    switch (e.data) {
    case 'location': content_start_loading(); break;
    }
  };
  window.addEventListener("message", receiveMessage, false);

  // This will be triggered when the iframe is completely loaded
  content.on('load', content_finished_loading);
}

$(window).on("message", function(e) {
  console.log("message", e)
});

iFrameResize({
  log:false,
  checkOrigin: false
});

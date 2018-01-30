if('loading' !== document.readyState) {
  window.parent.postMessage('Client message: ' + window.location.href,'*');
}

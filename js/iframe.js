console.log(window.location);
if(window.location.href.split('/').pop() === 'map') {
  // window.parent.postMessage('Client message: ' + window.location.href,'*');
  window.parent.postMessage(
    {
      location: window.location.href
    },
    '*');
}

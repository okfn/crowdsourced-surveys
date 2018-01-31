var surveyId = 691;
var hostname = window.location.hostname;
var subdomain = hostname.split('.')[0];
var envSuffix = undefined;

var envs = {
  'default': '-staging',
  'tz-schools-staging': '-staging',
  'tz-schools': ''
};

if(!hostname) {
  subdomain = 'default';
}

envSuffix = envs[subdomain];

$(document).ready(function() {
  $('#ifrm').attr(
    'src',
    'https://crowdsurvey' + envSuffix + '.herokuapp.com/posts/create/' + surveyId
  );
});


$(window).on("message", function(e) {
  if (e.originalEvent.data.location) {
    path = e.originalEvent.data.location.split('/').pop();
    if (path === 'map') {
      $('#ifrm').hide();
      document.writeln('Thank you!');
    }
  }
});

iFrameResize({
  log:false,
  checkOrigin: false
});

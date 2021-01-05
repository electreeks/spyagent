window.addEventListener("load", function(){

  var video = document.querySelector("#userStream");

  let refresh = setInterval(function() {
    $('#js_page_refresher').load(document.URL +  ' #js_page_refresher');
  }, 1000);

  if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function (stream) {
        video.srcObject = stream;

      })
      .catch(function (err0r) {
        alert("Something went wrong! Check if you allowed Electreeks to access your camera.");
      });
  }



});

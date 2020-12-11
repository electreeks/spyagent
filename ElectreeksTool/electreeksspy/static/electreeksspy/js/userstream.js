window.addEventListener("load", function(){

  var video = document.querySelector("#userStream");

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

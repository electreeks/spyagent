window.addEventListener("load", function(){

  var video = document.querySelector("#userStream");
  var jshandler = document.querySelector("#jshandler");
  var stupid = "{{ stupid }}";

  let refresh = setInterval(function() {
    $('#jshandler2').load(document.URL +  ' #jshandler2');
  }, 2000);
 /*
  let refresh = setInterval(function() {
    $('#jshandler').load(document.URL +  ' #jshandler');
  }, 2000);
*/
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

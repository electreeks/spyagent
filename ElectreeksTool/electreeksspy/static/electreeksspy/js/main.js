window.addEventListener("load", function(){


  let refresh = setInterval(function() {
    $('#js_page_refresher').load(document.URL +  ' #js_page_refresher');
  }, 3000);

});

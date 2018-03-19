'use strict'

$(function(){
  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    var color = request.color;
    $('body').css('background-color', color);
  });
});

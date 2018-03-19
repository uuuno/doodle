'use strict'

$(function(){
	$('.box').on('click', function(){
	  var color = $(this).css('background-color');

		chrome.tabs.query({active: true, lastFocusedWindow: true},function(tabs){
			chrome.tabs.sendMessage(tabs[0].id, {"color": color}, function(response){});
		});
	});

});

/*
 * Event Handlers for the Transcription Tracker Page
 */

/*
 * Switch the button image from graph to info button
 * so the user knows what view the button will take them to
 */
$('#chart').on('click', function() {
	$('#graph-progress-btn').toggleClass('glyphicon-signal').toggleClass('glyphicon-info-sign');
	//add something to handle tooltips here too
	toggleGraphView();
});

$('.panel-select').on('click', function() {
	$('.panel-select').removeClass('panel-active');
	$(this).addClass('panel-active');
	var name = $(this).children("span").text();
	$('#progress-header > span').text("");
	$('#progress-header > span').text("Progress for " + name);
	//also switch progress view
});

function toggleGraphView() {
	$('#experience').toggle();
	$('#graph').toggle();
}

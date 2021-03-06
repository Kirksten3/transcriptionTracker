<!DOCTYPE html>
<html>
	<head>
		<!-- file://oande.sig.oregonstate.edu/Ecampus/Files/CDT%20Student%20Workers/Jake/Projects/Transcription%20Tracker/HTML%20CSS/index.html -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
		<link rel="stylesheet" href="gui/site.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.10.6/moment.js"></script>
	</head>
	<body>
		<nav class="navbar navbar-inverse navbar-fixed-top">
        	<div class="container-fluid">
            	<p class="navbar-text navbar-left">
            		<b>Transcription Tracker</b>
            	</p>
            	<p class="navbar-text navbar-right" style="margin-right:0px;">
            		<b>Pretend You're Having Fun</b>
            	</p>
            </div>
        </nav>
		
		<div class="container" style="margin-top:75px;">
			<div class="row">
				<div class="col-md-4">
					<!-- scoreboard info -->
					<div class="panel panel-default">
						<div class="panel-heading clearfix">
							<span style="padding-top:7.5px;" class="panel-title pull-left">Scoreboard</span>
							<a id="chart" href="#" class="btn btn-default btn-md pull-right">
								<!-- use this id to switch between image onclick in jquery -->
					        	<span id="graph-progress-btn" class="glyphicon glyphicon-signal"></span> 
					        </a>
						</div>
						<div class="panel-body">
							<div class="panel-group" style="margin-bottom: 0px;">
								<?php
									UI::CreateUserBoxes();
								?>
								<!-- these will have to be propagated automatically in the future -->
								<!--
								<div class="panel panel-default">
									<div class="panel-body">
										<img src='gui/assets/Kendall.png' class='image-thumbnail' />
										<span>Kendall Henery</span>
										<imggroup>
											<img src='gui/assets/badge-slot.png' class='image-badge' />
											<img src='gui/assets/badge-slot.png' class='image-badge' />
											<img src='gui/assets/badge-slot.png' class='image-badge' />
										<imggroup>
									</div>
								</div>
								<div class="panel panel-default">
									<div class="panel-body">
										<img src='gui/assets/Zach.png' class='image-thumbnail' />
										<span>Zach Homen</span>
										<imggroup>
											<img src='gui/assets/badge-slot.png' class='image-badge' />
											<img src='gui/assets/badge-slot.png' class='image-badge' />
											<img src='gui/assets/badge-slot.png' class='image-badge' />
										<imggroup>
									</div>
								</div>
								<div class="panel panel-default">
									<div class="panel-body">
										USER 3
									</div>
								</div>
								<div class="panel panel-default">
									<div class="panel-body">
										USER 4
									</div>
								</div> -->
							</div>
							<!-- List of everyone -->
						</div>
					</div>
				</div>
				<div class="col-md-1">
					<div class="divider-vertical-l"></div>
					<div class="divider-vertical-r"></div>
				</div>
				<div class="col-md-7">
					<div id='experience'>
						<!-- Experience -->
						<div>
							<div class="panel panel-default">
								<div id='progress-header' class="panel-heading">
									<span></span>
								</div>
								<div class="panel-body">
									PROGRESS GOES HERE
								</div>
							</div>
						</div>
						<div>
							<div class="panel panel-default">
								<div class="panel-heading">
									Newfound Knowledge
								</div>
								<div class="panel-body">
									KNOWLEDGE STUFF HERE
								</div>
							</div>
						</div>
					</div>
					<!-- hidden until signal (graph) button is pressed -->
					<div id='graph' style="display:none;">
						<!-- graph section -->
						<div>
							<div class="panel panel-default">
								<div class="panel-heading">
									Bar chart showing student comparison
								</div>
								<div class="panel-body">
									CHART GOES HERE
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		
		<!-- scripts -->
		<script src="gui/eventHandlers.js" type="text/javascript"></script>
	</body>
</html>
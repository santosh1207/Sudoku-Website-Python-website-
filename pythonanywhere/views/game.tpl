% setdefault('startTime', 0)
% setdefault('gameKey', '')
% setdefault('error', False)
% setdefault('css', ["/static/game.css"])
% rebase base title="Game", user_logged_in=user_logged_in, Ads=[{'img':'/static/logo2.jpg', 'link':'http://www.educationworld.com/'}], CSSs=css, JSs=["/static/game.js"]
% if (user_logged_in):
	<p id="error" class="btn btn-warning"></p>
	<br/>
	<center>
	<form id="gameForm" class="grid" class="form-group form-group-lg">
		% for row in game:
		<div class="row">
			% for col in row:
				<div class="cell">
					<input type="text" class="form-control"
				% if col > 0:
					value="{{ col }}" disabled
				% else:
					required aria-required="true" pattern="[1-9]" maxlength=1
				% end
					size=1></input>
				</div>
			% end
		</div>
		% end
	</form>
	<div class="controls">
	<center>
		<p><a id="hintBtn" class="btn btn-success btn-lg btn-block" role="button">Show A Hint</a></p>
		<p><a id="vrfySol" class="btn btn-warning btn-lg btn-block" role="button">Verify Solution</a></p>
		<p><a id="dispSol" class="btn btn-danger btn-lg btn-block" role="button">Display Solution</a></p>
		<br/>
		% if startTime > 0:
		<p><h4>Time Remaining</h4><span id="timer">{{ startTime }}</span></p>
		% end
	<center>
	</div>
	</center>
	<br/>
	<form id="successForm" class="hidden" method="post" action="/success">
		<input id="gameKey" type="hidden" value="{{solution}}"></input>
		<input name="timeLeft" id="timeLeft" type="hidden" value="0"></input>
	</form>
% else:
	<h1>Sudoku</h1>
	% if error:
		<p class="error"><strong>Error:</strong> {{ error }}</p>
	% end
	<p>Register/Login to Play</p>
	<p><a class="btn btn-success btn-lg" href="login" role="button">Log-In &raquo;</a></p>
	<p><a class="btn btn-primary btn-lg" href="register" role="button">Register &raquo;</a></p>
% end
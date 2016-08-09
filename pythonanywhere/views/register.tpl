% setdefault('error', False)
% rebase base title="Register", user_logged_in=user_logged_in, JSs=["http://code.jquery.com/ui/1.11.4/jquery-ui.js"], CSSs=["http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css"]
% if not(user_logged_in):
	<h3>Register</h3>
	% if error:
		<p class="error"><strong>Error:</strong> {{ error }}</p>
	% end
	<form class="form-signin" method=POST action="register">
		<input type="name" name="inputName" id="inputName" class="form-control" placeholder="Name" required autofocus><br/>
		<input type="date" name="inputDOB" id="inputDOB" class="form-control" placeholder="Date of Birth" required autofocus><br/>
		<input type="email" name="inputEmail" id="inputEmail" class="form-control" placeholder="Email address" required autofocus><br/>
		<input type="password" name="inputPassword" id="inputPassword" class="form-control" placeholder="Password" required><br/>
		<button type="submit" class="btn btn-lg btn-success btn-block">Sign Up</button>
	</form>
% else:
	<h3>You are already registered!</h3>
	<p><a class="btn btn-success btn-lg" href="logout" role="button">Log Out &raquo;</a> <a class="btn btn-primary btn-lg" href="play" role="button">Play &raquo;</a></p>
% end

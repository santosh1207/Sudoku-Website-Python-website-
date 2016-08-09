% setdefault('error', False)
% rebase base title="Login", user_logged_in=user_logged_in
% if not(user_logged_in):
	<h3>Login</h3>
	% if error:
		<p class="error"><strong>Error:</strong> {{ error }}</p>
	% end
	<form class="form-signin" method=POST action="login">
		<input type="email" name="inputEmail" id="inputEmail" class="form-control" placeholder="Email address" required autofocus><br/>
		<input type="password" name="inputPassword" id="inputPassword" class="form-control" placeholder="Password" required><br/>
		<button type="submit" class="btn btn-lg btn-success btn-block">Sign in</button>
	</form>
	<br/>
	<hr/>
	<br/>
	<div>
	<h4>Not Registerd?<h4>
	<a href="/register" id="btnRegister" class="btn btn-lg btn-primary btn-block" type="button">Get Registered</a>
	</div>
% else:
	<h3>You are already logged in!</h3>
	<p><a class="btn btn-success btn-lg" href="logout" role="button">Log Out &raquo;</a> <a class="btn btn-primary btn-lg" href="play" role="button">Play &raquo;</a></p>
% end

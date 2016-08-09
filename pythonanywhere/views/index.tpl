% setdefault('error', False)
% rebase base title="Welcome", user_logged_in=user_logged_in
% if (user_logged_in):
	<h1>Rules</h1>
	<p>Placeholder for the rules of sudoku</p>
	<p><a class="btn btn-primary btn-lg" href="/play" role="button">Play Now &raquo;</a></p>
% else:
	<h1>Sudoku</h1>
	% if error:
		<p class="error"><strong>Error:</strong> {{ error }}</p>
	% end
	<p>Register/Login to Play</p>
	<p><a class="btn btn-success btn-lg" href="/login" role="button">Log-In &raquo;</a> <a class="btn btn-primary btn-lg" href="/register" role="button">Register &raquo;</a></p>
% end

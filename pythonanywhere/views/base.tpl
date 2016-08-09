% setdefault('CSSs', [])
% setdefault('JSs', [])
% setdefault('Ads', [])
% setdefault('title', 'Enjoy')
% setdefault('message', '')
% setdefault('error', False)

<!DOCTYPE html>
<html>
<head>
	<title>Sudoku - {{ title or '' }}</title>
	<!-- Latest compiled and minified CSS -->
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
	<!-- Jumbotron theme -->
    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
	% for css in CSSs:
	<link href="{{ css }}" rel="stylesheet">
	% end
</head>
<body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
		<div class="container">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="/">Sudoku</a>
			</div>
			<div id="navbar" class="navbar-collapse collapse">
			% if user_logged_in:
                <div class="navbar-form navbar-right btn-group">
                    <a class="btn btn-default" href="/about">About Us</a>
                    <a class="btn btn-default" href="/play">Play</a>
                    <a class="btn btn-default" href="/">Rules</a>
                    <a class="btn btn-default" href="/logout">Logout</a>
                </div>
			% else:
				<form class="navbar-form navbar-right" method=POST action="login">
					<div class="form-group">
						<input type="email" name="inputEmail" placeholder="Email" class="form-control">
					</div>
					<div class="form-group">
						<input type="password" name="inputPassword" placeholder="Password" class="form-control">
					</div>
					<button type="submit" class="btn btn-success">Sign in</button>
				</form>
			% end
			</div><!--/.navbar-collapse -->
		</div>
    </nav>
    <div id="flash" class="flash">{{ message }}</div>
    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
		<div class="container">
		</div>
    </div>
    <div class="container">
		<div class="row">
			<div class="col-md-12">
			%include
			</div>
		</div>
		<footer class="footer">
			<p>&copy; Mahesh 2016</p>
			% for ad in Ads:
			<a href={{ ad['link'] }} target="_blank"><img src= {{ ad['img'] }} width="100%"></a>
			% end
		</footer>
    </div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
	<!-- Latest compiled and minified JavaScript -->
	<script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>
	% for js in JSs:
	<script src="{{ js }}"></script>
	% end
</body>
</html>
$(function() {
	var timer = document.getElementById('timer');
	var initTime = (+new Date) + parseInt(timer.innerHTML) * 1000;
	var errorObj = document.getElementById('error');
	var keeptimer = true;
	var sudoku = document.getElementById('gameForm').elements;
	var validValue = new RegExp('[1-9]');
	var gameStr = document.getElementById('gameKey').value;
	var hintsRemaining = Math.floor(parseInt(timer.innerHTML)/70); //easy:2, medium:3, hard:5
	var timeDiff = 0;

	function promptNewGame() {
		$('.controls').html('<a id="newGame" class="btn btn-success btn-lg btn-block" role="button">New Game</a>');
		$('#newGame').click(function(){
			$('#successForm').submit();
		});
	}
	
	function onTimeOut() {
		keeptimer = false;
		$('#gameForm input').each(function(){
			index = $('#gameForm input').index(this);
			value = parseInt(gameStr.charAt(index));
			this.value = value;
			this.setAttribute('disabled','true');
		});
		promptNewGame();
	}
	
	function updateTimer() {
		timeDiff = initTime - (+new Date);
		if (timeDiff < 1000) {
			initTime = 0;
			flashErrorMsg('Time Out! Solution is being displayed.');
			onTimeOut();
		} else {
			time = new Date(timeDiff);
			timer.innerHTML = twoDigits(time.getUTCHours()) + ':'
							+ twoDigits(time.getUTCMinutes()) + ':'
							+ twoDigits(time.getUTCSeconds());
			if (keeptimer)
				setTimeout(updateTimer, 1000);
		}
	}

	function removeError(cell) {
		cell.removeAttribute('aria-invalid');
		cell.focus();
	}

	function removeAllErrors() {
		$('input[aria-invalid="true"]').each(function(){
			this.removeAttribute('aria-invalid');		
		});
	}

	function flashCell(elem) {
		elem.setAttribute('aria-invalid','true');
		setTimeout(function(){removeError(elem)}, 500);
		elem.focus();
	}

	function flashErrorMsg(msg) {
		errorObj.innerHTML="<strong>ERROR:</strong> " + msg;
		errorObj.style.display = "inherit";
	}
	
	function flashCellError(cell, msg="") {
		flashErrorMsg(msg);
		flashCell(cell);
	}

	function flashSuccess() {
		errorObj.innerHTML="<strong>Congratulations:</strong> Your solution is correct";
		errorObj.style.display = "inherit";	
		document.getElementById('timeLeft').value = Math.floor(timeDiff/1000);
		promptNewGame();
	}

	function twoDigits(n) {
		return (n < 10) ? '0'+n : n;
	}

	function validateCell(elem) {
		if(!validValue.test(elem.value)) {
			flashCell(elem);
			elem.value="";
			return false;
		} 		
	}
	
	function verifySolution() {
		var row, col, cell, curVal, sum, product;
		
		emptyCells = $('#gameForm input').filter(function(){return this.value.length == 0});
		if (emptyCells.length > 0) {
			elem = emptyCells[0];
			flashCellError(elem, "Cell is empty");
			return false;
		}

		for (row=0; row<9; row++) {
			for (col=0; col<8; col++){
				cell = row * 9 + col;
				for (idx=col+1; idx<9; idx++) {
					prevCell = row*9 + idx;
					if (sudoku[cell].value == sudoku[prevCell].value) {
						flashCell(sudoku[prevCell]);
						flashCellError(sudoku[cell], "Row contains duplicates");
						return false;
					}
				}
			}
		}

		for (col=0; col<9; col++) {
			for (row=0; row<8; row++){
				cell = row * 9 + col;
				for (idx=row+1; idx<9; idx++) {
					prevCell = idx*9 + col;
					if (sudoku[cell].value == sudoku[prevCell].value) {
						flashCell(sudoku[prevCell]);
						flashCellError(sudoku[cell], "Column contains duplicates");
						return false;
					}
				}
			}
		}
		for (blockRow=0; blockRow<3; blockRow++) {
			for (blockCol=0; blockCol<3; blockCol++) {
				for (row=0; row<3; row++) {
					for (col=0; col<3; col++){
						cell = blockRow*27 + blockCol*3 + row*9 + col;
						for (ridx=row; ridx<3; ridx++) {
							for (cidx=col; cidx<3; cidx++) {
								prevCell = blockRow*27 + blockCol*3 + ridx*9 + cidx;
								if (cell != prevCell && sudoku[cell].value == sudoku[prevCell].value) {
									flashCell(sudoku[prevCell]);
									flashCellError(sudoku[cell], "Block contains duplicates");
									return false;
								}
							}
						}
					}
				}
			}
		}
		flashSuccess();
	}

	function showHint(){
		if (hintsRemaining > 0) {
			emptyCells = $('#gameForm input').filter(function(){return this.value.length == 0});
			elem = emptyCells[Math.floor(Math.random() * emptyCells.length)];
			index = $('#gameForm input').index(elem);
			value = parseInt(gameStr.charAt(index));
			elem.value = value;
			flashCell(elem);
			if (--hintsRemaining < 1) {
				$('#hintBtn').hide();
			}
		}
	}
	
	$('#hintBtn').click(showHint);
	$('#vrfySol').click(verifySolution);
	$('#dispSol').click(onTimeOut);
	$('#error').click(function(){$(this).hide();});
	$('input').change(function(){validateCell(this)});
	setTimeout(updateTimer, 1000);
});
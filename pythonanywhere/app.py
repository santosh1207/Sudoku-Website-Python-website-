from sudoku import sudoku, maskedGame
from datetime import date, datetime
import bottle
import anydbm
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

gameTypes = ["easy", "medium", "hard"]
gameCells = {"easy": 25, "medium": 21, "hard": 17}
gameTimes = {"easy": 150, "medium": 240, "hard": 360}

application = SessionMiddleware(bottle.app(), session_opts)
db = anydbm.open('/home/kluemaster/sudoku/data/sudokudb', flag='c')
appsession = bottle.request.environ.get('beaker.session')
request = bottle.request

def user_logged_in():
    appsession = bottle.request.environ.get('beaker.session')
    return 'username' in appsession

@bottle.route('/static/<filename>')
def server_static(filename):
  return bottle.static_file(filename, root='/home/kluemaster/sudoku/static/')

@bottle.error(404)
@bottle.error(405)
@bottle.view('404')
def page_not_found(e):
    return dict(user_logged_in=user_logged_in())

@bottle.route("/")
@bottle.view('index')
def main():
    return dict(user_logged_in=user_logged_in())

@bottle.get("/register")
@bottle.view('register')
def register_page():
    return dict(user_logged_in=user_logged_in())

@bottle.post("/register")
@bottle.view('register')
def register_response():
    name = request.forms['inputName'].strip()
    udob = request.forms['inputDOB'].strip()
    user = request.forms['inputEmail'].strip()
    pwrd = request.forms['inputPassword'].strip()
    if name=="" or udob=="" or user=="" or pwrd=="":
        return dict(user_logged_in=user_logged_in(), error='All fields are required.')
    else:
        if db.has_key(user):
            return dict(user_logged_in=user_logged_in(), error='User already exists.')
        else:
            db[user] = "#^#".join(['0', name, udob, pwrd])
            return bottle.redirect('/login')

@bottle.get("/login")
@bottle.view('login')
def login_page():
    return dict(user_logged_in=user_logged_in())

@bottle.post("/login")
@bottle.view('login')
def login_page():
    user = request.forms['inputEmail'].strip()
    pwrd = request.forms['inputPassword'].strip()
    if user=="" or pwrd=="":
        return dict(user_logged_in=user_logged_in(), error='All fields are required.')
    if db.has_key(user):
        userData = db[user]
        secs, name, udob, uwrd = userData.split('#^#',3)
        if pwrd != uwrd:
            return dict(user_logged_in=user_logged_in(), error='Password is incorrect.')
        else:
            current = date.today()
            birth = datetime.strptime(udob, "%m/%d/%Y")
            currAge = (current.year - birth.year) - ((current.month, current.day) < (birth.month, birth.day))
            appsession = bottle.request.environ.get('beaker.session')
            appsession['css'] = ['/static/game.css']
            if currAge > 12 and currAge < 20:
                appsession['css'].append('/static/teen.css')
            else:
                if currAge < 13:
                    appsession['css'].append('/static/child.css')
                else:
                    appsession['css'].append('/static/adult.css')
            appsession['username'] = user
            appsession['timeLeft'] = int(secs)
            return bottle.redirect('/play')
    else:
        return dict(user_logged_in=user_logged_in(), error='User doesn\'t exist.')

@bottle.route("/play")
@bottle.view('selector')
def play():
    if user_logged_in():
        return dict(user_logged_in=user_logged_in())
    else:
        return bottle.redirect('/')

@bottle.route("/about")
@bottle.view('about')
def about():
    return dict(user_logged_in=user_logged_in())

@bottle.post("/success")
def success():
    if user_logged_in():
        appsession = bottle.request.environ.get('beaker.session')
        appsession['timeLeft'] = int(request.forms.get('timeLeft') or 0)
        userData = db[appsession['username']]
        _, rest = userData.split('#^#',1)
        db[appsession['username']] = '#^#'.join([str(appsession['timeLeft']), rest])
    return bottle.redirect('/play')

@bottle.route("/game")
@bottle.route("/game/<gameType>")
@bottle.view('game')
def game(gameType='hard'):
    if user_logged_in():
        newgame = sudoku()
        if gameType not in gameTypes:
            gameType = 'hard'
        mskgame = maskedGame(newgame, gameCells[gameType])
        gameStr = ''.join(str(col) for row in newgame for col in row)
        appsession = bottle.request.environ.get('beaker.session')
        startTime = gameTimes[gameType]+appsession['timeLeft']
        appsession['timeLeft'] = 0
        userData = db[appsession['username']]
        _, rest = userData.split('#^#',1)
        db[appsession['username']] = '#^#'.join(['0', rest])
        return dict(user_logged_in=user_logged_in(), game=mskgame, startTime=startTime, solution=gameStr, css=appsession['css'])
    return bottle.redirect('/')

@bottle.get('/logout')
def logout():
    if user_logged_in():
        appsession = bottle.request.environ.get('beaker.session')
        userData = db[appsession['username']]
        _, rest = userData.split('#^#',1)
        db[appsession['username']] = '#^#'.join([str(appsession['timeLeft']), rest])
        del appsession['username']
        appsession.invalidate()
    return bottle.redirect('/')

if __name__ == "__main__":
    bottle.run(app=application, reloader=True)
import flask


index = flask.Blueprint('index', __name__, template_folder='templates')


@index.route('/', methods=['GET'])
def base():
    return flask.render_template('index.html')

from flask import Flask, g, jsonify, abort, request
import psycopg2
import pylibmc

app = Flask(__name__)


def get_db():
    if not hasattr(g, 'postgres'):
        conn = psycopg2.connect(database='ticketo', user='ticketo', password='1', host='localhost', port=5432)
        g.postgres = conn
    return g.postgres


def get_mc():
    if not hasattr(g, 'memcache'):
        mc = pylibmc.Client(["127.0.0.1"], binary=True, behaviors={"tcp_nodelay": True, "ketama": True})
        g.memcache = mc
    return g.memcache


@app.teardown_appcontext
def close_connection(exception):
    pg = getattr(g, 'postgres', None)
    if pg is not None :
        pg.close()


@app.errorhandler(404)
def not_found(error):
    response = jsonify({'code': 404,'message': 'Not found'})
    response.status_code = 404
    return response


@app.route('/')
def index():
    return 'Hello, Tickets!'


@app.route('/api/v1/tickets', methods=['POST'])
def ticket_create():
    return 'not implemented'


@app.route('/api/v1/tickets/<int:ticket_id>', methods=['PUT'])
def ticket_change_state(ticket_id):
    return 'not implemented'


@app.route('/api/v1/tickets/<int:ticket_id>/comments', methods=['POST'])
def ticket_add_comment(ticket_id):
    return 'not implemented'


@app.route('/api/v1/tickets/<int:ticket_id>')
def ticket_get(ticket_id):
    mc = get_mc()
    ticket = mc.get(str(ticket_id))
    if ticket is not None:
        return jsonify(ticket)

    db = get_db().cursor()
    db.execute('SELECT * FROM tickets WHERE id = %s;', [ticket_id])
    ticket = db.fetchone()

    if ticket is None:
        abort(404)
    else:
        col_names = [el[0] for el in db.description]
        data = dict(zip(col_names, ticket))
        mc[str(ticket_id)] = data
        res = jsonify(data)
        return res


if __name__ == '__main__':
    app.run()

from flask import Flask, g, jsonify
import psycopg2

app = Flask(__name__)


def get_db():
    if not hasattr(g, 'postgres'):
        conn = psycopg2.connect(database='ticketo', user='ticketo', password='1', host='localhost', port=5432)
        cur = conn.cursor()
        g.postgres = conn
        g.postgres_cursor = cur
    return g.postgres_cursor


@app.teardown_appcontext
def close_connection(exception):
    pg = getattr(g, 'postgres', None)
    pgcur = getattr(g, 'postgres_cursor', None)
    if pg is not None and pgcur is not None:
        pgcur.close()
        pg.close()


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
    return 'not implemented'


if __name__ == '__main__':
    app.run()

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import redis
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

DATABASE_URL = os.getenv('DATABASE_URL')
REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
INSTANCE_ID = os.getenv('INSTANCE_ID', 'app1')

try:
    redis_client = redis.from_url(REDIS_URL, decode_responses=True)
    redis_client.ping()
except Exception as e:
    print(f"Redis connection failed: {e}")
    redis_client = None


def get_db():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


@app.route('/health')
def health():
    status = {
        'status': 'healthy',
        'instance': INSTANCE_ID,
        'timestamp': datetime.now().isoformat(),
        'services': {}
    }

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        status['services']['database'] = 'connected'
    except Exception as e:
        status['status'] = 'unhealthy'
        status['services']['database'] = f'error: {str(e)}'

    try:
        if redis_client:
            redis_client.ping()
            status['services']['redis'] = 'connected'
        else:
            status['services']['redis'] = 'not configured'
    except Exception as e:
        status['services']['redis'] = f'error: {str(e)}'

    code = 200 if status['status'] == 'healthy' else 503
    return jsonify(status), code


@app.route('/')
def index():
    user_id = 1
    cache_key = f'tasks:user:{user_id}'

    if redis_client:
        try:
            cached = redis_client.get(cache_key)
            if cached:
                tasks = json.loads(cached)
                return render_template('index.html', tasks=tasks, instance=INSTANCE_ID)
        except Exception:
            pass

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            'SELECT id, title, description, completed, created_at FROM tasks WHERE user_id = %s ORDER BY created_at DESC',
            (user_id,)
        )
        tasks = cur.fetchall()
        cur.close()
        conn.close()

        if redis_client:
            try:
                redis_client.setex(cache_key, 300, json.dumps(tasks, default=str))
            except Exception:
                pass

        return render_template('index.html', tasks=tasks, instance=INSTANCE_ID)
    except Exception as e:
        return f'Erro: {e}', 500


@app.route('/add', methods=['POST'])
def add_task():
    user_id = 1
    title = request.form.get('title')

    if not title:
        return redirect(url_for('index'))

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO tasks (user_id, title, completed) VALUES (%s, %s, %s)',
            (user_id, title, False)
        )
        conn.commit()
        cur.close()
        conn.close()

        if redis_client:
            redis_client.delete(f'tasks:user:{user_id}')

        return redirect(url_for('index'))
    except Exception as e:
        return f'Erro: {e}', 500


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    user_id = 1

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            'UPDATE tasks SET completed = NOT completed, updated_at = NOW() WHERE id = %s AND user_id = %s',
            (task_id, user_id)
        )
        conn.commit()
        cur.close()
        conn.close()

        if redis_client:
            redis_client.delete(f'tasks:user:{user_id}')

        return redirect(url_for('index'))
    except Exception as e:
        return f'Erro: {e}', 500


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    user_id = 1

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('DELETE FROM tasks WHERE id = %s AND user_id = %s', (task_id, user_id))
        conn.commit()
        cur.close()
        conn.close()

        if redis_client:
            redis_client.delete(f'tasks:user:{user_id}')

        return redirect(url_for('index'))
    except Exception as e:
        return f'Erro: {e}', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

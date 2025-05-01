from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    try:
        R = float(request.args.get('R', 1.0))
        t_max = float(request.args.get('t_max', 10.0))
        step = int(request.args.get('step', 100))
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid parameters'}), 400

    t = np.linspace(0, t_max, step)
    # Cycloid parametric equations
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))

    # Velocity components (first derivatives)
    vx = R * (1 - np.cos(t))
    vy = R * np.sin(t)

    # Acceleration components (second derivatives)
    ax = R * np.sin(t)
    ay = R * np.cos(t)

    data = {
        't': t.tolist(),
        'x': x.tolist(),
        'y': y.tolist(),
        'vx': vx.tolist(),
        'vy': vy.tolist(),
        'ax': ax.tolist(),
        'ay': ay.tolist()
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

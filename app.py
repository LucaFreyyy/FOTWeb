from flask import Flask, render_template, request, jsonify
import chess

app = Flask(__name__)
board = chess.Board()

@app.route('/')
def index():
    return render_template('index.html', board=board.fen())

@app.route('/move', methods=['POST'])
def move():
    move = request.json.get('move')
    try:
        board.push_san(move)
        return jsonify({'fen': board.fen(), 'legal': True})
    except:
        return jsonify({'error': 'Invalid move', 'legal': False})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

NODE_COUNT = 20  # >100 nodes
EDGE_DENSITY = 3  # Avg edges per node

def generate_graph():
    nodes = []
    edges = []

    # Define source and sink
    nodes.append({'id': 'S', 'label': 'Source', 'color': '#00ff99'})
    nodes.append({'id': 'T', 'label': 'Sink', 'color': '#ff4d4d'})

    # Create intermediate nodes
    for i in range(1, NODE_COUNT + 1):
        nodes.append({
            'id': f'N{i}',
            'label': f'N{i}',
            'title': f'Node N{i}',
            'color': '#2196f3'
        })

    all_node_ids = [f'N{i}' for i in range(1, NODE_COUNT + 1)]

    # Connect source to first few
    for i in range(1, 6):
        capacity = random.randint(10, 50)
        edges.append({
            'from': 'S',
            'to': f'N{i}',
            'label': f'{random.randint(1, capacity)}/{capacity}',
            'color': '#03dac6'
        })

    # Random edges between intermediate nodes
    for node_id in all_node_ids:
        for _ in range(EDGE_DENSITY):
            target = random.choice(all_node_ids)
            if node_id != target:
                capacity = random.randint(5, 30)
                edges.append({
                    'from': node_id,
                    'to': target,
                    'label': f'{random.randint(0, capacity)}/{capacity}',
                    'color': '#cccccc'
                })

    # Connect last few nodes to sink
    for i in range(NODE_COUNT - 5, NODE_COUNT):
        capacity = random.randint(20, 60)
        edges.append({
            'from': f'N{i}',
            'to': 'T',
            'label': f'{random.randint(10, capacity)}/{capacity}',
            'color': '#ff8a65'
        })

    return {'nodes': nodes, 'edges': edges}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
    return jsonify(generate_graph())

if __name__ == '__main__':
    app.run(debug=True)

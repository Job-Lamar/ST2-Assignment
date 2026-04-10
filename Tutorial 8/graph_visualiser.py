# === graph_visualizer.py ===
from graph import Graph
import tkinter as tk
import math

class GraphVisualizer(tk.Tk):
    def __init__(self, graph):
        super().__init__()
        self.title("Graph Visualizer")
        self.graph = graph

        self.canvas = tk.Canvas(self, width=500, height=500, bg='white')
        self.canvas.pack()

        self.vertex_positions = {}

        # Input fields
        input_frame = tk.Frame(self)
        input_frame.pack()

        tk.Label(input_frame, text="Vertex:").grid(row=0, column=0)
        self.vertex_entry = tk.Entry(input_frame, width=5)
        self.vertex_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="From:").grid(row=1, column=0)
        self.from_entry = tk.Entry(input_frame, width=5)
        self.from_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="To:").grid(row=1, column=2)
        self.to_entry = tk.Entry(input_frame, width=5)
        self.to_entry.grid(row=1, column=3)

        tk.Label(input_frame, text="Weight:").grid(row=2, column=0)
        self.weight_entry = tk.Entry(input_frame, width=5)
        self.weight_entry.grid(row=2, column=1)

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add Vertex", command=self.add_vertex).grid(row=0, column=0)
        tk.Button(btn_frame, text="Remove Vertex", command=self.remove_vertex).grid(row=0, column=1)

        tk.Button(btn_frame, text="Add Edge", command=self.add_edge).grid(row=1, column=0)
        tk.Button(btn_frame, text="Remove Edge", command=self.remove_edge).grid(row=1, column=1)

        tk.Button(btn_frame, text="BFS", command=self.run_bfs).grid(row=2, column=0)
        tk.Button(btn_frame, text="DFS", command=self.run_dfs).grid(row=2, column=1)

        self.draw_graph()

    # Draw graph
    def draw_graph(self):
        self.canvas.delete("all")
        radius = 20
        spacing = 150

        n = len(self.graph.graph)
        angle_gap = 360 / n if n else 0
        center_x, center_y = 250, 250

        # Draw vertices
        for i, v in enumerate(self.graph.graph):
            angle = math.radians(i * angle_gap)
            x = center_x + spacing * math.cos(angle)
            y = center_y + spacing * math.sin(angle)

            self.vertex_positions[v] = (x, y)

            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='lightblue')
            self.canvas.create_text(x, y, text=v)

        # Draw edges
        for v in self.graph.graph:
            x1, y1 = self.vertex_positions[v]
            for nbr in self.graph.graph[v]:
                x2, y2 = self.vertex_positions[nbr]

                self.canvas.create_line(
                    x1, y1, x2, y2,
                    arrow=tk.LAST if self.graph.directed else None
                )

                # Draw weights
                if self.graph.weighted:
                    w = self.graph.weights.get((v, nbr), '')
                    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                    self.canvas.create_text(mid_x, mid_y, text=str(w), fill="red")

    # Graph operations
    def add_vertex(self):
        v = self.vertex_entry.get()
        if v:
            self.graph.add_vertex(v)
            self.draw_graph()

    def remove_vertex(self):
        v = self.vertex_entry.get()
        if v in self.graph.graph:
            self.graph.graph.pop(v)

            # remove references
            for key in self.graph.graph:
                if v in self.graph.graph[key]:
                    self.graph.graph[key].remove(v)

            self.draw_graph()

    def add_edge(self):
        v1 = self.from_entry.get()
        v2 = self.to_entry.get()
        w = self.weight_entry.get()

        if v1 and v2:
            if self.graph.weighted:
                weight = int(w) if w else 1
                self.graph.add_edge(v1, v2, weight)
            else:
                self.graph.add_edge(v1, v2)

            self.draw_graph()

    def remove_edge(self):
        v1 = self.from_entry.get()
        v2 = self.to_entry.get()

        if v1 in self.graph.graph and v2 in self.graph.graph[v1]:
            self.graph.graph[v1].remove(v2)

            if self.graph.weighted:
                self.graph.weights.pop((v1, v2), None)

            self.draw_graph()

    # BFS / DFS
    def run_bfs(self):
        if self.graph.graph:
            start = next(iter(self.graph.graph))
            order = self.graph.bfs(start)
            self.highlight(order)

    def run_dfs(self):
        if self.graph.graph:
            start = next(iter(self.graph.graph))
            order = self.graph.dfs(start)
            self.highlight(order)

    def highlight(self, order):
        self.draw_graph()
        for i, v in enumerate(order):
            self.after(i * 500, lambda v=v: self.highlight_node(v))

    def highlight_node(self, v):
        x, y = self.vertex_positions[v]
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill='yellow')
        self.canvas.create_text(x, y, text=v)

# Run program
if __name__ == "__main__":
    g = Graph(directed=True, weighted=True)

    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')

    g.add_edge('A', 'B', 10)
    g.add_edge('B', 'C', 20)
    g.add_edge('C', 'A', 30)

    app = GraphVisualizer(g)
    app.mainloop()
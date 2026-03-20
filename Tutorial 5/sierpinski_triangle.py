# sierpinski_triangle.py
from tkinter import *  # Import tkinter

class SierpinskiTriangle:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Sierpinski Triangle")  # Set a title

        self.width = 200
        self.height = 200

        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # Frame for input
        frame1 = Frame(window)
        frame1.pack()

        Label(frame1, text="Enter an order: ").pack(side=LEFT)

        self.order = StringVar()
        Entry(frame1, textvariable=self.order, justify=RIGHT).pack(side=LEFT)

        Button(
            frame1,
            text="Display Sierpinski Triangle",
            command=self.display
        ).pack(side=LEFT)

        window.mainloop()  # Start event loop

    def display(self):
        self.canvas.delete("line")

        p1 = [self.width / 2, 10]
        p2 = [10, self.height - 10]
        p3 = [self.width - 10, self.height - 10]

        self.displayTriangles(int(self.order.get()), p1, p2, p3)

    def displayTriangles(self, order, p1, p2, p3):
        if order == 0:  # Base condition
            self.drawLine(p1, p2)
            self.drawLine(p2, p3)
            self.drawLine(p3, p1)
        else:
            # Midpoints
            p12 = self.midpoint(p1, p2)
            p23 = self.midpoint(p2, p3)
            p31 = self.midpoint(p3, p1)

            # Recursive calls
            self.displayTriangles(order - 1, p1, p12, p31)
            self.displayTriangles(order - 1, p12, p2, p23)
            self.displayTriangles(order - 1, p31, p23, p3)

    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags="line"
        )

    def midpoint(self, p1, p2):
        return [
            (p1[0] + p2[0]) / 2,
            (p1[1] + p2[1]) / 2
        ]


SierpinskiTriangle()  # Run program
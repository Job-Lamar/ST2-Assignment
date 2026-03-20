from tkinter import *
import math

class KochSnowflake:
    def __init__(self):
        window = Tk()
        window.title("Koch Snowflake")

        self.width = 200
        self.height = 200

        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # Input frame
        frame1 = Frame(window)
        frame1.pack()

        Label(frame1, text="Enter an order: ").pack(side=LEFT)

        self.order = StringVar()
        Entry(frame1, textvariable=self.order, justify=RIGHT).pack(side=LEFT)

        Button(
            frame1,
            text="Display Koch Snowflake",
            command=self.display
        ).pack(side=LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")

        # Triangle points
        p1 = [self.width / 2, 50]
        p2 = [50, self.height - 50]
        p3 = [self.width - 50, self.height - 50]

        try:
            order = int(self.order.get())
        except:
            order = 0

        # Draw 3 Koch edges
        self.drawKochLine(order, p1, p2)
        self.drawKochLine(order, p2, p3)
        self.drawKochLine(order, p3, p1)

    def drawKochLine(self, order, p1, p2):
        if order == 0:
            self.drawLine(p1, p2)
        else:
            x1, y1 = p1
            x5, y5 = p2

            # Divide into thirds
            x2 = x1 + (x5 - x1) / 3
            y2 = y1 + (y5 - y1) / 3

            x4 = x1 + 2 * (x5 - x1) / 3
            y4 = y1 + 2 * (y5 - y1) / 3

            # Peak of triangle
            dx = x4 - x2
            dy = y4 - y2

            angle = math.radians(60)

            x3 = x2 + dx * math.cos(angle) - dy * math.sin(angle)
            y3 = y2 + dx * math.sin(angle) + dy * math.cos(angle)

            p2_new = [x2, y2]
            p3_new = [x3, y3]
            p4_new = [x4, y4]

            # Recursive calls
            self.drawKochLine(order - 1, p1, p2_new)
            self.drawKochLine(order - 1, p2_new, p3_new)
            self.drawKochLine(order - 1, p3_new, p4_new)
            self.drawKochLine(order - 1, p4_new, p2)

    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags="line"
        )


# Run program
KochSnowflake()
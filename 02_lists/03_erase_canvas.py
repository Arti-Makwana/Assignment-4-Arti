#Implement an 'eraser' on a canvas.

#  #The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.



import tkinter as tk

CELL_SIZE = 40
ROWS = 10
COLS = 10

def main():
    def create_grid():
        """Draw the blue cell grid and store references."""
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                cells[(row, col)] = rect

    def erase(event):
        """Set cells under cursor to white."""
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        if (row, col) in cells:
            canvas.itemconfig(cells[(row, col)], fill='white')

    # Set up the main window
    root = tk.Tk()
    root.title("Canvas Eraser")

    canvas_width = COLS * CELL_SIZE
    canvas_height = ROWS * CELL_SIZE
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Create grid and bind mouse events
    cells = {}
    create_grid()
    canvas.bind("<B1-Motion>", erase)  # Hold and drag with left mouse button

    root.mainloop()

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

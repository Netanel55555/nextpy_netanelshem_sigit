import tkinter as tk
from tkinter import PhotoImage


class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Netanel Shem Tov Sigit")

        self.label = tk.Label(root, text="Hello Sigit")
        self.label.pack(pady=10)

        self.button = tk.Button(root, text="What is the best course in IDF?", command=self.show_image)
        self.button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

    def show_image(self):
        self.img = PhotoImage(file="/home/netanel55/PycharmProjects/nextPyNetanel/Unit 6/sigit2.png")
        self.image_label.config(image=self.img)


if __name__ == "__main__":
    root = tk.Tk()
    gui = SimpleGUI(root)
    root.mainloop()

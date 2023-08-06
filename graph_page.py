import tkinter as tk
from PIL import Image, ImageTk
import graph_maker as gm
from data import advice_list as al
import calculate
import random

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FONT_PATH = "fonts/Bobaland.ttf"
FONT_SIZE_LABEL = 24

# Advice list variables
stressful_actions = al.stressful_actions
depressing_actions = al.depressing_actions

# Variables to store the previous indices
prev_stressful_indices = []
prev_depressing_indices = []

def create_image_label(root, image_path, x, y):
    img = Image.open(image_path)
    img = img.resize((500, 340), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(root, image=img, bg="white")
    image_label.image = img
    image_label.place(x=x, y=y)
    return image_label

def update_label2():
    label2.config(text=calculate.get_mental_health())

def update_label4():
    global prev_stressful_indices
    global prev_depressing_indices

    advice_list = []
    max_advice_count = 5

    if calculate.is_stressed():
        r_indices = []
        while len(r_indices) < max_advice_count:
            r_num = random.randrange(0, len(stressful_actions))
            if r_num not in prev_stressful_indices:
                r_indices.append(r_num)
        advice_list.extend([stressful_actions[idx] for idx in r_indices])
        prev_stressful_indices = r_indices

    elif calculate.is_depressed():
        r_indices = []
        while len(r_indices) < max_advice_count:
            r_num = random.randrange(0, len(depressing_actions))
            if r_num not in prev_depressing_indices:
                r_indices.append(r_num)
        advice_list.extend([depressing_actions[idx] for idx in r_indices])
        prev_depressing_indices = r_indices
    if len(advice_list) != 0:
        ltxt4 = "\n".join([f"{i+1}. {advice}" for i, advice in enumerate(advice_list)])
        label4.config(text=ltxt4)
    elif len(advice_list) == 0:
        label4.config(text="Staying Happy!")

def main():
    root = tk.Tk()
    root.title("Statistics")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.configure(bg="white")
    root.resizable(False, False)

    additional_text = "You Might Have:"
    label = tk.Label(root, text=additional_text, font=(FONT_PATH, FONT_SIZE_LABEL), bg="white")
    label.pack(pady=50)

    global label2
    label2 = tk.Label(root, text="Error.", bg="white", font=("Arial", 18),
                      justify=tk.LEFT)
    label2.place(x=600, y=110)

    additional_text = "You Should Try:"
    label = tk.Label(root, text=additional_text, font=(FONT_PATH, FONT_SIZE_LABEL), bg="white")
    label.pack(pady=205)

    global label4
    label4 = tk.Label(root, text="Error.", bg="white", font=("Arial", 18),
                      justify=tk.LEFT)
    label4.place(x=600, y=405)

    images = [
        ("imgs/stress_graph.png", 0, 20),
        ("imgs/depress_graph.png", 0, 360)
    ]

    gm.create_depress_graph()
    gm.create_stress_graph()

    for image_path, x, y in images:
        create_image_label(root, image_path, x, y)
    update_label4()
    update_label2()
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import font
import classify

root = None  # Define root as a global variable

def create_textbox(parent, font_path, font_size):
    custom_font = font.Font(family=font.nametofont('TkDefaultFont').actual()['family'], size=font_size)
    text_box = tk.Text(parent, font=custom_font, width=50, height=12, wrap=tk.WORD, bd=2, relief=tk.SOLID)
    text_box.pack(fill=tk.BOTH, expand=True)
    return text_box

def submit_button_click():
    # Get the text from the textbox and store it in a variable
    journal_text = textbox.get("1.0", tk.END)

    # Do something with the journal_text variable (e.g., print it)
    classify.emotion_classify(journal_text)

    # Close the window after processing the text
    root.destroy()
    import graph_page
    graph_page.main()

def main():
    global root  # Make root a global variable
    # Create the main application window
    root = tk.Tk()
    root.title("Daily Journal")
    window_width = 850
    window_height = 550
    root.geometry(f"{window_width}x{window_height}")

    # Set the window background color to white
    root.configure(bg="white")

    # Disable window resizing
    root.resizable(False, False)

    # Specify the .ttf font file path
    font_path = "fonts/Bobaland.ttf"
    font_size_label = 28
    font_size_textbox = 14

    # Create a label with additional text above the textbox
    additional_text = "Your Daily Journal:"
    label = tk.Label(root, text=additional_text, font=(font_path, font_size_label), bg="white")
    label.pack(pady=50)  # Add some padding between the label and the textbox, adjust as needed

    # Create the textbox with the specified font and black border
    global textbox  # Make the textbox a global variable to access it in the submit_button_click() function
    textbox = create_textbox(root, font_path, font_size_textbox)

    # Center the textbox horizontally and move it down a little bit
    textbox.place(relx=0.5, rely=0.50, anchor=tk.CENTER)  # Adjust the rely value as needed

    # Create the "Submit" button aligned to the bottom right of the textbox
    next_button = tk.Button(root, text="Submit", height=2, width=10, command=submit_button_click)
    next_button.place(relx=0.799, rely=0.87, anchor=tk.SE)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

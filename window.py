import tkinter as tk
import requests

def force_update():
    url = "http://127.0.0.1:5000/status"
    data = {
    "status": "force"
    }
    response = requests.post(url, json=data)
    lyrics_text.delete(1.0, tk.END)
    lyrics_text.insert(tk.END, "Refreshing...")

root = tk.Tk()
root.title("lyrics")
root.geometry("400x1080")

root.configure(bg="#2c2c2c")
root.wm_attributes("-alpha", 0.7)
root.wm_attributes("-topmost", True)

minimized = False

def toggle_window():
    global minimized
    global last_maximised_width
    if not minimized:
        last_maximised_width = root.winfo_width()
        root.geometry("120x50+" + str(root.winfo_x()+root.winfo_width()-120) + "+" + str(root.winfo_y()))
        
        lyrics_text.pack_forget()
        scrollbar.pack_forget()
        refresh_button.config(state=tk.DISABLED)
        refresh_button.pack_forget()
        collapse_button.config(text="expand")
        minimized = True
    else:
        root.geometry(str(last_maximised_width) + "x1080+" + str(root.winfo_x()-last_maximised_width+root.winfo_width()) + "+" + str(root.winfo_y()))
        lyrics_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=20)
        
        collapse_button.config(text="collapse")
        minimized = False
        refresh_button.config(state=tk.NORMAL)
        refresh_button.pack(side="left", padx=5)

toolbar = tk.Frame(root, bg="#4a4a4a")
toolbar.pack(side="top", fill="x", padx=5, pady=5)

collapse_button = tk.Button(
    toolbar,
    text="collapse",
    bg="#4a4a4a",
    fg="white",
    command=toggle_window,
)
collapse_button.pack(side="right", padx=5)

refresh_button = tk.Button(
    toolbar,
    text="refresh",
    bg="#4a4a4a",
    fg="white",
    command=force_update,
)
refresh_button.pack(side="left", padx=5)

lyrics_text = tk.Text(root, bg="#2c2c2c", fg="white", wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 10))
scrollbar = tk.Scrollbar(root, command=lyrics_text.yview)
lyrics_text.config(yscrollcommand=scrollbar.set)
lyrics_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=20)

def update_lyrics():
    try:
        response = requests.get("http://127.0.0.1:5000/get_lyrics")
        data = response.json()
        current_lyrics = lyrics_text.get(1.0, tk.END).strip()
        if current_lyrics != data["lyrics"]:
            lyrics_text.config(state=tk.NORMAL)
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, data["lyrics"])
            lyrics_text.config(state=tk.DISABLED)
    except:
        pass
    root.after(1000, update_lyrics)

update_lyrics()
root.mainloop()
import tkinter as tk
from tkinter import ttk
from recommendation import get_recommendation

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation System")

# Create a label and entry widget for the movie title
title_label = ttk.Label(root, text='Enter a movie title:')
title_label.grid(column=0, row=0, padx=10, pady=10, sticky='w')
title_entry = ttk.Entry(root, width=30)
title_entry.grid(column=1, row=0, padx=10, pady=10, sticky='w')

# Create a label and listbox for the recommendations
recommendations_label = ttk.Label(root, text='Recommendations:')
recommendations_label.grid(column=0, row=1, padx=10, pady=10, sticky='w')
recommendations_listbox = tk.Listbox(root, width=70, height=10)
recommendations_listbox.grid(column=0,row=2,columnspan=3, padx=10, pady=10, sticky='w')

# Create a function to display the recommendations when the user enters a movie title
def display_recommendations():
    title = title_entry.get()
    recommendations = get_recommendation(title)
    recommendations_listbox.delete(0, tk.END)
    for recommendation in recommendations:
        recommendations_listbox.insert(tk.END, recommendation)
        
# Create a function to clear the recommendations listbox and the title entry field
def clear_recommendations():
    recommendations_listbox.delete(0, tk.END)
    title_entry.delete(0, tk.END)

# Create a button to display the recommendations
display_button = ttk.Button(root, text='Recommend', command=display_recommendations)
display_button.grid(column=2, row=0, padx=10, pady=10, sticky='w')

# Create a button to clear the recommendations listbox
clear_button = ttk.Button(root, text='Clear', command=clear_recommendations)
clear_button.grid(column=2, row=1, padx=10, pady=10, sticky='w')

# Bind the Enter key to the display_button
title_entry.bind('<Return>', lambda event: display_button.invoke())
# Start the main loop
root.mainloop()
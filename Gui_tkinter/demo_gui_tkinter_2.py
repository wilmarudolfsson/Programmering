import tkinter as tk

root = tk.Tk()

# Add labels at specified row and column.
# width to make all cells have same width independent of text length

row_0_column_0 = tk.Label(root,
                          text='1',
                          borderwidth=2,
                          relief="sunken",
                          width=20,
                          pady=30)
row_0_column_0.grid(row=0, column=0)

row_0_column_1 = tk.Label(root,
                          text='2',
                          borderwidth=2,
                          relief="sunken",
                          width=20,
                          pady=30)
row_0_column_1.grid(row=0, column=1)

row_1_column_0 = tk.Label(root,
                          text='3',
                          borderwidth=2,
                          relief="sunken",
                          width=20,
                          pady=30)
row_1_column_0.grid(row=1, column=0)

row_1_column_1 = tk.Label(root,
                          text='4',
                          borderwidth=2,
                          relief="sunken",
                          width=20,
                          pady=30)
row_1_column_1.grid(row=1, column=1)

row_2_column_0 = tk.Label(root,
                          text='5',
                          borderwidth=2,
                          relief="sunken",
                          width=20,
                          pady=30)
row_2_column_0.grid(row=2, column=0)

row_2_column_1 = tk.Label(root,
                          text='6',
                          borderwidth=2,
                          relief="sunken",
                          width=20,
                          pady=30)
row_2_column_1.grid(row=2, column=1)

row_3_column_0 = tk.Label(root,
                          text='7',
                          borderwidth=2,
                          relief="sunken",
                          width=20,
                          pady=30)
row_3_column_0.grid(row=3, column=0)

row_3_column_1 = tk.Label(root,
                          text='8',
                          borderwidth=2,
                          relief="sunken",
                          width=20,
                          pady=30)
row_3_column_1.grid(row=3, column=1)

root.mainloop()
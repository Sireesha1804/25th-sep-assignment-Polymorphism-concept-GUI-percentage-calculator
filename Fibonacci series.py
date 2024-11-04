import tkinter as tk

def generate_fibonacci(n):
    fibonacci_series = [0, 1]
    for i in range(2, n):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series[:n]

def show_fibonacci():
    n = int(entry.get())
    fibonacci_series = generate_fibonacci(n)
    result_label.config(text="Fibonacci Series: " + ", ".join(map(str, fibonacci_series)))

root = tk.Tk()
root.title("Fibonacci Series Generator")

# Input field for the number of terms
tk.Label(root, text="Enter number of terms:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Button to generate the Fibonacci series
generate_button = tk.Button(root, text="Generate", command=show_fibonacci)
generate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the GUI application
root.mainloop()
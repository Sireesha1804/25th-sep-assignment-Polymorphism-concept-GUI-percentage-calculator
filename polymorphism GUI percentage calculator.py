import tkinter as tk
from tkinter import messagebox

class Grade:
    def __init__(self, subjects):
        self.subjects = subjects

    def calculate_percentage(self):
       class GradeA(Grade):
        def calculate_percentage(self):
         total_marks = sum(self.subjects.values())
         return (total_marks / (len(self.subjects) * 100)) * 100

class GradeB(Grade):
    def calculate_percentage(self):
        total_marks = sum(self.subjects.values())
        return (total_marks / (len(self.subjects) * 80)) * 100

class GradeC(Grade):
    def calculate_percentage(self):
        total_marks = sum(self.subjects.values())
        return (total_marks / (len(self.subjects) * 60)) * 100

def __init__(self, subjects):
        self.subjects = subjects

def calculate_percentage(self):
       

 class GradeA (Grade):
    def calculate_percentage(self):
        total_marks = sum(self.subjects.values())
        return (total_marks / (len(self.subjects) * 100)) * 100

class GradeB(Grade):
    def calculate_percentage(self):
        total_marks = sum(self.subjects.values())
        return (total_marks / (len(self.subjects) * 80)) * 100

class GradeC(Grade):
    def calculate_percentage(self):
        total_marks = sum(self.subjects.values())
        return (total_marks / (len(self.subjects) * 60)) * 100
        


class GradeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Percentage Calculator")

        self.grade_var = tk.StringVar(value="A")

        # Dropdown for selecting grade

        tk.Label(root, text="Select Grade:").pack()
        self.grade_dropdown = tk.OptionMenu(root, self.grade_var, "A", "B", "C")
        self.grade_dropdown.pack()

        # Entry for subjects
        self.subject_entries = {}
        for i in range(1, 6):
            tk.Label(root, text=f"Subject {i} Marks:").pack()
            entry = tk.Entry(root)
            entry.pack()
            self.subject_entries[f"Subject {i}"] = entry

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate Percentage", command=self.calculate_percentage)
        self.calculate_button.pack()

    def calculate_percentage(self):
        # Get marks from entries
        marks = {}
        for subject, entry in self.subject_entries.items():
            try:
                marks[subject] = int(entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid marks for {subject}.")
                return

        # Create appropriate grade object and calculate percentage
        grade = self.grade_var.get()
        if grade == "A":
            grade_instance = GradeA(marks)
        elif grade == "B":
            grade_instance = GradeB(marks)
        elif grade == "C":
            grade_instance = GradeC(marks)

        percentage = grade_instance.calculate_percentage()
        messagebox.showinfo("Percentage", "The percentage for Grade {grade} is: {percentage:.2f}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculatorApp(root)
    root.mainloop()

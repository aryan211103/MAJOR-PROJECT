import tkinter as tk
from tkinter import ttk, messagebox

class StudentForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information Form")

        # GPA Entry
        self.gpa_label = tk.Label(root, text="GPA (Out of 4):")
        self.gpa_label.grid(row=0, column=0, padx=10, pady=5)
        self.gpa_entry = tk.Entry(root)
        self.gpa_entry.grid(row=0, column=1, padx=10, pady=5)

        # Bachelor's Degree Selection
        self.degree_label = tk.Label(root, text="Bachelor's Degree:")
        self.degree_label.grid(row=1, column=0, padx=10, pady=5)
        self.degree_options = [
            'Robotics', 'Computer Engineering', 'Mechanical Engineering',
            'Software Engineering', 'Information Technology',
            'Electrical Engineering', 'Chemical Engineering',
            'Data Science', 'Civil Engineering', 'Artificial Intelligence'
        ]
        self.degree_var = tk.StringVar()
        self.degree_menu = ttk.Combobox(root, textvariable=self.degree_var, values=self.degree_options)
        self.degree_menu.grid(row=1, column=1, padx=10, pady=5)

        # Skills Multiple Choice
        self.skills_label = tk.Label(root, text="Skills:")
        self.skills_label.grid(row=2, column=0, padx=10, pady=5)
        self.skills_options = [
            'Artificial Intelligence', 'Cloud Computing', 'Computer Networks',
            'Data Structures & Algorithms (DSA)', 'DevOps', 'Machine Learning',
            'Operating Systems', 'PostgreSQL', 'SQL', 'Web Development'
        ]
        self.skill_vars = []
        for idx, skill in enumerate(self.skills_options):
            var = tk.BooleanVar()
            self.skill_vars.append(var)
            chk = tk.Checkbutton(root, text=skill, variable=var)
            chk.grid(row=3 + idx // 2, column=idx % 2, padx=10, pady=2)

        # Languages Multiple Choice
        self.languages_label = tk.Label(root, text="Languages:")
        self.languages_label.grid(row=8, column=0, padx=10, pady=5)
        self.languages_options = ['C', 'C++', 'Java', 'JavaScript', 'Python', 'R', 'Ruby']
        self.language_vars = []
        for idx, language in enumerate(self.languages_options):
            var = tk.BooleanVar()
            self.language_vars.append(var)
            chk = tk.Checkbutton(root, text=language, variable=var)
            chk.grid(row=9 + idx // 2, column=idx % 2, padx=10, pady=2)

        # Job Experience Entry
        self.job_exp_label = tk.Label(root, text="Job Experience (Years):")
        self.job_exp_label.grid(row=12, column=0, padx=10, pady=5)
        self.job_exp_entry = tk.Entry(root)
        self.job_exp_entry.grid(row=12, column=1, padx=10, pady=5)

        # Extra Curricular Entry
        self.extra_label = tk.Label(root, text="Extra Curricular Activities:")
        self.extra_label.grid(row=13, column=0, padx=10, pady=5)
        self.extra_entry = tk.Entry(root)
        self.extra_entry.grid(row=13, column=1, padx=10, pady=5)

        # Internship Duration Entry
        self.internship_label = tk.Label(root, text="Internship Duration (Months):")
        self.internship_label.grid(row=14, column=0, padx=10, pady=5)
        self.internship_entry = tk.Entry(root)
        self.internship_entry.grid(row=14, column=1, padx=10, pady=5)

        # Research Papers Entry
        self.research_label = tk.Label(root, text="Number of Research Papers:")
        self.research_label.grid(row=15, column=0, padx=10, pady=5)
        self.research_entry = tk.Entry(root)
        self.research_entry.grid(row=15, column=1, padx=10, pady=5)

        # Submit Button
        self.submit_btn = tk.Button(root, text="Submit", command=self.submit)
        self.submit_btn.grid(row=16, column=0, columnspan=2, padx=10, pady=10)

    def submit(self):
        # Collect data from form
        gpa = self.gpa_entry.get()
        degree = self.degree_var.get()
        job_exp = self.job_exp_entry.get()
        extracurricular = self.extra_entry.get()
        internship_duration = self.internship_entry.get()
        research_papers = self.research_entry.get()

        # Collect skills and languages
        skills = [skill for idx, skill in enumerate(self.skills_options) if self.skill_vars[idx].get()]
        languages = [lang for idx, lang in enumerate(self.languages_options) if self.language_vars[idx].get()]

        # Display collected data (You can modify this part to match with dataset)
        student_data = f"""
        GPA: {gpa}
        Bachelor's Degree: {degree}
        Job Experience: {job_exp} years
        Extra Curricular Activities: {extracurricular}
        Internship Duration: {internship_duration} months
        Research Papers: {research_papers}
        Skills: {", ".join(skills)}
        Languages: {", ".join(languages)}
        """
        messagebox.showinfo("Student Information", student_data)


if __name__ == "__main__":
    root = tk.Tk()
    form = StudentForm(root)
    root.mainloop()

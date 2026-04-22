import matplotlib.pyplot as plt
students = ["Arun","Bina","Chitra","Divya","Esha"]
marks = [75,85,90,70,95]
plt.plot(students,marks,marker = 'o')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()  
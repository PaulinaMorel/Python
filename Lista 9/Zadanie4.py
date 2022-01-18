import matplotlib.pyplot as plt
     
names   = ["C", "Java", "Python", "C++", "C#", "Visual Basic", "Java Script", "PHP", "R", "Groovy"]
values  = [17.38, 11.96, 11.72, 7.56, 3.95, 3.84, 2.20, 1.99, 1.90, 1.84]

plt.figure(figsize=(12, 5))
plt.bar(names, values)
plt.xlabel("Języki programowania")
plt.ylabel("Udział procętowy")
plt.show()
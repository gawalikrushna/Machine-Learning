import matplotlib.pyplot as plt

def main():
    language = ["c","C++","Java","Python"]
    students = [30,40,35,55]

    plt.bar(
        language,
        students,
        width= 0.6,            # width of bar
        edgecolor = "black" ,  # border colours of bar
        linewidth = 1,         # width of bar border
        alpha = 0.8,           # trancperance 0.0 to 1.0
        label = "Students"     # legend test
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of students")

    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()
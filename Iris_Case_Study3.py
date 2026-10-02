from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris Classification Case Study")

    Dataset = load_iris()

    # Meta data of the dataset

    print("Independent variables are : ")
    print(Dataset.feature_names)
    print("Length of independent variables : ",len(Dataset.feature_names))

    print("Dependent variables are : ")
    print(Dataset.target_names)
    print("Length of dependent variables : ",len(Dataset.target_names))


if __name__ == "__main__":
    main()  
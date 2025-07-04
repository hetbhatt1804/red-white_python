import numpy as np
print("Welcome to the numpy analyzer!")
print("1. create a numpy array")
print("2 perform mathematical operations")
print("3 combine or split arrays")
print("4. search, sort, or filter arrays")
print("5. compute aggregates and statistics")
print("6. exit")

class Numpyanalyzer:
    def __init__(self):
        self.array = None

    def create_array(self):
        print("\nArray Creation:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        c = input("Enter your choice: ")
        if c == '1':
            d = input("Enter elements separated by space: ").split()
            elements = []
            for i in d:
                elements.append(int(i))

            self.array = np.array(elements)
            print("Array created successfully:\n", self.array)

        elif c == '2':
            r = int(input("Enter number of rows: "))
            col = int(input("Enter number of columns: "))
            d = input(f"Enter {r * col} elements separated by space: ").split()
            elements = []
            for i in d:
                elements.append(int(i))
            self.array = np.array(elements).reshape(r, col)
            print("Array created ", self.array)

            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            s = input("Enter your choice: ")

            if s == '1':
                ri = int(input("Enter row index: "))
                ci = int(input("Enter column index: "))
                print("Element at position:", self.array[ri, ci])

            elif s == '2':
                rr = input("Enter row range start:end: ")
                cr = input("Enter column range start:end: ")
                rs, re = rr.split(":")
                cs, ce = cr.split(":")
                rs = int(rs)
                re = int(re)
                cs = int(cs)
                ce = int(ce)
                print("Sliced Array:\n", self.array[rs:re, cs:ce])

        elif c == '3':
            d1 = int(input("Enter first dimension: "))
            d2 = int(input("Enter second dimension: "))
            d3 = int(input("Enter third dimension: "))
            d = input(f"Enter {d1*d2*d3} elements separated by space: ").split()
            elements = []
            for i in d:
                elements.append(int(i))
            self.array = np.array(elements).reshape(d1, d2, d3)
            print("Array created successfully:", self.array)

    def perform_math(self):
        print("Mathematical Operations:")
        print("1 Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        c = input("Enter your choice: ")

        d = input(f"Enter {self.array.size} elements separated by space: ").split()
        elements = []
        for i in d:
            elements.append(int(i))
        arr2 = np.array(elements).reshape(self.array.shape)

        print("original Array:", self.array)
        print("second Array:", arr2)

        if c == '1':
            print("result of addition:", self.array + arr2)
        elif c == '2':
            print("result of subtraction:", self.array - arr2)
        elif c == '3':
            print("result of multiplication:", self.array * arr2)
        elif c == '4':
            print("result of division:", self.array / arr2)

    def combine_split(self):
        print("1. combine arrays")
        print("2. split array")
        c = input("enter your choice: ")

        if c == '1':
            d = input(f"enter {self.array.size} elements separated by space: ").split()
            elements = []
            for i in d:
                elements.append(int(i))
            arr2 = np.array(elements).reshape(self.array.shape)
            combined = np.vstack((self.array, arr2))
            print("combined array ", combined)

        elif c == '2':
            axis = int(input("Enter axis to split on : "))
            print("Split Arrays:\n", np.split(self.array, 2, axis=axis))

    def search_sort_filter(self):
        print("\n1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        c = input("Enter your choice: ")

        if c == '1':
            v = int(input("Enter value to search: "))
            ind = np.where(self.array == v)
            print("Value found at indices:", ind)
        elif c == '2':
            print("Sorted Array:", np.sort(self.array, axis=-1))
        elif c == '3':
            v = int(input("Enter value to filter greater than: "))
            print("Filtered Values:", self.array[self.array > v])

    def aggregates_statistics(self):
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        c = input("Enter your choice: ")

        if c == '1':
            print("Sum:", np.sum(self.array))
        elif c == '2':
            print("Mean:", np.mean(self.array))
        elif c == '3':
            print("Median:", np.median(self.array))
        elif c == '4':
            print("Standard Deviation:", np.std(self.array))
        elif c == '5':
            print("Variance:", np.var(self.array))

analyzer = Numpyanalyzer()

while True:
    choice = input("\nEnter your choice: ")

    if choice == '1':
        analyzer.create_array()
    elif choice == '2':
        analyzer.perform_math()
    elif choice == '3':
        analyzer.combine_split()
    elif choice == '4':
        analyzer.search_sort_filter()
    elif choice == '5':
        analyzer.aggregates_statistics()
    elif choice == '6':
        print("Thank you for using the NumPy Analyzer!\nGoodbye!")
        break
    else:
        print("Invalid choice, try again.")
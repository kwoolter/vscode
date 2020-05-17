import package1 as p1
import matplotlib.pyplot as plt
import pandas as pd
import random

def main():
    print("Hello World")

    p1.f1()
    p1.f2()

    df = pd.DataFrame([], columns=list("XYZ"))

    a = p1.A("Keith")
    
    for i in range(0,10):
        #a.move(p1.A.VECTOR_NORTH, 2)
        a.move(random.choice(p1.A.VALID_VECTORS), random.randint(1,3))
        df2 = pd.DataFrame([list(a.pos)], columns=list("XYZ"))
        df = df.append(df2, ignore_index=True)

    print(df)

    ax = plt.gca()
    df.plot(kind="scatter", x="X", y="Y", ax=ax)
    plt.show()

    input("Press Enter to finish")


if __name__ == "__main__":
    main()
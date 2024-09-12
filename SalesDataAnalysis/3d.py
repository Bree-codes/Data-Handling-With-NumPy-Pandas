import numpy as np


if __name__ == "__main__":
    dArray = np.array([
        [[1,2,3,4,5], [5,4,3,2,1]],
        [[6,7,8,9,10], [10,9,8,7,6]]
    ])

    ans = np.sum(dArray, axis=2)

    print(f"3D sum {ans}.")

    ans2 = np.sum(ans, axis=1)

    print(f"2D sum {ans2}.")

    ans3 = np.sum(ans2)

    print(f"ANS {ans3}")
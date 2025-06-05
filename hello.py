import numpy as np
import pandas as pd

def main():
    # Example usage of numpy and pandas
    arr = np.array([1, 2, 3])
    df = pd.DataFrame({'A': arr, 'B': arr * 2})
    print(df)

if __name__ == "__main__":
    main()
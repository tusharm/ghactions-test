import sys
import pandas  as pd

if __name__ == '__main__':
    for i in sys.path:
        print(i)    

    print('Pandas version: ' + pd.__version__)
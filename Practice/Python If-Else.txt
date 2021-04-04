import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    print('Not Weird' if (n % 2 == 0 and (n > 20 or 2 < n < 5)) else 'Weird')
    
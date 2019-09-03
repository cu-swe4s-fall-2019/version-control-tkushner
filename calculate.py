#use add and divide with input arguments
#first print the sum of the values, then the first divided by the second
import argparse
import sys
import math_lib as ml




if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ', sys.argv[0], '[first value] [second value]')
        sys.exit(2)

    x1 = int(sys.argv[1])
    x2 = int(sys.argv[2])

    print('the sum is: '+str(ml.add(x1,x2)))
    print('first/second is: '+ str(ml.div(x1,x2)))

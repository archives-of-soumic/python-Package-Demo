import os
import sys
import os.path

CURRENT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
BASE_PATH = os.path.abspath(os.path.join(CURRENT_PATH, os.pardir))

if BASE_PATH not in sys.path:
    sys.path.insert(0, BASE_PATH)

from measure import metrics 
import measure.norms

if __name__ == "__main__":
    print(CURRENT_PATH)
    print(BASE_PATH) 
    metrics.metric(1)
    measure.norms.norms()
    pass 

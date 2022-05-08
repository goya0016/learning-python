import cowsay
import sys
from sayings import goodbye
if len(sys.argv) == 2:
    cowsay.cow('Hello, ' + sys.argv[1])
    goodbye(sys.argv[1])
    # cowsay.trex('Hello, ' + sys.argv[1])

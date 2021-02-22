import os
import sys
from check_clients import check_clients
from utils import get_length


# Get Files
masterFile = sys.argv[1]
outputFileName = os.path.splitext(masterFile)[0] + "_modified.csv"

# Track the initial length of the master file
initialLength = get_length(masterFile)

clients = check_clients(masterFile, outputFileName, initialLength)

print("Clients: " + clients)
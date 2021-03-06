class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def mod(x,m):
    return(str(x%m))

exString = "#"

for i in range(1000000):
    print(bcolors.OKBLUE + exString*114 + bcolors.BOLD)
    print(bcolors.HEADER + exString*114 + bcolors.BOLD)
    print(bcolors.OKGREEN + exString*114 + bcolors.BOLD)
    print(bcolors.WARNING + exString*114 + bcolors.BOLD)

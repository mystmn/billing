class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def msg(arg="", text=""):
        print bcolors.arg + text + bcolors.ENDC
#print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
#print bcolors.OKGREEN + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
#print bcolors.OKBLUE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
#print bcolors.HEADER + "Warning: No active frommets remain. Continue?" + bcolors.ENDC

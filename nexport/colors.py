class color:
    DEFAULT =       '\033[39m'
    BLACK =         '\033[30m'
    RED =           '\033[31m'
    GREEN =         '\033[32m'
    YELLOW =        '\033[33m'
    BLUE =          '\033[34m'
    MAGENTA =       '\033[35m'
    CYAN =          '\033[36m'
    LIGHTGRAY =     '\033[37m'
    DARKGRAY =      '\033[90m'
    LIGHTRED =      '\033[91m'
    LIGHTGREEN =    '\033[92m'
    LIGHTYELLOW =   '\033[93m'
    LIGHTBLUE =     '\033[94m'
    LIGHTMAGENTA =  '\033[95m'
    LIGHTCYAN =     '\033[96m'
    WHITE =         '\033[97m'

    def test():
        print(f"{color.DEFAULT}█{color.BLACK}█{color.DARKGRAY}█{color.LIGHTGRAY}█{color.WHITE}█")
        print(f"{color.RED}█{color.GREEN}█{color.YELLOW}█{color.BLUE}█{color.MAGENTA}█{color.CYAN}█")
        print(f"{color.LIGHTRED}█{color.LIGHTGREEN}█{color.LIGHTYELLOW}█{color.LIGHTBLUE}█{color.LIGHTMAGENTA}█{color.LIGHTCYAN}█{color.DEFAULT}")
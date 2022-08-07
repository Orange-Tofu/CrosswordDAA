import termcolor
from trie import Trie
import copy
from rich import print, pretty
from subprocess import call
import sys
import os
import pyfiglet
from rich.console import Console
import time
from rich.style import Style
from rich.progress import track

danger_style = Style(color='red', blink=True, bold=True)
flagf = 1
console = Console()
trie = Trie()


def check(grid, trie, i, j, i_diff, j_diff, moves):
    n, m = len(grid), len(grid[0])
    node = trie
    start_i, start_j = i, j
    substring = ''
    flag = 0
    l = 0
    while 0 <= i < n and 0 <= j < m:
        if grid[i][j] not in node.children:
            break
        substring += grid[i][j]
        node = node.children[grid[i][j]]
        if node.is_end:
            moves.append(((start_i, start_j), (i, j)))
            si, sj = start_i, start_j
            if flagf:
                strf = '[+] Found  ' + substring + '  at: ' + str(((start_i, start_j), (i, j)))
                console.print(strf, style='#00ff00')
                time.sleep(.4)
            l = len(substring)
            trie.delete(substring)
            flag = 1
        i += i_diff
        j += j_diff
    if (flag):
        n, m = len(grid), len(grid[0])
        x = 0
        while 0 <= si < n and 0 <= sj < m and x < l:
            g[si][sj] = "-"
            x += 1
            si += i_diff
            sj += j_diff


def solve(grid, words):
    moves = []
    trie = Trie().build(words)
    n, m = len(grid), len(grid[0])
    for i in track(range(n), description="[bold green]Solving...", auto_refresh=False, console=console):
        # for i in range(n):
        for j in range(m):
            if grid[i][j] in trie.children:
                for i_diff, j_diff in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    check(grid, trie, i, j, i_diff, j_diff, moves)
    return moves, trie


def display():
    move, trie = solve(grid, words)
    left = trie.get_strings()
    if (left == []):
        console.print("\n[+] SUCCESSFULLY FOUND ALL THE WORDS!", style='#00ff00')
    else:
        console.print("\n[-] COULDN'T FIND: " + str(left) + " IN GRID!", style='red')
        console.print("[-] CHECK THE INPUT FILES AND RETRY!", style='red')
    for i in range(n):
        console.print()
        for j in range(n):

            if (g[i][j] == "-"):
                console.print(grid[i][j], style='bold blue', end=' ')

            else:
                console.print(grid[i][j], style='bold white', end=' ')
    exit()


if __name__ == '__main__':
    pretty.install()
    _ = call('clear' if os.name == 'posix' else 'cls')
    ascii_banner = pyfiglet.figlet_format("WordSearchSolver", font='slant', width=110)
    termcolor.cprint(ascii_banner, 'cyan')
    console.print("[magenta underline]Made by:[/magenta underline] Janesh    Akash    Ayushi    Anujna",
                  style='bold green')
    print()
    console.rule("[bold blue]STARTING")
    print()
    n = 0
    words = set()
    with console.status("[bold blue]Getting Input ready"):
        time.sleep(1)
        if (len(sys.argv) not in [2, 3, 4]):
            console.print("[!!} FATAL: MISSING SYSTEM ARGUMENTS!!\n[!!} Aborting!", style=danger_style)
            console.print("\n[-] Tip: Run 'python3 Solver.py -h' ", style='bold green underline')
            exit()


        elif (sys.argv[1] == '-h'):
            console.rule('[bold red]Help Manual')
            styleh = Style(color='magenta', italic=True)
            console.print()
            console.print("Welcome to Word Search Solver", style='italic cyan', justify='center')
            console.print()
            console.print("NOTE: For the tool to run the required library dependencies should be installed.",
                          style=styleh)
            console.print(
                "[yellow]This can be done manually or run 'pip3 install -r requirements.txt' to install/check if all the requirements are present")
            console.print("NOTE: the requirement.txt file is present with the tool", style=styleh)
            console.print()
            console.print('[bold white]-h       :[/bold white]\tHelp manual', style=styleh)
            console.print('[bold white]<sysarg1>:[/bold white]\tText file with n x n grid.', style=styleh)
            console.print(
                '[bold white]<sysarg2>:[/bold white]\tText file containing words (word lenght to be less than the size of the grid).',
                style=styleh)
            console.print(
                '[bold white]<sysarg3>:[/bold white]\t[OPTIONAL] -v: verbose (default)\n\t\t           -f: Fast (less animation and faster | recommended for lager file)',
                style=styleh)
            exit()
        elif (len(sys.argv) == 4):
            if (sys.argv[3] != '-f'):
                console.print("[!!] FATAL: INVALID ARGUMENT\n[!!] Aborting! ", style=danger_style)
                console.print("[-] Tip: Run 'python3 Solver.py -h' ", style='bold green underline')
                exit()
            flagf = 0
            gridFile = sys.argv[1]
            with open(gridFile, 'r') as f:
                grid = []
                n = len(f.readline().strip().split())
                f.seek(0)
                if (len(f.readlines()) == n):
                    f.seek(0)
                    for i in range(n):
                        line = f.readline().strip("\n").split()
                        grid.append(line)
                    console.print("\n[+] Grid parsed!", style='#00ff00')
                    g = copy.deepcopy(grid)
                else:
                    console.print("[!!] FATAL: THE GRID FILE IS INVALID\n[!!] Aborting! ", style=danger_style)
                    console.print("[-] Tip: Run 'python3 Solver.py -h' ", style='bold green underline')

                    exit()
            wordfile = sys.argv[2]
            with open(wordfile, 'r') as f2:
                word = []
                l = len(f2.readlines())
                f2.seek(0)
                for i in range(l):
                    word.append(f2.readline().strip('\n').upper())
                word.sort(key=len, reverse=True)
                lw = len(word[0])
                if (lw > n):
                    console.print("[!!] FATAL: THE WORD LENGTH IS LARGER THAN THE GRID\n[!!] Aborting!",
                                  style=danger_style)
                    console.print("[-] Tip: Run 'python3 Solver.py -h' ", style='bold green underline')

                    exit()
                words.update(word)
                console.print("\n[+] Wordlist parsed !", style='#00ff00')

        else:
            gridFile = sys.argv[1]
            with open(gridFile, 'r') as f:
                grid = []
                n = len(f.readline().strip().split())
                f.seek(0)
                if (len(f.readlines()) == n):
                    f.seek(0)
                    for i in range(n):
                        line = f.readline().strip("\n").split()
                        grid.append(line)
                    console.print("\n[+] Grid parsed!", style='#00ff00')
                    g = copy.deepcopy(grid)
                else:
                    console.print("[!!] FATAL: THE GRID FILE IS INVALID\n[!!] Aborting! ", style=danger_style)
                    console.print("[-] Tip: Run 'python3 Solver.py -h' ", style='bold green underline')

                    exit()
            time.sleep(.5)
            wordfile = sys.argv[2]
            with open(wordfile, 'r') as f2:
                l = len(f2.readlines())
                f2.seek(0)
                word = []
                for i in range(l):
                    word.append(f2.readline().strip('\n').upper())
                word.sort(key=len, reverse=True)
                lw = len(word[0])
                if (lw > n):
                    console.print("[!!] FATAL: THE WORD LENGTH IS LARGER THAN THE GRID\n[!!] Aborting! ",
                                  style=danger_style)
                    console.print("[-] Tip: Run 'python3 Solver.py -h' ", style='bold green underline')

                    exit()
                words.update(word)
                console.print("\n[+] Wordlist parsed! ", style='#00ff00')
                time.sleep(1)

    console.rule('[bold blue]SOLVING')
    if (flagf):
        display()
    time.sleep(1)
    display()

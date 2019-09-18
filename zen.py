
from termcolor import colored, cprint
from random import *
from predefined_shapes import *

colors = {
    0:'grey',
    1:'red',
    2:'green',
    3:'yellow',
    4:'blue',
    5:'magenta',
    6:'cyan',
    7:'white',
}
back_colors = {
    0:'on_grey',
    1:'on_red',
    2:'on_green',
    3:'on_yellow',
    4:'on_blue',
    5:'on_magenta',
    6:'on_cyan',
    7:'on_white',
}

#class Board

#class Piece

def solution(b_file, s_file):
    myboard = []
    with open(b_file) as f:
        lines = f.read().splitlines()
    for l in lines:
        myrow = list(map(int, l.split()))
        myboard.append(myrow)
    #myboard = [
    #        [1,1,1,1,1,1,1,1],
    #        [1,1,1,1,1,1,1,1],
    #        [1,1,1,1,1,1,0,0],
    #        [1,1,1,1,1,1,0,0],
    #        [1,1,1,1,0,0,0,0],
    #        [1,1,0,0,0,0,0,0],
    #        [1,1,0,0,0,0,0,0],
    #        ]

    pieces = []
    with open(s_file) as f:
        lines = f.read().splitlines()
    for s in lines:
        pieces.append(eval(s))
    #pieces = [Ls_flipxy, L_m90, L_m90_flipy, L_flipx, I_3_1, L_90, L_flipy, I_3_1, T_m90, ___]#, T_90, L_flipx, L_flipy, L, T_m90, __, Ls_flipx, Ls_flipy]
    #shuffle(pieces)
    #print(myboard)
    #print(pieces)

    if not myboard or not myboard[0]: 
        return False

    M = len(myboard)
    N = len(myboard[0])
    #print(M,N)

    ### make first board
    ### or make first piece

    ### make board
    def is_clear(myboard):
        for i,row in enumerate(myboard):
            for j,n in enumerate(row):
                if n==-1:
                    return False
        return True

    def is_valid(p,i,j):
        for x,row in enumerate(p):
            for y,n in enumerate(row):
                if n==0 and not (0<=i+x<M and 0<=j+y<N):
                    return False
                elif n==0 and myboard[i+x][j+y]!=1:
                    return False
        return True

    def update_board(k,p,i,j):
        for x,row in enumerate(p):
            for y,n in enumerate(row):
                if n==0: myboard[i+x][j+y]=k
        return

    def revoke_board(p,i,j):
        for x,row in enumerate(p):
            for y,n in enumerate(row):
                if n==0: myboard[i+x][j+y]=1
        return

    def print_board(myboard):
        for row in myboard:
            for n in row:
                if n==0:
                    print('{:3} '.format(n),end='')
                else:
                    cprint('{:3} '.format(n),colors[(n+3)%7],back_colors[(n+1)%7],end='')
            print()
        return

    def generate_invalid(m,n,s):
        return

    def get_pattern(myboard):
        #for i in range(M):
        #    for j in range(N):
        #        if myboard[i][j]==1:
        return


    def check_bottleneck(myboard):
        #get_pattern(myboard)
        return True

    used = set()
    it = [0]
    def make_board(i,j):
        it[0] += 1
        if it[0]%1000000==0: print(f'Iteration {it[0]}')
        if it[0]%10000000==0: print_board(myboard)
        
        if not check_bottleneck(myboard): return False

        if i==M:
            #print('moved to last')
            #print(used)
            #print_board(myboard)
            if len(used)==len(pieces) and is_clear(myboard):
                print_board(myboard)
                return True
            else:
                return False

        di,jj = divmod(j+1,N)
        ii = i+di
        #if myboard[i][j]!=1:
        if 0:
            if make_board(ii,jj):
                return True
            else:
                return False
        else: # make valid board
            for k,p in enumerate(pieces):
                if k in used: continue
                if is_valid(p,i,j):
                    used.add(k)
                    update_board(k+2,p,i,j)
                    if make_board(ii,jj):
                        return True
                    else:
                        revoke_board(p,i,j)
                        used.remove(k)
            if make_board(ii,jj):
                return True
            else:
                return False

    return make_board(0,0)

if __name__ == '__main__':
    import sys
    solved = solution(sys.argv[1],sys.argv[2])
    print(solved)


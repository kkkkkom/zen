
from termcolor import colored, cprint
from random import *

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

def solution():
    T_flipy = [
            [1,0,1],
            [0,0,0],
            ]
    Z_flipx = [
            [1,0,0],
            [0,0,1],
            ]
    T_90 = [
            [1,0],
            [0,0],
            [1,0],
            ]
    L_flipx = [
            [1,0],
            [1,0],
            [0,0],
            ]
    L_flipy = [
            [0,0],
            [0,1],
            [0,1],
            ]
    L = [
            [0,1],
            [0,1],
            [0,0],
            ]
    L_m90 = [
            [1,1,0],
            [0,0,0],
            ]
    L_90 = [
            [0,0,0],
            [0,1,1],
            ]
    L_m90_flipy = [
            [0,0,0],
            [1,1,0],
            ]
    T_m90 = [
            [0,1],
            [0,0],
            [0,1],
            ]
    Ls_flipx = [
            [1,0],
            [0,0],
            ]
    Ls_flipy = [
            [0,0],
            [0,1],
            ]
    Ls_flipxy = [
            [0,0],
            [1,0],
            ]
    T = [
            [0,0,0],
            [1,0,1],
            ]
    I_2_1 = [
            [0],
            [0],
            ]
    I_3_1 = [
            [0],
            [0],
            [0],
            ]
    _ = [[0]]
    __ = [
            [0,0],
            ]
    ___ = [
            [0,0,0],
            ]
    I_3_2 =[
            [0,0],
            [0,0],
            [0,0],
            ]
    myboard = [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0],
            ]
    #myboard = [
    #        [0,0,1,1,0,0,0,0],
    #        [0,1,1,1,0,0,0,0],
    #        [0,0,1,1,1,0,0,0],
    #        [0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0],
    #        ]
    #pieces = [T_flipy, Z_flipx, T_90, L_flipx, L_flipy, L, T_m90, __, Ls_flipx, Ls_flipy]
    pieces = [Ls_flipxy, L_m90, L_m90_flipy, L_flipx, I_3_1, L_90, L_flipy, I_3_1, T_m90, ___]#, T_90, L_flipx, L_flipy, L, T_m90, __, Ls_flipx, Ls_flipy]
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

    used = set()
    def make_board(i,j):
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
    solved = solution()
    print(solved)


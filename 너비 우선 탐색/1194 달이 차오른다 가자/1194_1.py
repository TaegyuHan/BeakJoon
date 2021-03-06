"""
    Solution code for "BaekJoon 달이 차오른다 가자".

    - Problem link: https://www.acmicpc.net/problem/1194
"""
from sys import stdin as input
from collections import deque
import sys; sys.setrecursionlimit(2500)
input = open('./1194.txt')


class M:
    """ 이동 """
    GO = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]


class D:
    """ 데이터 """
    ROW, COL = map(int, input.readline().split())
    board = []
    visited = []
    move_count = 0
    key = 0
    my_row = 0
    my_col = 0

    WALL = "#"
    ME = "0"
    GROUND = "."
    EXIT = "1"

    keys = {
        "a": 1,
        "b": 2,
        "c": 4,
        "d": 8,
        "e": 16,
        "f": 32
    }

    @staticmethod
    def input_board():
        """ 판 데이터 받기 """
        for row in range(D.ROW):
            tmp = list(input.readline().strip())
            D.board.append(tmp)
            for col in range(D.COL):
                if tmp[col] == D.ME:
                    D.my_row, D.my_col = row, col

    @staticmethod
    def init_vistied():
        """ 방문 처리 초기화 """
        D.visited = [[[False] * D.COL for _ in range(D.ROW)] for _ in range(64)]

class P:

    def _show_board(self, board):
        """ 판 확인하기 """
        for row in board:
            print(*row)
        print()

    def _check_key(self, door, key):
        """ 키 존재 확인하기 """
        if D.keys[door.lower()] & key:
            return False
        return True

    def _BFS(self):
        """ BFS 탐색 """
        D.init_vistied()
        move_count = 0
        keys = 0
        q = deque([(D.my_row, D.my_col, move_count, keys)])

        while q:
            crow, ccol, cmove, ckeys = q.popleft()
            if D.visited[ckeys][crow][ccol]: continue
            D.visited[ckeys][crow][ccol] = True
            print(crow, ccol)

            for trow, tcol in M.GO:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL): continue
                print(nrow, ncol)
                if (state := D.board[nrow][ncol]) == D.WALL: continue
                if state.isupper() and self._check_key(state, keys): continue
                # 키 얻음
                if state.islower():
                    q.append((nrow, ncol, cmove + 1, ckeys | D.keys[D.board[nrow][ncol]]))
                    continue
                #
                if D.board[nrow][ncol] == D.EXIT:
                    D.move_count += (cmove + 1)
                    print(D.move_count)
                    exit()

                q.append((nrow, ncol, cmove + 1, ckeys))

        return False

    def run(self) -> None:
        D.input_board()

        while self._BFS():
            pass

        print(-1)

if __name__ == '__main__':
    P = P()
    P.run()
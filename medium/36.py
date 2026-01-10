class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        line_x = defaultdict(set)
        line_y = defaultdict(set)
        groups = defaultdict(set)

        for i in range(ROWS):
            for j in range(COLS):
                val = board[i][j]
                
                # ignorando os pontinhos (vazio)
                if val == ".":
                    continue

                # validacao da linha
                if val in line_x[i]:
                    return False
                line_x[i].add(val)

                # validacao da coluna
                if val in line_y[j]:
                    return False
                line_y[j].add(val)

                leader_i = i - (i % 3)
                leader_j = j - (j % 3)

                leader = (leader_i, leader_j)       

                if val in groups[leader]:
                    return False
                groups[leader].add(val)     

        return True  






        






        


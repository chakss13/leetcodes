class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            seen1 = set()
            row = board[i]
            column = [board[j][i] for j in range(9)]
            for val in row:
                if val == '.':
                    continue
                elif val in seen or val not in { '1', '2', '3', '4','5', '6', '7', '8', '9'}:
                    return False
                seen.add(val)

            for val1 in column:
                if val1 == '.':
                    continue 
                elif val1 in seen1 or val1 not in { '1', '2', '3', '4','5', '6', '7', '8', '9'}:
                    return False
                seen1.add(val1)
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                box_seen = set()
                for i in range(3):
                    for j in range(3):
                        val2 = board[box_row+i][box_col+j]
                        if val2 == '.':
                            continue 
                        elif val2 in box_seen or val2 not in { '1', '2', '3', '4','5', '6', '7', '8', '9'}:
                            return False
                        box_seen.add(val2)

        
        return True

        
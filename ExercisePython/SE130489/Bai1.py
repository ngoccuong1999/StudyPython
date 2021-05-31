size = 8
solutions = 0
position = [-1] * size
# dat queen
targetRow = 0
if targetRow == size:
    self.showFullBaz(positions)
    self.solutions += 1
else:
    for column in range(self.size):
        if self.check_place(positions, target_row, column):
            positions[target_row] = column
            self.put_queen(positions, target_row + 1)
print("Found", self.solutions, "solutions.")

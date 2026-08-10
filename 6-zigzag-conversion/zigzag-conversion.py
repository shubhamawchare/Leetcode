class Solution(object):
    def convert(self, s, numRows):

        # Special case
        if numRows == 1 or numRows >= len(s):
            return s

        # Create one string for each row
        rows = [""] * numRows

        current_row = 0
        direction = 1

        # Process every character
        for char in s:

            # Add character to current row
            rows[current_row] += char

            # Change direction at top and bottom
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            # Move to next row
            current_row += direction

        # Combine all rows
        return "".join(rows)
from manim import *

class FibonacciTabulation(Scene):
    def construct(self):
        # Title
        title = Text("Dynamic Programming: Fibonacci (Tabulation)").to_edge(UP)
        self.play(Write(title))

        # Create table headers
        headers = ["Index", "F(0)", "F(1)", "F(2)", "F(3)", "F(4)", "F(5)", "F(6)", "F(7)", "F(8)"]
        header_row = VGroup(*[Text(header).scale(0.6) for header in headers]).arrange(RIGHT, buff=0.8)
        header_row.to_edge(UP, buff=1.5)
        
        self.play(FadeIn(header_row))

        # Create the grid to hold Fibonacci values
        grid = VGroup()
        for i in range(3):  # Three rows: Header, intermediate, and final
            row = VGroup()
            for j in range(10):  # Columns: Index 0 to 9
                cell = Square(side_length=0.6)
                if i == 0:  # Fill header row with index numbers
                    cell_text = Text(str(j)).scale(0.5) if j > 0 else Text("").scale(0.5)
                else:
                    cell_text = Text("").scale(0.5)
                cell_text.move_to(cell.get_center())
                cell_group = VGroup(cell, cell_text)
                row.add(cell_group)
            row.arrange(RIGHT, buff=0.1)
            grid.add(row)
        grid.arrange(DOWN, buff=0.1)
        grid.next_to(header_row, DOWN, buff=0.5)
        
        self.play(Create(grid))

        # Define Fibonacci sequence to fill
        fib = [0, 1] + [0] * 8  # Start with two known values

        # Animation of filling the table
        for i in range(2, len(fib)):
            fib[i] = fib[i - 1] + fib[i - 2]

            # Highlight the previous two cells used for calculation
            self.play(
                grid[1][i - 1][0].animate.set_fill(ORANGE, opacity=0.5),
                grid[1][i - 2][0].animate.set_fill(ORANGE, opacity=0.5),
            )

            # Add the calculated value to the table
            new_value = Text(str(fib[i])).scale(0.5).move_to(grid[1][i][0].get_center())
            self.play(FadeIn(new_value))
            grid[1][i].add(new_value)

            # Reset colors
            self.play(
                grid[1][i - 1][0].animate.set_fill(WHITE, opacity=1),
                grid[1][i - 2][0].animate.set_fill(WHITE, opacity=1),
            )

        # Final display of the filled table
        self.play(Indicate(grid, scale_factor=1.1))
        self.wait(2)

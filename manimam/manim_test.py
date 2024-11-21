from manim import *

class CircleToYankee(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(color=BLUE, fill_opacity=0.5)
        circle.set_height(2)  # Set the size of the circle

        # Display the circle on the screen
        self.play(Create(circle))
        self.wait(1)

        # Transform the circle into the word "Yankee"
        text = Text("Niegarian Prince's Money Bag", font_size=72, color=RED)
        self.play(Transform(circle, text))
        self.wait(2)

from manim import *

class RollingBallToCube(Scene):
    def construct(self):
        # Create the ground line
        ground = Line(LEFT * 7, RIGHT * 7)
        self.add(ground)

        # Ball properties
        ball_radius = 0.5
        ball_color = BLUE

        # Create the ball
        ball = Circle(radius=ball_radius, color=ball_color, fill_opacity=1)
        ball.shift(LEFT * 6 + UP * (ball_radius))
        self.add(ball)

        # Path for the ball
        path = Line(LEFT * 6, RIGHT * 6)
        total_distance = path.get_length()

        # Rolling effect
        def update_ball(mob, alpha):
            distance = interpolate(0, total_distance, alpha)
            mob.move_to(LEFT * 6 + RIGHT * distance)
            rotation_angle = -distance / ball_radius
            mob.rotate(rotation_angle - mob.get_angle())

        # Letters to form "Cube"
        letters = VGroup(
            Text("C"),
            Text("u"),
            Text("b"),
            Text("e")
        ).arrange(RIGHT, buff=1)
        letters.move_to(DOWN * 2)

        # Animations
        self.play(
            UpdateFromAlphaFunc(ball, update_ball),
            rate_func=linear,
            run_time=8
        )
        self.wait(0.5)

        # Reveal letters as the ball passes
        reveal_animations = []
        for letter in letters:
            reveal_animations.append(FadeIn(letter))
            self.wait(0.5)

        self.play(*reveal_animations)
        self.wait(2)

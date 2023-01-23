from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)
        self.play(Create(circle))

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity =0.5)

        square = Square()
        square.rotate(PI/4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

           
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(Rotate(square, angle=PI/4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class AnimatedLogo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        circle = Circle(radius = 75/200)
        circle.shift(RIGHT)
        circle.shift(DOWN)
        circle.set_stroke(color="#E63946", width=0)
        logo = SVGMobject('logo-nikita.svg', True)
        logo_border = SVGMobject('logo-border', True)
        logo_container = SVGMobject('logo-container.svg',True)
        
        logo_n_border = SVGMobject('logo-n-border.svg', True)
        logo_n_filled = SVGMobject('logo-n-filled.svg', True)
        logo_circle_border = SVGMobject('logo-circle-border.svg', True)
        logo_circle_filled = SVGMobject('logo-circle-filled.svg', True)
        logo_border.set_stroke(width = 5)
        logo_container.scale(1.5)
        logo_container.set_stroke(width = 20)

        #self.play(Create(logo_border),Transform(logo_border,logo),Circumscribe(logo, color = '#E63946'),Create(logo_container), run_time = 1.5)
        self.play(Create(logo_border), run_time = 2)
        self.play(Transform(logo_border,logo), Circumscribe(logo, color = '#E63946'), run_time = 0.75)
        #self.play(Circumscribe(logo, color = '#E63946'), run_time = 0.5)
        self.play(FadeIn(logo_container), run_time = 0.25)
        #self.play(Rotate(logo_container, angle = PI/2), runtime = 0.5)
        #self.play(GrowFromEdge(logo_container, DOWN), run_time = 0.5)
        Wait


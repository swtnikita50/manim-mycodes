from manim import *

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
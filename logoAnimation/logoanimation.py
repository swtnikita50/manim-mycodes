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

class AnimatedLogo2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_height = 3.25
        self.camera.frame_width = 3.25

        logo = SVGMobject('logo-nikita.svg', True)
        logo_border = SVGMobject('logo-border', True)
        logo_container = SVGMobject('logo-container.svg',True)
        
        logo_n_border = SVGMobject('logo-n-border.svg', True)
        logo_n_filled = SVGMobject('logo-n-filled.svg', True)
        logo_circle_border = SVGMobject('logo-circle-border.svg', True)
        logo_circle_filled = SVGMobject('logo-circle-filled.svg', True)
        logo_box = SVGMobject('logo-box.svg', True)

        #scaling
        logo_circle_border.scale(750/2000)
        logo_container.scale(1.5)

        #dimensions
        logo_border.set_stroke(width = 5)
        logo_circle_border.set_stroke(width = 5)
        logo_n_border.set_stroke(width = 5)
        logo_container.set_stroke(width = 20)
        

        #position
        logo_circle_border.align_to(logo_border, DR)
        logo_n_border.align_to(logo_border, DL)

        #animate
        self.play(Create(logo_n_border),Create(logo_circle_border), run_time = 2)
        self.play(Transform(logo_border,logo), Circumscribe(logo, color = '#E63946'), run_time = 0.75)
        self.play(FadeIn(logo_container), run_time = 0.25)
        #self.play(Create(logo_border),Transform(logo_border,logo),Circumscribe(logo, color = '#E63946'),Create(logo_container), run_time = 1.5)
        #self.play(Create(logo_border), run_time = 2)
        #self.play(Transform(logo_border,logo), Circumscribe(logo, color = '#E63946'), run_time = 0.75)
        #self.play(Circumscribe(logo, color = '#E63946'), run_time = 0.5)
        #self.play(FadeIn(logo_container), run_time = 0.25)
        #self.play(Rotate(logo_container, angle = PI/2), runtime = 0.5)
        #self.play(GrowFromEdge(logo_container, DOWN), run_time = 0.5)

class AnimateName(Scene):
    def construct(self):
        self.camera.background_color = '#050404'
        name = Text('Nikita Sehrawat').scale(1)
        name.shift(LEFT)
        #name_hindi = Text('निकिता सहरावत', font="sans-serif")
        self.play(Write(name, reverse = True), name.animate.shift(ORIGIN), run_time = 2)
        self.play(name.animate.to_edge(LEFT))
        self.play( Unwrite(name, reverse = False), run_time = 2)


class AnimateShreyansh(Scene):
    def construct(self):
        #self.camera.background_color = WHITE
        name = Tex("S","hreyansh","D","arshan").scale(2)
        self.play(Write(name), run_time = 2)
        name_initials = Tex('S','D').scale(5)
        animations = [
            FadeOut(name[1], scale = '0.5'),
            FadeOut(name[3], scale = '0.5'),
            Transform(name[1],name_initials[1]),
            Transform(name[3],name_initials[2],)
        ]
        #self.paly(AnimationGroup(*animations, lag_ratio=0, run_time = 2))
        #self.play( run_time = 2)

class AnimateAerospaceLogo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        dept_name = Text('Department of Aerspace Engineering', color = BLACK).move_to([0,-1.5,0])
        inst_name = Text('Indian Institute of Technology, Kharagpur', color = BLACK).move_to([0,-2,0])
        
        dept_name.scale(0.5)
        inst_name.scale(0.5)

        aerospace_logo = SVGMobject('aerospace-logo.svg', True)
        text_container = Rectangle(width=6.5, height=1).move_to([0,-1.75,0]) 
        aerospace_logo_path = SVGMobject('aerospace-logo-path.svg', True)
        aerospace_logo_plane = SVGMobject('aerospace-logo-plane.svg', True).scale(0.1)

        #dot = Dot(color=BLACK).move_to(aerospace_logo_plane.get_start())
        trace = TracedPath(aerospace_logo_plane.get_center, dissipating_time=0.3, stroke_opacity=[0, 1])
        trace.set_color(BLACK)
        aerospace_logo_path.set_stroke(width=1)
        path = aerospace_logo_path.family_members_with_points()[0]
        
        l1 = Line(LEFT, RIGHT)
        #self.add(aerospace_logo_path)

        self.add(trace, aerospace_logo_plane)
        self.play(MoveAlongPath(aerospace_logo_plane, path), rate_func=linear, run_time = 1)
        self.play(FadeIn(aerospace_logo), run_time=1)
        self.play(Write(dept_name), Write(inst_name), ShowPassingFlash(
                text_container.copy().set_color("#00655F"),
            ), run_time = 1.5)

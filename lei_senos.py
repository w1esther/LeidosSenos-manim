from manim import *
import numpy as np

class LeiDosSenos(MovingCameraScene):

    def construct(self):
        
        plano = NumberPlane(
            background_line_style={'stroke_opacity': 0.4}
        )
        self.add(plano)
        self.wait(1)

        circuculo = Circle(radius=2, color=BLUE)

        self.play(Write(circuculo))
        
        self.wait(2)

        ponto1_tri = np.array([0, 2, 0])
        ponto2_tri = np.array([-1.6, -1.2, 0])
        ponto3_tri = np.array([1.6, -1.2, 0])
        ponto_origem = np.array([0, 0, 0])

        dot1 = Dot(ponto1_tri, color=RED)
        dot2 = Dot(ponto2_tri, color=RED)
        dot3 = Dot(ponto3_tri, color=RED)
        dot4 = Dot(ponto_origem, color=BLUE)

        linha1 = Line(ponto1_tri, ponto2_tri)
        linha2 = Line(ponto1_tri, ponto3_tri)

        l2_1 = Line(ponto2_tri, ponto1_tri)
        l2_2 = Line(ponto2_tri, ponto3_tri)

        l3_1 = Line(ponto3_tri, ponto1_tri)
        l3_2 = Line(ponto3_tri, ponto2_tri)
        
        angulo_alfa = Angle(linha1, linha2, color=YELLOW)
        angulo_beta = Angle(l2_2, l2_1, color=ORANGE)
        angulo_gama = Angle(l3_1, l3_2, color=PURPLE)

        triangulo = Polygon(ponto1_tri, ponto2_tri, ponto3_tri, color=WHITE)

        label_ponto_a = MathTex(r'A').shift(2.3*UP).scale(0.8)
        label_ponto_b = MathTex(r'B').scale(0.8).shift(1.5*DOWN + 1.9*LEFT)
        label_ponto_c = MathTex(r'C').scale(0.8).shift(1.5*DOWN + 1.9*RIGHT)

        self.play(Write(triangulo), FadeIn(dot1), FadeIn(dot2), FadeIn(dot3), FadeIn(label_ponto_a), FadeIn(label_ponto_b), FadeIn(label_ponto_c), FadeIn(dot4))

        self.wait(2)

        alfa_label = MathTex(r"\alpha").scale(0.7).shift(1.4*UP)
        beta_label = MathTex(r"\beta").scale(0.7).shift(0.9*LEFT + 0.8*DOWN)
        gama_label = MathTex(r"\gamma").scale(0.7).shift(0.8*DOWN + 0.9*RIGHT)

        self.play(FadeIn(alfa_label), FadeIn(gama_label), FadeIn(beta_label), FadeIn(angulo_alfa), FadeIn(angulo_gama), FadeIn(angulo_beta))
        
        self.wait(2)

        label_lado_a = MathTex(r'a').scale(0.8).shift(1.5*DOWN)
        label_lado_b = MathTex(r'b').scale(0.8).shift(0.5*UP + 1.1*RIGHT)
        label_lado_c = MathTex(r'c').scale(0.8).shift(0.5*UP + 1.1*LEFT)

        self.play(FadeIn(label_lado_a), FadeIn(label_lado_c), FadeIn(label_lado_b))

        self.wait(2)
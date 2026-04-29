from manim import *
import numpy as np

class LeiDosSenos(MovingCameraScene):

    def construct(self):
        
        # plano = NumberPlane(
        #     background_line_style={'stroke_opacity': 0.4}
        # )
        # self.add(plano)
        # self.wait(1)

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
        ponto1 = np.array([-0.85, 0.4, 0])
        ponto2 = np.array([0, -1.2, 0])
        ponto3 = np.array([0.85, 0.4, 0])

        linha_origem_c = Line(ORIGIN, ponto1, color=PINK)
        linha_origem_a = Line(ORIGIN, ponto2, color=PINK)
        linha_origem_b = Line(ORIGIN, ponto3, color=PINK)

        l1 = Line(ponto1, ORIGIN)
        l2 = Line(ponto1, ponto1_tri)

        l3 = Line(ponto2, ORIGIN)
        l4 = Line(ponto2, ponto2_tri)

        l5 = Line(ponto3, ORIGIN)
        l6 = Line(ponto3, ponto3_tri)

        self.play(Write(linha_origem_c), Write(linha_origem_a), Write(linha_origem_b))

        self.bring_to_front(triangulo)
        self.bring_to_front(dot1, dot2, dot3, dot4)

        self.wait(1)

        ang_reto = RightAngle(l1, l2, length=0.25, color=GREEN)
        ang_reto2 = RightAngle(l3, l4, length=0.25, color=GREEN)
        ang_reto3 = RightAngle(l5, l6, length=0.25, color=GREEN)

        self.play(Create(ang_reto), Create(ang_reto2), Create(ang_reto3))

        self.bring_to_front(triangulo)
        self.bring_to_front(dot1, dot2, dot3, dot4)

        self.wait(2)

        raio1 = Line(ORIGIN, ponto2_tri, color=DARK_GRAY)
        raio2 = Line(ORIGIN, ponto1_tri, color=DARK_GRAY)
        raio3 = Line(ORIGIN, ponto3_tri, color=DARK_GRAY)

        label_raio1 = MathTex(r'r').scale(0.5).shift(0.8*LEFT + 0.4*DOWN)
        label_raio2 = MathTex(r'r').scale(0.5).shift(0.8*RIGHT + 0.4*DOWN)
        label_raio3 = MathTex(r'r').scale(0.5).shift(0.2*LEFT + 0.8*UP)

        self.play(Create(raio1), Create(raio2), Create(raio3))

        self.bring_to_front(dot1, dot2, dot3, dot4)

        self.play(FadeIn(label_raio1), FadeIn(label_raio2), FadeIn(label_raio3))

        self.wait(2)

        tri_BOC = Polygon(ponto2_tri, ORIGIN, ponto3_tri, fill_color=YELLOW, fill_opacity=0.2)

        self.play(self.camera.frame.animate.scale(0.7))

        self.play(FadeIn(tri_BOC))

        self.bring_to_front(dot1, dot2, dot3, dot4)

        ang_BOC = Angle(raio1, raio3, color=YELLOW)

        alfa_label2 = MathTex(r"2\alpha").scale(0.5).shift(0.55*DOWN)

        alfa_label21 = MathTex(r"\alpha").scale(0.5).shift(0.55*DOWN + 0.3*RIGHT)
        alfa_label22 = MathTex(r"\alpha").scale(0.5).shift(0.55*DOWN + 0.3*LEFT)

        self.play(Create(ang_BOC), FadeIn(alfa_label2))

        self.wait()

        label_lado_a2 = MathTex(r'\frac{a}{2}').scale(0.5).shift(1.55*DOWN+0.5*LEFT)
        label_lado_a3 = MathTex(r'\frac{a}{2}').scale(0.5).shift(1.55*DOWN+0.5*RIGHT)

        self.play(FadeOut(alfa_label2), FadeIn(alfa_label21), FadeIn(alfa_label22), FadeIn(label_lado_a2), FadeIn(label_lado_a3), FadeOut(label_lado_a))

        self.play(self.camera.frame.animate.shift(1*LEFT))

        seno_alfa = MathTex(r'Sen(\alpha) = \frac{\frac{a}{2}}{r}').shift(4*LEFT)
        seno_alfa2 = MathTex(r'Sen(\alpha) = \frac{a}{2r}').shift(4*LEFT)
        seno_alfa3 = MathTex(r'Sen(\alpha)\cdot2r = a').shift(4*LEFT)
        seno_alfa4 = MathTex(r'2r = \frac{a}{Sen(\alpha)}').shift(4*LEFT)

        self.wait(2)

        self.play(FadeIn(seno_alfa))

        self.wait()

        self.play(Transform(seno_alfa, seno_alfa2))

        self.wait()

        self.play(Transform(seno_alfa, seno_alfa3))

        self.wait()

        self.play(Transform(seno_alfa, seno_alfa4))

        self.wait(2)

        self.play(seno_alfa.animate.scale(0.5).shift(2*UP))

        self.wait()

        tri_BOA = Polygon(ponto2_tri, ORIGIN, ponto1_tri, fill_color = ORANGE, fill_opacity = 0.3)

        angulo_BOA = Angle(raio2, raio1, color=ORANGE)

        gama_label2 = MathTex(r"2\gamma").scale(0.5).shift(0.6*LEFT)

        self.play(FadeOut(tri_BOC), FadeIn(tri_BOA), Create(angulo_BOA), FadeIn(gama_label2))

        self.bring_to_front(dot1, dot2, dot3, dot4)

        self.wait()

        gama_label3 = MathTex(r"\gamma").scale(0.5).shift(0.6*LEFT)
        gama_label4 = MathTex(r"\gamma").scale(0.5).shift(0.4*LEFT + 0.5*UP)

        lado_c = MathTex(r'\frac{c}{2}').scale(0.5).shift(1.2*UP + 0.7*LEFT)
        lado_c2 = MathTex(r'\frac{c}{2}').scale(0.5).shift(0.3*DOWN + 1.4*LEFT)

        self.play(FadeOut(gama_label2), FadeIn(gama_label3), FadeIn(gama_label4), FadeIn(lado_c), FadeIn(lado_c2), FadeOut(label_lado_c))

        self.wait(2)

        seno_gama = MathTex(r'Sen(\gamma) = \frac{\frac{c}{2}}{r}').shift(4*LEFT)
        seno_gama2 = MathTex(r'Sen(\gamma) = \frac{c}{2r}').shift(4*LEFT)
        seno_gama3 = MathTex(r'Sen(\gamma)\cdot2r = c').shift(4*LEFT)
        seno_gama4 = MathTex(r'2r = \frac{c}{Sen(\gamma)}').shift(4*LEFT)

        self.play(FadeIn(seno_gama))

        self.wait()

        self.play(Transform(seno_gama, seno_gama2))

        self.wait()

        self.play(Transform(seno_gama, seno_gama3))

        self.wait()

        self.play(Transform(seno_gama, seno_gama4))

        self.wait(2)

        self.play(seno_gama.animate.scale(0.5).shift(1.2*UP))

        self.wait(2)

        tri_AOC = Polygon(ponto1_tri, ORIGIN, ponto3_tri, fill_color = PURPLE, fill_opacity=0.2)
        angulo_AOC = Angle(raio3, raio2, color=PURPLE)

        beta_label2 = MathTex(r"2\beta").scale(0.5).shift(0.55*UP + 0.3*RIGHT)

        self.play(FadeOut(tri_BOA), FadeIn(tri_AOC), Create(angulo_AOC), FadeIn(beta_label2))

        self.bring_to_front(dot1, dot2, dot3, dot4)

        self.wait(1)

        beta_label3 = MathTex(r"\beta").scale(0.5).shift(0.55*UP + 0.3*RIGHT)
        beta_label4 = MathTex(r"\beta").scale(0.5).shift(0.2*DOWN + 0.6*RIGHT)

        lado_b = MathTex(r'\frac{b}{2}').scale(0.5).shift(1.2*UP + 0.7*RIGHT)
        lado_b2 = MathTex(r'\frac{b}{2}').scale(0.5).shift(0.3*DOWN + 1.4*RIGHT)

        self.play(FadeOut(beta_label2), FadeIn(beta_label3), FadeIn(beta_label4), FadeIn(lado_b), FadeIn(lado_b2), FadeOut(label_lado_b))

        self.wait(2)

        seno_beta = MathTex(r'Sen(\beta) = \frac{\frac{b}{2}}{r}').shift(4*LEFT)
        seno_beta2 = MathTex(r'Sen(\beta) = \frac{b}{2r}').shift(4*LEFT)
        seno_beta3 = MathTex(r'Sen(\beta)\cdot2r = b').shift(4*LEFT)
        seno_beta4 = MathTex(r'2r = \frac{b}{Sen(\beta)}').shift(4*LEFT)

        self.play(FadeIn(seno_beta))

        self.wait()

        self.play(Transform(seno_beta, seno_beta2))

        self.wait()

        self.play(Transform(seno_beta, seno_beta3))

        self.wait()

        self.play(Transform(seno_beta, seno_beta4))

        self.wait(2)

        self.play(seno_beta.animate.scale(0.5).shift(0.4*UP))

        self.wait(2)

        self.play(FadeOut(tri_AOC))

        self.play(self.camera.frame.animate.scale(1.3).shift(1*RIGHT + 1*UP))

        lei_senos = MathTex(r'\frac{a}{Sen(\alpha)} = \frac{c}{Sen(\gamma)} = \frac{b}{Sen(\beta)} = 2r').shift(3.1*UP).scale(0.8)

        label_lei_senos = Text('Lei dos Senos:').scale(0.6).shift(4*UP)

        self.play(FadeOut(seno_alfa), FadeOut(seno_beta), FadeOut(seno_gama), FadeIn(lei_senos), FadeIn(label_lei_senos))

        self.wait(2)
from manim import *

class LatexExample(Scene):
    def construct(self):
        equation = MathTex(r"\frac{d}{dx}f(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}")
        #era Tex e not MathTex che da errore 
        self.play(Write(equation))
        self.wait()

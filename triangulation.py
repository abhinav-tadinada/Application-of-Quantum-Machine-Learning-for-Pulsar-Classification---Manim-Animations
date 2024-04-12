from manim import *

class PulsarScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # Title
        title = Text("Novel Spacecraft Triangulation", font_size=48).to_edge(UP).set_color(YELLOW)
        
        # Create the spacecraft
        rocket = Triangle().scale(0.5).set_fill(WHITE, opacity=1)
        rocket_label = Text("Spacecraft using \nProposed Device", font_size=20).next_to(rocket, DOWN)
        
        # Create pulsars
        pulsar_positions = [UP + LEFT, UP + RIGHT, DOWN + 2 * RIGHT]
        pulsars = [Circle(radius=0.2, color=YELLOW).move_to(pos) for pos in pulsar_positions]
        pulsar_labels = [
            Text("Pulsar", font_size=24, color=YELLOW).next_to(pulsars[i], DOWN) for i in range(3)
        ]
        
        # Create vectors
        vectors = [Arrow(rocket.get_center(), pulsars[i].get_center(), buff=0, color=WHITE)
                   for i in range(3)]
        vector_labels = [
            MathTex(r"\vec{v}_" + str(i+1), color=WHITE, font_size = 24).next_to(vectors[i], RIGHT)
            for i in range(3)
        ]
        
        # Create equations in a table format
        equation_texts = [
            r"v = \frac{d}{t}",
            r"d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}",
            r"\alpha = \cos^{-1}\left(\frac{x_2-x_1}{d}\right)",
            r"\delta = \sin^{-1}\left(\frac{y_2-y_1}{d}\right)"
        ]
        equations = VGroup(*[MathTex(eq, color=WHITE, font_size=24) for eq in equation_texts])
        equations.arrange(DOWN, buff=0.5).to_edge(DOWN)
        
        equations.to_corner(DL)
        # Add title, rocket and label
        self.add(title, rocket, rocket_label)
        self.wait(1)
        
        # Add pulsars one by one
        for pulsar, label in zip(pulsars, pulsar_labels):
            self.play(FadeIn(pulsar, scale=0.5), Write(label))
            self.wait(0.5)
        
        # Draw vectors one by one
        for vector, v_label in zip(vectors, vector_labels):
            self.play(Create(vector))
            self.play(Write(v_label))
            self.wait(0.5)
        
        # Show equations with separators
        self.play(Create(equations))
        self.wait(3)


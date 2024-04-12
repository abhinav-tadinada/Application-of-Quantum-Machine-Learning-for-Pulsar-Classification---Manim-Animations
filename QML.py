#!/usr/bin/env python
# coding: utf-8

# In[1]:


from manim_notebook import *



# In[8]:


get_ipython().run_cell_magic('manim', '-p', '\n\nclass PangoRender(Scene):\n    def construct(self):\n        # Initialize the title and its transformation\n        morning = Text("Quantum Machine Learning", font="Arial")\n        morning.scale(2)  # Scale the text by a factor of 2\n        morn = Text("Quantum Machine Learning - Data Flow", font="Arial")\n        morn.to_edge(UP)\n        self.play(Write(morning))\n        self.play(Transform(morning, morn))  # Transform the main title\n        self.wait(.5)  # Wait after the transformation\n\n        # Define the green rectangle dimensions and create it\n        green_rectangle = Rectangle(width=4, height=5, color=GREEN)\n        green_rectangle.set_stroke(GREEN, width=10)  # Set the stroke color and width\n        green_rectangle.shift(1*DOWN)  # Slightly lower the position of the rectangle\n\n        # Add a subtitle above the green rectangle with a different font\n        green_subtitle = Text("Data Input", font="Times New Roman", color=WHITE).next_to(green_rectangle, UP, buff=0.5)\n\n        # Create a dot to trace the green rectangle\n        green_trace_point = Dot()\n        green_trace_point.move_to(green_rectangle.get_start())\n\n        # Create a traced path using TracedPath to draw the green rectangle\n        green_traced_path = TracedPath(green_trace_point.get_center, stroke_color=GREEN, stroke_width=10)\n\n        # Animate the dot tracing the outline of the green rectangle and subtitle appearance\n        self.add(green_traced_path, green_subtitle)  # Add the traced path and subtitle to the scene\n        self.play(MoveAlongPath(green_trace_point, green_rectangle), run_time=1)  # Speed up the tracing\n        self.wait(.5)\n\n        # Create purple squares along the midline of the green rectangle\n        squares = VGroup(*[\n            Square(side_length=1.0, color=PURPLE, fill_opacity=1).move_to(green_rectangle.get_center() + i*1.8*UP)\n            for i in range(1, -2, -1)  # Positions: 1 UP, CENTER, 1 DOWN along the midline\n        ])\n\n        # Display all squares at once after the green rectangle is traced\n        self.play(FadeIn(squares), run_time=1)\n\n        # Display RY notation in each square using subscripted gamma and a number\n        gammas = ["RY(γ₁)", "RY(γ₂)", "RY(γ₃)"]\n        gamma_texts = [Text(gamma, font="CMU Serif", color=BLACK).scale(0.7).move_to(square.get_center()) for square, gamma in zip(squares, gammas)]\n        self.play(LaggedStart(*(FadeIn(gamma_text) for gamma_text in gamma_texts), lag_ratio=0.5), run_time=1)\n\n        self.wait(2)  # Wait for 2 seconds\n\n        # Move the grouped elements to the left\n        moving_group = VGroup(green_rectangle, green_subtitle, squares, *gamma_texts)\n        self.play(\n            ApplyMethod(moving_group.shift, 5*LEFT),  # Move 5 units to the left using ApplyMethod\n            rate_func=smooth\n        )\n\n        self.wait(1)\n\n        # Trace a new blue rectangle exactly where the original green one was, using the same format\n        blue_rectangle = Rectangle(width=4, height=5, color=BLUE)\n        blue_rectangle.set_stroke(BLUE, width=10)\n        blue_rectangle.shift(1*DOWN)  # Position it where the green one started\n\n        # Create a dot to trace the blue rectangle\n        blue_trace_point = Dot()\n        blue_trace_point.move_to(blue_rectangle.get_start())\n        blue_traced_path = TracedPath(blue_trace_point.get_center, stroke_color=BLUE, stroke_width=10)\n        self.add(blue_traced_path)\n        self.play(MoveAlongPath(blue_trace_point, blue_rectangle), run_time=1)\n        self.wait(0)\n\n        # Immediately show the "Data Processing" subtitle after tracing the blue rectangle\n        processing_subtitle = Text("Data Processing", font="Times New Roman", color=WHITE).next_to(blue_rectangle, UP, buff=0.5)\n        self.play(FadeIn(processing_subtitle))\n\n        # Add three horizontal thin dark blue lines inside the blue rectangle to divide it into fourths\n        lines = [\n            Line(blue_rectangle.get_left(), blue_rectangle.get_right(), color=DARK_BLUE).move_to(blue_rectangle.get_center() + blue_rectangle.height * (i / 4 - 1/2) * UP)\n            for i in range(1, 4)  # positions at 1/4, 1/2, and 3/4\n        ]\n        for line in lines:\n            self.play(ShowCreation(line))\n\n        # Add smaller purple squares and labels to the inside left edge of the blue rectangle\n        for i, line in enumerate(lines):\n            small_square = Square(side_length=0.5, color=PURPLE, fill_opacity=1).next_to(line, LEFT, aligned_edge=line.get_start())\n            small_label = Text(gammas[i], font="CMU Serif", color=BLACK).scale(0.35).move_to(small_square.get_center())\n            self.play(FadeIn(small_square), FadeIn(small_label))\n\n        # Add custom speedometer icons to the inside right edge of the blue rectangle\n        for line in lines:\n            # Drawing a simple speedometer icon: a circle with an arrow\n            speedometer = VGroup(\n                Circle(radius=0.2, color=GRAY).next_to(line, aligned_edge=line.get_end()),  # Aligned with the right edge\n                Line(ORIGIN, 0.1*UP, color=GRAY).next_to(line, aligned_edge=line.get_end())  # Simple line to represent the arrow part\n            )\n            self.play(GrowFromCenter(speedometer))\n\n        # Create vertical lines and circles at specified positions\n        vline1 = Line(lines[0].get_center() + 0.25 * blue_rectangle.width * LEFT, lines[1].get_center() + 0.25 * blue_rectangle.width * LEFT, color=DARK_BLUE)\n        circle1 = Circle(radius=0.1, color=DARK_BLUE).move_to(vline1.get_start())\n        vline2 = Line(lines[1].get_center(), lines[2].get_center(), color=DARK_BLUE)\n        circle2 = Circle(radius=0.1, color=DARK_BLUE).move_to(vline2.get_start())\n        vline3 = Line(lines[0].get_center() + 0.25 * blue_rectangle.width * RIGHT, lines[2].get_center() + 0.25 * blue_rectangle.width * RIGHT, color=DARK_BLUE)\n        circle3 = Circle(radius=0.1, color=DARK_BLUE).move_to(vline3.get_start())\n\n        self.play(ShowCreation(vline1), GrowFromCenter(circle1))\n        self.play(ShowCreation(vline2), GrowFromCenter(circle2))\n        self.play(ShowCreation(vline3), GrowFromCenter(circle3))\n     \n    # Draw an arrow from the green rectangle to the blue rectangle\n        green_to_blue_arrow = Arrow(green_rectangle.get_right(), blue_rectangle.get_left(), buff=0.1, color=WHITE)\n        self.play(GrowArrow(green_to_blue_arrow))\n\n        # Add a new yellow rectangle to the right of the blue rectangle, half the height and on the upper half of the screen\n        yellow_rectangle = Rectangle(width=2, height=2, color=YELLOW)\n        yellow_rectangle.next_to(blue_rectangle, RIGHT, buff=1.5)  # Further to the right\n        yellow_rectangle.align_to(blue_rectangle, UP)\n        self.play(FadeIn(yellow_rectangle))\n\n        # Add vertical \'1\' and \'0\' inside the yellow rectangle\n        one_zero_one = VGroup(\n            Text("101", font="Helvetica", color=WHITE).scale(1.5),\n            Text("011", font="Helvetica", color=WHITE).scale(1.5),\n            Text("010", font="Helvetica", color=WHITE).scale(1.5)\n        ).arrange(DOWN, buff=0.1).move_to(yellow_rectangle.get_center())\n\n        self.play(FadeIn(one_zero_one))\n\n        # Draw an arrow from the blue rectangle to the yellow rectangle\n        blue_to_yellow_arrow = Arrow(blue_rectangle.get_right(), yellow_rectangle.get_left(), buff=0.1, color=WHITE)\n        self.play(GrowArrow(blue_to_yellow_arrow))\n\n        # Add a subtitle for the yellow rectangle\n        output_subtitle = Text("Data Output", font="Times New Roman", color=WHITE).next_to(yellow_rectangle, UP, buff=0.5)\n        self.play(FadeIn(output_subtitle))\n\n        # Add an orange rectangle below the yellow rectangle\n        orange_rectangle = Rectangle(width=2, height=1, color=ORANGE)\n        orange_rectangle.next_to(yellow_rectangle, DOWN, buff=0.2)\n        orange_rectangle.shift(1 * DOWN)\n        self.play(FadeIn(orange_rectangle))\n\n        # Write \'Optimization\' inside the orange rectangle\n        optimization_text = Text("Optimization", font="Times New Roman", color=WHITE).scale(0.7).move_to(orange_rectangle.get_center())\n        self.play(FadeIn(optimization_text))\n\n        # Draw arrows connecting the yellow and orange rectangles, and orange to blue rectangle\n        yellow_to_orange_arrow = Arrow(yellow_rectangle.get_bottom(), orange_rectangle.get_top(), buff=1, color=WHITE)\n        orange_to_blue_arrow = Arrow(orange_rectangle.get_left(), blue_rectangle.get_right(), buff=1, color=WHITE)\n        self.play(GrowArrow(yellow_to_orange_arrow), GrowArrow(orange_to_blue_arrow))\n\n        self.wait(2)\n')

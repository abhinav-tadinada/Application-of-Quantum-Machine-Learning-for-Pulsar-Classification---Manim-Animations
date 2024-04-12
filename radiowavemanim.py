from manim import *
import numpy as np

class SpinningEarth(ThreeDScene):
    def construct(self):
        # Get the width and height of the frame
        frame_width = config.frame_width
        frame_height = config.frame_height

        # Create a black background with thin white gridlines
        background = NumberPlane(color=WHITE)
        background.add_coordinates()
        background.set_opacity(0.1)

        # Add LaTeX text in the top-left corner
        pulsar_text = Tex("Pulsar: A Neutron Star", color=WHITE).scale(0.7)
        pulsar_text.to_corner(UL)

        # Add a bunch of very small white dots to the black background to symbolize stars
        num_stars = 1000
        stars = VGroup(*[Dot(
                    point=np.array([
                        np.random.uniform(-frame_width / 2, frame_width / 2),
                        np.random.uniform(-frame_height / 2, frame_height / 2),
                        0
                    ]),
                    radius=np.random.uniform(0.01, 0.05),
                    color=WHITE)
                for _ in range(num_stars)])

        # Create a sphere (the Earth) and set its material to be white/yellow with light
        earth = Sphere(radius=2, resolution=(25, 25), color=YELLOW)
        earth.set_fill(color=YELLOW, opacity=1)
        earth.set_shade_in_3d(True)

        # Create cones to represent light beams at the poles
        cone_height = 7  # Smaller height for better visualization
        cone_north = Cone(base_radius=1, height=cone_height, resolution=(15, 15), color=PURPLE_E)
        cone_south = Cone(base_radius=1, height=cone_height, resolution=(15, 15), color=PURPLE_E)

        # Position the cones' tips at the poles of the Earth
        cone_north.next_to(earth, UP, buff=0)  # 'buff=0' places the base right at the sphere's surface
        cone_south.next_to(earth, DOWN, buff=0)  # Same for the southern cone

        # Rotate cones to stand upright (the correct vertical position)
        cone_north.rotate(-PI/2, LEFT)
        cone_south.rotate(PI/2, LEFT)

        # Set the initial camera orientation
        self.set_camera_orientation(phi=-200 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=4)  # Slower camera rotation

        # Add the background, pulsar text, Earth, and cones to the scene
        self.add(earth, cone_north, cone_south)

        # Create a non-moving layer for stationary objects
        stationary_layer = VGroup(background, pulsar_text, stars)
        self.add(stationary_layer)

        # Define the axis of rotation for the cones (around their own vertical axis)
        axis_of_rotation_north = cone_north.get_center() - earth.get_top()
        axis_of_rotation_south = cone_south.get_center() - earth.get_bottom()

        # Continuous rotation of the cones around their axis
        cone_north.add_updater(lambda m, dt: m.rotate(dt * PI, axis=axis_of_rotation_north, about_point=earth.get_top()))
        cone_south.add_updater(lambda m, dt: m.rotate(-dt * PI, axis=axis_of_rotation_south, about_point=earth.get_bottom()))

        # Animate the Earth spinning around its axis
        self.play(
            Rotate(earth, 8*TAU, axis=UP, run_time=4, rate_func=linear),
        )

        # Hold the final scene
        self.wait(1)

        # Fade everything into just black
        self.play(FadeOut(stationary_layer), FadeOut(earth), FadeOut(cone_north), FadeOut(cone_south))
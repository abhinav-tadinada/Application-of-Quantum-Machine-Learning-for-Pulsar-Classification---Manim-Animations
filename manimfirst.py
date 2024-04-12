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

        # Add non-moving background, stars, and text to the scene
        self.add(background, stars, pulsar_text)

        # Add moving Earth and cones to the scene
        moving_group = VGroup(earth, cone_north, cone_south)
        self.add(moving_group)

        # Define the axis of rotation for the Earth and cones (around the vertical axis)
        earth_rotation_axis = UP  # Universal up vector

        # Continuous rotation of Earth and cones around their axis
        moving_group.add_updater(lambda m, dt: m.rotate_about_origin(dt * PI, earth_rotation_axis))

        # Start animation
        self.wait(5)  # Duration for the animation in seconds

        # Remove updater function when the scene is done animating
        moving_group.clear_updaters()

        # Fade out all objects smoothly
        self.play(FadeOut(VGroup(background, stars, pulsar_text, earth, cone_north, cone_south)))

from manim import *

class SurfaceOfRevolution(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Define function and surface
        func = lambda x: np.sin(2 * x)
        surface = ParametricSurface(
            lambda u, v: np.array([
                np.cos(u),
                np.sin(u) * func(v),
                np.sin(u) * np.sqrt(1 - func(v)**2)
            ]),
            u_range=[0, TAU],
            v_range=[-1, 1],
            checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(50, 50)
        ).fade(0.5)

        # Add surface and axes to scene
        self.play(Create(axes), Create(surface), run_time=2)
        self.wait(1)

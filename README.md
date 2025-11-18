### Computer Vision: Camera Models, Projection & Calibration

This repository contains implementations of fundamental computer vision concepts, focusing on camera geometry, projection matrices, single-view metrology, and multi-camera calibration analysis.

#### Table of Contents

- Part 1: Synthetic Projection Scenarios

- Part 2i: EPFL Terrace Dataset Analysis

- Part 2ii: Height Estimation (Single View Metrology)


#### Part 1: Synthetic Projection Scenarios

In this module, we simulate a camera capturing a 3D object (a LEGO figure) to understand how intrinsic and extrinsic parameters affect the 2D image. We utilize the pinhole camera model $\mathbf{x} = P \mathbf{X} = K [R | t] \mathbf{X}$ to explore five key scenarios:

- **Scenario 1 (Focal Length)**: We vary the focal length (400mm, 800mm, 1600mm) with a fixed camera position to observe how increasing $f$ narrows the Field of View (FOV) and flattens the perspective.

- **Scenario 2 (Z-Translation)**: We translate the camera along the Z-axis (depth) to contrast how physical movement affects scale differently than zooming with a lens.

- **Scenario 3 (XY-Translation)**: We shift the camera laterally (X/Y axes) to visualize parallax effects and the shift of the principal point relative to the subject.

- **Scenario 4 (Rotation)**: We apply rotation matrices to the camera to observe how changing the viewing angle induces perspective distortion.

- **Scenario 5 (Dolly Zoom)**: We implement the "Vertigo Effect" by simultaneously moving the camera backwards and increasing the focal length, keeping the subject size constant while drastically warping the background.

#### Part 2i: EPFL Terrace Dataset Analysis

**Objective**: Analyze a real-world multi-camera pedestrian dataset to validate camera calibration and projection geometry.

**Pipeline**

- Tsai Calibration Parsing: Parsed .xml calibration files to extract Intrinsic ($K$), Rotation ($R$), and Translation ($t$) matrices.

- Vanishing Points & Horizon: Computed vanishing points ($VP_x, VP_y, VP_z$) using the projection matrix columns and visualized the Horizon Line ($L_\infty$) on video frames.

- Ground Truth Processing: Parsed gt_terrace1.txt to extract pedestrian locations on a 2D grid and converted them to 3D World Coordinates (mm).

- Reprojection: Projected 3D world coordinates back onto 2D image planes using $P = K[R|t]$ to verify calibration accuracy against video feeds.

- Matrix Decomposition & Error Analysis:

  Decomposed the Projection Matrix $P$ back into $K, R, t$ using RQ Decomposition.

  Compared decomposed values with original Tsai parameters.

- Result: Relative errors were found to be near-zero ($\approx 10^{-16}$), confirming the mathematical reversibility of the camera model.

3D Visualization: Plotted the 3D positions of all 4 cameras relative to the world origin to verify spatial configuration.

#### Part 2ii: Height Estimation (Single View Metrology)

**Objective**: Estimate the real-world height of an unknown object (e.g., a water bottle) using a single image and a reference object of known height (e.g., a notebook).

**Methodology** (Algorithm 8.1)

Assuming both objects stand on the same ground plane and the camera is level, we use the ratio of pixel heights:

$$H_{unknown} = h_{pixel\_unknown} \times \left( \frac{H_{ref}}{h_{pixel\_ref}} \right)$$


Interactive Tool: A Python script (click.py) allows users to click 4 points on an image.jpeg (Reference Top/Base, Unknown Top/Base).

Automated Calculation: The points are saved to JSON and processed to output the estimated height in meters/cm which are then used to add values into the main function.

Visualization: Generates an annotated image showing the measurement lines and calculated height.


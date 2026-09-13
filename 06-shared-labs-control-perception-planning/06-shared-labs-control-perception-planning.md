# Module 6: Shared Labs — Control, Kinematics, Perception, Planning

**Estimated time:** 5 weeks · **50–70 hours** (Standard) · Fast path: 2 weeks · 25–35 hours  
**Prerequisites:** Modules 1–5. You have a line follower and/or an arm, ROS 2 Python, and Module 4 math.

This module is **labs**, not a second undergraduate degree. You already tuned a P controller by feel. You already used libraries that hid IK and filters. Here you implement the thin versions that interviews and debugging actually use.

Defer LQR, MPC, screw theory, MoveIt Task Constructor, and Stachniss's full SLAM course to a track — or never, if your track does not need them.

## Goals

By the end of this module you should be able to:

- Implement PID from scratch, with a plot, and explain each term from data
- Compute forward kinematics for a 3-DOF chain by hand and solve IK numerically
- Calibrate a camera and turn a pixel into a ray / a 3D guess
- Run a small object detector on a camera image
- Grow an RRT in 2D and say what "sampling-based planning" means
- Run an EKF (or a documented library EKF) on a simulated differential-drive robot

## 6.1 PID, from data (not from vibes)

### What to learn

- What P, I, and D each do, and the failure mode of each
- Integrator windup
- Derivative noise and why you filter D
- Steady-state error: integrator vs. gravity compensation
- Feedforward — the cheapest improvement most people never add

You do **not** need Åström cover-to-cover. You do not need Brunton's full bootcamp unless you take a controls-heavy Autonomy or Embedded path later.

### Resources

| Resource | Format | Why | Path |
|---|---|---|---|
| [Understanding PID Control, Brian Douglas](https://www.mathworks.com/videos/series/understanding-pid-control.html) | Free videos | Windup, D-filtering, tuning | Mandatory |
| [The Fundamentals of Control Theory, Brian Douglas](https://engineeringmedia.com/books) | Free book | Written companion, skim matching chapters | Optional |
| [Control Bootcamp, Steve Brunton](https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m) | Free videos | State space / LQR — **Autonomy or curiosity**, not trunk | Optional |
| [Feedback Systems, Åström and Murray](https://fbswiki.org/wiki/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers) | Free PDF | Rigorous reference | Optional |

### Practice tasks

**Mandatory.** On the **line follower** (preferred) or a simulated plant if the robot is dead:

1. Implement PID **from scratch** (no library).
2. Log a step or a line disturbance to CSV.
3. Plot at least P vs. PD (or P vs. PD vs. PID).
4. Write which one you would ship and why.

If the Module 2 balancer still works, it is a better plant. Do not rebuild it for this lab.

**Optional.** Add feedforward. Show integrator windup, then a clamp or reset.

### Assessment criteria

- PID from scratch in your repo
- A plot you can talk about for five minutes
- You can explain windup with a sentence that mentions your own log

## 6.2 Kinematics (not dynamics)

The heading used to say "dynamics." Inverse dynamics and Lagrangians are not trunk material. Product-of-exponentials is cleaner than DH; you only need enough to compute FK and a numerical IK.

### What to learn

- Homogeneous transforms and composing them
- Forward kinematics
- Numerical inverse kinematics
- Jacobian and what a singularity **feels** like
- Joint limits vs. workspace
- Joint-space vs. Cartesian interpolation at slogan level

### Resources

| Resource | Format | Why | Path |
|---|---|---|---|
| [Modern Robotics, Kevin Lynch](http://hades.mech.northwestern.edu/index.php/Modern_Robotics) — chapters on FK, IK, Jacobians | Free | Standard treatment (PoE) | Mandatory chapters only |
| [Robotics Toolbox for Python](https://github.com/petercorke/robotics-toolbox-python) | Free | Verify your FK | Mandatory |
| [QUT Robot Academy](https://robotacademy.net.au) | Free | Short videos when a paragraph does not stick | Optional |
| Modern Robotics Coursera | Free audit | Deadlines | Optional |

### Practice tasks

**Mandatory.**

1. Compute FK for **3 DOF** of your arm (or a 3-DOF subset of SO-101) by hand from link lengths.
2. Verify against Robotics Toolbox or your own NumPy.
3. Write a numerical IK that drives the end effector to a commanded XY or XYZ.
4. Command a pose near a singularity and write what happened.

**Optional.** Full 5-DOF SO-101 FK. Jacobian matrix printed at a singular configuration. MoveIt pick-and-place (see 6.5 Optional).

### Assessment criteria

- 3-DOF FK by hand that matches code
- Numerical IK in your repo
- You can point at a configuration and say which freedom was lost

## 6.3 Camera calibration and a 3D guess

### What to learn

- Intrinsics and distortion
- Pinhole projection
- Pixel vs. ray vs. world point (you need depth or a plane assumption for the last one)
- Why lighting changes break naive vision

### Resources

| Resource | Format | Why |
|---|---|---|
| [OpenCV camera calibration tutorial](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html) | Free docs | Do this from memory eventually |
| [FREE OpenCV Bootcamp](https://courses.opencv.org/courses/course-v1:OpenCV+Bootcamp+CV0/about) | Free | Optional 2–3 hours if you have never touched images |

### Practice tasks

**Mandatory.** Calibrate a real camera (phone webcam is fine) with a printed chessboard. Report reprojection error. Undistort a frame.

**Mandatory.** Detect a coloured object **or** an ArUco marker and estimate a 3D position using a plane assumption or a known marker size. Then change the lighting and write what broke.

**Optional.** Open3D plane fit on a depth camera point cloud. Buy or borrow a RealSense / Orbbec if your track is Autonomy or Learning.

### Assessment criteria

- Calibration file + reprojection error in the README
- Pixel → 3D script with an explicit assumption (plane or marker size)
- Failure write-up when lighting changes

## 6.4 A modern detector (shallow)

Junior perception postings expect a detector, not only colour thresholding.

### What to learn

- What a bounding box, confidence, and class id are
- That you will not train YOLO from scratch this month
- Letterboxing, input size, and why a model that works on a demo video fails on your webcam

### Resources

Pick one maintained path (names move; use current Ultralytics or ONNX Runtime docs for a small YOLO-class model):

- Ultralytics YOLO quickstart on a webcam
- Or Roboflow / Hugging Face hosted model if you cannot install GPU drivers — CPU is fine for one lab

### Practice tasks

**Mandatory.** Run a pretrained detector on your webcam or a phone video. Record 20 seconds. Count false positives. Write three sentences on a failure mode (motion blur, class confusion, lighting).

**Optional.** Fine-tune on 50 images of an object you care about. This becomes track work if it grows.

## 6.5 Planning: RRT in 2D

Nav2 and MoveIt hide this. Interviews do not.

### What to learn

- Grid search (A*) vs. sampling (RRT / RRT*)
- Collision checking as the expensive core
- Completeness vs. optimality at slogan level

### Resources

- A short notebook: implement RRT in a 2D occupancy grid (many university gists; write your own 150 lines rather than wrapping OMPL)
- [Planning Algorithms, LaValle](http://lavalle.pl/planning/) — reference, not a course this month

### Practice tasks

**Mandatory.** 2D RRT from start to goal among rectangles. Animate or screenshot the tree. Change the step size and write what happened.

**Optional.** A* on the same map; compare path length and time. MoveIt simulated pick-and-place with one collision object — useful if you like arms, not required for trunk.

## 6.6 EKF on a differential-drive robot

Complementary filter was Module 2. Interviews say "Kalman." This lab is the bridge.

### What to learn

- Predict vs. update
- State `[x, y, θ]`, input as wheel or body velocity, measurement as GPS-like position or landmarks
- Why linearization (EKF) appears when motion is nonlinear
- You may use `filterpy` (Labbe) rather than writing every matrix from a blank file — but you must write the **state and measurement models** yourself

### Resources

| Resource | Format | Why |
|---|---|---|
| [Kalman and Bayesian Filters in Python, Roger Labbe](https://rlabbe.github.io/Kalman-and-Bayesian-Filters-in-Python/) — chapters through EKF | Free book | Best free filtering education |
| A unicycle / differential-drive kinematics page (any reputable notes) | Free | Motion model |

### Practice tasks

**Mandatory.** Simulated diff-drive with noisy odometry and occasional noisy position measurements. EKF tracks the pose. Plot true vs. odom vs. EKF.

**Optional.** Same filter on logged encoder + IMU from the line follower. This is Autonomy-track quality if you finish it.

## Module 6 Milestones

| Criterion | Test | Required? |
|---|---|---|
| PID from scratch + plot | CSV and figure on GitHub | Mandatory |
| 3-DOF FK by hand + numerical IK | Notebook or script on your arm geometry | Mandatory |
| Camera calibration + pixel to 3D with stated assumption | README numbers | Mandatory |
| Pretrained detector on your camera | Video + failure note | Mandatory |
| 2D RRT | Image of the tree | Mandatory |
| EKF on simulated diff-drive | Plot true / odom / EKF | Mandatory |
| LQR, MPC, Underactuated Robotics | — | Optional / track |
| MoveIt pick-and-place | — | Optional |
| Full OpenCV Bootcamp + Stachniss semester | — | Optional |

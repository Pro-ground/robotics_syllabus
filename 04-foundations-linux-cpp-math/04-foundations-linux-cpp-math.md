# Module 4: Foundations Patch — Linux, C++, and Enough Math

**Estimated time:** 2 weeks · **25–35 hours** (Standard) · Fast path: 1 week · 12–20 hours  
**Prerequisites:** Modules 1–3. You can write basic Python and use Git at the Module 1 level.

This is the patch that Module 5 used to assume you already had. ROS 2 on Ubuntu, one `rclcpp` node, Jacobians, and an EKF all require it. Two focused weeks here is faster than three confused months later.

## Goals

By the end of this module you should be able to:

- Install packages, edit files, and run commands on Ubuntu (native, dual-boot, or a VM/container)
- Explain compile vs. interpret, write a small C++ program, and build it with CMake
- Multiply a 3×3 matrix by a vector by hand and in Python/NumPy
- State what a derivative, a transpose, and a probability distribution are for in robotics
- Use Git branches and a pull-request-shaped workflow on your own repo

## 4.1 Linux

ROS 2's supported path is Ubuntu. Fighting Windows-native ROS is not a proficiency move.

### What to learn

- Filesystem, permissions, `apt`, `sudo`, environment variables
- Networking enough to SSH to a robot and `ping` it
- Why Docker exists (you will use a ROS image in Module 5 even if you never write a Dockerfile yet)
- systemd at "I can restart a service and read a log" level — Embedded and Autonomy tracks go further

### Resources

| Resource | Format | Why | Path |
|---|---|---|---|
| [The Missing Semester](https://missing.csail.mit.edu/) lectures 1–2, 5 | Free | Shell and command line, if you skipped them in Module 1 | Mandatory unless Fast-path skip |
| Ubuntu Desktop install guide for your version (24.04 if you will use ROS 2 Jazzy) | Free docs | Native or VM | Mandatory unless you already live on Ubuntu |
| [Docker Get Started](https://docs.docker.com/get-started/) (overview only) | Free | So Module 5's container option is not magic | Optional |

### Practice tasks

1. **Mandatory unless Fast-path skip.** Install Ubuntu 24.04 (dual-boot, spare machine, or a VM with at least 8 GB RAM assigned). Confirm you can `apt install` a package, edit a file with a terminal editor or VS Code, and clone a repo.
2. **Mandatory unless Fast-path skip.** SSH into that machine from another device, or from the host into the VM.
3. **Optional.** Pull `ubuntu:24.04` in Docker and run `uname -a` inside it.

### Assessment criteria

- Can you install a `.deb` package from the terminal and find the binary on `PATH`?
- Can you explain what `~/.bashrc` is for?
- Can you copy a file to another machine with `scp` or equivalent?

## 4.2 C++ as a tool (not a personality)

Job listings say C++ and Python. This module teaches **survival C++**: enough to read and write one ROS 2 node and not fear a compiler error. It does not teach template metaprogramming.

### What to learn

- Types, references, pointers at "why a dangling pointer crashes" level
- `std::vector`, `std::string`, range-for
- Headers vs. sources, include guards
- CMake: one library, one executable
- `unique_ptr` vs. raw `new` — prefer the first
- Compile error reading: the first error is the one that matters

### Resources

| Resource | Format | Why | Path |
|---|---|---|---|
| [A Tour of C++, selected chapters, or learncpp.com chapters 1–11](https://www.learncpp.com/) | Free | Practical beginner C++ | Mandatory unless you already write C++ |
| [CMake tutorial (official, basic project)](https://cmake.org/cmake/help/latest/guide/tutorial/index.html) Step 1–2 | Free | How robotics actually builds C++ | Mandatory unless Fast-path skip |
| [CppCoreGuidelines (skim)](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) | Free | What "modern C++" means in interviews | Optional |

Do not start *Effective C++* or template books this fortnight.

### Practice tasks

1. **Mandatory.** Write a C++ program that reads a CSV of timestamped sensor values and prints mean and max. Build it with CMake. Put it on GitHub.
2. **Mandatory.** Introduce a deliberate compile error, then a runtime error (out-of-range). Write three sentences on how you found each.
3. **Optional.** Same program with `std::unique_ptr` owning a small helper object.

### Assessment criteria

- Can you write and build a non-trivial ~50–100 line C++ program with CMake without copy-pasting a whole project you do not understand?
- Can you explain compile-time vs. run-time failure with an example from your repo?

## 4.3 Linear algebra, calculus, probability — only what Module 6 needs

You do not need a full engineering math year. You need fluency with the objects that appear in kinematics, PID, and an EKF.

### What to learn

- Vectors, dot and cross products, norms
- Matrix multiply, inverse of a 2×2 by hand, "singular" means "cannot invert"
- 2D rotation matrices; homogeneous transforms as a 3×3 (2D) or 4×4 (3D) that you can multiply
- Derivative as rate of change — enough to see why D in PID is noisy
- Integral as accumulated error — enough to see I-windup
- Mean, variance, Gaussian "bell curve" as a model of sensor noise
- Bayes at slogan level: prior, measurement, posterior — enough that Kalman is not mysticism

### Resources

| Resource | Format | Why | Path |
|---|---|---|---|
| [3Blue1Brown, Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) videos 1–6 | Free | Geometric intuition for vectors and matrices | Mandatory unless Fast-path skip |
| [Khan Academy, gradients / derivatives refresh](https://www.khanacademy.org/math/differential-calculus) as needed | Free | Only if derivatives are rusty | As needed |
| [Seeing Theory, basic probability](https://seeing-theory.brown.edu/) | Free | Distributions and variance | Mandatory unless Fast-path skip |
| NumPy [quickstart](https://numpy.org/doc/stable/user/quickstart.html) | Free | You will implement labs in Python | Mandatory |

### Practice tasks

1. **Mandatory.** On paper: rotate the point (1, 0) by 90° with a 2×2 matrix. Confirm in NumPy.
2. **Mandatory.** Multiply two 2D homogeneous transforms (translate then rotate). Show the point's final position by hand and in NumPy.
3. **Mandatory.** Sample 200 noisy measurements of a constant. Compute mean and variance in Python. Plot a histogram.
4. **Optional.** Inverse of a 2×2; then try a singular matrix and catch the error.

### Assessment criteria

- Can you multiply a rotation matrix and a vector without looking it up?
- Can you explain in one minute why a singular Jacobian means the arm cannot move in some direction?
- Can you explain measurement noise as a distribution, not as "the sensor is wrong"?

## 4.4 Git beyond init / push

### What to learn

- Feature branches, rebase vs. merge at "I know the difference" level
- `.gitignore` for `build/`, `__pycache__/`, bags, datasets
- Commit messages that say why
- How an open-source contribution looks: issue, small PR, CI

### Practice tasks

1. **Mandatory.** On your C++ CSV repo, open a branch, change something, merge back, push. History should show more than one commit.
2. **Optional.** Find a "good first issue" on a package you will actually use later (Nav2, LeRobot, ros2_control). You do not have to finish a PR this week. File a reproduction or a docs typo if you can do it honestly.

## Module 4 Milestones

| Criterion | Test | Required? |
|---|---|---|
| Ubuntu environment you control | `apt`, editor, git clone, SSH | Mandatory unless already true |
| C++ + CMake program on GitHub | CSV stats program builds from a clean clone | Mandatory |
| 2D transform by hand and in NumPy | Written + script | Mandatory |
| Noise as a distribution | Histogram + mean/variance | Mandatory |
| Git branch workflow | Visible on GitHub | Mandatory |

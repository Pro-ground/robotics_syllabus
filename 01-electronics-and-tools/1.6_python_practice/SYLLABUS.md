# Python for Robotics Software

A minimum path from zero Python to enough competence to handroll robotics software.

> **Target stack:** Python 3.12, Ubuntu 24.04, ROS 2 Jazzy LTS, rclpy, NumPy, and pytest.

Python is how most robot behaviour is tried, wired, and operated. C++ is how the hot path is finished. This syllabus stops at the point where you can write a package other people can launch — *not* at navigation internals, arms, or trained models.

Each topic below has a write-in file in this folder. Run it with `python`. If you get stuck, open the matching `*_answers.py` file. Phase 4 and 5 here stay as ordinary Python, so you can check a change by running the file again. A later ROS 2 workspace is a different job.

---

## Table of Contents

| Phase | Topic |
|-------|-------|
| **Phase 1** | Python you will actually type |
| **Phase 2** | Files, errors, and tests |
| **Phase 3** | Arrays and planar geometry |
| **Phase 4** | A ROS 2 node you can launch |
| **Phase 5** | One closed loop |

---

## Phase 1 — Python you will actually type

> **Math:** By the end of this phase you will step a body forward on a flat plane. That needs secondary-school algebra, sine and cosine, and heading as an angle in radians. You take a forward speed and a turning rate, advance them by a small time interval, and update position and heading. There is no calculus — only adding a little motion onto the last pose.

### Scripts, values, and functions

Run a file from the terminal. Numbers, booleans, strings, and "no value." Variables and formatted strings. Branching, loops, early returns, and functions with default arguments. Write small decision functions in the shape a sensor callback will later take.

### Lists, dictionaries, and shared data

Lists for sequences: scans, waypoints, samples. Dictionaries for named fields: parameters, JSON, message-like records. The important pitfall is not the data structure — it is that two names can point at the same object. If a callback must keep its own copy, make that copy on purpose.

### Modules and a project layout

Imports, packages, and the usual "only run this when I am the main file" guard. A virtual environment and `pip`. One boring project layout, reused every time.

### Consolidation Task — Pose Workshop

Represent a pose and a twist, step the pose forward from velocity, and keep a short history. Do not silently change the values you were given.

---

## Phase 2 — Files, errors, and tests

### Errors and logs

Catch failures, raise your own when a value is illegal, and log instead of printing. Learn to tell "the sensor did not arrive" from "this calculation is not allowed."

### Files, config, and time

Paths, JSON, and YAML. A clock that only moves forward — on a robot that matters more than the calendar. Enough file reading and writing to load parameters and dump a short log.

### Tests on functions

`pytest` on the functions you own. If a transform or a limit is wrong, a test should say so before a robot does.

### Consolidation Task — Log Parser

Read a folder of JSON samples, check the keys you expect, write a summary file, and exit with a failure code when a row is bad.

---

## Phase 3 — Arrays and planar geometry

> **Math:** Treat a list of numbers as a vector: add, scale, take a length, pick a component. Trigonometry returns in practical form — sine, cosine, and the two-argument arctangent that knows which quadrant you are in. Measure angles in radians and wrap them so they stay in a sensible range.
>
> You will use small matrices, mostly two-by-two, to rotate a point. Then put a rotation and a translation together so you can ask: where is this point if I am standing over there, facing that way? Plot when a result looks wrong; a picture is how you notice a heading wrapping the wrong way.

### NumPy

Multidimensional arrays, shape, and indexing. Do the work with array operations rather than a Python loop over every sample. Poses and scans start here.

### Planar geometry

Position, heading, rotation of a point, and a transform that includes both rotation and translation. Build this yourself before you import a geometry stack.

### Consolidation Task — Kinematics Library

A small installable package that can transform a point, step a pose forward, and wrap an angle, with tests and one plot of a simulated path.

---

## Phase 4 — A ROS 2 node you can launch

> **Math:** A frame is a named coordinate system. A transform is the arithmetic that takes a point or a pose from one name to another. You need to apply that transform and turn it around. Time is a single number on each message; subtract stamps to see how old a reading is.
>
> Laser data arrives as a range and an angle. On the plane that pair becomes an x and a y. Keep units explicit: metres, radians, metres per second.

### Workspace and the graph

Nodes, topics, and parameters. A colcon workspace and a Python package with an entry point. Use the command-line tools until listing nodes and topics is boring.

### An rclpy node

A node class with a publisher, a subscription, and a timer. Callbacks that return quickly. Parameters loaded from YAML.

### Stamps, frames, and a launch file

Common messages for velocity commands, laser scans, and stamped poses. Every pose needs a timestamp and a frame name. One launch file that starts your nodes. Recording a bag is the default way to freeze a run.

### Consolidation Task — Two-Node Stack

One node publishes a fake laser scan. Another reads it and publishes a velocity command. Launch both. Drive the stop distance from a parameter.

---

## Phase 5 — One closed loop

> **Math:** A wheeled robot on a plane can drive forward and turn. From those two numbers you can say how position and heading change. Odometry is that same step applied to what the wheels reported.
>
> A command is usually a heading or speed error, scaled and then limited. Clamp to a maximum speed and a maximum turn rate. A watchdog is a comparison against the clock: if the last good command is older than a timeout, publish zeros and sit still.
>
> Stay at rates Python can honestly hold — tens of times per second. Faster than that, without hitching, does not belong here.

### Drive a simulated wheeled robot

Differential-drive motion and integrated odometry. Read a sensor, aim at a point or follow a short list of waypoints, and publish a limited command.

### Stop when things go stale

Zero the command on shutdown and when the last good input is too old. Reject values that are not finite. This is the safety rule the rest of the stack assumes.

### Consolidation Task — Closed Loop

A differential-drive robot in a simulator, a Python node that uses odometry and a laser, commands that stay inside limits, a timeout that zeros those commands, tests on the geometry and the clamps, a launch file, and a bag of the run.

### Exercises in this folder

A `consolidation` file is a placeholder for the end-of-phase task. Fill it in after the files listed above it.

| File | Phase | Topic |
|------|-------|-------|
| `001_format_pick.py` | 1 | Functions, strings, and lists |
| `002_decisions.py` | 1 | Branching on a sensor value |
| `003_loops.py` | 1 | `for`, `while`, and `range` |
| `004_timed_loop.py` | 1 | Period, leftover wait, and a time step |
| `005_angles.py` | 1 | Degrees, radians, distance, heading |
| `006_dicts_copy.py` | 1 | Dictionaries and a copy you made on purpose |
| `007_env_pip.py` | 1 | Virtual environment and pip (lab) |
| `008_modules.py` | 1 | Import a file; run only as the main program |
| `009_pose_workshop.py` | 1 | Pose, twist, history; do not change the inputs |
| `010_consolidation_pose_workshop.py` | 1 | Placeholder: Pose Workshop |
| `011_file_io_json.py` | 2 | CSV in, JSON out |
| `012_error_handling.py` | 2 | Retries and a named error |
| `013_config_clock.py` | 2 | Settings file; a clock that only moves forward |
| `014_function_tests.py` | 2 | Tests in their own functions |
| `015_drive_log.py` | 2 | Clean a log, replay it, write JSON |
| `016_consolidation_log_parser.py` | 2 | Placeholder: Log Parser |
| `017_numpy_basics.py` | 3 | Arrays, variance, moving average |
| `018_numpy_robotics.py` | 3 | Rotate a point; blend two angle guesses |
| `019_kinematics.py` | 3 | Wrap, rotate, transform, step a pose |
| `020_consolidation_kinematics_library.py` | 3 | Placeholder: Kinematics Library |
| `021_pub_sub.py` | 4 | Send and receive on a named stream |
| `022_stamps_frames.py` | 4 | Stamp, frame name, range and angle to x,y |
| `023_two_node_stack.py` | 4 | Fake scan in, command out, stop distance |
| `024_consolidation_two_node_stack.py` | 4 | Placeholder: Two-Node Stack |
| `025_diff_drive.py` | 5 | Odometry and a limited command toward a point |
| `026_watchdog.py` | 5 | Zero the command if input is stale or not finite |
| `027_closed_loop.py` | 5 | One step: scan, command, limits, timeout, odometry |
| `028_consolidation_closed_loop.py` | 5 | Placeholder: Closed Loop |

---

## What this path leaves out

Tuples and sets, generators, asyncio, class hierarchies, quality-of-service catalogues, services and actions until a later job needs them, navigation and manipulation stacks, camera models, bindings into C++. Look those up when a specific robot demands them.

## What "done" means

From a blank workspace you can write a Python package that launches a node, reads a sensor, keeps a pose in a named frame, publishes a limited command, and zeros that command on timeout. The geometry is covered by tests. You can explain why two callbacks must not share the same mutable dictionary.

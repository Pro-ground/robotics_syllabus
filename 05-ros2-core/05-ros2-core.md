# Module 5: ROS 2 Core

**Estimated time:** 5 weeks · **50–70 hours** (Standard) · Fast path: 3 weeks · 35–45 hours  
**Prerequisites:** Module 4 — Ubuntu you control, survival C++, Git. Modules 1–3 hardware literacy. **This module does not assume you already know ROS 2.**

This is how companies wire robots. It is also the month people lose to install weekends. Prefer a **container or The Construct** on day one. Native install is fine if you already like Ubuntu package fights.

You write nodes in **Python first**. You write **one** C++ node so C++ is a tool, not a checkbox. You do not need Nav2 mastery here — that is the Autonomy track. You do not need MoveIt mastery here — one planned motion can wait for Module 6 Optional or the tracks.

## Goals

By the end of this module you should be able to:

- Write ROS 2 nodes in Python that use topics, services, and actions
- Write **one** equivalent node in C++ (`rclcpp`) and explain what differed
- Describe your own robot in xacro with frames, inertias, and collision geometry
- Simulate that robot in Gazebo with working LiDAR **or** camera
- Drive it through `ros2_control` rather than raw topic spam
- Record and replay a bag
- Diagnose a broken TF tree

## 5.1 Distro, install, and the ROS 1 trap

ROS 2 releases every May. Even years are LTS with five years of support; odd years get about 18 months.

| Distro | Codename | Release | EOL | Notes |
|---|---|---|---|---|
| **Lyrical** | Luth | May 2026 | May 2031 | Current LTS, targets Ubuntu 26.04 |
| **Jazzy** | Jalisco | May 2024 | May 2029 | **Start here** — more tutorials and courses still target Jazzy |
| Kilted | Kaiju | — | Dec 2026 | Do not start here |
| Humble | Hawksbill | — | May 2027 | Legacy |

**Start on Jazzy** unless your track employer already standardized on Lyrical. Move later when the tutorial stack catches up.

**Install options, in the order you should consider them:**

1. [The Construct](https://www.theconstruct.ai/) free tier — browser, no dual-boot
2. Official ROS 2 Jazzy Docker / VS Code Dev Container
3. Native Ubuntu 24.04 install

Pick one and stay on it for the module.

### The ROS 1 trap

ROS 1 is dead. Noetic reached end of life on 31 May 2025. Learn the signals:

**ROS 1:** `catkin_make`, `roscore`, `rosrun`, `rospy`, XML-only launch files  
**ROS 2:** `colcon build`, no master, `ros2 run`, Python launch files

If you see ROS 1 signals, close the tab or convert carefully. Do not start a new project in ROS 1.

### Estimated hours

- Distro install and a workspace that builds: 3–8 hours (budget a weekend if native)
- ROS 1 vs ROS 2 recognition: 1 hour

## 5.2 Graph concepts (Python first)

### What to learn

- Nodes, topics, services, and actions — which of the three a problem needs
- Custom `.msg` and `.srv`
- Parameters and YAML
- Python launch files, arguments, remaps
- `colcon` workspaces and package layout
- `ros2 bag` for anything that only fails occasionally
- QoS: when "it publishes but nothing receives," check reliability/durability before rewriting the node. Read the official Concepts pages. No popular course teaches this well.

### Resources

| Resource | Format | Why |
|---|---|---|
| [Official ROS 2 Tutorials (Jazzy)](https://docs.ros.org/en/jazzy/Tutorials.html) | Free docs | Canonical: nodes, topics, services, actions, parameters, launch, tf2, URDF |
| [The Construct](https://www.theconstruct.ai/) | Free tier / paid | Browser ROS, removes install pain |
| [Articulated Robotics](https://articulatedrobotics.xyz/tutorials/) | Free | End-to-end: URDF, sim, ros2_control, Pi, SLAM |
| [MOGI-ROS](https://github.com/orgs/MOGI-ROS/repositories) | Free | University course, Jazzy + Gazebo Harmonic |
| [Automatic Addison](https://automaticaddison.com/tutorials/) | Free | Recipe-style, Jazzy and Lyrical |
| [ROS 2 for Beginners, Edouard Renard](https://www.udemy.com/course/ros2-for-beginners/) | Udemy on sale | Optional video if you bounce off docs |

### Estimated hours

- Official tutorials through topics, services, actions, parameters, launch: 10–14 hours
- Practice graph: 6–10 hours

### Practice tasks

**Mandatory.** Multi-node system, no robot:

1. A sensor publisher
2. A processing node
3. A service for configuration
4. A parameterised aggregator

Use your own `.msg` / `.srv`, a Python launch file with arguments. Record a bag and replay it. Verify the data.

**Mandatory.** Rewrite **one** of those nodes in C++ (`rclcpp`). Same topic names, same message type. Do not rewrite the whole graph.

**Optional.** Pay for Renard or sit The Construct courses if docs are not sticking.

### Assessment criteria

- Can you explain topic vs. service vs. action?
- Can you define a custom message and use it in two nodes?
- Can you record and replay a bag?
- Can you point at your C++ node and say what the Python version did not force you to think about (types, lifetimes, executor)?

## 5.3 URDF, TF, and describing a robot

### What to learn

- URDF and xacro
- `robot_state_publisher` computes transforms from joint positions
- `joint_state_publisher` / `_gui` invents or publishes joint positions — it does not compute TF
- RViz
- Inertias: missing tags make Gazebo explode or sink
- Collision vs. visual geometry
- tf2 — the concept that blocks most people

### Common issues

| Problem | Fix |
|---|---|
| Confusing `joint_state_publisher` with `robot_state_publisher` | First invents joints, second computes TF |
| Missing inertial tags | Always include mass and inertia |
| Missing static transform to the sensor frame | Causes more beginner SLAM failures than any algorithm |
| 400 lines of XML | xacro from day one |

### Resources

| Resource | Format | Why |
|---|---|---|
| [Articulated Robotics, Coordinate Transforms](https://articulatedrobotics.xyz/category/coordinate-transforms-for-robotics) | Free | Frames and transforms |
| [Official URDF tutorial](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher-cpp.html) | Free docs | Canonical walkthrough |
| Renard Level 2 (Udemy) | Paid | Optional if you want video xacro |

### Practice tasks

**Mandatory.** Your own robot in xacro — not TurtleBot:

1. Differential-drive base **or** a simplified SO-101-style arm (pick the platform you will capstone in Module 7)
2. At least one sensor frame (lidar mast or camera / wrist camera)
3. Correct inertias
4. Separate collision and visual geometry
5. Full TF tree visible in RViz, driven by `joint_state_publisher_gui`

**Optional.** Two-DOF pan-tilt head on the rover.

### Assessment criteria

- URDF/xacro with at least 4 degrees of freedom (wheels + joints, or arm joints)
- TF tree complete in RViz
- Non-zero masses, finite inertias
- You can break a frame on purpose and fix it

## 5.4 Simulation (Gazebo enough)

Gazebo Classic (1–11) reached end of life in January 2025. Current Gazebo is Fortress / Garden / Harmonic / Ionic / Jetty. Pair it with your distro:

| ROS 2 | Gazebo |
|---|---|
| Humble | Fortress |
| Jazzy | Harmonic |
| Kilted | Ionic |
| Lyrical | Jetty |

| Simulator | GPU | Use now? |
|---|---|---|
| **Gazebo** | No | **Yes. This module.** |
| **MuJoCo** | No | Learning track / Module 6 optional |
| Isaac Sim | RTX 4080+ 16GB | Only if you already have the card and a reason |
| PyBullet | No | Skip — unmaintained |
| Genesis | No | Watch, do not portfolio on it yet |

### Practice tasks

**Mandatory.** Spawn your xacro robot in Gazebo. Add a LiDAR **or** camera plugin. Confirm data on a ROS 2 topic and in RViz. Teleop something (joints or base).

**Optional.** Custom SDF world with obstacles. Both LiDAR and camera.

### Assessment criteria

- Robot spawns without exploding
- Sensor data on the expected topic
- You can teleop in Gazebo through ROS 2

## 5.5 ros2_control

Most self-taught candidates have never touched this. One working config is enough for the trunk.

### What to learn

- Hardware interfaces, controller manager, `<ros2_control>` in xacro
- `diff_drive_controller` **or** a joint trajectory / forward command controller for an arm
- YAML
- The idea of sim-to-real: same controller, different hardware plugin

### Resources

| Resource | Format | Why |
|---|---|---|
| [ros2_control documentation](https://control.ros.org/jazzy/index.html) | Free docs | Prefer Jazzy docs, not Rolling, while you are on Jazzy |
| [Articulated Robotics, ros2_control on real hardware](https://articulatedrobotics.xyz/tutorials/mobile-robot/applications/ros2_control-real/) | Free | Sim-to-real narrative |

### Practice tasks

**Mandatory.** Add `<ros2_control>` tags. Configure a controller in YAML. Drive the robot in Gazebo with teleop or a scripted command.

**Optional.** Action server that drives a commanded distance (rover) or a joint goal (arm) with feedback and cancellation.

**Optional.** Follow Articulated Robotics onto a Raspberry Pi. This becomes Autonomy-track work if it grows.

### Assessment criteria

- YAML controller config you can explain line by line
- Robot moves via the controller, not by publishing wheel torques by hand

## 5.6 SLAM and Nav2 — literacy only

You need to **see** mapping and a Nav2 goal succeed in simulation so the words are not empty. Tuning costmaps, writing BT nodes, and real lidar platforms are the Autonomy track.

### Practice tasks

**Mandatory.** In a Gazebo world you did not have to invent from scratch (TurtleBot4 sim or your robot if it already works): run SLAM Toolbox, save a map, send **one** Nav2 goal from RViz, screen-record it.

**Optional.** Your own robot + your own world + costmap tuning. Do this in [`08-track-autonomy/08-track-autonomy.md`](../08-track-autonomy/08-track-autonomy.md).

### Assessment criteria

- You can say what a smeared map usually means (odometry) vs. a SLAM bug
- You have a video of a robot driving to a goal in sim

## Module 5 Milestones

| Criterion | Test | Required? |
|---|---|---|
| Python nodes with topics, services, actions, custom msgs, bag | Graph repo | Mandatory |
| One `rclcpp` node in the same graph | Builds and talks to the Python nodes | Mandatory |
| Own robot in xacro, correct TF and inertias | RViz screenshot + file | Mandatory |
| Gazebo + one sensor topic | RViz + topic echo | Mandatory |
| ros2_control teleop or scripted motion | Video | Mandatory |
| One Nav2 goal in simulation | Screen recording | Mandatory |
| Diagnose a broken TF tree | You break it, you fix it | Mandatory |
| Full Nav2 / costmap / BT / real lidar | — | Autonomy track |
| Nodes in C++ *and* Python for every concept | — | Not required |

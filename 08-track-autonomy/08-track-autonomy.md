# Track: Autonomy and Mobile Robotics

**Estimated time:** 12 weeks · **120–160 hours** (Mandatory only: ~80–100)  
**Prerequisites:** Module 7. You have a ROS 2 graph, a TF tree you can fix, and at least literacy Nav2 in sim.

Pick this track if you want the **largest number of robotics jobs**: AMRs, warehouse, outdoor robots, field service, "controls engineer" postings that are really navigation plus debugging.

Do **not** also complete the Learning and Embedded tracks.

## Goals

- Map, localize, and navigate in simulation with costmaps you tuned
- Explain smeared maps, TF errors, and QoS misses from your own logs
- Run an EKF or AMCL-style localization you can defend
- Write **one** piece of C++ that is not a tutorial clone (a node, a BT plugin, or a controller plugin)
- Optional: the same stack on a real lidar robot

## Mandatory projects

### 1. Your robot, your map, tuned Nav2

Use **your** Module 5 xacro robot (or a maintained TurtleBot sim if yours is still exploding — then schedule a week to fix yours).

1. Custom or substantially modified SDF world
2. SLAM Toolbox map that is not smeared
3. Localization mode
4. Nav2 to three goals without you touching the keyboard
5. Costmap inflation / obstacle layer notes: what you changed and why
6. Screen recording + bag of a failure and a success

**Hours:** 25–40

### 2. Localization lab on a log

Take a bag from project 1 (or the Module 6 EKF sim).

- Compare raw odom vs. AMCL or your EKF vs. "ground truth" (Gazebo pose)
- Plot error
- Break TF on the lidar frame on purpose, show the map die, fix it

**Hours:** 10–15

### 3. One C++ contribution to the stack

Examples that are enough:

- `rclcpp` node that filters scans or gates `cmd_vel` with a watchdog
- A trivial Nav2 BT plugin or a parameterised condition
- A small controller plugin that does "drive a heading"

Quality bar: builds on a clean clone, has a README, has a test or a recorded demo.

**Hours:** 15–25

### 4. Architecture write-up

One page: nodes, QoS choices, what happens when the lidar drops. This is interview bait.

**Hours:** 4–6

## Optional projects

- Real hardware: RPLIDAR C1 + Pi + encoder base (~$250–450 DIY) or MentorPi / Waveshare kit. Do **not** start hardware until projects 1–2 work in sim.
- GPS waypoint nav (Nav2 tutorial)
- Keepout zones, collision monitor, docking
- RTAB-Map if you have RGB-D
- Docker-compose that brings the whole stack up
- A* vs. Nav2 planner on the same map (reuse Module 6 RRT/A*)
- Field-service style: given a broken launch file, document the debug log

## Resources

| Resource | Why |
|---|---|
| [Nav2 tutorials](https://docs.nav2.org/jazzy/tutorials/) | SLAM, keepout, docking, custom planner/controller — **pin Jazzy** if that is your distro |
| [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox) | Default 2D SLAM |
| [Articulated Robotics](https://articulatedrobotics.xyz/tutorials/) | Pi + lidar narrative |
| Official ROS 2 QoS / Concepts | When topics go silent |
| Module 6 EKF + Labbe | When AMCL is a black box you cannot debug |

## Hardware (only if you do the real-robot optional)

| Tier | Cost | What |
|---|---|---|
| 0 | $0 | Stay in Gazebo. Valid for this track if the logs and plots are real. |
| 1 | $250–450 | RPLIDAR C1, Pi 4/5, encoder base, driver, battery |
| 2 | $300–535 | Hiwonder MentorPi M1 or Waveshare UGV Rover ROS 2 kit |

## Milestones

| Criterion | Required? |
|---|---|
| Untouched-keyboard Nav2 in **your** world with notes on costmaps | Mandatory |
| Localization error plot from a bag | Mandatory |
| One C++ node or plugin you can defend | Mandatory |
| Architecture + QoS page | Mandatory |
| Real lidar robot | Optional |
| Custom planner | Optional |

## What "done" looks like for jobs

Three polished artifacts: Nav2 video, localization plot, C++ repo. Apply to AMR, warehouse, and "ROS 2 navigation" roles while you start Module 11. Technician and field-service roles are valid entry points; they are not a consolation prize.

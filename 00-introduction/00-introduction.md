# Introduction

This syllabus is a structured, project-driven pathway that serves as a guide to learn robotics. It assumes zero electronics or design knowledge, and aims to equip a person with skills to get work in **one robotics specialism**, with literacy in the rest.

The main path teaches the physical stack that every specialism sits on: circuits, firmware, motors, CAD, and a short ROS 2 core. After a shared set of labs and one integration capstone, the student picks **one** of three tracks to study in more detail. The aim is to become proficient quickly.

This guide will not make you a senior robotics engineer. Rather, it will make you someone who can build, debug, and ship working robots, and prove it with a portfolio.

## Time model

The hours estimated in this syllabus include sufficient time to accomodate delays caused by failed prints, driver installs, and debugging actual robotics problems.

| Path | Who it is for | Pace | Duration |
|---|---|---|---|
| **Standard** | Starting from zero electronics; can already use a computer | **12–15 hours/week** | **12 months** |
| **Fast** | Already fluent in Python, Git, and a Linux terminal | **15–20 hours/week**, skip marked Fast-path skips | **6 months** |
| **Part-time slow** | Less than 8 hours/week | Same modules, same order | **18 months** |

Note: The guide contains a 'fast path', indicated by the option to skip sections.

Students should only skip items tagged with the *Fast-path skip* label. Do not skip Mandatory tasks. If you cannot already write a Python script, use virtualenvs, and survive on the command line, you are on the Standard path.

## Why this syllabus exists

Most robotics learning paths fail for the same reasons:

1. **They start too high.** People buy an Arduino kit, blink an LED, and never learn why the circuit worked or how to debug it when it doesn't.
2. **They skip the physical layer.** Someone learns ROS 2 without knowing what a PWM signal is, then wonders why nothing works on real hardware.
3. **They learn only one layer.** A pure software person can train a policy but cannot make a motor turn. A mechanical designer can model a bracket but cannot wire it.
4. **They collect certificates, not projects.** A portfolio is made of things that moved, not courses you finished.
5. **They stay generalists forever.** Full-stack literacy is useful. Hireable proficiency is depth in one job.

If your goal is to become a robotics engineer, you do not need a mechanical engineering degree. You need to be able to make physical things do what you tell them to, reliably. You also need a portfolio that proves you can do this.

## What a robotics engineer actually does

The job splits into 'specialisms'. Robotics engineers typically pick one and maintain literacy in the rest:

- **Perception and computer vision** — cameras, LiDAR, point clouds, object detection
- **Controls and state estimation** — PID, Kalman filters, IMUs, sensor fusion
- **Motion planning and manipulation** — path planning, trajectory generation, grasping
- **Robot learning** — imitation learning, reinforcement learning, vision-language-action models
- **Embedded and firmware** — microcontrollers, RTOS, motor control, real-time timing
- **Simulation** — Gazebo, MuJoCo, Isaac Sim, URDF/SDF modeling
- **Systems and integration** — tying sensors, actuators, controllers, and planners together
- **Deployment and operations** — reliability, functional safety, field service, maintenance

A job listing will say “C++ and Python, both” and “experience on real hardware.” It will rarely say “specific degree.” It will often list “debugging” as a skill.

## How the pathway is organized

```
Modules 1–3     Foundational: electronics, robots, CAD / arm
Module 4        Coding and maths patch: Linux, C++ survival, linear algebra
Module 5        ROS 2 core (Python first, one C++ node)
Module 6        Shared labs: PID, kinematics, camera, YOLO, RRT, EKF
Module 7        Integration capstone (same robot, several layers)
Modules 8–10    Pick ONE track: Autonomy / Embedded / Learning
Module 11       Portfolio and interviews (overlaps the last month of your track)
```

Each module contains:

- **Concepts** — what you need to understand
- **Resources** — curated reading, video, and interactive materials
- **Estimated hours** — build time, not watch time
- **Practice tasks** tagged **Mandatory**, **Optional**, or **Fast-path skip**
- **Assessment criteria** — how to know you have actually learned it

Work the foundational modules in order. After Module 7, open only the track you chose. Do not collect all three tracks unless you have another year.

### Mandatory / Optional / Fast-path skip

| Tag | Meaning |
|---|---|
| **Mandatory** | Required for the milestone. If you skip it, you do not have proficiency at this layer. |
| **Optional** | Builds depth. Do it if you have time or if it matches your intended track. |
| **Fast-path skip** | Standard-path learners should still do it. Fast-path learners may skip if they can already pass the assessment without it. |

### Suggested calendar (Standard, 12 months)

| Months | Module | Hours |
|---|---|---|
| 1–2 | 1 Electronics and tools | 80–100 |
| 3–4 | 2 Microcontrollers and first robots | 90–120 |
| 5–6 | 3 Mechanical design and CAD | 80–120 |
| 6 (last 2 weeks) | 4 Foundations patch | 25–35 |
| 7 | 5 ROS 2 core | 50–70 |
| 8 | 6 Shared labs | 50–70 |
| 9 | 7 Integration capstone | 40–55 |
| 10–12 | One specialization track + Module 11 | 120–160 |

### Suggested calendar (Fast, 6 months)

You already write Python, use Git, and live in a Linux terminal.

| Weeks | What | Notes |
|---|---|---|
| 1–3 | Module 1 Mandatory only | Fast-path skip CS50P and long textbook reads |
| 4–7 | Module 2 Mandatory only | Line follower required; balancer optional |
| 8–11 | Module 3 Mandatory only | Single follower arm; skip the printed reducer |
| 12 | Module 4 | C++ and math only; skip Linux/Git you already have |
| 13–15 | Module 5 Mandatory only | |
| 16–17 | Module 6 Mandatory only | |
| 18–19 | Module 7 | |
| 20–26 | One track (Mandatory only) + Module 11 | |

## Hardware costs

Tiers where hardware applies:

- **Tier 0** — simulators only. Zero cost. Learn the concept before buying anything.
- **Tier 1** — minimum kit. Enough to build the Mandatory projects.
- **Tier 2** — adds essential tools (soldering iron, better multimeter, solder, etc.).
- **Tier 3** — bench power supply, **USB oscilloscope or equivalent**, **logic analyzer**, storage.

Prices are approximate and sourced from major vendors as of September 2026. They will change. The relationships between tiers matter more than any single price.

| Spend | Typical total | What it unlocks |
|---|---|---|
| Tier 0 | $0 | Simulation literacy only. You can finish ROS, labs, and much of Learning. You cannot claim hardware proficiency. |
| Trunk Tier 1 | ~$360–$620 | Line follower + single SO-101 follower (print yourself or use a service) |
| Trunk Tier 2 | ~$800–$1,200 | Soldering, better tools, more reliable builds |
| Trunk Tier 3 | ~$1,000–$1,500 | Scope, logic analyzer, bench PSU — required if you take the Embedded track seriously |
| Track extras | $0–$500 | Autonomy real lidar platform, or Learning GPU time / extra demos |

The 3D printer and the robot arm are the two largest single costs. A printer does not pay for itself on one build. It pays for itself on iteration: the tenth revision of a bracket costs 40 cents and 25 minutes at home, against $8 and a week from a print service.

**Fast hardware path:** single SO-101 follower (~$122 plus filament or a $31 printed set), no printer if you use a Fab Lab or JLC3DP, no leader arm (use sim or a gamepad for teleop).

## The three tracks (pick one after Module 7)

By Module 7 you have literacy across the physical stack, ROS 2, and a few core algorithms. Then you choose one direction.

| Track | File | Best for | Job market |
|---|---|---|---|
| **Autonomy / Mobile robotics** | [`08-track-autonomy/08-track-autonomy.md`](../08-track-autonomy/08-track-autonomy.md) | Largest number of jobs | Nav2, SLAM, perception, C++, field service |
| **Embedded / Mechatronics / Integration** | [`09-track-embedded/09-track-embedded.md`](../09-track-embedded/09-track-embedded.md) | Immediate employment, contracting | Firmware, RTOS, motor control, safety, integration |
| **Robot learning / Embodied AI** | [`10-track-learning/10-track-learning.md`](../10-track-learning/10-track-learning.md) | Frontier companies, highest ceiling | LeRobot, imitation learning, RL, PyTorch |

Literacy in the other two is enough. Depth in all three is a career, not a syllabus.

## Success metrics

By the end of the Standard path you should be able to:

1. Read a schematic and build the circuit it describes on a breadboard
2. Program a microcontroller to drive motors and read sensors in real time
3. Model a part in CAD, manufacture it, and have it fit
4. Write ROS 2 nodes, describe a robot in xacro, and record a bag
5. Implement a PID controller, compute forward kinematics, calibrate a camera, and run a shallow planning and filtering lab
6. Put **the same robot** under ROS 2 with logging and a safety cutoff (Module 7)
7. Show depth in **one** track, not a survey of all three
8. Answer three levels of follow-up questions about any line of your own code
9. **Build at least six working projects; polish three** for applications (video, metrics, failure analysis)

## A note on honesty

This syllabus will not make you a senior robotics engineer in six or twelve months. What it will make you is someone who can build, debug, and ship working robots, who understands the stack from the electrical layer up to a planner or a learned policy, and who has the physical portfolio to prove it.

That is enough to get you into the field, and the field is where you compound your talents.

# Module 7: Integration Capstone

**Estimated time:** 4 weeks · **40–55 hours**  
**Prerequisites:** Modules 1–6 Mandatory work. Pick **one** physical or simulated platform you already have.

Survey modules stack layers. Proficiency is the same machine with several layers on at once. This module is that project. It is Mandatory for both Standard and Fast paths.

## Choose one platform and do not switch

| Platform | Use if | Strength |
|---|---|---|
| **Line-follower / rover chassis from Module 2** | You built it and it still drives | Best for Autonomy-leaning learners; natural odometry and bags |
| **SO-101 or other arm from Module 3** | You calibrated it | Best for Learning- or manipulation-leaning learners |
| **Gazebo model from Module 5 only** | Hardware is dead, in customs, or illegal to import | Valid. Label the portfolio "sim capstone." You must still do logging and a safety cutoff in software |

Do not buy a new robot for this module.

## Goals

On **one** robot, you should be able to:

1. Describe it in ROS 2 (reuse Module 5 xacro or finish it)
2. Command it through a controller, not an Arduino sketch you cannot observe
3. Log a bag (or equivalent synchronized log) of the run
4. Enforce a **safety cutoff** you can demonstrate
5. Deploy **one** skill from Module 6 on that same robot (classical or learned)
6. Publish a README with video, architecture diagram, metrics, and "What broke and how I fixed it"

## What "safety cutoff" means here

This is not ISO certification. It is the habit.

Pick at least one hardware-plausible rule and **show it fire**:

- E-stop button or key that zeros commands
- Watchdog: if the PC / ROS node dies, firmware stops the motors within a declared time
- Current or tilt limit that disables PWM
- Workspace box: arm command outside a cube is rejected
- Software timeout: no command for 200 ms → brake

Film the cutoff. Write the latency you measured (even if it is "about 80 ms on a phone stopwatch").

## Suggested shapes (pick one)

### A. Rover under ROS 2

- ESP32 or Pi as the real-time / Linux computer you actually have
- `ros2_control` or a thin bridge node (serial/UDP) if full ros2_control on the ESP32 is too much — document the trade
- Bag: cmd_vel, wheel ticks, one sensor
- Safety: e-stop or timeout
- Skill: PID heading or line hold from Module 6, **or** the EKF pose on a short run, **or** "detector sees red, robot stops"

### B. Arm under ROS 2

- Joint states published
- Scripted or joystick pose
- Bag: joints, commanded pose
- Safety: workspace box or dead-man timeout
- Skill: numerical IK to a camera-seen marker, **or** detector + "move above the object" (no need for a perfect grasp)

### C. Sim-only

Same checklist in Gazebo. Safety cutoff is still mandatory (timeout or workspace). Skill still mandatory. README must say sim-only in the first paragraph.

## What not to do

- Do not start Nav2 from scratch if you chose the arm
- Do not train ACT this month unless you already have the dataset and it is your track sneak-preview — Training belongs in Module 10
- Do not rewrite the URDF three times. Freeze geometry in week 1
- Do not add a second robot

## Week rhythm

| Week | Focus |
|---|---|
| 1 | Bring-up: robot in ROS 2, TF, one command path |
| 2 | Logging + safety cutoff, filmed |
| 3 | One Module 6 skill on this robot |
| 4 | Metrics, README, 90-second video, freeze the repo |

## Assessment criteria (all Mandatory)

- Architecture diagram (boxes: sensors, compute, actuators, ROS nodes)
- Video ≤ 2 minutes: idle, skill, **cutoff firing**, recovery or safe stop
- Bag or log file linked or described (if too large for GitHub, say where it lives)
- One quantitative metric: cutoff latency, tracking error, success rate over N trials
- "What broke and how I fixed it" with at least two real failures
- You can answer three levels of questions about **this** repo

## After this module

Open **exactly one** of:

- [`08-track-autonomy/08-track-autonomy.md`](../08-track-autonomy/08-track-autonomy.md)
- [`09-track-embedded/09-track-embedded.md`](../09-track-embedded/09-track-embedded.md)
- [`10-track-learning/10-track-learning.md`](../10-track-learning/10-track-learning.md)

Then use [`11-portfolio-and-career/11-portfolio-and-career.md`](../11-portfolio-and-career/11-portfolio-and-career.md) in the last month of that track. Do not start a second track until you have applied somewhere with the first.

# Module 11: Portfolio, Interviews, and Entering the Field

**Estimated time:** Overlaps the last 4 weeks of your track · **20–35 hours**  
**Prerequisites:** Module 7 plus Mandatory work on **one** track.

This is not a third survey of robot learning. The learning projects live in [`10-track-learning/10-track-learning.md`](../10-track-learning/10-track-learning.md).

## Goals

- State which track you are on and why
- **Polish three** of the **six or more** projects you built
- Answer three levels of follow-up questions about your own code
- Apply before you feel ready

## What to polish

You should already have at least six working artifacts across the trunk (line follower, CAD part / arm, ROS graph, Module 6 labs, capstone, track project). Recruiters will not watch six. They will watch **three**.

Pick:

1. **The capstone** (Module 7) — always
2. **The best track project** — always
3. **One more** that shows a different layer (electronics debug, CAD fit, PID plot, Nav2, firmware watchdog, or LeRobot numbers)

Each of the three READMEs needs:

1. A video at the top
2. A wiring or architecture diagram
3. The actual numbers you measured
4. **"What broke and how I fixed it"**

High signal:

- Commit history that shows iterative debugging, not one dump commit
- Real-robot deployment with reliability data when you have hardware
- A public dataset if you are on the Learning track
- A small, honest contribution to a package you use
- Systems work that joins sensors to actuators with a cutoff

Red flags:

- ROS 1 with no ROS 2 evidence
- Projects that die on the third question
- Pure deep learning with no embodiment
- Tutorial certificates instead of repos

## Interviews

Robotics interviews are not generic software interviews. LeetCode is a weaker predictor here. You should be able to do the Module 6 labs on a whiteboard at half speed:

- Inverse kinematics intuition
- PID and windup
- Complementary filter vs. Kalman / EKF
- SLAM vs. localization; smeared maps
- A* vs. RRT
- C++ vs. Python trade-offs
- A debugging story from **your** capstone
- A ROS 2 graph on a whiteboard (topics, when you would use an action)

At better companies: a broken MuJoCo or Gazebo scene; a ROS architecture scoped to their robot.

Practice: someone interrogates you about your repo for twenty minutes. Why that gain, why that sensor, what happens if the battery sags, what you tried first.

[Glassdoor robotics engineer questions](https://www.glassdoor.com/Interview/robotics-engineer-interview-questions-SRCH_KO0,17.htm) exist if you want volume. Your own code is a better use of the same hour.

## The demand picture (honest)

Physical-AI capital has been large (Crunchbase and trade press through 2026). Hiring lags capital. North American robot orders have been roughly flat in units in some recent half-years (A3). BLS codes that contain robotics engineers are not growing like software. Robotics is a smaller labour market than software.

The accurate claim is not "everyone will get hired." It is that money is arriving faster than people who can make machines work, that shortages are **specialism-specific**, and that the entry tier is unusually open without a degree.

Largest posting volume is often **Automation and Robotics Technician**. Many of those roles accept an associate's degree or a certificate (O*NET). That is a real on-ramp.

## Pay (ranges, US-centric, sources disagree)

| Level | US range | Notes |
|---|---|---|
| Entry | $80k–$100k | Payscale/Salary.com-class figures |
| O*NET/BLS median | ~$123k | Official-ish blended figure |
| Mid (3–6 years) | $120k–$165k | Conventional employers |
| Senior | $160k–$230k | Mainstream |
| Frontier physical-AI | $200k–$400k+ | Base at a few labs; equity-weighted |

Outside the US, medians are much lower (Germany ~€70k, UK base often £32k–£50k, India far below US intern pay). Always check a current local source.

Teleop / data collection can be $22–$35/hour with no degree — often on-site in expensive cities. Technician median is a different, more stable number (BLS). Neither is "I trained π₀."

## Entry points that do not require a degree

- Teleoperation and data collection
- Robotics technician / field service
- Internship or contractor bring-up work from the Embedded track
- A small ROS or firmware contract if your Module 7 repo is embarrassingly clear

## Practice tasks

**Mandatory.** Rewrite the three READMEs to the standard above.

**Mandatory.** One mock interview on the capstone repo (friend, mentor, or a recorded self-interrogation — worse, still useful).

**Mandatory.** Send **three** applications or three cold, specific messages (internship, technician, startup) before you add another optional lab.

**Optional.** One documentation PR or issue on Nav2, LeRobot, ros2_control, or MoveIt.

## Milestones

| Criterion | Test |
|---|---|
| Track chosen and justified in one paragraph | Top of your GitHub profile or a site README |
| Three polished projects | Video, numbers, failure analysis |
| Six+ projects exist in some form | You did not only polish |
| Three-deep answers on your own code | Mock interview |
| Applications sent | Three, dated |

## What to take away

1. **Build the Mandatory projects.** Optional is optional.
2. **Write down what broke.** That section is the part that cannot be faked from a tutorial.
3. **Apply before you feel ready.** The gap between "I am learning robotics" and "I work in robotics" is mostly nerve plus one repo a stranger can run.
4. Twelve months at 12–15 hours/week, or six if you already program, is enough to change what you can do with your hands. It is not senior. It is entry.

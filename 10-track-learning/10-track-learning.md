# Track: Robot Learning and Embodied AI

**Estimated time:** 12 weeks · **120–160 hours** (Mandatory only: ~80–110)  
**Prerequisites:** Module 7. You have an arm (or MuJoCo) and you can record a synchronized log.

Pick this track if you want **frontier / embodied-AI** work: imitation learning, datasets, policies on hardware. It is the highest ceiling and the most competitive. A dataset **you** collected beats another notebook on PushT.

Do **not** treat CS 285 as the track. Lectures support the projects; they do not replace them.

## Goals

- Record demonstrations, train a policy, deploy, measure, improve
- Explain behaviour cloning vs. ACT vs. diffusion policy, with failure modes
- Fine-tune or run **one** small VLA (SmolVLA-class) once, so the acronyms are not theoretical
- Change a reward in sim and watch behaviour change
- Publish numbers, not vibes

## Mandatory projects

### 1. LeRobot record–train–deploy–retrain

On SO-101, xArm, or MuJoCo if that is your honest hardware situation:

1. One simple task (cube in bin, or "open drawer" in sim)
2. **50** demonstrations
3. Train ACT (or the current LeRobot-recommended baseline)
4. Deploy. Measure success over ≥20 trials
5. Record **50 more** demos that cover the failure modes
6. Retrain. Measure again
7. README table: success before / after, what the extra data fixed

Follow [LeRobot docs](https://huggingface.co/docs/lerobot/index) and the [SO-101 guide](https://huggingface.co/docs/lerobot/so101).

**Hours:** 35–50 (data collection dominates)

### 2. Dataset quality note

One page in the repo:

- How you standardized the start pose
- How you handled gripper bounce and occlusion
- Three examples of a sloppy demo you **rejected**

**Hours:** 4–6

### 3. One VLA contact

Run **SmolVLA** (or the current compact open model recommended for your hardware) on a documented task. Fine-tune if you have the VRAM; otherwise run inference on a public checkpoint and write what transferred and what did not.

You do not need OpenVLA 7B. You do not need to recite every model in a table unless you have run or read each paper.

**Hours:** 10–20

### 4. RL in sim, one behaviour change

[MuJoCo Playground](https://github.com/google-deepmind/mujoco_playground) Colab or local:

1. Train the stock locomotion or manipulation tutorial
2. Change the reward
3. Show a before/after clip and a sentence on the gait or policy change

Isaac Lab is Optional and needs RTX hardware. Do not block the track on it.

**Hours:** 8–15

## Optional projects

- Diffusion Policy on the same dataset; compare success vs. ACT
- Upload a dataset to the LeRobot Hub
- CS 285 selected lectures (imitation, policy gradients) — **after** project 1 exists
- Isaac Lab sim-to-real if you have the GPU
- Wrist camera + Module 6 detector as a crude "is the object there?" success signal
- A small contribution to LeRobot docs or an issue with a reproduction

## VLA literacy (do not memorize as a substitute for project 3)

| Model | Open weights? | Notes |
|---|---|---|
| π₀ / π₀-FAST / π₀.₅ | Yes (Apache 2.0) | Transfer to your robot is not guaranteed |
| OpenVLA | Yes | Large; read, do not start here on an SO-101 |
| GR00T N1.x | Code open; weights under NVIDIA license | Often mis-described as Apache |
| SmolVLA | Yes | Right size for this track |
| RT-2 | No public weights | Paper only |

## Resources

| Resource | Why |
|---|---|
| [LeRobot](https://huggingface.co/docs/lerobot/index) | Default stack |
| [Hugging Face Robotics Course](https://huggingface.co/learn/robotics-course/unit0/1) | Sim/units if the arm is in the mail |
| [CS 285, Levine](https://rail.eecs.berkeley.edu/deeprlcourse) | Optional theory |
| [Isaac Lab](https://github.com/isaac-sim/IsaacLab) | Optional, GPU-heavy |

## Hardware

| Path | Notes |
|---|---|
| Leader + follower SO-101 | Best data quality |
| Follower + gamepad / phone teleop | Fast path from Module 3 |
| MuJoCo only | Allowed; say so; weaker for "real robot" jobs |
| GPU | Colab is enough for ACT and Playground. A local 8–16 GB card makes iteration saner. |

## Milestones

| Criterion | Required? |
|---|---|
| ACT (or baseline) on **your** data with before/after success rates | Mandatory |
| Dataset quality page with rejected demos | Mandatory |
| One SmolVLA-class run with a transfer note | Mandatory |
| Reward-change RL clip | Mandatory |
| Diffusion comparison, Hub upload, Isaac, CS 285 | Optional |

## What "done" looks like for jobs

The metric table and the second dataset are the portfolio. Apply to robot-learning internships, data collection / teleop roles at frontier labs (a real foot in the door), and smaller embodied-AI startups. Do not claim "I do VLAs" if you only read the table.

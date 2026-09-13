# Module 2: Microcontrollers, Motors, Sensors, and Your First Robots

**Estimated time:** 8 weeks · **90–120 hours** (Standard) · Fast path: 4 weeks · 50–70 hours  
**Prerequisites:** Module 1 — you can read a schematic, build a circuit, and write basic Python. Soldering can still be in progress if you are on Tier 1.

## Goals

By the end of this module you should be able to:

- Drive a motor at a controlled speed using PWM and understand the difference between duty cycle and actual RPM
- Read an encoder and close a position loop around it
- Wire and read an I2C sensor from its datasheet without a tutorial
- Fuse accelerometer and gyroscope data into a stable angle estimate
- Explain what P, I, and D each do by describing what your robot did when you changed them
- Show **one** working robot on GitHub with wiring, code, and a written account of what broke (two if you do the balancer)

## 2.1 Arduino

Start on Arduino rather than ESP32 because the ecosystem is enormous and every tutorial targets it. You will move to ESP32 within weeks, and nothing you learn here is wasted.

### What to learn

- `digitalWrite`, `digitalRead`, `analogRead`, `analogWrite` — what PWM actually is
- Interrupts — why polling a button in a loop eventually fails you
- I2C and SPI — how to wire them and how to read a sensor datasheet to find the address
- Serial debugging — your primary tool for months
- Non-blocking timing with `millis()` instead of `delay()` — `delay()` ruins every robot you build
- Debouncing — hardware (capacitor) vs. software (timer)
- Serial communication — UART at the protocol level
- A three-state loop: **idle / run / fault**. Every later robot is this machine with more states.

### Resources

| Resource | Format | Why |
|---|---|---|
| [Paul McWhorter, Arduino Lessons](https://toptechboy.com/arduino-lessons/) | Free videos | Over 100 lessons taught slowly with homework |
| [Arduino Built-in Examples](https://docs.arduino.cc/built-in-examples/) | Free docs | Runnable sketches already inside your IDE |
| [Arduino Official Docs, Learn](https://docs.arduino.cc/learn/) | Free docs | Authoritative reference for digital/analog I/O, PWM, I2C, SPI, UART |
| [Arduino Project Hub](https://projecthub.arduino.cc/) | Free | 6,000+ projects with wiring and code |

### Estimated hours

- McWhorter: pick 8–10 key lessons, not all 100: 6–8 hours
- Arduino docs as lookup: 2–3 hours
- Practice tasks: 6–10 hours

### Practice tasks

**Mandatory.** Reaction-timer game:

1. An LED fires after a random delay
2. A button stops the clock
3. The time in milliseconds prints to serial
4. It uses interrupts, debouncing, and non-blocking timing
5. It has a score

This is demonstrable in 15 seconds of video and teaches interrupts, debouncing, and non-blocking timing.

**Optional.** Add an idle / run / fault state machine (fault = button held for 2 s, or a disconnected sensor).

### Assessment criteria

- Can you read an I2C sensor by opening its datasheet and finding the register addresses?
- Can you replace `delay()` with `millis()` in an existing sketch?
- Can you explain why `delay()` blocks everything else running on the microcontroller?

## 2.2 ESP32

The ESP32 is where you go the moment you want WiFi, Bluetooth, more processing power, or two cores — and it is cheaper than an Arduino Uno.

- Buy an ESP32-S3 as your main board (most capable current variant)
- Buy one classic ESP32 so older tutorial code runs unmodified (Optional)
- Seeed XIAO ESP32-C3 for when you need something tiny (Optional)

**Decision framework:**

| Approach | When to use |
|---|---|
| Arduino framework | Speed to a working robot, largest library ecosystem — **use this for Module 2** |
| ESP-IDF | Real control over tasks, cores, power, timing — Embedded track, not this month |
| MicroPython | Fast sensor experimentation — NOT for a balancing loop (garbage collection pauses wreck timing) |

### Resources

| Resource | Format | Why |
|---|---|---|
| [Random Nerd Tutorials, Getting Started with ESP32](https://randomnerdtutorials.com/getting-started-with-esp32/) | Free | Highest-signal free tutorial library for this chip, 250+ project index |
| [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/index.html) | Free docs | Source of truth once you outgrow the Arduino layer |
| [Arduino ESP32 Core documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/) | Free docs | Espressif's own docs for the Arduino layer |
| [DroneBot Workshop ESP32 hub](https://dronebotworkshop.com/esp32-2/) | Free | Long-form, wiring-diagram-heavy tutorials |

### Hardware prices (verified, September 2026)

| Board | Price | Source |
|---|---|---|
| ESP32-S3-DevKitC-1, 8MB flash | $15.95 | Adafruit |
| Classic ESP32 Dev Board | $15.00 | Adafruit |
| Seeed XIAO ESP32-C3 | $4.99 | Seeed Studio |
| Generic ESP32 clones | $4–9 (approx.) | AliExpress |

### Practice tasks

**Mandatory.** Set up an ESP32-S3 in the Arduino IDE, upload Blink, then read one analog or I2C sensor over serial.

**Optional** (fun; not on the robotics critical path). Serve a web page from the ESP32 that shows live sensor readings and buttons that drive a servo, accessed from your phone on the same network.

### Assessment criteria

- Can you set up an ESP32-S3 in the Arduino IDE and upload a sketch?
- Can you explain the difference between Arduino framework and ESP-IDF in one paragraph?
- Optional: can you serve a page from the ESP32 and control hardware from it?

## 2.3 Motors, Drivers, and Actuation

This is where electronics stops being abstract — motors draw real current and behave badly. Four types matter. You must **use** brushed DC + encoder. You must **know** the other three exist.

| Motor type | Characteristics | Use case |
|---|---|---|
| **Brushed DC gearmotor** | Cheap, needs an H-bridge, no position feedback unless you add an encoder | Default for a first rover |
| **Hobby servo** | Internal closed loop, ~180° travel, no feedback out | Simple position control |
| **Smart serial bus servo** | Daisy-chained, position/velocity/current feedback, 12-bit magnetic encoder | Modern low-cost arms (Module 3) |
| **Stepper** | Open-loop absolute positioning, high holding torque | Precision positioning, CNC |

**What to memorize:** The L298N is in every tutorial and you should **not** use it. It is an obsolete bipolar-transistor H-bridge that drops about 2V across its output stage, gets hot, and wastes your battery. Learn it because the tutorials use it, then switch to the TB6612FNG or DRV8833.

Also learn: a **power budget**. Spreadsheet columns: device, voltage, typical current, stall/peak current, duty. If stall current × motors > regulator or battery rating, you will brown out. That is the Module 1 verbal exam made quantitative.

### Resources

| Resource | Format | Why |
|---|---|---|
| [DroneBot Workshop, Controlling DC Motors with L298N](https://dronebotworkshop.com/dc-motors-l298n-h-bridge/) | Free | DC motor theory, PWM, H-bridge internals — then do not use this driver |
| [SparkFun TB6612FNG Hookup Guide](https://learn.sparkfun.com/tutorials/tb6612fng-hookup-guide/all) | Free docs | Pinout, wiring, library — why this is the driver you should actually use |
| [DroneBot Workshop, Stepper Motors with Arduino](https://dronebotworkshop.com/stepper-motors-with-arduino/) | Free | Unipolar vs. bipolar, microstepping, NEMA sizing |
| [SimpleFOC documentation](https://docs.simplefoc.com/) | Free docs | Field-oriented control — Embedded track on-ramp, not this month |

### Hardware prices (verified)

| Component | Price | Source |
|---|---|---|
| Adafruit DRV8833 motor driver | $5.95 | Adafruit |
| SparkFun TB6612FNG breakout | $14.77 | SparkFun |
| Pololu gearmotor with encoder assembly | $19.95 each | Pololu |
| Pololu A4988 stepper driver carrier | $8.95 | Pololu |
| FeeTech STS3215 smart servo, 12V 30 kg·cm | $31.71 | RobotShop |

### Practice tasks

1. **Mandatory.** Drive one DC motor forward and backward at five different speeds using PWM.
2. **Mandatory.** Add an encoder and write a function that turns the wheel exactly one full revolution regardless of battery voltage.
3. **Mandatory.** Write a one-page power budget for the line follower (below). Include stall current.
4. **Optional if you have a current sensor or a meter in series.** Measure supply current at idle, free run, and stall. Compare to the budget.
5. **Optional.** Stepper one-revolution demo.

The encoder task is your first real closed loop, and it is much harder than it sounds.

### Assessment criteria

- Can you identify which driver to use for a given motor and voltage?
- Can you read an encoder and compute RPM?
- Can you explain why the L298N should be avoided?
- Can you show a power budget that would have predicted a brownout?

## 2.4 Sensors and Reading the Physical World

### What to learn

- Ultrasonic sensors: cheap but wide cone, poor on soft surfaces
- Time-of-flight (ToF) laser: narrow cone, no double-imaging
- IMUs: accelerometer (gravity vector), gyroscope (angular rate), magnetometer (heading)
- Sensor fusion: combining multiple sensors to get a better estimate
- Complementary filters: four lines, works for balancing
- Kalman filters: when and why the complementary filter fails (implement in Module 6, not here)

**Beginner tip:** For a balancing robot, write a complementary filter before you write a Kalman filter.

```
angle = α * (angle + gyro * dt) + (1 - α) * accelAngle
```

with α around 0.98. It works. Graduate to Kalman when you understand why the complementary filter fails.

### Resources

| Resource | Format | Why |
|---|---|---|
| [Adafruit BNO085 9-DoF IMU guide](https://learn.adafruit.com/adafruit-9-dof-orientation-imu-fusion-breakout-bno085/overview) | Free docs | IMU that does sensor fusion on-chip, hands you a quaternion |
| [Kalman and Bayesian Filters in Python, Roger Labbe](https://rlabbe.github.io/Kalman-and-Bayesian-Filters-in-Python/) | Free book | Best free filtering education — **Module 6**, not this month |
| [MathWorks, Understanding Sensor Fusion and Tracking](https://www.mathworks.com/videos/series/understanding-sensor-fusion-and-tracking.html) | Free videos | Conceptual overview |

### Sensor prices (verified)

| Sensor | Price | Notes |
|---|---|---|
| HC-SR04 ultrasonic | ~$4 | Cheap obstacle detection, wide cone, poor on soft surfaces |
| VL53L0X ToF laser | ~$15 | Narrow 35° cone, no double-imaging problems |
| MPU-6050 6-DoF IMU | ~$13 | The cheap classic — you do the fusion yourself (the point) |
| BNO085 9-DoF IMU | ~$30 | Fusion on-chip, UART mode built for robotics |
| Pololu magnetic encoder pair | ~$9 | For adding odometry to motors that lack it |
| RPLIDAR C1 360° LiDAR | ~$69 | Autonomy track hardware, not required this month |

### Practice tasks

1. **Mandatory.** Mount an IMU on a board. Print the pitch angle to serial.
2. **Mandatory.** Hold the board perfectly still and watch the number drift anyway.
3. **Mandatory.** Add a complementary filter and watch that drift disappear.

This is the single most important lesson in state estimation, and it took you twenty minutes.

### Assessment criteria

- Can you read an IMU and output pitch/yaw/roll?
- Can you implement a complementary filter in Arduino C++ or Python?
- Can you explain why the gyroscope drifts and the accelerometer is noisy?

## 2.5 Your First Robots

A line-following robot is a closed control loop with sensor input, actuator output, and a tuning problem — which is exactly what a larger robot is, only smaller and cheaper to break.

**The line follower is Mandatory. The balancer is Optional / stretch.** The balancer creates real proficiency if you finish it. It also destroys calendars. Fast-path learners skip it unless they have spare weeks.

### Robot A (Mandatory): Line-following robot

**Quality build ~$105:**

| Component | Price |
|---|---|
| ESP32-S3 | $15.95 |
| Pololu Romi chassis kit | $39.95 |
| TB6612FNG driver | $14.77 |
| QTR-8RC reflectance array | $12.95 |
| Batteries and holder | ~$12 |
| Wiring and headers | ~$10 |

**Budget build ~$38:**

| Component | Price |
|---|---|
| Generic ESP32 | ~$6 |
| 2WD acrylic chassis | ~$12 |
| DRV8833 | $5.95 |
| 5× TCRT5000 sensors | ~$3 |
| Batteries | ~$6 |
| Wiring | ~$5 |

Keep this chassis. Module 7 can put it under ROS 2.

### Robot B (Optional / stretch): Self-balancing robot

**Quality build ~$134:**

| Component | Price |
|---|---|
| ESP32-S3 | $15.95 |
| 2× gearmotor with encoder assemblies | $39.90 |
| TB6612FNG | $14.77 |
| MPU-6050 | $12.95 |
| Printed/laser-cut chassis | ~$10 |
| LiPo and charger and wheels | ~$30 |
| Misc | ~$10 |

**Budget build ~$62:** Same idea, generic ESP32, acrylic chassis, DRV8833.

### Practice tasks

1. **Mandatory.** Build the line follower. Tune it with a P controller. Then add the D term and watch the oscillation change. Film both versions. The video of a badly tuned robot next to the same robot tuned properly is one of the most persuasive things a beginner can put in a portfolio.
2. **Mandatory.** Repo includes wiring, power budget, and "What broke and how I fixed it."
3. **Optional / stretch.** Build the balancer. It will not work until your filter and your loop timing are both correct. That frustration is the point. Stand for at least 5 seconds. Module 6 can reuse it for PID plots if it still exists.

### Assessment criteria

- Can you tune a P controller on the line follower and explain what each term does from **your** video?
- Do you have one repo with video and failure analysis?
- Optional: can the balancer stand for 5 seconds?

## Module 2 Milestones

| Criterion | Test | Required? |
|---|---|---|
| Drive a motor at a controlled speed and know PWM duty vs. actual RPM | Measure RPM at different duty cycles | Mandatory |
| Read an encoder and close a position loop around it | Command a specific number of revolutions | Mandatory |
| Wire and read an I2C sensor from its datasheet without a tutorial | Given a new sensor, read it solo | Mandatory |
| Fuse accelerometer and gyroscope data into a stable angle estimate | Complementary filter on hardware | Mandatory |
| Explain P, I, and D from your own robot's behaviour | Verbal explanation linked to the line-follower video | Mandatory |
| Show a working line follower on GitHub with wiring, code, and failure analysis | One repo with video | Mandatory |
| Power budget that includes stall | Spreadsheet or README table | Mandatory |
| Balancing robot stands 5 seconds | Video | Optional |

##### Libraries for robotics:

- robot framework
- pyro
- dart
- Pyrobot
- pydy : study of multibody dynamics.
- SOFA: physics based simulations.
- Klamp't: robot modelling, simulating, planning.
- pybotics: robot kinematics and calibration.
- idyntree: control, estimation and simulation.

##### Which libraries and tools in Python/C++ tend to see a lot of use in robotics?

```
- I think it really depends what area you're in, I do a mix of high-level (behavior trees) and low-level control (model predictive control, path planning, force control), so take my answer with a grain of salt.

For C++ linalg I use/see Eigen a lot, have a look at e.g. an example controller. I see mutexes used pretty often in C++, callback functions are also used everywhere. Realtime requirements are not uncommon, and I'd suggest at least knowing when that's needed, how far you can get with RT_PREEMPT (which is in main linux kernel now).

For Python I end up using asyncio a lot; both directly and via ROS2 (e.g. ROS2 futures). Pretty often we need to send a command and wait for something to finish up (e.g. open gripper), I personally find async a nice design pattern for that but some people just find it overcomplicated. Typehints, dataclasses, venvs, etc are all kind of standard Python things that are appreciated but not too specific to robotics.

On top of basic programming skills, I'd also suggest getting familiar with at least one kinematics and/or dynamics library, I use Pinocchio and Brax. If you're doing perception or control, IMO you should also get familiar with at least one autodiff/optimization system. Tensorflow/Pytorch have these features, but are specialized for ML (e.g. they prioritize reverse-mode autodiff, unconstrained optimization, etc) and have IMO limited flexibility. I like being able to whip up a little optimization problem to fit a calibration or solve some least-squares problem pretty easy, and I find CasADi and JAX very useful.

Oh I'd also suggest being able to use the command line effectively: ssh, scp, network tools, grep, tmux, dmesg, lsusb, environment variables, file permissions. It's also pretty helpful to learn at least one command line editor (vi, emacs, or god forbid nano).

- I'm a university student doing master's and what you said is exactly what I have been experiencing as well by our professors.

In probabilistic robotics we have had use of Eigen for c++.

In Underactuated Robotics we have had python+ casadi, usage of pytorch for AI stuff, libraries of python you mentioned are spot on.

Also network tools, ssh, command line editors, grep also a useful suggestion.
```

[docs.robotframework.org](https://docs.robotframework.org/)

Some types of libraries in Robotics:
- dynamics simulation
- inverse kinematics
- ML/motion planning and control
- optimization
- robot modelling
- robot platform, multiphysics


# Autoware-software-VG-optimization

**VoxelGrid (VG) optimisation for Autoware**

This repository provides a set of ROS 2 packages, build scripts, and helper tools that integrate advanced **VoxelGrid optimisation** algorithms into the open-source [Autoware](https://www.autoware.org/) autonomous-driving stack.

---

## ✨ Features

| Category      | Key points                                                                                        |
| ------------- | ------------------------------------------------------------------------------------------------- |
| **Planning**  | Curvature-aware trajectory smoothing · Jerk-bounded speed/gear profiles · Cost-aware optimisation |
| **Runtime**   | Real-time-safe C++ optimiser node · Python scripts for parameter sweeps                           |
| **Ecosystem** | Compatible with Autoware `master` on ROS 2 **Humble** (Ubuntu 22.04) · x86\_64 & Jetson           |
| **Tooling**   | `install/` bootstrap scripts · CMake presets & Makefile helpers · Bag parsing/plotting utils      |
| **Testing**   | Continuous integration (`colcon test`) · Example scenarios for LGSVL & CARLA                      |

---

## 📂 Repository layout

```text
.
├── build/        # Makefile & CMake presets
├── install/      # OS / ROS / Autoware bootstrap scripts
├── src/          # ROS 2 packages (nodes, msgs, launch files)
├── log/          # Bag-parsing & plotting helpers
├── .gitattributes
└── LICENSE       # MIT
```

---

## 🚀 Quick start

> Reference platform: **Ubuntu 22.04** + **ROS 2 Humble**.

### 1. Install system & ROS 2 dependencies

```bash
sudo apt update && sudo apt install -y git curl build-essential
./install/setup_ubuntu22_humble.sh
```

### 2. Clone & build the workspace

```bash
git clone --recurse-submodules https://github.com/XMZhangAI/Autoware-software-VG-optimization.git
cd Autoware-software-VG-optimization
source /opt/ros/humble/setup.bash
colcon build --symlink-install
```

### 3. Launch a demo scenario

```bash
source install/setup.bash
ros2 launch vg_opt_demo demo_straight_lane.launch.xml
```

The demo starts LGSVL in headless mode, loads a simple lane map, and runs the optimiser to compute a speed-and-gear profile in real time. Logs and bag files are saved to `log/<ISO-timestamp>/`.

---

## ⚙️ Configuration

All optimiser parameters live in **`src/vg_opt/config/optimizer.yaml`**.

| Parameter        | Description                            | Default         |
| ---------------- | -------------------------------------- | --------------- |
| `max_accel`      | Longitudinal acceleration limit (m/s²) | `2.5`           |
| `max_jerk`       | Jerk limit for ride comfort (m/s³)     | `3.0`           |
| `gear_set`       | Allowed discrete gear ratios           | `[1,2,3,4,5,6]` |
| `solver.eps_abs` | OSQP absolute tolerance                | `1e-4`          |

Tune these values, then relaunch any affected nodes.

---

## 🛠️ Development workflow

| Task                  | Command                                     |
| --------------------- | ------------------------------------------- |
| Format C++ & Python   | `make format`                               |
| Run unit tests        | `colcon test --packages-select vg_opt_core` |
| Coverage report       | `make coverage`                             |
| Lint (ament + flake8) | `make lint`                                 |

Pull requests should pass **all** checks (`make precommit`) before review.

---

## 🤝 Contributing

1. **Open an issue** describing the bug/feature.
2. Discuss design for substantial changes.
3. Fork ➜ branch ➜ commit ➜ PR (small, focused, with tests).
4. Ensure CI passes.

All contributions are released under the MIT licence.

---

## 📜 Citation

If you use this code in academic work, please cite **both Autoware and this add-on**.

```bibtex
@misc{zhang2025vgopt,
  author       = {Xuanming Zhang},
  title        = {VoxelGrid Optimisation for Autoware},
  howpublished = {\url{https://github.com/XMZhangAI/Autoware-software-VG-optimization}},
  year         = {2025},
  note         = {MIT Licensed}
}
```

---

## 📄 License

This project is released under the **MIT License** (see `LICENSE`).

---

## 🙏 Acknowledgements

Built on the excellent work of the **Autoware Foundation** community, plus open-source libraries such as **OSQP**, **Eigen**, and **pybind11**.

---

*Happy hacking & safe driving!*

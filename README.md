# Unsocial Network

This `README.md` was created using my package [README_genie](https://github.com/browshanravan/README_genie).

Simulate and visualise the evolution of beliefs in social networks using agent‐based modeling. Agents (“digizens”) interact over customisable network topologies, update their beliefs based on in‐group and out‐group influences, and produce interactive plots of belief trajectories and network states.

---

## Table of Contents

- [About This Project](#about-this-project)  
- [Project Description](#project-description)  
- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Quickstart](#quickstart)  
- [Usage](#usage)  
  - [Command-Line Simulation](#command-line-simulation)  
- [Development](#development)  
  - [Dev Container](#dev-container)  
- [Project Structure](#project-structure)  
- [License](#license)  

---

## About This Project

Unsocial Network is an agent-based toolkit for exploring how individual beliefs evolve through social influence in different network topologies. By tuning parameters such as openness, stubbornness, in-group/out-group trust, and network randomness, researchers can study polarization, consensus formation, and the impact of network structure on opinion dynamics.

---

## Project Description

At its core, the project defines two main classes:

- **DigiSapien**: Represents an individual agent with attributes:
  - `belief` (–1 to 1 scale)
  - `openness` (willingness to change)
  - `stubbornness` (resistance to change)
  - `influence_strength`
  - `ingroup_trust_weight` vs. `outgroup_trust_weight`
  - A method to compute a weighted update of belief based on neighbor snapshots.

- **DigiScape**: Manages a network of `DigiSapien` agents:
  - Supports **fully-connected**, **small-world** (Watts–Strogatz), and **scale-free** (Barabási–Albert) graphs.
  - Initialises agents with random attributes drawn from normal or exponential distributions.
  - Runs iterative belief‐update rounds, capturing each agent’s belief trajectory.
  - Produces:
    - **Belief Evolution Plot**: Time series of individual belief trajectories with a neutral reference line.
    - **Network Visualisation**: Layout of agents colored by current belief and shaped by group membership.

Possible use cases include:
- Studying political polarisation dynamics.
- Assessing the role of network topology in consensus formation.
- Educational demonstrations of complex systems and social influence.

---

## Features

- Configurable network topology and parameters  
- Per‐agent randomness in belief, openness, stubbornness, influence  
- In‐group vs. out‐group weighting for belief updates  
- Time‐series and network visualisations via Matplotlib  
- Docker / DevContainer configuration for reproducible development  

---

## Getting Started

### Prerequisites

- Python 3.10 or higher  
- pip  

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/behzadrowshanravan/unsocial_network.git
   cd unsocial_network
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

### Quickstart

By default, parameters are set in `main.py`. You can modify:

```python
NETWORK_TYPE = "small_world"       # fully_connected, small_world, scale_free
DIGIZEN_COUNT = 30
NUMBER_OF_ROUNDS = 100
NEIGHBOR_COUNT = 4
NETWORK_RANDOMNESS = 0.2
GROUPS = ["Left", "Right"]
```

---

## Usage

### Command-Line Simulation

Run the main script:

```
python main.py
```

This will:

1. Initialise the network and agents.
2. Execute the belief‐update simulation.
3. Display:
   - **Belief Evolution** over rounds.
   - **Network Plot** with belief‐colored nodes.


---

## Development

### Dev Container

A [DevContainer](.devcontainer/) is provided for VS Code and GitHub Codespaces:

- Based on Microsoft’s universal container image.
- Python 3.10 pre-installed.
- Just open the folder in Codespaces or VS Code with Remote-Containers enabled.

---

## Project Structure

```
.
├── LICENSE
├── README.md
├── requirements.txt                # pip dependencies
├── main.py                         # entry point
├── .devcontainer/                  
│   ├── Dockerfile
│   └── devcontainer.json
└── unsocial_network/
    └── src/
        └── utils.py               # DigiSapien & DigiScape implementations
```

---

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
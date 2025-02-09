# 10-Armed Bandit Environment for Gymnasium

This repository provides custom bandit environments for reinforcement learning experiments, inspired by the classic example in Sutton and Barto's _Reinforcement Learning: An Introduction_. Built on top of Gymnasium, these environments are designed to facilitate experiments with bandit algorithms in a simple, reproducible setup.

## Overview

The project offers two distinct environments:

- **KBandits-v0**: A flexible bandit environment where you can define the number of arms and assign custom reward distributions. This environment serves as a base for exploring various bandit problem scenarios.

- **KBanditsGaussian-v0**: A 10-armed Gaussian bandit environment that replicates the experimental setup described by Sutton and Barto. In this environment, each arm has a true reward value sampled from a normal distribution, and each pull produces a reward drawn from another Gaussian distribution centered at that true value.

Both environments feature a minimal observation space (a dummy observation) since the bandit problem does not require a complex state representation. They keep track of the number of steps taken and the cumulative reward (balance).

## Installation

Since this package is not available on PyPI, you can install it directly from the repository. You have a couple of options:

### Option 1: Installing from a Local Clone

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BRJoaquin/10-armed-bandit-gymnasium.git
   cd 10-armed-bandit-gymnasium
   ```

2. **Install the package in editable mode (recommended for development):**

   ```bash
   pip install -e .
   ```

### Option 2: Installing Directly from a Notebook

If you are working in a Google Colab notebook or any other notebook environment, you can run the following commands in a cell to clone and install the package:

```python
!pip install git+https://github.com/BRJoaquin/10-armed-bandit-gymnasium.git
```

This will clone the repository into your working directory and install the package along with its dependencies as specified in the `pyproject.toml` file.

## Usage

Once installed, the environments are automatically registered with Gymnasium. You can create and interact with them just like any other Gymnasium environment. Here is an example of how to use the 10-armed Gaussian bandit environment in a Python script or notebook:

```python
import gymnasium as gym
# Importing the package ensures that the environments are registered
import k_bandits_env

# Create the 10-armed Gaussian bandit environment
env = gym.make("k_bandits_env/KBanditsGaussian-v0")

# Reset the environment (optionally with a seed)
observation, info = env.reset(seed=42)
print("Initial observation:", observation)
print("Info:", info)

# Execute an action (for example, pulling the first arm)
observation, reward, terminated, truncated, info = env.step(0)
print("Reward received:", reward)
print("Updated info:", info)

env.close()
```

## Replicating Sutton and Barto

The 10-armed Gaussian bandit environment is specifically designed to mirror the experimental setup from Sutton and Barto's work. It is ideal for testing various exploration-exploitation strategies and comparing the performance of different bandit algorithms.

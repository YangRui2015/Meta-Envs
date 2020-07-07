# Meta-RL environment
This is an environment package forked from https://github.com/katerakelly/oyster, which is used for training meta-RL algorithm PEARL, we just make it an independent package for less dependency and easy installation.

## why use this package
* There is still no acknowledged environment for meta-RL, reasearchers always revise the environment for their own reasearch purpose;
* The environment files in PEARL have some old version dependency (rand_param_envs need gym 0.7.4 and mujoco-py 0.5.7), our package contains these packages, so you don't need to install these packages anymore. 

## Installation
```
git clone 
cd meta_envs
pip install -e .
```

# Usage
```
import meta_envs
from meta_envs import ENVS
from meta_envs.wrappers import NormalizeBoxEnv
```

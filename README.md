# Meta-RL environment
This is an environment package forked from https://github.com/katerakelly/oyster, which is used for training meta-RL algorithm PEARL, we just make it an independent package for less dependency and easy installation.

## why use this package
* There is still no acknowledged environment for meta-RL, reasearchers always revise the environment for their own reasearch purpose;
* The environment files in PEARL have some old version dependency (rand_param_envs need gym 0.7.4 and mujoco-py 0.5.7), our package contains these packages, so you don't need to install these packages anymore. 

## Installation
This package uses Mujoco for simulation, so you install mujoco200 and mujoco_py 2.0 (we didn't test with mujoco151). In addition, if you want to use rand params envs, you need to add mujoco131 in the same folder of mujoco200 (./mujoco/mujoco131).

```
git clone 
cd meta_envs
pip install -e .
```

# Usage
```
import numpy as np
import meta_envs
from meta_envs import ENVS
from meta_envs.wrappers import NormalizeBoxEnv
env_params = {'n_tasks': 2, 'randomize_tasks': True}
env = NormalizedBoxEnv(ENVS['cheetah-dir'](env_params))
shape = np.prod(env.action_space.shape)
env.reset()
env.step(np.random.random(shape))
```


# Update
* 2020.7.7 first update 

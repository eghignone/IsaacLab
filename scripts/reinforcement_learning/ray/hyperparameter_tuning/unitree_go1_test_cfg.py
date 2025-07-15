# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import pathlib
import sys

# Allow for import of items from the ray workflow.
UTIL_DIR = pathlib.Path(__file__).parent.parent.parent
sys.path.append(str(UTIL_DIR))
import tuner
import util
from ray import tune


class UnitreeGo1JobCfg(tuner.JobCfg):
    """In order to be compatible with :meth: invoke_tuning_run, and
    :class:IsaacLabTuneTrainable , configurations should
    be in a similar format to this class. This class can vary env count/horizon length,
    CNN structure, and MLP structure. Broad possible ranges are set, the specific values
    that work can be found via tuning. Tuning results can inform better ranges for a second tuning run.
    These ranges were selected for demonstration purposes. Best ranges are run/task specific."""

    def __init__(self, cfg={}, vary_env_count: bool = False, vary_cnn: bool = False, vary_mlp: bool = False):
        cfg = util.populate_isaac_ray_cfg_args(cfg)

        # Basic configuration
        cfg["runner_args"]["--task"] = tune.choice(["Isaac-Velocity-Rough-Unitree-Go1-v0"])
        cfg["runner_args"]["headless_singleton"] = "--headless"
        cfg["runner_args"]["enable_cameras_singleton"] = "--enable_cameras"
        cfg["hydra_args"]["agent.max_iterations"] = 20

        # tune for PPO entropy coefficient
        cfg["hydra_args"]["agent.algorithm.entropy_coef"] = tune.uniform(0.01, 0.05)

        super().__init__(cfg)

# how to run the ray server:
-> enter container
-> echo "import ray; ray.init(); import time; [time.sleep(10) for _ in iter(int, 1)]" | ./isaaclab.sh -p

# how to start parameter tuning:
-> enter container
-> ./isaaclab.sh -p scripts/reinforcement_learning/ray/tuner.py   --cfg_file scripts/reinforcement_learning/ray/hyperparameter_tuning/unitree_go1_test_cfg.py   --cfg_class UnitreeGo1JobCfg   --run_mode local   --workflow scripts/reinforcement_learning/rsl_rl/train.py   --num_workers_per_node 1

# creating a new project
- not having a .gitignore (even empty) in the root directory causes `./isaaclab.sh --new` to fail.
- isaaclab feels so broken?? If you install the new project not editable, `python scripts/list_envs.py` does not work, and probably many other things 

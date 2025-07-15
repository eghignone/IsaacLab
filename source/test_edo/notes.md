# how to run the ray server:
-> enter container
-> echo "import ray; ray.init(); import time; [time.sleep(10) for _ in iter(int, 1)]" | ./isaaclab.sh -p

# how to start parameter tuning:
-> enter container
-> ./isaaclab.sh -p scripts/reinforcement_learning/ray/tuner.py   --cfg_file scripts/reinforcement_learning/ray/hyperparameter_tuning/unitree_go1_test_cfg.py   --cfg_class UnitreeGo1JobCfg   --run_mode local   --workflow scripts/reinforcement_learning/rsl_rl/train.py   --num_workers_per_node 1


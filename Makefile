
all: 

if750a_drone_bt:
	@echo "Running IF750A Drone BT"
	bot-procman-sheriff -l procman/if750a_drone_bt open_env
if750a_aerial_manipulation_exp1:
	@echo "Running IF750A Aerial Manipulation Exp1:human control"
	bot-procman-sheriff -l procman/if750a_aerial_manipulation_exp1 open_env
if750a_aerial_manipulation_exp2:
	@echo "Running IF750A Aerial Manipulation Exp2:semi-autonomous"
	bot-procman-sheriff -l procman/if750a_aerial_manipulation_exp2 open_env
real_aerial_manipulation:
	@echo "Running real world Aerial Manipulation task"
	bot-procman-sheriff -l procman/real_aerial_manipulation open_env
real_bt_explore_pattern_block:
	@echo "Running real world explore pattern block task"
	bot-procman-sheriff -l procman/real_bt_explore open_env
aerial_simulator_lab:
	@echo "Running Aerial Simulator Lab"
	bot-procman-sheriff -l procman/aerial_simulator_lab open_env
if750a_aerial_manipulation_test:
	@echo "Running IF750A Aerial Manipulation test"
	bot-procman-sheriff -l procman/if750a_aerial_manipulation_test open_env
if750a_aerial_manipulation_stay_height:
	@echo "Running IF750A Aerial Manipulation test"
	bot-procman-sheriff -l procman/if750a_aerial_manipulation_stay_height open_env
if750a_nanya_factory:
	@echo "Running IF750A Nanya"
	bot-procman-sheriff -l procman/if750a_nanya_factory open_env
demo_test:
	@echo "Running demo test"
	bot-procman-sheriff -l procman/demo_test open_env
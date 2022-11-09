# heuristic-agnostic

This repository is the accompanying code implementation for the author's Honors Thesis, ***Towards Heuristic Agnostic Active Multi-Objective Information Gathering in
Human-Robot Interaction: A Deep Q-Learning Approach***.

This thesis is an extention of the paper, ***Active Probing and Influencing Human Behaviors Via Autonomous Agents***, submitted to ***2023 IEEE International Conference on Robotics and Automation (ICRA)***.

This work is an collaboration between University of Southern California (USC) and Carnegie Mellon University (CMU). For all correspondence, please contact **Shuangge Wang** (larrywan@usc.edu).

![p1](https://user-images.githubusercontent.com/77814631/193433536-dbaed09b-8bde-471b-834f-320c92466b9c.png)

## Workflow
### Information Gathering

#### Multi-Objective Information Gathering
Program implemeted for gathering multi-objective information in `./probing_multi-objective/`. Among those four, three are active appraoches that adopt different objective metrics, and one is a passive learning approach.
To run, please navigate to each subdirectory and enter `python run.py` to run the implementation.

#### Desired Velocity Information Gathering
Four benchmarks are implemeted for gathering desired velocity information in `./probing_velocity/`. Among those four, three are active appraoches that adopt different objective metrics, and one is a passive learning approach.
To run, please navigate to each subdirectory and enter `python run.py` to run the implementation.

![Figure_1](https://user-images.githubusercontent.com/77814631/200958967-8f677860-7771-4c32-9334-ac0cca2bf34e.png=50%x) ![Figure_2](https://user-images.githubusercontent.com/77814631/200958964-194c4b18-8c7f-4c55-84b5-2ed15971c3d7.png=50%x) 


### Influence
#### Influence Velocity
Please navigate to `./influence_veocity/` and enter `python run.py` to run the implementation.
![p2](https://user-images.githubusercontent.com/77814631/193433537-35d137e1-17a8-4509-b097-b6e0cdbc9c5c.png)


#### Influence Headway
Two benchmarks are implemeted for influencing headway in `./influence_headway/`, one active and the other passive approach.
To run, please navigate to each subdirectory and enter `python run.py` to run the implementation.
![p3](https://user-images.githubusercontent.com/77814631/193433541-ec69e3cf-f7ff-468b-b14b-ead6a87cb617.png)


### Utilities
Some other peripheral scripts, `plot.py` and `animate.py`, are implemented for creating visual presentaion. They do not bear any dependencies on the main programs.

## Dependencies
All import dependencies and requirements are presented in `requirements.txt`, which is also available down below.
```
imageio==2.22.0
matplotlib==3.5.2
numpy==1.23.3
opencv_python==4.6.0.66
pygame==2.1.0
scipy==1.8.1
```

## Contacts
**Shuangge Wang** (University of Southern California), larrywan@usc.edu  
**Yiwei Lyu** (Carnegie Mellon University), yiweilyu@andrew.cmu.edu  
**John M. Dolan** (Carnegie Mellon University), jdolan@andrew.cmu.edu  
**Bhaskar Krishnamachari** (University of Southern California), bkrishna@usc.edu

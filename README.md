# heuristic-agnostic

This repository is the accompanying code implementation for the author's Honors Thesis, ***Towards Heuristic Agnostic Active Multi-Objective Information Gathering in
Human-Robot Interaction: A Deep Q-Learning Approach***.

This thesis is an extention of the paper, ***Active Probing and Influencing Human Behaviors Via Autonomous Agents***, submitted to ***2023 IEEE International Conference on Robotics and Automation (ICRA)***.

This work is an collaboration between University of Southern California (USC) and Carnegie Mellon University (CMU). For all correspondence, please contact **Shuangge Wang** (larrywan@usc.edu).

![p1](https://user-images.githubusercontent.com/77814631/193433536-dbaed09b-8bde-471b-834f-320c92466b9c.png)

## Workflow
### Information Gathering

#### Multi-Objective Information Gathering
Program implemeted for gathering multi-objective information in `./probing_multi-objective/`. To run, please navigate to each subdirectory and enter `python run.py train` or `python run.py inference` to run the implementation.

<img src="https://user-images.githubusercontent.com/77814631/200962047-36db8b69-b996-4bca-abad-4f7ea6df6f2d.png" width=45% height=50%><img src="https://user-images.githubusercontent.com/77814631/200962048-a47aa4c1-f792-4f9b-9062-3a8761738396.png" width=45% height=50%>

#### Desired Velocity Information Gathering
Program implemeted implemeted for gathering desired velocity information in `./probing_velocity/`. To run, please navigate to each subdirectory and enter `python run.py train` or `python run.py inference` to run the implementation.

<img src="https://user-images.githubusercontent.com/77814631/200959775-8168a96c-d95f-405f-a2d6-0448ac22e855.png" width=45% height=50%><img src="https://user-images.githubusercontent.com/77814631/200959771-4492b933-131f-4514-93ac-b72585ce8721.png" width=45% height=50%>



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

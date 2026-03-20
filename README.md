# T-Rex NEAT AI 🦖

A T-Rex endless runner game rebuilt in Python, currently being developed as an 
environment to train an AI agent using NEAT (NeuroEvolution of Augmenting Topologies).

## Background
I originally built a T-Rex game in JavaScript — you can see that version on my GitHub 
profile. That project made me curious about one thing: what if instead of a human 
playing it, an AI taught itself to play it through trial and error? That question is 
what started this project.

## What It Is Right Now
A fully working T-Rex game built in Python using Pygame. The dino jumps over cacti, 
gravity and collision detection are implemented, and the score increases as you survive.
This is the base environment the AI will be trained on.

## What's Next
- [ ] Add sprite images for the dino and cactus (replacing placeholder rectangles)
- [ ] Integrate neat-python library
- [ ] Feed AI inputs: cactus distance, cactus speed, dino Y position
- [ ] Train the model generation by generation — each session runs 1-2 hours
- [ ] Watch the AI improve in real time across generations
- [ ] Final goal: an agent that survives indefinitely

## How NEAT Works
NEAT stands for NeuroEvolution of Augmenting Topologies. Instead of manually 
designing a neural network, NEAT evolves one. Each generation, the worst-performing 
agents die and the best ones reproduce with small mutations. Over hundreds of 
generations, the network learns the optimal behaviour — in this case, when to jump.

## Tech Stack
- Python
- Pygame
- neat-python (coming soon)

## Requirements
- Python 3.11
- Pygame

## Installation

**Step 1 — Download the project file**  
Click the green **Code** button on this page → **Download ZIP**. Extract it, 
or directly download `trex.py`.

**Step 2 — Install dependencies**  
Open terminal in the project folder and run:
```
pip install pygame
```

**Step 3 — Run**
```
py -3.11 trex.py
```

Press **Space** to jump.

## Related
Check out the original JavaScript version on my GitHub profile — that's where this 
all started.

## Status
Active development — AI training coming soon

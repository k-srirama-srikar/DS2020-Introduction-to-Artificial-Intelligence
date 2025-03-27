## Week 12


### Day 23 - 25.03.2025
---

#### Decision Tree Learning

What is learning? \
We are given data $x \in \R^D$ (x is a datapoint is a in a D dimensional space) and from this we want to learn about output $y$ typically a label... \
$f:x \rarr y$ \
$f$ is a linear function or a quadratic function or smthng that we define... \
In the current scenarion we model $f$ as a Neural Network... \
This is referred as supervised learning... \
A category of supervised learning is Decision Tree structure...

Decision Tree Structure... \
Learning CLassification Tree... \
Entropy(I) represents the expected number of bits to encode the class (+ or -) of a randomly drawn member of I


ID3 algorithm...\
Iterative Dichotomizer 3 (Examples, Target-Attribute, Attributes) \
Create a root node


### Day 24 - 27.03.2025

Avoid overfitting
- two (three) strategies to prevent overfitting
  - stop growing when data split is not stastically significant
  - grow full tree then post prune
  - using ensembke - random/decision forests
- how to select best tree
  - measure performance over training data
  - measure performance over seperate validation data
  - add complexity penalty to performance measure (we prefer shallower trees)

- reduced error pruning
  - split data into training and validation set
  - do until further pruning is harmful
    - evaluate the impact on the validation set of the pruning each possible subtree (node plus those below it)
    - greedily remove the subtree that results in the maximum improvement over the validation set
  - produces the smallest version of the correct tree
- rule post pruning
  - infer the decision tree from the training set
  - convert the learned tree 
- used in c4.5 or something...


> if you were to take any path from the root to the terminal state we end up with a premise and a consequence or a set of rules (set of if statements)



Miscelleaneous issues in decision trees
- alternative measures for selecting attributes
  - problem with information gain... 
  - gain ratio
- cost sensitive information gain
  - we dont want to take the most expensive feature and put it in the root node




----


### Markov Decision Process

Example : Grid world
- a maze-like problem
  - the agent lives in a grid
  - walls block the movement
- noisy movement: actions donot always go as planned
  - .8 times north goes north
  - .1 times noth takes west and 0.1 times takes east
- the agent receives rewards each time step


- an mdp is defined by
  - a set of states s - S
  - a set of actions a - A
  - a transition function T(s,a,s')
  - a reward function R(s,a,s')
  - a start state
  - maybe a termminal state
- mdps are non deterministic search problems
  -  one way to solve them is expectimax search
  

What is markov abt mdp?
- markov generally means that given the present state the future and past are independent
- ie future is indept of past given present
- this is just like search wherer the successor function could onlyb depend on the current state not the history

Ploicies
- in deterministic single agent search problems we wanted an optimal plan or sequence of actions from start to goal 
- for mdps we want optimal policy $\pi^*:S \rightarrow A$
  - a policy gives an action for each state
  - an optimal policy is one that maximizes expected utility if followed
  - an explicit policy defines a reflex agent
- expectimax didnt compute entire policies
  - it only computed the action for a single state only
  - optimal policies can change based on the reward policies
  - the goal is to discover the optimal policy

Example: racing
- a robot wants to travel far quickly
- racing search tree

MDP search tree:
- each mdp state projects an expectimax-like search tree...
- transition prob = prob of ending up at the next state * reward probability


reward now or later??


discounting...
- it is reasonabel to maximize the sum of rewards
- reasonable to prefer rewards now to rewards late
- one solution: value of the rewards decay exponenetially 


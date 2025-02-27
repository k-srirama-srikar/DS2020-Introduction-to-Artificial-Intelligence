# Introduction To AI - DS2020
### Dr. Narayan C Krishnan
## Week - 01

### Day 01 - 07.01.2025
3-0-2-4 : Credit Course

[Course info](https://seekayan.github.io/s25ds2020.html) can be found here.


16 weeks.... 5 labs(3,6,9,13,,15)... 
- week 1 (3) - Intelligent and Problem Solving Agents
- week 2 (1.5) - Search I
- week 3 (3) - Search II, lab 1
- week 4 (3) - Adversarial Search
- week 5 (3) - Logical Agents and Propositional Logic
- week 6 (3) - First Order Logic,, lab 2
- week 7 (3) - Buffer week, test 1,
- week 8 (3) - Planning
- week 9 (3) - Probabilistic Reasoning I, lab 3
- week 10 (3) - Probabilistic Reasoning II
- week 11 (3) - Decision Theory
- week 12 (3) - Markov Decision Process I, test 2
- week 13 (3) - Markov Decision Process II lab 4
- week 14 (1.5) - Reinforcement Learning I
- week 15 (3) - Reinforcement Learning II, lab 5
- week 16 (1.5) - Summary 
Tests - 30% (2 quizzes 15+15) \
Labs - 25% (5*5 and all labs are take home?!) \
End Sem - 45% (A4 sized cheat sheet allowed) \
Attendance - 1%

All put together we need to secure 40 pts to pass...
Refrence Materials - AI a Modern Approach book, [AI a Modern Approach website](http://aima.cs.berkeley.edu/global-index.html) \
All class materials will be accessible on moodle... \
And no lec slides except for the first week... \
Only written notes...

---

Intelligent Agent - acts rationally
```
     Environment 
Perce-|       | Action  
ption |       |
      > Agent >

```

```
agent(state, environment):
      agent.sensors
      return action
```
Rational agent - what is right is defined by a performance measure and we maximize the expected value of the performance measure given the percept sequence to date nad prior knowledge

PEAS (performance, environment, actuators, sensors) - specifying the task environment...

Types of agents:
- simple reflex agents
- model based reflex agents
- goal based agents
- utility based agents
- learning agents
### Day 2 - 09.01.2025
Simple Reflex Agent
```
function SIMPLE-REFLEX-AGENT(percept) returns an action
    persistent: rules, a set of condition–action rules
    state ← INTERPRET-INPUT(percept)
    rule ← RULE-MATCH(state, rules)
    action ← rule.ACTION
    return action
```

There are some condition action rules... \
And it almost instantaneoulsy performs the action... \
The issue is that we have to figure out all the possible conditions...
Model Based Reflex Agent

```
function MODEL-BASED-REFLEX-AGENT(percept) returns an action
    persistent: state, the agent’s current conception of the world state
        transition model, a description of how the next state depends on
        the current state and action
        sensor model, a description of how the current world state is reflected
        in the agent’s percepts
        rules, a set of condition–action rules
        action, the most recent action, initially none
    state ← UPDATE-STATE(state, action, percept, transition model, sensor model)
    rule ← RULE-MATCH(state, rules)
    action ← rule.ACTION
    return action
```

It posses the knowledge of how its action changes the env and how the env is changing it percepts the and estimates the state... \
i.e., the percepts need not provide the complete info of the environment... \
Goal Based Agents

```

```


We only specify the goal it needs to do and nothing else... \
It still has the state estimation and knows the actions it takes and its consequences... \
It internally thinks about its actions and plans... In a model based agent we provide the sequence of actions...
Utility Based Agents

Rather than abstractly defining the goal, we give a utility functions, which gives an idea of how it percieves a particular state (like how happy we are with its action), we try to max out the utility value...
Learning Based Agent

We leave it to the agent to figure out what is good and bad... \
The agent has the mentality of rewards and penalties... We'll talk about rl based agents

### Problem Solving Agents
Explanaiton of a kind: \
Consider a weighted graph and the agent wants to move around ant graph is not a fully connected graph... \
Formulation actions for tihs kind of a world is relativly simpler... \
The problem formulation is important, i.e., we try to identify the states initially \
Then we need to figure out what we need to specify, i.e., from each state we can define what actions can be peeformed from a paticular state... 

We make some assumptions to do this:
- the task environment observable, i.e, it doesn't need any state estimation processes
- it is a discrete environment
- We assume that the actions are deterministic
- The env is static
- The actions are sequential
- There is a single agent
The agent basically is figuring out a seq of actions to go from start state to goal state, this is the search procedure here
Problem formulation:
- Initial state... the agemt begins with an initial state
- Actions (ex: D $\rightarrow$ A; D $\rightarrow$ B; D $\rightarrow$ E)
- Goal state
- Path cost : cost associated with the action
Consider the 8 puzzle problem... we can consider it as vector/list of length 9 containing the elements and we try to figure out stuff... etc
What we are essentially doing is a serach...

We can't store all the edges and vertices...\
So we have a child generator function \
CGF(D,a) = A \
CGF(D,e) = E \
CGF(D) = {A,E} \
the cgf function either give the next state for a given action or the next possible states given only a particular state \
This gives a tree like structure... \
Frontier list, explored list... \
The search strategies differ in the order of the nodes explored... \
Now this calls for a way to evaluate a search strategy....

Some of the evaluations
- completeness: if a solution exists, does it always find the solution
- optimality: comes only if there's a cost associated with actions... i.e., we need to get the least cost solution...
- space complexity: memory reqd to conduct the search...
- time complexity: time reqd to formulate the solution... \
  Let us see some of the factors to calc the complexities
    - b - maximum branching factor (max no of states that can be visited from a state)
    - d - shallowest depth of the least cost solution 
    - m - maximum depth of the search space

The solution we are talking about right now is uninformed search
### Informed Search (Heuristic Search)

Informed search algorithms, also known as heuristic search algorithms, make use of additional problem-specific knowledge to find solutions more efficiently than uninformed search algorithms (such as Breadth-First Search and Depth-First Search). The key idea behind informed search is to use **heuristics** to guide the search towards the most promising paths.

#### Key Concepts:
1. **Heuristic (h(n))**:
   - A heuristic is a function that estimates the cost or distance from a given node `n` to the goal.
   - The heuristic function depends only on the current state at node `n`.
   - If the node is a goal, then `h(n) = 0` because no further steps are needed.
   - A good heuristic helps guide the search towards the goal quickly, reducing the time complexity of the search.
   
2. **g(n)**:
   - This represents the cost of reaching node `n` from the initial state.
   
3. **f(n)**:
   - The evaluation function, often used in algorithms like A*, is the sum of two components: the cost to reach the node and the estimated cost to reach the goal from that node.
   - The function `f(n)` is defined as:
     \[
     f(n) = g(n) + h(n)
     \]
   - The value of `f(n)` helps in prioritizing which node to explore next during the search.

4. **Goal**:
   - A goal is a state that satisfies the criteria for a solution to the problem.
   - When the search reaches a goal node, the solution has been found.

### Related Algorithms

#### 1. **Greedy Best-First Search (Greedy BFS)**:
   - This is a simple heuristic search algorithm that focuses solely on minimizing the estimated cost from the current state to the goal. The evaluation function in Greedy BFS is:
     \[
     f(n) = h(n)
     \]
   - It chooses the node with the lowest heuristic value (i.e., the node that appears to be closest to the goal) and expands it first. 
   - **Pros**: Greedy BFS is generally fast because it focuses on the heuristic.
   - **Cons**: It doesn't always find the shortest path because it ignores the cost to reach the current node (g(n)).

#### 2. __A* Search__:
   - A* is a more sophisticated search algorithm that combines the strengths of **Dijkstra’s Algorithm** (which minimizes the cost to reach a node, `g(n)`) and **Greedy Best-First Search** (which minimizes the estimated cost to the goal, `h(n)`).
   - The evaluation function in A* is:
     \[
     f(n) = g(n) + h(n)
     \]
   - **A* Search** always finds the optimal solution if the heuristic is admissible (i.e., it never overestimates the true cost to reach the goal).
   - **Pros**: A* is complete, optimal (with an admissible heuristic), and can be more efficient than uninformed search methods.
   - **Cons**: The performance of A* can be affected by the quality of the heuristic.

### Summary of Algorithms:
1. **Greedy Best-First Search**:
   - **Evaluation function**: `f(n) = h(n)`
   - Focus: Minimizes the estimated cost to the goal.
   - Not guaranteed to find the shortest path.

2. __A* Search__:
   - **Evaluation function**: `f(n) = g(n) + h(n)`
   - Focus: Minimizes the total cost (path cost + estimated cost to the goal).
   - Guaranteed to find the optimal solution if the heuristic is admissible.

In conclusion, **informed search** uses heuristics to improve the efficiency of the search process. Both Greedy BFS and A* search are popular informed search algorithms, with A* being more commonly used for optimal solutions.
Here is a Python implementation of **Greedy Best-First Search (Greedy BFS)** and **A* Search**. Both algorithms require a problem space where the nodes, state transitions, and heuristics are defined. For simplicity, I'll implement these searches on a grid-based problem where the goal is to move from a start position to a goal position.

### Python Implementation:

#### 1. **Greedy Best-First Search (Greedy BFS)**:



#### 2. __A* Search__:



### Explanation of the Code:

#### Greedy Best-First Search:
- **open_list**: This is a priority queue (using `heapq` in Python) that stores nodes to explore, with each node having a priority determined by its heuristic value (`h(n)`).
- **closed_list**: A set that keeps track of nodes that have already been explored.
- **heuristic function**: In this example, the Manhattan distance is used as the heuristic function (`manhattan_heuristic`), which estimates the cost from the current node to the goal.
- The algorithm explores nodes by always selecting the one with the lowest heuristic value (`f(n) = h(n)`).

#### A* Search:
- **open_list**: Similar to Greedy BFS, this is a priority queue, but in A*, nodes are prioritized by the total cost function `f(n) = g(n) + h(n)` where `g(n)` is the cost to reach node `n` from the start and `h(n)` is the heuristic estimate to the goal.
- **g_cost**: A dictionary that stores the cost to reach each node from the start.
- The algorithm explores nodes by considering both the cost to reach them (`g(n)`) and the estimated cost to the goal (`h(n)`).

### Example Grid:
- In both algorithms, we assume the grid allows movement in four directions (up, down, left, right).
- The heuristic used (`manhattan_heuristic`) is a simple estimation for a grid where diagonal movement is not allowed.

### Results:
- **Greedy BFS** will find a path to the goal based on the heuristic alone, but it doesn't guarantee the shortest path.
- **A* Search** will also find a path, but it guarantees the shortest path if the heuristic is admissible.

These algorithms can be adapted for more complex environments or different types of problems by modifying the neighbor generation and the heuristic.

## Week 13

### Day 24 - 03.04.2025

A **Markov Decision Process (MDP)** is a mathematical framework used to describe decision-making problems in situations where outcomes are partially random and partially under the control of a decision maker. MDPs are widely used in reinforcement learning, robotics, and other fields involving sequential decision making.

#### Key components of an MDP:
1. **States (S)**: A set of all possible states the system can be in.
2. **Actions (A)**: A set of actions available to the agent to transition between states.
3. **Transition Function (T)**: The probability that taking a specific action in a specific state will result in a specific next state. This is often represented as \( T(s, a, s') \), which gives the probability of transitioning from state \( s \) to state \( s' \) by taking action \( a \).
4. **Reward Function (R)**: The immediate reward received after taking action \( a \) in state \( s \) and transitioning to state \( s' \).
5. **Discount Factor (γ)**: A number between 0 and 1, denoted as γ, which represents the importance of future rewards. A higher value of γ places more importance on future rewards.
6. **Policy (π)**: A strategy that defines the action that the agent will take given a state. The goal is to find the optimal policy that maximizes the cumulative reward. A function that maps states to actions.

The objective in an MDP is to find the optimal policy, which maximizes the expected sum of rewards over time, starting from an initial state.

#### Bellman Equation:
The Bellman equation is central to the solution of MDPs. It provides a recursive decomposition of the value function \( V(s) \), which represents the expected cumulative reward from state \( s \):

$V(s) = \max_a \left( R(s, a) + \gamma \sum_{s'} T(s, a, s') V(s') \right)$

Where:
- $V(s)$ is the value function of state $s$,
- $R(s, a)$ is the immediate reward of taking action $a$ in state $s$,
- $\gamma$ is the discount factor,
- The sum over $s'$ represents the expected value of the next state.



Recursive definition of value 
- $V^*(s)=max_aQ^*(s,a)$
- $Q^*(s,a)= \sum_{s'}T(s,a,s')[R(s,a,s')+ \gamma V^*(s')]$
- $V*(s)=max_a\sum_{s'}T(s,a,s')[R(s,a,s')+ \gamma V^*(s')]$
- we are going from s to s'




#### Example of a simple MDP:
Let's take a very simple example with the following components:
- States: $S = \{S0, S1\}$
- Actions: $A = \{a0, a1\}$
- Transition probabilities: $T(S0, a0, S1) = 1$ , $T(S1, a1, S0) = 1$
- Rewards: $R(S0, a0) = 10$, $R(S1, a1) = -1$
- Discount factor: $\gamma = 0.9$

#### Python Implementation of an MDP

Below is a simple Python program to solve an MDP using value iteration:

```python
import numpy as np

# Define the states, actions, rewards, and transition probabilities
states = ['S0', 'S1']
actions = ['a0', 'a1']

# Reward function: R[state][action]
rewards = {
    'S0': {'a0': 10, 'a1': 0},
    'S1': {'a0': 0, 'a1': -1}
}

# Transition function: T[state][action][next_state] - transition probabilities
transition_probs = {
    'S0': {'a0': {'S1': 1.0}},
    'S1': {'a1': {'S0': 1.0}}
}

# Discount factor (gamma)
gamma = 0.9

# Value iteration function
def value_iteration(states, actions, rewards, transition_probs, gamma, threshold=1e-6):
    # Initialize value function V(s) arbitrarily (e.g., zero for all states)
    V = {s: 0.0 for s in states}
    
    while True:
        delta = 0  # Change in value function in this iteration
        # Create a copy of V to store the updated values for this iteration
        new_V = V.copy()

        for state in states:
            # For each state, perform value iteration
            action_values = []  # List to store the expected value for each action
            for action in actions:
                expected_value = 0
                # Sum over all possible next states
                for next_state, prob in transition_probs[state][action].items():
                    expected_value += prob * (rewards[state].get(action, 0) + gamma * V[next_state])
                action_values.append(expected_value)
            
            # Update the value for the current state
            new_V[state] = max(action_values)
            delta = max(delta, abs(new_V[state] - V[state]))  # Track the largest change
        
        V = new_V
        
        if delta < threshold:  # If the value function has converged, stop
            break
    
    return V

# Perform value iteration
optimal_values = value_iteration(states, actions, rewards, transition_probs, gamma)

# Output the optimal values for each state
print("Optimal values for each state:")
for state, value in optimal_values.items():
    print(f"{state}: {value}")

```

#### Explanation of the Code:
1. **States, Actions, Rewards, and Transition Probabilities**: 
   - `states` defines the list of states the agent can be in.
   - `actions` defines the possible actions the agent can take.
   - `rewards` is a dictionary that holds the reward values for each state-action pair.
   - `transition_probs` holds the transition probabilities between states when an action is taken.

2. **Value Iteration**:
   - We initialize the value function \( V(s) \) for each state as zero.
   - The `value_iteration` function repeatedly updates the value function based on the Bellman equation until convergence, which is defined as the change in value being smaller than a given threshold.

3. **Result**:
   - The program outputs the optimal values for each state after the value iteration process converges.

> The program computes the optimal value function for the states `S0` and `S1`. It will give you the expected cumulative rewards from each state under the optimal policy.
## Week 14

### Day 25 - 08.04.2024

#### Policy methods

Observations with value iteration
- value iteration represents the Bellman unpdates: \
    $V_{k+1}(s) \leftarrow max_a \sum_{s'}T(s,a,s')[R(s,a,s')+ \gamma V_K(s')]$
- $O(S^2 A)$



Fixed Polices
- expectimax tree max over all actions to compute the optimal values
  - if we fixed some policy $\pi (s)$ then the tree would be simpler - only one action per state
  - ... though the tree's value would depend on which policy we fixed

Fixed policy details


Policy Evaluation
- Turn recursive Bellman equations into updates
- $V^\pi_0(s)=0$
- $V_{k+1}^{\pi} \leftarrow \sum_{s'} T(s, \pi(s), s')[R(s, \pi(s), s')+ \gamma V_k^\pi (s')]$
- $O(S^2)$ per iteration
- and the resulting alg is referred to as ,odified policy iteration


policy extraction


Computing the actions from values
- lets imagine we have the optimal values $V^*(s)$
- we need to do a mini-expectimax (one step)
- this is called policy extraction since it gets the policy implied by the values
- $\pi^*(s)=\argmax_a\sum_{s'}T\dots$







### Reinforcement Lerning

Basic idea
- recieve feedback in the form of rewards
- agent's utility is defined by the reward function

still assume an MDP \
still looking for a policy $\pi(s)$

new twist: dont know T or R
- we dont know which states are good or what the actions do
- must actually try actions and states out to learn



Method 1 - Adaptive dynamic programming
- idea
  - learn model emperically
  - solve the mdp as if the learned moder were correct
  - model basedd learning
- emperical model learning
  - simplest case
    - count the ourcomes for each s,a
    - noramlixe to give estimate of T(s,a,s')
    - discover R(s,a,s') the first to,e we experience (s,a,s')
  - more complex learners are possible if more domain knowledge is available
- estimate the transitions and rewards
- interactable for large spaces
- the adp agent is limited only by its ability to learn the transition model
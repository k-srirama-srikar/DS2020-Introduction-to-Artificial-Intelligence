## Week 15

### Day 26  - 15.04.2025

#### Method 2 - Direct Utility Estimation
- monte carlo policy evaluation
- to estimat $V^{\pi (s)}$
- loop over episodes
  - the first time step t that state s is visited in an episode
  - increase the counter N(s) number of times s is visited in teh episodes (can be multiple times in an episode)
  - total return T(s) - sum of the returns from each visit
  - Estimated return $\hat{V}^{\pi(s)}$

Incremental Mean \
$\mu_k=\mu_{k-1}+1/k(x_k)$
...


#### Method 3 - Temporal Difference Learning
- idea - learn from every experience 
  - update V(s) each time we experience a transition (s,a,s',r)
  - likely outcomes s' will contribute to updates more often
- temporal difference learning of values
  - policy still fixed, still doing evaluation
  - sample = $R(s, \pi(s), s')+\gamma \hat{V}^\pi(s)$ - td target
  - $\hat{V}^\pi(s) \leftarrow \hat{V}^\pi(s)+\alpha(sample - \hat{V}^\pi(s))$
    - $sample - \hat{V}^\pi(s)$ - temporal difference(td) error


TD and ADP
- both try to make local adjustments to utility etimates
- td adjusts a state to agree to its observed successor
- adp adjusts the state to agree to with all the successors that might occur, weighted 


#### Active Reinforcement Learning
- Passive learning agent
  - simplified task : policy evaluation
- Active learning agent
  - Full reinforcement learning
- the learning agent makes choices (multi arm bandit problem)





#### Modified ADP agent
- exploration function... we modify the bellman eqn...
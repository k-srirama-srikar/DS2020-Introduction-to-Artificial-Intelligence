## Week 4
### Day 07 - 28.01.2025
#### Local Search
- _Hill Climbing_
- _Simulated Annealing_
- _Local Beam Search_
- _Genetic Algorithms_ - The idea is to combine stocastic local beam search... here we look at a pair... \
    We represent a state using a string ...
    Basicslly starts with an initial population... we start with k randokmly generated states... \
    Fitness value or evaluation function describes the goodness of the state.
    Eg : No. of queens not in conflict, then higher the eval function, better the fitness value \
    There are two ops - Cross over, mutation
    <br>We choose a random index to slice and do a crossover operation... then the next operation in the mutation..
    <br> we pick a state and change its value... \
    We can use the fitness function and through it we define a probability distribution over the current population... \
    
     ```
    function GENETIC-ALGORITHM(population, fitness) returns an individual
        repeat
            weights ← WEIGHTED-BY(population, fitness)
            population2 ← empty list
            for i = 1 to SIZE(population) do
                parent1, parent2 ← WEIGHTED-RANDOM-CHOICES(population, weights, 2)
                child ← REPRODUCE(parent1, parent2)
                if (small random probability) then child ← MUTATE(child)
                add child to population2
                population ← population2
        until some individual is fit enough, or enough time has elapsed
        return the best individual in population, according to fitness

    function REPRODUCE(parent1, parent2) returns an individual
        n ← LENGTH(parent1)
        c ← random number from 1 to n
        return APPEND(SUBSTRING(parent1, 1, c), SUBSTRING(parent2, c + 1, n))
    ```
    or we can also write it as below
    ``` 
    initial population : P0, {c1, c2, ...., ck} |P0| = k
        prob distribution over P0 based on fitness function f0
    for iterations 1 to max_states
        M : samole pairs of states from P(i-1) based on f (we check for the goal state here)
        for every pair j-1 to M
            preform cross ove
            perform mutation
        recomplete fi and update Pi
    ```
    Has lots of use on combinatorial searches... but in general it is not preferred to do optimization

#### Search with partial observations
Here a state becomes a belief state... and once it performs some actions, the size of belief state changes... and the agent can still perform reational actions or rational behaviour... We'll look into it in Partially Observable Markov Decision Process...



Now lets add some complexity to the search space... \
Say, there are two adgents in the task env... ie... Adversarial Search....

#### Adversarial Search
> to be cont'd.....




### Day 08 - 30.01.2025

#### Adverserial Search
- Fully observable, static, deterministic, zero-sum, turn-taking game
- We are interested in finding a strategy to win the game
- Max player, min player...
- ex 
  ```
              A
            /   \
          a1     a2
          /\     /\
        10  9   5  15
  ```
  Now the max player will chose a1 as in the next turn min player choose the terminal state. \
  Each path is a sequence of actions alternating between max player and min player. \
-  `MiniMax Algorithm`:  \
    We are alternating between `min` and `max`
    ```python
    def max_value(state):
        if terminal(state):
            return utility(state)
        s = child_gen_fun(state)
        # s = [s1,s2,...., sn]
        return max(min_value(s1), min_value(sn)) # all the values

    def min_value(state):
        if terminal(state):
            return utility(state)
        s = child_gen_fun(state)
        return min(max_value(s1), max_value(sn))
    
    def minimax(state):
        return max_value(state)
        # or we can use the child gen function to get the list and 
        # get the max of all the min_values of the children and
        # then we would get the action as well because the child  
        # generator function returns the action to proceed as well
    ```
    This is a brute force search algorithm... 
    - $completeness$ - yes if search space is optimal
    - $optimal$ - yes
    - $time \space complexity$ $O(b^m)$
    - $space \space complexity$ $O(b*m)$ \
    Ex : for a game of chess $b \approx 35$ and $m = 100$

- We can make the max min alg by pruning the search tree... this can reducing the search tree and we are not reducing the optimal payoff... \
  This is called `alpha-beta pruning`... the $\alpha$ corresponds to the highest payoff we have found and similarly $\beta$ correspond to the value for min player \
  The tree that givess max pruning is called a didatic seaech tree.
  This reduce the complexity to $O(b^\frac{m}{2})$ 
- Now we can have an evaluation function instead of the unility value, i.e., a heuristic... we could use pattern data bases ig... to create an evaluation value... \
- ordering matters... pattern databases... \
- When the agent cant go all the way, it has to make imperfect decisions...
- Imperfect Decisions : Proposed by claude shannon (shanon's entropy)
  - cutoff depth (replaces the terminal test)
  - Eval func (replaces the utility func)


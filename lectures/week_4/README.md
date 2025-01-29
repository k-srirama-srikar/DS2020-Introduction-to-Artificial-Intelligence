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

## Week - 03
### Day 05 - 21.01.2025
More about heuristics...

In order for the heuristic to be a proper one, $f$, where $f(n)=g(n)+h(n)$ has to be monotonic... \
$f(n):max{f(parent(n)), g(n)}+h(n)$ and $f(n)$ is path max correction... \
$h$ is monotonic if $h(n) \le h(n') + c(n,a,n')$ \
If $h$ is monotonic, \
$f(n'):g(n')+h(n') = g(n)+h(n') + c(n,a,n') \ge g(n) +h(n) = f(n)$ \
this will result f is monotonic along the path, i.e., if h is monotonic, then there's no need for path mx correction...

for an optimal A* search \
Effective branching factor: 1+b* + b*^2 + ... + b*^d = N+1... we say that the A* search is efficient when b* is close to 1... and the heuristic defines the efficiency of the A* search 

Consideer the 8 tiles problem...

h<sub>i</sub> : misplaced tiles, \
h<sub>r</sub> : manhattan distance ($|x_1 - x_2|+|y_1 - y_2|$) \
If $h_1(n) \ge h_2(n) \forall n$, here we say that $h_1$ is a dominant heuristic as $h_2$ expands more nodes than $h_1$ \
This is  in a generic sense but not forn this case... here $h_2 \ge h_1$

Now the question comes how do we generate these heuristics? \
For a siple heuristic, generation takes less time and searching requires a lot and the opposite for h* \
This is the reason we use something called pattern databases... \
We create a databases of samller problems with the solutions of the exact cost of solving it... \
Then we store these subproblem... and once we do the larger problem when we reach a particular configuration we do a look up from the database and then the heuristic is the subproblem

Iterative deepening A* search: \
A* is only a threshold for the dfs...

> Lab 1: \
> We are in a 4x4 grid.... some of the grids have walls \
> we have gold in some places and there is an exit state \
> there's a seq to pick up gold... all he knows if to go and pick up gold at (i,j) \
> Now the moment it reaches the goal, it knows about the next goal state and finally the exit state \
> Solution must essentially be all the paths..
> TO DO: \
> We need to write the child gen function that takes the pos and gives the children \
>  Goal test function: implement bfs, dfs using only a list
> in case there's no solution it should output the same


#### Local Search:
here the solution is the goal state but bot the path taken...

### Day 06 - 23.01.2025
Beyond Classical Search:
- goal itself is the solution, path to the goal is irrrelevant.
- Ex: Travelling salesman problem...
- state space: all possible configurations..
- we are interested in findinag the goal, where goal is an optimal configuration
- start from some configuration and we try to improve it
- constant space (we're not keeping track of the past configs, or storing the future configs)

_Hill Climbing Search_:
- efficient but incomplete
- steepest aceent approach
- greedy local algorithm
- equivalent would be hill descending search and we use the steepest descent search... and we'll be using this in machine learning...
- hill climbing algorithm
    ```
    hill_climbing_search:
        node =  current.state:
        loop do:
            neighbors=cgf(node)
            max_meighbor=arg_max{vlaue[neighbors]}
            if value[max_neighbor]> or greater than equal to value[node]:
                node=max_neighbor
        conditions for the loop to terminate:
            - the value of the max neighbor is less than the value of the node
            - no neighbors
            - ?
    ```
- ridge... where the hill climbing search fails
- random sideways moves - when it is stuck at a shoulder... 
- ranodm restart hill climbing - when it is stuck at a local optimum... (this will be a complete search)
- Stocastic hill climbing - if there are more than two states that are greater than the current state, we randomly go to one of the state

_Simulated Annealing_:
- we do some bad moves to escape from a local maxima
- tries to include both hill climbing and random walk
- inspires from annealing of material... or whatever
- temp high $\implies$ allow for random moves
- temp low $\implies$ hill climbing search
- schedule [t] $\rightarrow$ T (maps the iteration to temprature) 
- Alg
```
	  for t : 1 to float('inf') 
         T = schedule[t]
         if T=0 then return the current state
         next = a randomly selected successor of the current state
         del e = value[next] = value[current]
         if del e> 0 then current e next
         else current  = next only with the probalility e^(del e/T)
```


_local beam search_:
- where instead of keeping track of a single state, we keep track of k best states so far and do the search on these states
- k is the size of the beam 
- and the exploration happens in parallel
- an unfavourable case would be that all the states explore the same hill... so we add some stocasticity
- stocastic beam search




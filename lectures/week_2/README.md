# Week - 2
### Day 3 - 15.01.2025
### Uninformed Search
```
search (initial state, problem) -> seq of actions:
    # we r given a graph of sorts and we dont know abt it
    # nad we build it as we progress
    # the problem defines the actions and the resuolts of the actions
    frontier_list : [inital state]
    explored_list : set()
    while true:
        if forntier_list == []: then return failure
        select a state from the frontier list
        if the selected state is the goal state: then return success, the path(the seq of actions,)
        expand on the state: call the child genreator functions 
        add all the children not in explored_list or frontier_list to the frontier_list
        add the state to the explored_list
```

This is the search procedure in an abstract sense...
Ex: \
initial_st = 1 \
i := [i+1,i+2] \
we wont store the graph in these cases rather we use the functions to move next
### Strategies:
- _Breadth First Search_ \
Say fl: 2 3 4 7 8 say 2:[10,11] \
if we pick from the first element and add the new ones at the end \
New fl in the abv case is fl: 3 4 7 8 10 11 \
but if we pick the last elem then we need to add new elems to the beginnig \
expand the shallowest unexplored state \
Now, time to see some props \
    - $Completeness$ - Yes if the branching factor ($b$) of the search space is finite \
    - $Optimality$ - If there were uiniform cost then it it is optimal \
    - $Space \space Complexity$ - If there is a branching factor ($b$) and the ans is present is at depth ($d$) then the complexity is $O(b^d)$, essentially it is exponential
    - $Time \space Complexity$ - This is also exponential of time $O(b^{d+1})$

- _Uiform Cost Search_ \
$g(n)$ : cost of reaching state, from inital state \
Implement fl : as a priority queue \
    - $Completeness$ - yes if cost $\ge$ $\epsilon$ > 0
    - $Optimal$ - Yes cause expansion is based on $g(n)$
    - $Space \space Complexity$ - if c* is the optimal cost, then there'll be nodes of cost greater than or equal to c*, so it's kinda hard to say anything abt it

- _Depth First Search_ \
Expand the deepest unexpanded state \
We exhaustively search a paths form an element and then move on to the next element of the same level 
    - $Completness$ - yes assuming that the search space is finite
    - $Optimal$ - nope
    - $Tme \space Complexity$ - It'll be exponential in $m$ where $m$ is the depth of the tree viz. $O(b^m)$
    - $Space \space Complexity$ - Space Complexity is linear in $m$ i.e., $O(b*m)$, which is a good space complexity...

### Day 4 - 16.01.2025
We've discussed about some ideas of searching and we realised that dfs stores memory in linear time so how to use this?
- _Depth Limited Search_ \
DFS until depth until depth $l$
    - $Space \space Complexity$ is linear
    - $Completeness$ - No

- _Iterative Deepening Search_ \
DLS from $l \in (0, \infty)$ \ 
    - $Completeness$ - Yes
    - $Optimality$ - Yes if uniform cost
    - $Time Complexity$ - Exponential in $d$
    - $Space Complexity$ - linear in $d$

- _Iterative Lengthening Search_ \
$g(n)$ - least cost of reaching $n$ from initital state **(exact cost)** \
And this $g(n)$ wouold be a threshold instead of $l$
All the search strategies are uninformed (and are called dumb)...
### Informed (Heuristic) Search
The heuristic encodes problem specific knowledge \
we use a $h(n)$ which is an estimated cost of reaching the lowest cost goal state from $n$ \
$h(n)=0$ if $n$ is a goal state... Note that all we need to estimate $h(n)$ is just the state $n$ \
$f(n)$ - evaluation function = $g(n)+h(n)$ - its the cost of reaching the goal state passing through the state n... \
Refer to `week1.ipynb`
- _Greedy Best First Search_ \
$h(n)$ - priority queue 
    - $Completeness$ - Yes
    - $Optimal$ - No
    - $Time$ - Exponential in $m$
    - $Space$ - Exponetial in $m$
- _A* Search_ \
Here we combine $g(n)$ and $h(n)$ \
Avoid expanding paths which are already expensive \
Identical to Uniform Cost Search (Dijkstra's) 
    - $Completeness$ - Yes
    - $Optimal$ - No, but then why A*?? \
    Well we need to use an admissible heuristic function to make it better

_Admissible Heuristic_ \
$h$ is an admissible Heuristic iff \
$h(n) \le h*(n)  \space \forall n$ \
$h$*$(n)$ - true cost to reach a goal state from $n$ \
$h(n) \ge 0 \space \forall n$ \
Admissible heuristic gaurantees an optimal solution
_Ex: 8 puzzle problem_ \
A valid heuristic can be the distance between coordinates of the empty tile \
No of misplaced tiles can be one \
total dist bw coordinates of every tiles \
Now, what we are interested is the optimality of A* search and admissible heuristic.... 
$Proof$  \
Let N be a goal state A* outputs... \
suppose $\exists$ another goal state N'... \
$f(N)<f(N')$ \
This essentially means $g(N')<g(N)$ \
When A* ppicked N for expansion, either N' or an ancestor of N', N" must have been in the frontier list, then $f(N)\le f(N'')$ \
ie.,s $g(N)+h(N)[which \space is \space 0]\le g(N'')+h(N'') \rightarrow 1$ \
$g(N')= g(N'')+dist(N',N'')$ \
and, $h(N'') \le h*(N'') = dist(N',N'')$ \
$g(N') \ge g(N'')+h(N'') \ge g(N) \rightarrow 2$ \
Now this is a comtradiction
- $Space Complexity$ - exponential
- $Time Complexity$ -  
    A* expands all n such that f(n) < c* \
    may expand n : f(n) = c* \
    never expands n : f(n) > c* \
    So its hard to explicitly characterise, so we can say it depends the error in h*

we'll talk about monotonicity or consistency heurisitc...

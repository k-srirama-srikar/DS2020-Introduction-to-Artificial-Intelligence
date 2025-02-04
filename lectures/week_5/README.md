## Week 5
### Day 09 - 04.02.2025
#### Advarserial search
- consider the _min max algorithm_ <br> we consider a game search tree and now let us consider $\alpha - \beta$ pruning <br> we previously talked about this and we considered that this helps in pruning large subtrees  but it depends on the order of the nodes expanded <br> terminal states - utility function.... we can cutoff the search at depth $d$ to reduce the time spent... and the search ends in a non terminal state... now we have to estimate the utility... and so we need a _cutoff test_ and we estimate the utility of that particular node... <br>  ```function evalution_func():
		i/p : state
		o/p : utility estimate```
- cutoff depth - _Quiescence search_ , which essentially says to go deeper when the game state is in a flux... 
	- horizon effect - 
		- f1: queen is alive
		- f2 : # elephants stll alive
		- ...
		- $f = \sum^{N}_{i=1} w_if_i(r)$ - the feature functions

Now, lets talk about _Stochastic Games_ 
- element of randomness ... eg. roll of dice
	- chance nodes in the game tree

> [!NOTE]
   **Lab 2** - Going to be a variant of lab 1... (There'll still be Yantra collector) 
> Now... there'll be a cost assocaited with each state.. We'll  implement `Uniform Cost Search` and we define some heuristics... and not euclidean or manhattan heuristics... the heuristics need to be implemented on your own and we do a `greedy best first serch` and then we implement `A* search` 

#### Logical Agents
- atomic state space:


- knowledge based agents: 
	- knowledge base : represent the facts about the world
	- Inference Engine : to derive new facts about the world..
- Logical representation and reasoning 
	- sentence - indiv piece of knowledge..
	- syntax - which sentences are legal 

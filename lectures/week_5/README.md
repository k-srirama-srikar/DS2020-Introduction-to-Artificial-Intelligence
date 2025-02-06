## Week 5
### Day 09 - 04.02.2025
#### Adversarial search
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

---
### Day 10 - 06.02.2025
#### Knowledge based agents 
- representing states and actions
- incorporate new principles
- update the internal representation
- deduce hidden properties of the world
- deduce the appropriate actions

1. Observability : No : Local Perception
2. Deterministic
3. Sequential
4. Static
5. Discrete
6. Single agent

Representation :
- $Logic$ - sentence
- sentence
	1. syntax (grammar) or legal sentences
	2. semantics or the meaning of legal sentences

- $Models$ - worlds with respect to which the truth values can be evaluated. M is a model of a sentence $\alpha$ if $\alpha$ is `true` in M. And M($\alpha$) : set of all models of $\alpha$ 
- $Entailment$ - KB $\models$  $\alpha$ iff $\alpha$ id true in all the worlds where KB is true <br> Example: 1 - sun rises in east, 2 - arunachal pradesh is the eastern most state in india, $\alpha$ - sunrises first in ind in aru pra; then we say that KB $\models$ $\alpha$ (read knowledge base entails alpha) <br> consider the knowledge base to be a hay stack... entailment tells if alpha is present in the haystack and inference tells about how to find it
- $Inference$ - finding $\alpha$ from all the consequences of the Knowledge Base... <br> sound: an inference algorithm is called _sound_ if the inference algorithm derives only entailed sentences... and we always want it to be sound... <br> complete: if the procedure can derive any entailed sentence, then that inference procedure is _complete_ 

##### Propositional Logic
1. Atomic sentences - single prop symbols... ex: $S_{11} \space \rightarrow is \space (1,1) \space safe$ , values : $true \space | \space false$ 
2. Complex sentences: logical connectives
	- Negation : $\neg S$ {$S, \neg S$ } $\rightarrow$ literal
	- Conjunction : $S_1 \wedge S_2$
	- disjunction : $S_1 \vee S_2$ 
	- implication : $S1 \rightarrow S2$
	- bidirectional implication : $S_1 \leftrightarrow S_2$ 
3. Backus Norur form.... 
4. Semantics
	- Model will specify true or false values to every proposition symbol

Inference : proof techniques
- model checking :
	- truth table enumeration

---

$$

\mathcal{By:} \space \mathscr{Srirama \space Srikar}
$$

 



## Week - 08


### Day 15 - 25.02.2025

$\forall  \text{x student(DS2020, x)} \Rarr \text{smart(x)}$ \
$\text{student(DS2020, Hemanth)}$ \
$substitution \space \text{\{x | Hemanth\}}$ \
$smart(Hemanth)$


Most general unifiers

unify(knows(x, B), knows(A,B)) \
{x | A} 

unify(knows(x, A), knows(B,y)) \
{x|B, y|A}


unify(knows(x, A), knows(B,x)) \
there exists no substitution for which the expressions are identical... \
Now when we encounter where we encounter such wepressions and have same variable present in both the expressions, we have to standardize the expressions... \
ie, replace x with y or something like that.


unify(f(g(x,dog)), y) , f(g(cat,y), dog) \
{x|cat, y|dog}




Every clause in knowledge base is an Horn clause... \
There is atmost one positive literal \
$(A \wedge B) \Rarr C \space \space \equiv (\neg A \vee \neg B \vee C)$

$\text{KB :  course(DS2020)} \\ \space \space \space \space \space \space \text{      teacher(ck)}$

$\forall x \space \forall y \space (\text{teacher(x)} \wedge \text{course(y)}) \Rarr \text{instructor(x,y)}$


Forward chaining and backward chaining... we are ignoring this as this is seemingly not relevant...



### Day 16 - 27.02.2025

#### Planning

Representing states

- state : logical sentences
- goal condition : logical sentences
- operators / actions : $\equiv$ representations using logical syntax
- assumptions:
  - actions are indivisible
  - no concurrent actions are allowed
  - deterministic
  - single agent
  - omniscient agent (no sensing is reqd)
  - closed world assumption : everything known to be true must be explicitly stated in the state description. If its left out in the state description then we assume that the statement is false

**Planning Domain Definition Language (PDDL)**
- state : conjunction of ground functionless atoms positive ground literals \
            on(x,y) $\Rarr$ x is on y \
            on(B, table) \
            on(A, table) \
            on(C, A) \
            block(x) \
            block(A) block (B) block(C) \
            clear(x) \
            clear(B) \
            clear(C) \
            clear(A) $\rarr$ false (as block C is on A) \
            but we cant add negation to the state description... so we get the info abt clear A form the closed world assumption
- goal : conjunction of literals (positive or negative) possibly with variables
  - variables are existentially quantified
  - a partially specified state
  - say $\exists x,y,z \space \text{on(x,y)} \wedge \text{on(y,z)}$ (a on b on c)
  - a state `s` statisfies the goal `g` if `s` unifies with all the literals present in `g`
- actions : state transformation... its defined in a schema
  - action(s) [set of actions applicable at s] : results(s,a)
  - eg action - \
        action : pick(x) \
        precondition: $\text{clear(x)} \wedge \text{block(x)}$  
        effect : $\neg armclear$ \ 
        action: placeOnTable(x) (for the action, we are assuming that all the variables are esistenetially quantified) \
        precondition: clear(x), clear(y) \
        effect: on(x,y), $\neg$ clear(y)
- precondition : refers to what should be true for the action to be applicable.
- effect : consequence of applying the action \
            conjunction of positive and negative literals \
            s: a $\in$ actions(s) [when is action a applicable in state s] \
            a $\in$ actions(s) $\Rarr$ s $\models$ precondition(a) \
                del(a) $\rarr$ negative literals present in  effect of a \
                add(a) $\rarr$ positive literals present in the effect of a \
                And we assume that all actions take unit amount of time.



**Planning** : sequence of actions resulting in a state where the goal is satisfied

**Forward Search** (Progression) : can result in irrelevant states... but it is a sound procedure


**Backward Search** (Regression) : relevant state search...


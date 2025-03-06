## Week - 09

### Day 17 - 06.03.2025

### Goal stack planning

```python
# Algorithm sketch :
def goal_stack_planning():
    # push goals onto a stack
    stack = Stack()
    stack.push(goal)
    # goal is a conjunct of predicates
    # push each predicate in the goal conjunct on to the stack
    stak.push(predicate) #???
    while stack:
        # pop element from the stack
        elem = stack.pop()
        if type(elem) == "conjunct":
            # if the element is a conjugation 
            # select as ordering of the sub goals
            # in the conjunction  and push them onto the stack
        else if type(elem) = "predicate":
            # if the element is a perdicate
            if True: 
                # do nothing
            else:
                # push relevant action on to the stack
                # push precondition of the action onto the stack
                # push each predicate in the precondition onto the stack
        else:
            # element is an action 

```

serilizable order: order which results in the agent not doing any extra actions... (Ex: show that there exists no such serializable order in which the agent can escape form performing extra actions... susman's anomaly)

Refer to Prof Rao's(ASU) website for more about planning...



### Probabilistic Reasoning

> Reasoning with uncertainity

We deal with sentences which have a degree of truth associated with it.

- logical rep: sentences are either `true` or `false` {0,1}
- probablistic rep: numerical degree of certainity [0,1]. (the agent has a belief in the present state) P(A) x U(A) = expected utility...

Random variavles: ex: weather\
disc. rv {cold, warm, hot} \
weather = warm (the rvs defined here become the propositions and we can define the probablity dist<sup>n</sup> on the rv)

cavity : P(cavity=True) = 0.5\
prior / unconditional probability \
P(cavity): {0.5, 0.5}

and similarly, P(weather) = {0.1,0.2,0.7}

here we are talking about only one random variable

now, P(cavity, weather)... here `,` means `and`  and it represents the join distn on cavity and weather... and it can mean the cartesian product...


If we have N boolean random variables... then we will have $2^n$ listings in the table...

From the join distn can we get the indiv distributions?? yep...

P(W=cold) = $\sum_{cav=TF} \text{P(W=cold, cavity)}$ - Marginilasation


Conditional Probability...

... 
> lot of stuff happening...  
> read from [artint](https://artint.info/2e/html2e/ArtInt2e.Ch8.html)...



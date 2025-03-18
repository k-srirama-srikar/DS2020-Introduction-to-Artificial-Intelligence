## Week 11

### Day 21 - 18.03.2025

_D Seperation_
- causal chain
- common cause
  - observing the clause blocks the infuluence fo the cause
- common effect
  - x-road repair, y-cricket match, z-traffic
  -  
    ```mermaid
    graph TD
        X-->Z
        Y-->Z
    ```
  - $P(x,y,z)=P(x)P(y)P(z|x,y)$
  - can we show x is independent of y? So without observing z, the causes become independent...
  - $P(x|y)=\frac{P(x,y)}{P(z)}$
  - $P(x,y)=P(x,y,z)+P(x,y, \neg z)=P(x)P(y)$
  - This is different form the other cases
  - Observing an effect activates influence between the possible causes
- Active/Inactive Paths
  - A path is active if each triplet in the path is active - dependencies between nodes
    - active paths
      ```mermaid
      graph LR
          X-->Y
          Y-->Z
      ```
      ```mermaid
      graph TD
          y-->z
          y-->x
      ```
      ```mermaid
         graph TD 
            X-->Z(Z')
            Y-->Z(Z')
      ```


Example:
- Is X independent of Y in the below example
  ```mermaid
     graph TD
         X-->Z
         Y-->Z
         Z-->z'
    ```
- here z is not being observed and hence x is independent of Y
- x and y are not conditionally independent given z
- similarly x and y are not conditionally independent given z'




Example 2:
- See below
  ```mermaid
     graph TD
         a-->b
         b-->c
         b-->e
         e-->e'
         d-->e
   ```
- C independent of D? No
- A independent of E' given E. yes... because b is inactive
- A independent of D. ($A \rarr B \rarr E \larr D$)... here the common effect triplet(BED) is inactive as e is not being observed.
- A and D independent given E. No
- A and D are independent given B,E


Conditional Independence in BNs - Markov Blanket \
?? \
Idk th this is


Influence by enumeration
- We want to estimate - $P(Q|e_1,\dots , e_k)$
- step 1,2,3
- slightly intelligent way to sum out variables from the join without actually constructing its explicit reprresentation.



Evalustion Tree
- recursive depth first search... but there will be redudancies in the evalustion tree made by vanilla enumeration


Variable Elimination

Factor zoo...
- Factor Zoo I
  - joint distn P(X,Y)... sums to 1
  - Selected joint P(x,Y)... entries P(x,y) for fixed x all y, sums upto P(x)
- Factor Zoo II
  - Single Conditional... P(Y|x)... entries P(y|x) for fixed x, all y... sums to 1
  - Family of conditionals... P(Y|X)... entries of P(y|x) for all x, for all y... sums to |X| cardinality of rv X
- Factor Zoo III
  - Specified family... P(y|X)... sums to who knows


Example: Traffic Domain
- Random Variables
  - R: raining
  - T: traffic
  - L: latfe for flight
  - 
- Inference by enumeration - Procedural outline
  - procedure tracks objects called factors
  - inital factors are local CPTs (one per node)
  - any known values are selected


Operation 1 - Join factors (similar to a dbms join) \
Operation 2 - Eliminate

Marginilizing Early (=Variable Elimination)
- $R \rarr T \rarr L$
- Join on r $$
- eliminate r
- join on t
- eliminate t
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

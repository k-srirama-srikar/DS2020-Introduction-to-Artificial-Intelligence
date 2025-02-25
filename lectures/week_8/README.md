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
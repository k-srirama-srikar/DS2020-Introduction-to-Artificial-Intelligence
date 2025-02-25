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

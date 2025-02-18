parent(john, mary).
parent(mary, susan).
parent(john, peter).
parent(peter, arthur).
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

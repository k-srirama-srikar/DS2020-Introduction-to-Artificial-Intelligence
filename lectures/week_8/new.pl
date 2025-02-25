% Rule: If someone is a student of DS2020, they are smart.
smart(X) :- student(courses:DS2020, X).

% Fact: Hemanth is a student of DS2020.
student(courses:DS2020, hemanth).

% Query to check if Heman is smart
is_smart(X) :- smart(X), !.


% modus ponens...





% unification 

% Unifying two terms:
unify(Term1, Term2, Substitution) :-
    unify_terms(Term1, Term2, [], Substitution).

% Base case for constants (i.e., no further unification needed for constants):
unify_terms(Term, Term, Substitution, Substitution).

% Case for unifying variables with constants or other variables:
unify_terms(X, Y, Substitution, [X = Y | Substitution]) :-
    var(X), \+ var(Y),  % X is a variable and Y is a constant
    not_member(X, Substitution).  % Ensure there's no circular dependency

unify_terms(X, Y, Substitution, [X = Y | Substitution]) :-
    var(Y), \+ var(X),  % Y is a variable and X is a constant
    not_member(Y, Substitution).  % Ensure there's no circular dependency

unify_terms(X, Y, Substitution, NewSubstitution) :-
    var(X), var(Y),  % Both are variables
    X \= Y,  % Ensure they are not the same variable
    not_member(X, Substitution),
    not_member(Y, Substitution),
    NewSubstitution = [X = Y | Substitution].  % Add the new unification

% Case for unifying compound terms:
unify_terms(f(Functor1, Args1), f(Functor2, Args2), Substitution, NewSubstitution) :-
    Functor1 = Functor2,  % The functors must be the same
    unify_arguments(Args1, Args2, Substitution, NewSubstitution).

% Unifying lists of arguments:
unify_arguments([], [], Substitution, Substitution).  % Base case for empty lists
unify_arguments([Arg1 | Args1], [Arg2 | Args2], Substitution, NewSubstitution) :-
    unify_terms(Arg1, Arg2, Substitution, TempSubstitution),
    unify_arguments(Args1, Args2, TempSubstitution, NewSubstitution).

% Ensuring there is no circular dependency in the substitution:
not_member(_, []).
not_member(X, [X = _ | _]).
not_member(X, [_ = Y | Rest]) :- X \= Y, not_member(X, Rest).

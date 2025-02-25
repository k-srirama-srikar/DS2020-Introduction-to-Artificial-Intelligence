t.
f:- fail.

t(_).

f(_):- fail.

and(P,Q) :- P, Q, !.
or(P,Q) :- (P; Q), !.

:- op(400,xf,not).
:- op(500,xfx,and).
:- op(500,xfx,or).
:- op(600,xfx,implies).
:- op(600,xfx,equiv).

:- op(400,xf,~).
:- op(500,xfx,^).
:- op(500,xfx,v).
:- op(600,xfx,=>).
:- op(600,xfx,<=>).

~P :- not P.
P ^ Q :- P and Q.
P v Q :- P or Q.
P => Q :- P implies Q.
P <=> Q :- P equiv Q.

P implies Q :- not P or Q.
P equiv Q :- (P and Q) or (not P and not Q).
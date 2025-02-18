## Week 07

### Day 14 - 18.02.2025
### Propositional Logic
- declerative
- partial / disjunctive / neglected information
- compositional
- context independent / unambiguous
- limited expressive power

### First Order Logic (Predicate Logic):
- objects : Ex - Player / Yantra / Exit
- relations : Ex - Gold(Yantra1), father_of(someone), brother(p1, p2)
- constants: Ex: Player, someone
- Predicate Symbols: 
- 
-
- terms : father_of(someone) -> term
- atomic senetence : wall([1,1])
- complex sentences : atomic sentences combinedthrough logical operators
  - quantifiers:
    - $\forall$ : for all. universal... $\forall x | P(x) \rarr true$
    - $\exists$ : there exists... exestential quantifier... $\exist x \space Prime(x)$
      - De Morgan's laws
      - $\forall x \neg P(x) \equiv \neg \exists x \space P(x)$
      - $\neg (\forall x P(x)) \equiv \exist x \neg P(x)$
      - $\neg (\exist x \neg P(x)) \equiv \forall x P(x)$
      - $\exist x P(x) \equiv \neg (\forall x \neg P(x))$
      - worls $\equiv$ interpretations
      - s is valid if s is true for all interpretations
      - s is satisfiable: if $\exist$ an interpretation for which s is true
      - s is unsatisfiable: s is false for all interpretations. \
        $s_1 \models s_2$  $M(s_1) \subseteq M(s_2)$

- Ex : wall breeze ... where wall is there, there is breeze adj.. \
  $\forall i \forall j \space wall(i,j) \rArr [\forall k \space \forall l \space adj(i, j, k, l) \rArr Breeze(k, l)]$
- lifting lemma... idk wth it is...
- Instnantiation
  - universeally quantified sentence:
  - existentially quantified sentence:
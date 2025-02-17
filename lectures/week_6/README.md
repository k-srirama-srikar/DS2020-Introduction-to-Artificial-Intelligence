## Week 6
### Day 11 - 11.02.2025
### Logical Agents
- inference : KB $\models \space \alpha$. M(KB) $\subseteq$ M($\alpha$) 
    > Knowledge is a conjundction of sentences...
- Propositional logic
- Truth table enumereation
- Model: world in which the sentence is true 
    > world: truth values assigned to the symbols


1. **Truth table enumeration**:  Ex : $(\alpha \wedge \beta) \vee (\gamma \wedge \delta)$ - KB  (seven worlds where KB is true... $\gamma$ and $\delta$ are true in 4 worlds and similarly for the other and the world `T T T T` is common in both worlds so there are 7 worlds...) if $\omega$ is a  model then it'll be true in the 7 worlds as well... we do a dfs to get the solution...
2. **Theorem Proving**: (There'  a lang called lean which supports the theorm proving and with the advent of llms ppl are thinking to combine the theorem proving something...)
    - logical equivalences <br> 
        $(\alpha \vee \beta) \equiv (\beta \vee \alpha)$ \
        $\neg (\neg \alpha) \equiv \alpha$ \
        $(\alpha \rightarrow \beta) \equiv (\neg \alpha \vee \beta)$ (implication elimination) \
        $(\alpha \rightarrow \beta) \equiv (\beta \rightarrow \neg \alpha)$ (contraposition) \
        $(\alpha \Leftrightarrow \beta) \equiv (\alpha \Rightarrow \beta)\wedge (\beta \Rightarrow \alpha)$
    - valid : a sentence $\alpha$ is valid if it is true on all worlds ($\alpha$ is a tatutology)
    - KB $\models \space \alpha$ iff $(KB \Rightarrow \alpha)$ is valid
    - Satisfiability: A sentence $\alpha$ is satisfiable if it is true in some world... SAT problem - can u find a model for the problem? (it's an NP complete problem...)
    - Unsatisfiablity: a sentence $\alpha$ is unsatisfiable if it is true in no world... if $\alpha$ is unsatisfiable then $\neg \alpha$ is valid
    - $(KB \models \alpha)$ iff $\neg (KB \Rightarrow \alpha)$ is unsatisfiable $\equiv KB \wedge \neg \alpha$ is unsatisfiable... proof by contradiction...
    - Resolution (unit resolution) \
        KB = $((\alpha \vee \beta) \wedge \neg \beta) \equiv \space true$ this boils down to $\alpha$ ... if theres a disjucntion of literals and theres a literal with negation then we can get another disjunction excluding the negated literals...
        > clause : disjunction of literals
    - resolution procedure: assumes that the KB is in Conjunctive Normal Form...

    - full resolution rule (for cnf): \
        $(l_1 \vee ... \vee l_i \vee ... l_k) \space \space (m_1 \vee ... \vee m_j \vee ... m_n)$ and $l_i= \neg m_j$ (complimentary literal)... we are basically deriving new clauses which are true... or somthing like that...


---

<p align='center'> 
$\mathcal{By:} \space \mathscr{Srirama \space Srikar}$ 
</p>

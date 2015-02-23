from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES
from functools import partial

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    goal = OR(hypothesis)
    backchain = partial(backchain_to_goal_tree, rules)

    for rule in rules:
        csq = rule.consequent()
        if isinstance(csq, str): csq = [csq]

        for clause in csq:
            binds = match(clause, hypothesis)

            if binds != None:
                ants = rule.antecedent()
                if isinstance(ants, str): ants = [ants]

                op = None
                if isinstance(ants, OR): op = OR
                else: op = AND

                goal.append(op([backchain(populate(ant, binds)) for ant in ants]))

    return simplify(goal)


# Here's an example of running the backward chainer - uncomment
# it to see it work:
#print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')

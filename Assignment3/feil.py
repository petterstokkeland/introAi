 def alfaBetaMinValue(gameState, depth, agent, a, b):
            """
            Calculates the action that leads to the lowest score in our zero sum game.
            The score is calculated unbiased and a negative score means our ghost agent is "leading"
            ghost agents therefore aim to get the lowest possible score, even in a losing position. (optimal play)

            In alpha-beta pruning we cut our computation short if we know our best min() evaluation is lower than
            anything the parent alfaBetaMaxValue function would choose. threshold value is a.

            :param gameState:
            :param depth: the dept we currently are at.
            :param agent: agent, will be >0 (ghost-agent)
            :param a: alpha, the highest value we can find in our scope (depends on gameState)
            :param b: beta, the lowest value we can find in our scope (depends on gameState)
            :return:
            """
            # represents positive infinity, we are searching to make minimum as low as possible
            minimum = 1000000
            # we will set this variable as the best action (corresponds to minimum value)
            bestAction = None
            ghostActions = gameState.getLegalActions(agent)

            # if there are no legal actions we are in a terminal state
            if not ghostActions:
                return self.evaluationFunction(gameState), None

            for action in ghostActions:
                # emulates the state we want to check
                stateAfterAction = gameState.generateSuccessor(agent, action)
                # we are only interested the value
                evalValue, evalAction = alfaBetaMinOrMax(stateAfterAction, depth, agent + 1, a, b)
                if evalValue < minimum:
                    minimum, bestAction = evalValue, action
                # important: returns evalValue and action immediately if this is true, all computations will
                # result in giving parent alfaBetaMaxValue a worse choice than it already has
                if evalValue < a:
                    return evalValue, action
                b = min(b, evalValue)
            return minimum, bestAction

        def alfaBetaMaxValue(gameState, depth, agent, a, b):
            """
            Calculates the action that leads to the highest score in our zero sum game.
            The score is calculated unbiased and a negative score means our ghost agent is "leading"
            ghost agents therefore aim to get the lowest possible score, even in a losing position. (optimal play)

            In alpha-beta pruning we cut our computation short if we know our best max() evaluation is higher than
            anything the parent alfaBetaMinValue function would choose. threshold value is b.

            :param gameState:
            :param depth: the dept we currently are at.
            :param agent: agent, will be 0 (pacman-agent).
            :param a: alpha, the highest value we can find in our scope (depends on gameState)
            :param b: beta, the lowest value we can find in our scope (depends on gameState)
            :return:
            """
            # represents negative infinity, we are searching to make minimum as high as possible
            maximum = -1000000
            # we will set this variable as the best action (corresponds to maximum value)
            bestAction = None
            pacmanActions = gameState.getLegalActions(agent)

            # if there are no legal actions we are in a terminal state
            if not pacmanActions:
                return self.evaluationFunction(gameState), None

            for action in pacmanActions:
                # emulates the state we want to check
                stateAfterAction = gameState.generateSuccessor(agent, action)
                # we are only interested the value
                evalValue, evalAction = alfaBetaMinOrMax(stateAfterAction, depth, agent + 1, a, b)
                if evalValue > maximum:
                    maximum, bestAction = evalValue, action
                # important: returns evalValue and action immediately if this is true, all computations will
                # result in giving parent alfaBetaMinValue a worse choice than it already has
                if evalValue > b:
                    return evalValue, action
                a = max(a, evalValue)
            return maximum, bestAction
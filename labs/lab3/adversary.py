def score(pos, game):
        """
        Computes a utility score based on the player's distance to the goal vs the opponent's distance to the goal.

        Parameters:
        - pos (tuple): The position to evaluate.

        Returns:
        - int: The utility value (lower values are better for the player).
        """
        dist_to_goal = abs(pos[0] - game.goal_pos[0]) + abs(pos[1] - game.goal_pos[1])
        opponent_pos = game.p1_pos
        opponent_dist_to_goal = abs(opponent_pos[0] - game.goal_pos[0]) + abs(opponent_pos[1] - game.goal_pos[1])
        return opponent_dist_to_goal - dist_to_goal

def AdversaryMove(pos, game):
    """
    This function determines the best move for the adversary (Player 2) in the game.  
    The adversary aims to minimize the player's (Player 1) advantage by considering  
    possible future moves.

    Parameters:
    - pos (tuple): The current position of the adversary as (row, col).
    - game (Game object): The game instance that provides methods like `is_valid(position)` 
      to check valid moves and `heuristic(position)` to evaluate move quality.

    Return Value:
    - best_move (str): The optimal move direction ('N', 'S', 'E', 'W') that minimizes  
      the player's advantage. If no optimal move is found, a fallback valid move is chosen.
    """
    move_offsets = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)} # possible directions.
    best_score = float('inf')  # Player 2 minimizes
    best_move = None

    for move, offset in move_offsets.items():
        new_pos = (pos[0] + offset[0], pos[1] + offset[1])
        if game.is_valid(new_pos):
            player_score = score(new_pos,game)
            min_opponent_score = float('inf')
            # 2-level search
            for sub_move, sub_offset in move_offsets.items():
                sub_new_pos = (new_pos[0] + sub_offset[0], new_pos[1] + sub_offset[1])
                if game.is_valid(sub_new_pos):
                    sub_score = score(sub_new_pos,game)
                    min_opponent_score = min(min_opponent_score, sub_score)
            
            net_score = player_score - min_opponent_score
            # condition to choose best_move
            if net_score < best_score:
                best_score = net_score
                best_move = move
    
    # if no best move found
    if best_move is None:
        for move, offset in move_offsets.items():
            new_pos = (pos[0] + offset[0], pos[1] + offset[1])
            if game.is_valid(new_pos):
                return move

    return best_move


def NoviceMove(pos,game):
    """This function determines the move for a novice adversary (Player 2) in the game.  
    The novice adversary follows a very simple strategy:  
    - Always tries to move ('E')."""
    offset = {'E': (1, 0), 'S': (0, -1),'W': (-1, 0), 'N': (0, 1)}
    for direction, (dx, dy) in offset.items():
        new_pos = (pos[0] + dx, pos[1] + dy)
        if game.is_valid(new_pos):
            return direction
    
    
'''NOTE: THIS IS A POTENTIAL SOLUTION
         If approved we will be removing code part from all functions except play_game inside YantraCollector Class.
'''
import random
from adversary import AdversaryMove, NoviceMove
move_offsets = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
class YantraCollector:
    def __init__(self, p1_pos, p2_pos, goal_pos,grid_size,player1_strategy):
        """
        Initializes the game with the starting positions of Player 1, Player 2, and the goal position.
       

        Parameters:
        - p1_pos (tuple): (row, col) position of Player 1.
        - p2_pos (tuple): (row, col) position of Player 2.
        - goal_pos (tuple): (row, col) position of the goal.

        Returns:
        - None
        """
        self.p1_pos = p1_pos  
        self.p2_pos = p2_pos
        self.goal_pos = goal_pos
        self.grid_size = grid_size
        self.p1_strat = player1_strategy 
        self.is_p1_turn = True  # Track whose turn it is
        self.path=[]

    def is_valid(self, pos):
        """
        Checks if a position is within the game grid boundaries.

        Parameters:
        - pos (tuple): (row, col) position to check.

        Returns:
        - bool: True if position is valid, False otherwise.
        """
        # print(self.grid_size)
        # print("Pos", pos)
        # returns FAlse if the position is outside the grid and True otherwise
        if pos[0] < 0 or pos[0] >= self.grid_size or pos[1] < 0 or pos[1] >= self.grid_size:
            return False
        return True

    def move_player(self, player, direction):
        """
        Moves the given player in the specified direction. 
        ENSURE THAT THE PLAYER MAKES A MOVE THAT IS "VALID", i.e., IT IS MOVING TO A POSITION INSIDE THE GRID

        Parameters:
        - player (int): 1 for Player 1, 2 for Player 2.
        - direction (str): One of ['N', 'S', 'E', 'W'] indicating the movement direction.

        Returns:
        - None
        """
        move_offsets = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        
        if player == 1:
            new_pos = (self.p1_pos[0] + move_offsets[direction][0], self.p1_pos[1] + move_offsets[direction][1])
            if self.is_valid(new_pos):
                self.p1_pos = new_pos
        else:
            new_pos = (self.p2_pos[0] + move_offsets[direction][0], self.p2_pos[1] + move_offsets[direction][1])
            if self.is_valid(new_pos):
                self.p2_pos = new_pos

    def utility(self, pos):
        """
        Computes a utility score based on the player's distance to the goal vs the opponent's distance to the goal.

        Parameters:
        - pos (tuple): The position to evaluate. pos is a tuple of the position of Player 1 and Player 2.

        Returns:
        - int: The utility value (higher the value the better for player 1).
        """
        # returns the utility value based on the distance of the player from the goal and the distance of the opponent from the goal
        p1 =  pos[0]
        p2 =  pos[1]
        if p1 == self.goal_pos:
            return 1e9
        if p2 == self.goal_pos: 
            return -1e9
        # we get the manhattan distance of the player from the goal and the opponent from the goal
        # and then we return the difference of the distances
        p1_dist = abs(p1[0] - self.goal_pos[0]) + abs(p1[1] - self.goal_pos[1])
        p2_dist = abs(p2[0] - self.goal_pos[0]) + abs(p2[1] - self.goal_pos[1])
        return p2_dist - p1_dist

    def best_player_move(self, pos):
        """
        Determines the best move for Player 1 as per the current strategy for Player 1 (stored in self.p1_strat)

        Parameters:
        - pos (tuple): The current position of the player.
        - depth (int): Search depth for minimax.

        Returns:
        - str: The best move direction ('N', 'S', 'E', 'W').
        """
        # based on the strategy of player 1 we choose the best move
        if self.p1_strat == "random":
            return self.random_move(pos)
        elif self.p1_strat == "minimax_vanilla":
            # we initially explore the first set of game positions and 
            # then we call the minimax for each of the possible moves
            # and then we choose the move which gives the best value
            depth = 7
            best_dir = None
            best_val = float('-inf')
            dir_vals=[]
            for dir in move_offsets:
                p1_new = (pos[0] + move_offsets[dir][0], pos[1] + move_offsets[dir][1])
                p2_new = (self.p2_pos[0] + move_offsets[dir][0], self.p2_pos[1] + move_offsets[dir][1])
                if self.is_valid(p1_new):
                    p1 = p1_new
                else:
                    continue
                if self.is_valid(p2_new):
                    p2 = p2_new
                else:
                    p2=self.p2_pos
                new_pos = (p1, p2)
                val = self.minimax_vanilla(new_pos, depth-1, False)
                dir_vals.append((dir,val, new_pos))
                if val > best_val:
                    best_val = val
                    best_dir = dir
            return best_dir
        elif self.p1_strat == "minimax":
            depth = 5
            best_dir = None
            best_val = float('-inf')
            for dir in move_offsets:
                p1_new = (pos[0] + move_offsets[dir][0], pos[1] + move_offsets[dir][1])
                p2_new = (self.p2_pos[0] + move_offsets[dir][0], self.p2_pos[1] + move_offsets[dir][1])
                if self.is_valid(p1_new):
                    p1 = p1_new
                else:
                    continue
                if self.is_valid(p2_new):
                    p2 = p2_new
                else:
                    p2=self.p2_pos
                new_pos = (p1, p2)
                val = self.minimax(new_pos, depth-1, False)
                if val > best_val:
                    best_val = val
                    best_dir = dir
            return best_dir
            
    
    

    def random_move(self, pos):
        """
        Chooses a random valid move.
        Parameters:
        - pos (tuple): The current position.

        Returns:
        - str: A random move direction ('N', 'S', 'E', 'W').
        """
        # given a position we check for the directions which result in a valid move 
        # and then we choose a random direction from the valid moves
        valid_moves = []
        for move in move_offsets:
            new_pos = (pos[0] + move_offsets[move][0], pos[1] + move_offsets[move][1])
            if self.is_valid(new_pos):
                valid_moves.append(move)
        return random.choice(valid_moves) if valid_moves else None
    
    
    def minimax_vanilla(self, pos, depth, max_turn=True):
        """
        Determines the best move using the vanilla Minimax algorithm (without alpha-beta pruning).

        Parameters:
        - pos (tuple): The current position of the player.
        - depth (int): Search depth for minimax.
        - max_turn (bool): True if maximizing Player 1, False for minimizing Player 2.

        Returns:
        - int: The minimax score if called recursively.
        """
        if pos[0]==self.goal_pos or depth==0:
            return self.utility(pos)
        
        best_val = float('-inf') if max_turn else float('inf')
        for move in ['N', 'S', 'E', 'W']:
            new_pos = (pos[0], pos[1])
            p1_new = (new_pos[0][0] + move_offsets[move][0], new_pos[0][1] + move_offsets[move][1])
            if self.is_valid(p1_new):
                new_pos = (p1_new, new_pos[1])
            else: 
                continue
            # if its a valid move we update the position of the player 1
            # else we continue to the next move
            # if player 2 doesnt have a vlid move we continue the search
            # with the same position
            p2_new = (new_pos[1][0] + move_offsets[move][0], new_pos[1][1] + move_offsets[move][1])
            if self.is_valid(p2_new):
                new_pos = (new_pos[0], p2_new)
            val = self.minimax_vanilla(new_pos, depth-1, not max_turn)
            
            if max_turn:
                if val > best_val:
                    best_val = val
            else:
                if val < best_val:
                    best_val = val
        return best_val/10 if best_val>=1e4 else best_val
        # return best_val
        

    def minimax(self, pos, depth, alpha=float('-inf'), beta=float('inf'), max_turn=True):
        """
        Implements the minimax algorithm with alpha-beta pruning to determine the best move.

        Parameters:
        - pos (tuple): The current position.
        - depth (int): Depth remaining in search.
        - alpha (float): Alpha value for pruning.
        - beta (float): Beta value for pruning.
        - max_turn (bool): True if maximizing Player 1, False for minimizing Player 2.

        Returns:
        - int: The minimax score.
        """
        if pos[0] == self.goal_pos or depth == 0:
            return self.utility(pos)
        
        if max_turn:
            max_val = float('-inf')
            for move in ['N', 'S', 'E', 'W']:
                new_pos = (pos[0], pos[1])
                p1_new = (new_pos[0][0] + move_offsets[move][0], new_pos[0][1] + move_offsets[move][1])
                if self.is_valid(p1_new):
                    new_pos = (p1_new, new_pos[1])
                else:
                    continue
                p2_new = (new_pos[1][0] + move_offsets[move][0], new_pos[1][1] + move_offsets[move][1])
                if self.is_valid(p2_new):
                    new_pos = (new_pos[0], p2_new)
                # we get the new position and then we call the minimax for the new position
                val = self.minimax(new_pos, depth-1, alpha, beta, not max_turn)
                max_val = max(max_val, val)
                if max_val >= beta:
                    return max_val
                    # we prune the search here as the alpha is less than beta
                alpha = max(alpha, val)
            return max_val
        else:
            min_val = float('inf')
            for move in ['N', 'S', 'E', 'W']:
                new_pos = (pos[0], pos[1])
                p1_new = (new_pos[0][0] + move_offsets[move][0], new_pos[0][1] + move_offsets[move][1])
                if self.is_valid(p1_new):
                    new_pos = (p1_new, new_pos[1])
                else:
                    continue
                p2_new = (new_pos[1][0] + move_offsets[move][0], new_pos[1][1] + move_offsets[move][1])
                if self.is_valid(p2_new):
                    new_pos = (new_pos[0], p2_new)
                val = self.minimax(new_pos, depth-1, alpha, beta, not max_turn)
                min_val = min(min_val, val)
                if min_val <= alpha:
                    return min_val # here also we prune the search tree
                beta = min(beta, val)
            return min_val
        
    def play_game(self):
        """
        Runs the game loop until a player reaches the goal or a draw occurs.

        Returns:
        - str: "P1" if Player 1 wins, "P2" if Player 2 wins, or "draw" if there's no winner.
        """
        seen_positions = set()
        while True:
            state = (self.p1_pos, self.p2_pos)
            if self.p1_pos == self.p2_pos:
                return "draw"
            if state in seen_positions:
                return "draw"
            seen_positions.add(state)

            if self.is_p1_turn:
                best_move = self.best_player_move(self.p1_pos)
                self.path.append(best_move)
                self.move_player(1, best_move)
                self.move_player(2, best_move)  # P2 mimics P1
            else:
                best_move = AdversaryMove(self.p2_pos, self)
                self.move_player(2, best_move)
                self.move_player(1, best_move)  # P1 mimics P2
            
            # print(self.p1_pos, self.p2_pos)

            if self.p1_pos == self.goal_pos:
                return "P1"
            
            elif self.p2_pos == self.goal_pos:
                return "P2"
            
            self.is_p1_turn = not self.is_p1_turn

    def play_game_novice(self):
        """
        Runs the game loop where Player 2 follows a novice strategy (always moving East if possible).

        Returns:
        - str: "P1" if Player 1 wins, "P2" if Player 2 wins, or "draw" if there's no winner.
        """
        seen_positions = set()
        while True:
            state = (self.p1_pos, self.p2_pos)
            # print("State",state)
            if self.p1_pos == self.p2_pos:
                return "draw"
            if state in seen_positions:
                return "draw"
            seen_positions.add(state)

            if self.is_p1_turn:
                best_move = self.best_player_move(self.p1_pos)
                self.path.append(best_move)
                self.move_player(1, best_move)
                self.move_player(2, best_move)  # P2 mimics P1
            else:
                best_move = NoviceMove(self.p2_pos,self)  # Using NoviceMove
                self.move_player(2, best_move)
                self.move_player(1, best_move)  # P1 mimics P2
            
            # print(self.p1_pos, self.p2_pos)

            if self.p1_pos == self.goal_pos:
                return "P1"
            
            elif self.p2_pos == self.goal_pos:
                return "P2"
            
            self.is_p1_turn = not self.is_p1_turn  


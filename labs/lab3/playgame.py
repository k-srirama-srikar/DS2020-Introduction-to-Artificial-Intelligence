from player import YantraCollector

"""
This script runs the YantraCollector game by initializing different starting positions  
for Player 1 and Player 2, and then executing the game loop using different strategies.

Scenarios Covered:
1. Player 2 (Novice) vs Player 1 (Random)
2. Player 2 (Amateur) vs Player 1 (Random)
3. Player 2 (Novice) vs Player 1 (Minimax Vanilla - No Pruning)
4. Player 2 (Amateur) vs Player 1 (Minimax Vanilla - No Pruning)
5. Player 2 (Novice) vs Player 1 (Minimax with Alpha-Beta Pruning)
6. Player 2 (Amateur) vs Player 1 (Minimax with Alpha-Beta Pruning)

Each scenario runs for multiple predefined starting positions.
"""

def run_scenario(description, strategy, method):
    """Runs a scenario with a given strategy and method."""
    print(description)
    try:
        for p1_start, p2_start in positions:
            game = YantraCollector(p1_start, p2_start, goal_position,grid_size=7,player1_strategy=strategy)
            result = getattr(game, method)()
            print(f"For positions P1:{p1_start} P2:{p2_start}\nResult:", end="\t")
            print("Draw Game" if result == "draw" else f"{result} Wins")
        print("-" * 90)
    except Exception as e:
            print(f"Error occurred while running scenario '{description}': {e}")

if __name__ == "__main__":
    goal_position = (4, 4)
    positions = [((1, 4), (4, 0)), ((1, 4), (4, 6))]
    
    scenarios = [
        ("P1 Random Move vs P2 Novice", "random", "play_game_novice"),
        ("P1 Random Move vs P2 Amateur", "random", "play_game"),
        ("P1 Minimax Vanilla vs P2 Novice", "minimax_vanilla", "play_game_novice"),
        ("P1 Minimax Vanilla vs P2 Amateur", "minimax_vanilla", "play_game"),
        ("P1 Minimax Alpha-Beta vs P2 Novice", "minimax", "play_game_novice"),
        ("P1 Minimax Alpha-Beta vs P2 Amateur", "minimax", "play_game")
    ]
    
    for scenario in scenarios:
        run_scenario(*scenario)

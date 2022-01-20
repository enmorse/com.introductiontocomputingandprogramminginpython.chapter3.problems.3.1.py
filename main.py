# You are running a bingo game where you want to
# tweet the winner of each round of the game. You
# want to announce the name of who won in dollars.
# Make a function that takes those two words in as
# input, and then announces the win. For now, just
# print the statement that you will want to tweet later.

def bingo(name, won):
    print(f"{name.title()} Called Bingo! {name.title()} "
          f"Won ${str(won)} dollars.")


bingo("Ernest", 50)

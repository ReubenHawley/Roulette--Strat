# Roulette--Strat
a simple console based roulette game with the sole purpose of back testing strategies.This was the first game i built, originally using functional programing.After learning OOP, ported it over to an object oriented approach, this helped me grasp inheritance and objects.

---
__Definition__
> a gambling game in which a ball is dropped on to a revolving wheel with numbered compartments, the players betting on the number at which the ball comes to rest.
> Here i simulated the ball landing on a particular spot by using the random module
---
__How it works:__
> A player starts off with initial capital
> then a bet is placed on a particular place on the board
>supported bets include:
> - Numbers ( 0 - 36)
> - Columns (1st , 2nd , 3rd )
> - Rows (1st , 2nd , 3rd )
> - Colors( Black / RED )
> - High ( 19 - 36 )
> - Low ( 1 - 18 )
> - Odd
> - Even

> If the player guesses correctly then a wager multiplier is paid out based on the bet position and size.
> If the player guess incorrectly the initial bet is lost to the house.
> this repeats endlessly until the player stops or untill the funds reach 0.

__Wager Multiplier__

|Bet placed | multiplier |
|-----------|:----------:|
|Numbers |36|
|Columns |3|
|Rows |3|
|Colors |2|
|High |2|
|Low |2|
|Odd |2|
|Even |2|


__What i learned from this:__
> - Conditionals: catering for multiple responses, whether expected or not.
> - Event handling
> - Object Oriented Programming 

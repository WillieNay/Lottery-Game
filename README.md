# Lucky Number Game

This is a simple number guessing game where users can test their luck and win money by matching their chosen number with the system-generated lucky number. The game incorporates a secure random number generator for fairness.

---

## Features

1. **User Authentication**:
   - Ensures the user is at least 18 years old.
   - Requires the user to deposit at least $5000 to start playing.

2. **Secure Random Number Generation**:
   - Uses Python's `secrets.SystemRandom` for generating a secure random lucky number.

3. **Game Rules**:
   - Users must deposit more than $1000 per round to play.
   - Matching the lucky number (20) rewards the user with 10x the deposited amount.

4. **Interactive Gameplay**:
   - Allows users to play multiple rounds until they choose to quit or run out of funds.
   - Displays informative messages about the user's current balance and game results.

---

## Game Rules

**Eligibility**: Users must be at least 18 years old.
Users must deposit a minimum of $5000 to start.

**Gameplay**: Deposit at least $1000 each round to play.
Choose a lucky number between 10 and 99.
If your lucky number matches the system's lucky number (20), you win:
Winnings = Deposit Amount × 10
If you don't win, your deposit is deducted from your total balance.

**End of Game**: The game ends when your balance falls below $1000 or when you choose to quit.

---

## Key Functions

**secureNumber.randint(a, b)**: Generates a secure random number between a and b.

**Game Logic**: Compares the user's lucky number with the system-generated number.
Updates the user's balance based on the result.

**Input Validation**: Ensures valid age, name, and deposit values.

---

## Notes
**Winning Number**: The system's winning number is hardcoded as 20.
**Error Handling**: The script ensures robust input validation and prevents invalid entries.

---

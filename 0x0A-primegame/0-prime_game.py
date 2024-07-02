#!/usr/bin/python3
"""0-prime_game.py"""


def sieve_of_eratosthenes(max_num):
    """
    Generate a list of boolean values indicating the primality
    of numbers up to max_num using the Sieve of Eratosthenes algorithm.

    Args:
    max_num (int): The maximum number to check for primality.

    Returns:
    list: A list where the index represents the number
    and the value at that index is True if the number
    is prime, False otherwise.
    """
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def isWinner(x, nums):
    """
    Determine the overall winner after playing x rounds of the prime game.

    Args:
    x (int): The number of rounds.
    nums (list): A list of integers where each integer n
    represents the upper bound of the set {1, 2, ..., n} for each round.

    Returns:
    str or None: The name of the player with the most wins
    ("Maria" or "Ben"), or None if they have the same number of wins.
    """
    max_num = max(nums)
    is_prime = sieve_of_eratosthenes(max_num)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = [i for i in range(1, n + 1) if is_prime[i]]
        turn = 0
        while primes:
            current_prime = primes[0]
            primes = [p for p in primes if p % current_prime != 0]
            turn = 1 - turn
        if turn == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

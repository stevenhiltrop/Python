# FizzBuzz Algorithm

It’s finally time to learn how to solve FizzBuzz, the popular interview question designed to eliminate candidates: write a program that prints the numbers from 1 to 100. But for the multiples of 3, print “Fizz” instead of number, and multiples of five print “Buzz.” For multiples of three and five, print “FizzBuzz”.

To solve this problem, you need a way to check if a number is a multiple of three, a multiple of five, both, or neither. If a number is a multiple of three, if you divide it by three, there is no remainder.

The same applies to five. The modulo (%) operator returns the remainder. You can solve this problem by going through the numbers and checking if each number is divisible by three and five, only three, only five, or none
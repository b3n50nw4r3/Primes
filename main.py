# Check if a specific number is a prime number
def isPrime(number):
  for x in range(2, number):
    # If this is true, the number is not prime
    if number % x == 0:
      print(str(number) + " is not prime")
      return False
  # If it got here, the number is prime
  print(str(number) + " is prime")
  return True

# Repeat the application after the command is processed
while True:
  print("What number to check for prime?")
  number = int(input())
  isPrime(number)
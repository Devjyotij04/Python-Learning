def fizzbuzz(n):
    counter = 0
    while counter <= n :
        if counter % 3 == 0 and counter % 5 == 0 :
            print("FizzBuzz")
        elif counter % 3 == 0 :
            print("Fizz")
        elif counter % 5 == 0 :
            print("Buzz")
        else :
            print(counter)
        counter += 1

fizzbuzz(30)
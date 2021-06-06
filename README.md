# FibonnaciAPI
Flask API to find the nth number based on the value passed in the ID

Problem Statement:
Introduction: A researcher wants an API that iteratively keeps returning numbers in the Fibonacci series.
Write a class will behave like an Iterator, that will expose a next() function. On each call to next(), the
next integer in the Fibonacci series should be returned.

The class will also provide a constructor with an integer argument 'n'. The argument denotes the "jump"
value that will initialize the object 'n' steps ahead from the start of the series. The call to next() should
then return the values from this stepped ahead index in the series.

Example:
If an object is initialized as:

FibIterator iterator = new FibIterator(4);

int next = iterator.next();

The value of next should be 5.

Input: None
Output: The API should expose the next() function, that will return the appropriate number.


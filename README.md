# FibonnaciAPI
Flask API to find the nth number based on the value passed in the ID

# Problem Statement:
Introduction: A researcher wants an API that iteratively keeps returning numbers in the Fibonacci series.
Write a class will behave like an Iterator, that will expose a next() function. On each call to next(), the
next integer in the Fibonacci series should be returned.

The class will also provide a constructor with an integer argument 'n'. The argument denotes the "jump"
value that will initialize the object 'n' steps ahead from the start of the series. The call to next() should
then return the values from this stepped ahead index in the series.

Example:
If an object is initialized as:\
FibIterator iterator = new FibIterator(4);\
int next = iterator.next();\
The value of next should be 5.

Input: None
Output: The API should expose the next() function, that will return the appropriate number.


# Solution Fibonnaci Jump API

The Readme guide is for Windows OS:

Project Setup:
Create the folder structure by giving the following commands:\
1) md projects\
2) cd projects\
3) md api

Copy the code inside prasad_desai_programming_problem_2.py to api.py in the api folder you created for this project.

For Executuing the Application:\
1) Open cmd \
2) Navigate to the api folder\
3) Run the Flask application with the command: python api.py\

Flask will be running the application locally on the address: http://127.0.0.1:5000/

API Discription:

1) The link "http://127.0.0.1:5000/"  
	i) Lets us know if the server has started successfully\
2) The link "http://127.0.0.1:5000/api/fibonnaci/all"  
	i) Lets us know all the jump values the researcher has check.\
	ii) If we directly call this api without checking jump value for even once then an error "The fibonnaci for a jump number has not been called even once by researcher" will be displayed.\
	iii) If we have called jump api even once and then we call this api then it'll show a key, value pair dictionary which contains all the previous jump values passed by the researcher.

3) The link "http://127.0.0.1:5000/api/fibonnaci/?id=4"  
	i) In the above API link where id value is 4 represents/denotes the "jump" value that will initialize the object 'n' steps ahead from the start of the series. \
	ii) If the jump value is 6 then URL will be "http://127.0.0.1:5000/api/fibonnaci/?id=6"  
	iii)Reseacher has to pass this value manually.


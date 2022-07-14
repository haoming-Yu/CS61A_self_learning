- ___Functions___

  1. use the python interpreter as a calculator

     ```python
     from math import pi
     pi
     from math import sin
     sin # the interpreter will echo <built-in function sin> -> the type of sin function
     sin(pi/2) # 1
     ```

  2. assignment -> binding the name on the values

     ```python
     radius = 10
     radius # interpreter will echo 10
     2 * radius # interpreter will echo 20
     area, circ = pi * radius * radius, 2 * pi * radius # circ -> circumference -> you can bind multiple values and names using one statement(not expression, no value)
     ```

     assignment -> names are bound to the values, not bound to the place where they came from, that is, the way they are caluculated (the expresssion).
     assignment can alse be used to give alias to functions

     ```python
     max(1, 2, 3) # echo 3
     f = max
     f # echo <built-in function max>, now f can be used as max
     # but max can still be aliased to be alias of something different, like a value's name
     max = 7
     f(1, 2, max) # echo 7
     # if this function can not be found by the name, you can import it again to do the binding
     ```

     operator function -> 

     ```python
     from operator import add, mul
     # a import statement can bind built-in function with a name
     ```

     bind names with values

     1. use assignment statement

     2. use import statement -> just for built-in functions

     3. use def statement -> create our own functions

        ```python
        def square(x):
            return mul(x, x)
        square # the interpreter will echo <function square at 0x....>
        # and then we can call the function by using name square
        ```

        and this square function can be called globally, and `square(w)`(w is a number) is an expression that have the value returned by the return statement in the definition of function.

        ```python
        def sum_square(x, y):
            return square(x) + square(y)
        ```

        define a name which you need it to be sync using a function. 

        ```python
        def area(): # no arguments
            return pi * radius * radius
        area() # now it is a function, which can be calculated when it is called -> thus, it is sync with the changing of arguments.
        ```

- ___Expressions___

  1. primitive expressions: number or numeral`2` | name`add` | string`'hello'`
  2. call expressions: operator(operands, operands, ...) [nested is OK]

- ___Environment Diagrams___

  1. environment diagrams visualize the interpreter's process

  2. in python, names can not be repeated. It has to be bound to at most one value.

  3. an implementation: `https://pythontutor.com`

  4. you can draw it yourself -> code on the left, and frame on the right, the frame gives the scope information and the names and the values they are bound to.

  5. execution rule for assignment statements

     ```python
     a = 1
     b = 2
     b, a = a + b, b
     ```

     ___rules :___

     1. evaluate all expressions to the right of = from left to right.
     2. bind all names to the left of = to the resulting values in the current frame.

  6. a name can be bound to at most one value in a frame. If it is bound multiple times, the original value will be covered.

  7. for nested expressions -> can draw a evaluation tree to evaluate the nested expressions. First evaluate the operator according to the diagrams(frame), and then evaluate the operands, recursively if nested or needed.

- ___Defining functions___

  1. assignment is a simple means of abstraction: binds names to values

  2. function definition is a more powerful means of abstraction: binds names to expressions -> evaluated every time the function is called.

     ```python
     # first line -> function signature: indicates how many arguments a function takes (has all the information needed to create a local frame.)
     def <name>(<formal parameters>):
         # function body -> defines the computational process expressed by a function
         return <return expression>
     ```

     execution procedure for def statements:

     1. create a function with signature `<name>(<formal parameters>)`
     2. set the body of that function to be everything indented after the first line. (does not execute those expressions while defining functions. They are executed when the function is called.)
     3. bind `<name>` to that function in the current frame.

     execution procedure for calling/applying user-defined functions(version 1)

     1. add a local frame, forming a new environment
     2. bind the function's formal parameters to its arguments in that frame
     3. execute the body of the function in that new environment.

- ___Looking up names in environments___
  every expression is evaluated in the context of an environment. so far, the current environment is either:

  1. the global frame alone
  2. a local frame, followed by the global frame. -> totally two frames in the environment.

  __Note :__ 

  1. an environment is a sequence of frames; (a frame is a binding between names and values)
  2. a name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found. -> e.g. first look for the name in the local frame, if not found, look for it in the global frame.

- ___Debugging Tech___

  Look for all the information in this website: 
  https://inst.eecs.berkeley.edu/~cs61a/su20/articles/debugging.html

- 
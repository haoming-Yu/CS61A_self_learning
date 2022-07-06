- ___Computer Science___

  1. what problems can be solved using computation
  2. how to solve those problems
  3. what techniques lead to effective solutions

- ___Problems___

  1. managing complexity -> mastering abstraction (使用抽象的方法降低问题思考的复杂度)
  2. programing paradigms(范例)
  3. not all about 0's and 1's

- ___Expressions___

  1. describes a computation & evaluates to a value
  2. generalization ->  使用函数泛化所有表达式
  3. expression tree -> evaluates the nested call expression by recursively solve the problem nested call expression.
  4. expression -> the most important thing is to evaluate the information and the sequence which is called.

- ___Demo___

  1. Functions, Objects

     ```python
     shakes = open('shakespeare.txt') # open a file
     text = shakes.read().split() # text is a list, read the files out by spliting the words(automatically done using white characters)
     text[:25] # the first 25 words
     len(text) # the length of text, the number of elements, list can have duplicated words
     text.count('the') # output the number of word 'the'
     text.count('thou') # the same as the above
     words = set(text) # create a set using the list text, the set just stores the duplicated words once, just stores the unique element
     ```

  2. interpreter

     ```python
     'draw' # an element stored by using the list
     'draw'[::-1] # output 'ward' -> reversing order
     {w for w in words if w == w[::-1] and len(w) > 4} # 找到words中所有长度大于四的回文串
     {w for w in words if w[::-1] in words and len(w) == 4} # 语句翻译即可
     ```

- ___Other things___

  1. primitive expressions -> 原始表达式 
     `Names are also primitive expressions. Names evaluate to the value that they are bound to in the current environment. One way to bind a name to a value is with an assignment statement.`
  2. arithmetic expressions -> 算数表达式
     Numbers may be combined with mathematical operators to form compound expressions. In addition to `+` operator (addition), the `-` operator (subtraction), the `*` operator (multiplication) and the `**` operator (exponentiation), there are three division-like operators to remember:
     - Floating point division (`/`): divides the first number number by the second, evaluating to a number with a decimal point *even if the numbers divide evenly*.
     - Floor division (`//`): divides the first number by the second and then rounds down, evaluating to an integer.
     - Modulo (`%`): evaluates to the positive remainder left over from division.
     - Parentheses may be used to group subexpressions together; the entire expression is evaluated in PEMDAS order.
       (PEMDAS stands for **P- Parentheses, E- Exponents, M- Multiplication, D- Division, A- Addition, and S- Subtraction**.)
  3. assignment statements -> 赋值语句，实际上是进行绑定操作
     An assignment statement consists of a name and an expression. It changes the state of the program by evaluating the expression and *binding* its value to the name in the current frame.
     __Note:__ Note that the statement itself doesn't evaluate to anything, because it's a statement and not an expression. 
     When we ask for some name's value, the interpreter will look it up in the current environment and output its value.
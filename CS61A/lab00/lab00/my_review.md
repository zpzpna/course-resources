- [x] test 1：enter the output of expressions and assignment statements

---

  **/**(floating point division) | **//**(round division) | **%**(modulo )

> python3 ok -q python-basics -u

​		enter the command above in the folder and start the test 1.

​		However,in git-bash .it says "bash: python3: command not found"

---

​		Intsead,entering the following in terminal is effective

>  py -3 ok -q python-basics -u

---

- [x] test2: replace the underscores to implement the function

​		use`py -3 ` to test the result

---

notes: docstring and doctests（unit test）

input  code as 	` py -3 -m doctest xxx.py` and the unit test will start 

doctest can be embedded in a function or written in a separate txt file.

- in function

```python
def xxx:
	"""
	xxxxxxxxxxxxxxxxxxx
	
	>>>
	return xxx
	"""
    return xxxx

```

- in txt file

```python
>>> from xxx.py import add
>>>add(1,2)
3
>>>add(4,5)
2
```

input following in bash

`py -3 -m doctest -v xxx.txt`
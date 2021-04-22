lines_default = [
    '# tests.mock\\_file\n\n',
    '\n\n## mock\\_function\n\n',
    '\n\n```py\nmock_function(param_a,\n              param_b=1)\n              -> int\n```\n\n',
    'A mock function for testing purposes\n',
    '\n\n#### Parameters\n\n',
    '\n\n**param_a** _str_: A *test* _param_.\n\n',
    '\n\n**param_b** _int_: Another *test* _param_.\n\n| col A |: col B |\n|=======|========|\n| boo   | baa    |\n\n',
    '\n\n## **class** MockClass\n\n',
    'A mock class for testing purposes.',
    '\n\n## MockClass\n\n',
    '\n\n```py\nMockClass(param_c=1.1,\n          param_d=0.9)\n```\n\n',
    'Mock class initialisation\n',
    '\n\n#### Parameters\n\n',
    '\n\n**param_c** _float_: Yet another test param.\n\n',
    '\n\n**param_d** _float_: And another.\n\n',
    '\n\n#### MockClass.param\\_e\n\n',
    'A property describing property param_e',
    '\n\n## MockClass.hello\n\n',
    '\n\n```py\nMockClass.hello()\n                -> str\n```\n\n',
    'A random class method returning "hello"\n',
    '\n\n#### Returns\n\n',
    '\n\n**saying_hello**: A string saying "hello"\n\n'
]

lines_custom = [
    '# tests.mock\\_file\n\n',
    '\n\n## mock\\_function\n\n',
    '\n\n<FuncSignature>\n<pre>\nmock_function(param_a,\n              param_b=1)\n              -> int\n</pre>\n</FuncSignature>\n\n',
    'A mock function for testing purposes\n',
    '\n\n<FuncHeading>Parameters</FuncHeading>\n\n',
    "\n\n<FuncElement name='param_a' type='str'>\n\nA *test* _param_.\n\n</FuncElement>\n\n",
    "\n\n<FuncElement name='param_b' type='int'>\n\nAnother *test* _param_.\n\n| col A |: col B |\n|=======|========|\n| boo   | baa    |\n\n</FuncElement>\n\n",
    '\n\n## **class** MockClass\n\n',
    'A mock class for testing purposes.',
    '\n\n## MockClass\n\n',
    '\n\n<FuncSignature>\n<pre>\nMockClass(param_c=1.1,\n          param_d=0.9)\n</pre>\n</FuncSignature>\n\n',
    'Mock class initialisation\n',
    '\n\n<FuncHeading>Parameters</FuncHeading>\n\n',
    "\n\n<FuncElement name='param_c' type='float'>\n\nYet another test param.\n\n</FuncElement>\n\n",
    "\n\n<FuncElement name='param_d' type='float'>\n\nAnd another.\n\n</FuncElement>\n\n",
    '\n\n#### MockClass.param\\_e\n\n',
    'A property describing property param_e',
    '\n\n## MockClass.hello\n\n',
    '\n\n<FuncSignature>\n<pre>\nMockClass.hello()\n                -> str\n</pre>\n</FuncSignature>\n\n',
    'A random class method returning "hello"\n',
    '\n\n<FuncHeading>Returns</FuncHeading>\n\n',
    '\n\n<FuncElement name=\'saying_hello\'>\n\nA string saying "hello"\n\n</FuncElement>\n\n'
]

md_file_default = '''# tests.mock\_file



## mock\_function



```py
mock_function(param_a,
              param_b=1)
              -> int
```

A mock function for testing purposes


#### Parameters



**param_a** _str_: A *test* _param_.



**param_b** _int_: Another *test* _param_.

| col A |: col B |
|=======|========|
| boo   | baa    |



## **class** MockClass

A mock class for testing purposes.

## MockClass



```py
MockClass(param_c=1.1,
          param_d=0.9)
```

Mock class initialisation


#### Parameters



**param_c** _float_: Yet another test param.



**param_d** _float_: And another.



#### MockClass.param\_e

A property describing property param_e

## MockClass.hello



```py
MockClass.hello()
                -> str
```

A random class method returning "hello"


#### Returns



**saying_hello**: A string saying "hello"

'''

md_file_custom = '''# tests.mock\_file



## mock\_function



<FuncSignature>
<pre>
mock_function(param_a,
              param_b=1)
              -> int
</pre>
</FuncSignature>

A mock function for testing purposes


<FuncHeading>Parameters</FuncHeading>



<FuncElement name='param_a' type='str'>

A *test* _param_.

</FuncElement>



<FuncElement name='param_b' type='int'>

Another *test* _param_.

| col A |: col B |
|=======|========|
| boo   | baa    |

</FuncElement>



## **class** MockClass

A mock class for testing purposes.

## MockClass



<FuncSignature>
<pre>
MockClass(param_c=1.1,
          param_d=0.9)
</pre>
</FuncSignature>

Mock class initialisation


<FuncHeading>Parameters</FuncHeading>



<FuncElement name='param_c' type='float'>

Yet another test param.

</FuncElement>



<FuncElement name='param_d' type='float'>

And another.

</FuncElement>



#### MockClass.param\_e

A property describing property param_e

## MockClass.hello



<FuncSignature>
<pre>
MockClass.hello()
                -> str
</pre>
</FuncSignature>

A random class method returning "hello"


<FuncHeading>Returns</FuncHeading>



<FuncElement name='saying_hello'>

A string saying "hello"

</FuncElement>

'''
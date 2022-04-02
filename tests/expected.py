lines_default = '''
<div class="yap module">
  <h1 class="yap module-title" id="tests-mock-file">tests.mock_file</h1>
  <div class="yap doc-str">module docstring content more content</div>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">mock_function</h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig-title">
        <div class="yap func-sig-start">mock_function(</div>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a, </div>
          <div class="yap func-sig-param">param_b=2</div>
        </div>
        <div class="yap func-sig-end">)</div>
      </div>
    </div>
    <div class="yap doc-str-content">A mock function returning a sum of param_a and param_b if positive numbers, else None
      <h3 class="yap doc-str-heading">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
A *test* _param_.
</Markdown></div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_b</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
Another *test* _param_.

| col A |: col B |
|-------|--------|
| boo   | baa    |
</Markdown></div>
      </div>
      <h3 class="yap doc-str-heading">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">summed_number</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
The sum of _param_a_ and _param_b_.
</Markdown></div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">None</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
None returned if values are negative.
</Markdown></div>
      </div>
      <h3 class="yap doc-str-heading">Raises</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">ValueError</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
Raises value error if params are not numbers.
</Markdown></div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap doc-str-heading">Notes</h3><Markdown>
```python
print(mock_function(1, 2))
# prints 3
```

Random text

_Random table_

| col A |: col B |
|-------|--------|
| boo   | baa    |
</Markdown>
      </div>
    </div>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="parentclass">ParentClass</h2><Markdown>
A parent class
</Markdown>
    <div class="yap class-prop-def">
      <div class="yap class-prop-def-name">parent_prop</div>
      <div class="yap class-prop-def-type">str</div>
    </div>
    <section class="yap func">
      <h2 class="yap func-title" id="parentclass">ParentClass</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ParentClass(</div>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">Parent initialisation.
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Keyword args.
</Markdown></div>
        </div>
      </div>
    </section>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="childclass">ChildClass</h2><Markdown>
A child class
</Markdown>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass">ChildClass</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ChildClass(</div>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">param_c=1.1, </div>
            <div class="yap func-sig-param">param_d=0.9, </div>
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">Child initialisation.
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_c</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Yet another test param.
</Markdown></div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_d</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
And another.
</Markdown></div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Keyword args.
</Markdown></div>
        </div>
      </div>
    </section>
    <div class="yap class-prop">
      <div class="yap class-prop-name">param_e</div>
      <div class="yap class-prop-type"></div>
    </div>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass-hello">ChildClass.hello</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ChildClass.hello(</div>
          <div class="yap func-sig-params"></div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">A random class method returning &quot;hello&quot;
        <h3 class="yap doc-str-heading">Returns</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">str</div>
            <div class="yap doc-str-elem-type">saying_hello</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
A string saying "hello"
</Markdown></div>
        </div>
      </div>
    </section>
  </section>
</div>
'''

lines_custom = '''
---
import { Markdown } from 'astro/components';
import PageLayout from '../layouts/PageLayout.astro'
---

<PageLayout>
<div class="yap module">
  <h1 class="yap module-title" id="tests-mock-file">tests.mock_file</h1>
  <div class="yap doc-str">module docstring content more content</div>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">mock_function</h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig-title">
        <div class="yap func-sig-start">mock_function(</div>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a, </div>
          <div class="yap func-sig-param">param_b=2</div>
        </div>
        <div class="yap func-sig-end">)</div>
      </div>
    </div>
    <div class="yap doc-str-content">A mock function returning a sum of param_a and param_b if positive numbers, else None
      <h3 class="yap doc-str-heading">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
A *test* _param_.
</Markdown></div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_b</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
Another *test* _param_.

| col A |: col B |
|-------|--------|
| boo   | baa    |
</Markdown></div>
      </div>
      <h3 class="yap doc-str-heading">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">summed_number</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
The sum of _param_a_ and _param_b_.
</Markdown></div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">None</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
None returned if values are negative.
</Markdown></div>
      </div>
      <h3 class="yap doc-str-heading">Raises</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">ValueError</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
Raises value error if params are not numbers.
</Markdown></div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap doc-str-heading">Notes</h3><Markdown>
```python
print(mock_function(1, 2))
# prints 3
```

Random text

_Random table_

| col A |: col B |
|-------|--------|
| boo   | baa    |
</Markdown>
      </div>
    </div>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="parentclass">ParentClass</h2><Markdown>
A parent class
</Markdown>
    <div class="yap class-prop-def">
      <div class="yap class-prop-def-name">parent_prop</div>
      <div class="yap class-prop-def-type">str</div>
    </div>
    <section class="yap func">
      <h2 class="yap func-title" id="parentclass">ParentClass</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ParentClass(</div>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">Parent initialisation.
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Keyword args.
</Markdown></div>
        </div>
      </div>
    </section>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="childclass">ChildClass</h2><Markdown>
A child class
</Markdown>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass">ChildClass</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ChildClass(</div>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">param_c=1.1, </div>
            <div class="yap func-sig-param">param_d=0.9, </div>
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">Child initialisation.
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_c</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Yet another test param.
</Markdown></div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_d</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
And another.
</Markdown></div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Keyword args.
</Markdown></div>
        </div>
      </div>
    </section>
    <div class="yap class-prop">
      <div class="yap class-prop-name">param_e</div>
      <div class="yap class-prop-type"></div>
    </div>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass-hello">ChildClass.hello</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ChildClass.hello(</div>
          <div class="yap func-sig-params"></div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">A random class method returning &quot;hello&quot;
        <h3 class="yap doc-str-heading">Returns</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">str</div>
            <div class="yap doc-str-elem-type">saying_hello</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
A string saying "hello"
</Markdown></div>
        </div>
      </div>
    </section>
  </section>
</div>
</PageLayout>
'''

astro_file_default = '''
<div class="yap module">
  <h1 class="yap module-title" id="test-mock-file">test.mock_file</h1>
  <div class="yap doc-str">module docstring content more content</div>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">mock_function</h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig-title">
        <div class="yap func-sig-start">mock_function(</div>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a, </div>
          <div class="yap func-sig-param">param_b=2</div>
        </div>
        <div class="yap func-sig-end">)</div>
      </div>
    </div>
    <div class="yap doc-str-content">A mock function returning a sum of param_a and param_b if positive numbers, else None
      <h3 class="yap doc-str-heading">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
A *test* _param_.
</Markdown></div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_b</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
Another *test* _param_.

| col A |: col B |
|-------|--------|
| boo   | baa    |
</Markdown></div>
      </div>
      <h3 class="yap doc-str-heading">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">summed_number</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
The sum of _param_a_ and _param_b_.
</Markdown></div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">None</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
None returned if values are negative.
</Markdown></div>
      </div>
      <h3 class="yap doc-str-heading">Raises</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">ValueError</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
Raises value error if params are not numbers.
</Markdown></div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap doc-str-heading">Notes</h3><Markdown>
```python
print(mock_function(1, 2))
# prints 3
```

Random text

_Random table_

| col A |: col B |
|-------|--------|
| boo   | baa    |
</Markdown>
      </div>
    </div>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="parentclass">ParentClass</h2><Markdown>
A parent class
</Markdown>
    <div class="yap class-prop-def">
      <div class="yap class-prop-def-name">parent_prop</div>
      <div class="yap class-prop-def-type">str</div>
    </div>
    <section class="yap func">
      <h2 class="yap func-title" id="parentclass">ParentClass</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ParentClass(</div>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">Parent initialisation.
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Keyword args.
</Markdown></div>
        </div>
      </div>
    </section>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="childclass">ChildClass</h2><Markdown>
A child class
</Markdown>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass">ChildClass</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ChildClass(</div>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">param_c=1.1, </div>
            <div class="yap func-sig-param">param_d=0.9, </div>
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">Child initialisation.
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_c</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Yet another test param.
</Markdown></div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_d</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
And another.
</Markdown></div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Keyword args.
</Markdown></div>
        </div>
      </div>
    </section>
    <div class="yap class-prop">
      <div class="yap class-prop-name">param_e</div>
      <div class="yap class-prop-type"></div>
    </div>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass-hello">ChildClass.hello</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ChildClass.hello(</div>
          <div class="yap func-sig-params"></div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">A random class method returning &quot;hello&quot;
        <h3 class="yap doc-str-heading">Returns</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">str</div>
            <div class="yap doc-str-elem-type">saying_hello</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
A string saying "hello"
</Markdown></div>
        </div>
      </div>
    </section>
  </section>
</div>
'''

astro_file_custom = '''
---
import { Markdown } from 'astro/components';
import PageLayout from '../layouts/PageLayout.astro'
---

<PageLayout>
<div class="yap module">
  <h1 class="yap module-title" id="test-mock-file">test.mock_file</h1>
  <div class="yap doc-str">module docstring content more content</div>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">mock_function</h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig-title">
        <div class="yap func-sig-start">mock_function(</div>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a, </div>
          <div class="yap func-sig-param">param_b=2</div>
        </div>
        <div class="yap func-sig-end">)</div>
      </div>
    </div>
    <div class="yap doc-str-content">A mock function returning a sum of param_a and param_b if positive numbers, else None
      <h3 class="yap doc-str-heading">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
A *test* _param_.
</Markdown></div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_b</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
Another *test* _param_.

| col A |: col B |
|-------|--------|
| boo   | baa    |
</Markdown></div>
      </div>
      <h3 class="yap doc-str-heading">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">summed_number</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
The sum of _param_a_ and _param_b_.
</Markdown></div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">None</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
None returned if values are negative.
</Markdown></div>
      </div>
      <h3 class="yap doc-str-heading">Raises</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">ValueError</div>
        </div>
        <div class="yap doc-str-elem-desc"><Markdown>
Raises value error if params are not numbers.
</Markdown></div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap doc-str-heading">Notes</h3><Markdown>
```python
print(mock_function(1, 2))
# prints 3
```

Random text

_Random table_

| col A |: col B |
|-------|--------|
| boo   | baa    |
</Markdown>
      </div>
    </div>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="parentclass">ParentClass</h2><Markdown>
A parent class
</Markdown>
    <div class="yap class-prop-def">
      <div class="yap class-prop-def-name">parent_prop</div>
      <div class="yap class-prop-def-type">str</div>
    </div>
    <section class="yap func">
      <h2 class="yap func-title" id="parentclass">ParentClass</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ParentClass(</div>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">Parent initialisation.
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Keyword args.
</Markdown></div>
        </div>
      </div>
    </section>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="childclass">ChildClass</h2><Markdown>
A child class
</Markdown>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass">ChildClass</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ChildClass(</div>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">param_c=1.1, </div>
            <div class="yap func-sig-param">param_d=0.9, </div>
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">Child initialisation.
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_c</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Yet another test param.
</Markdown></div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_d</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
And another.
</Markdown></div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
Keyword args.
</Markdown></div>
        </div>
      </div>
    </section>
    <div class="yap class-prop">
      <div class="yap class-prop-name">param_e</div>
      <div class="yap class-prop-type"></div>
    </div>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass-hello">ChildClass.hello</h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig-title">
          <div class="yap func-sig-start">ChildClass.hello(</div>
          <div class="yap func-sig-params"></div>
          <div class="yap func-sig-end">)</div>
        </div>
      </div>
      <div class="yap doc-str-content">A random class method returning &quot;hello&quot;
        <h3 class="yap doc-str-heading">Returns</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">str</div>
            <div class="yap doc-str-elem-type">saying_hello</div>
          </div>
          <div class="yap doc-str-elem-desc"><Markdown>
A string saying "hello"
</Markdown></div>
        </div>
      </div>
    </section>
  </section>
</div>
</PageLayout>
'''
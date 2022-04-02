lines_default = '''
<div class="yap module">
  <h1 class="yap module-title" id="tests-mock-file">
    <a aria-hidden="true" href="#tests-mock-file" tab_index="-1">
      <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
      </svg>
    </a>tests.mock_file
  </h1>
  <div class="yap doc-str-content">module docstring content more content</div>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">
      <a aria-hidden="true" href="#mock-function" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>mock_function
    </h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig">
        <span>mock_function(</span>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a, </div>
          <div class="yap func-sig-param">param_b=2</div>
        </div>
        <span>)</span>
      </div>
    </div>
    <div class="yap doc-str-content">
      <Markdown class="doc-str-content">A mock function returning a sum of param_a and param_b if positive numbers, else None</Markdown>
      <h3 class="yap doc-str-heading">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">A *test* _param_.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_b</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">Another *test* _param_.

| col A |: col B |
|-------|--------|
| boo   | baa    |</Markdown>
        </div>
      </div>
      <h3 class="yap doc-str-heading">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">summed_number</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">The sum of _param_a_ and _param_b_.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">None</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">None returned if values are negative.</Markdown>
        </div>
      </div>
      <h3 class="yap doc-str-heading">Raises</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">ValueError</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">Raises value error if params are not numbers.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap doc-str-heading">Notes</h3>
        <Markdown class="doc-str-content">```python
print(mock_function(1, 2))
# prints 3
```

Random text

_Random table_

| col A |: col B |
|-------|--------|
| boo   | baa    |</Markdown>
      </div>
    </div>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="parentclass">
      <a aria-hidden="true" href="#parentclass" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>ParentClass
    </h2>
    <Markdown class="doc-str-content">A parent class</Markdown>
    <h3 class="yap doc-str-heading">Properties</h3>
    <div class="yap class-prop-elem-container">
      <div class="yap class-prop-def">
        <div class="yap class-prop-def-name">parent_prop</div>
        <div class="yap class-prop-def-type">str</div>
      </div>
      <div class="yap class-prop-def-desc"></div>
    </div>
    <h3 class="yap doc-str-heading">Methods</h3>
    <section class="yap func">
      <h2 class="yap func-title" id="parentclass">
        <a aria-hidden="true" href="#parentclass" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ParentClass
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ParentClass(</span>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">Parent initialisation.</Markdown>
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Keyword args.</Markdown>
          </div>
        </div>
      </div>
    </section>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="childclass">
      <a aria-hidden="true" href="#childclass" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>ChildClass
    </h2>
    <p class="doc-str-content">Inherits from
      <a class="yap class-base" href="#parentclass">ParentClass</a>.
    </p>
    <Markdown class="doc-str-content">A child class</Markdown>
    <h3 class="yap doc-str-heading">Properties</h3>
    <div class="yap class-prop-elem-container">
      <div class="yap class-prop-def">
        <div class="yap class-prop-def-name">param_e</div>
        <div class="yap class-prop-def-type"></div>
      </div>
      <div class="yap class-prop-def-desc"></div>
    </div>
    <h3 class="yap doc-str-heading">Methods</h3>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass">
        <a aria-hidden="true" href="#childclass" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ChildClass
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ChildClass(</span>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">param_c=1.1, </div>
            <div class="yap func-sig-param">param_d=0.9, </div>
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">Child initialisation.</Markdown>
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_c</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Yet another test param.</Markdown>
          </div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_d</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">And another.</Markdown>
          </div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Keyword args.</Markdown>
          </div>
        </div>
      </div>
    </section>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass-hello">
        <a aria-hidden="true" href="#childclass-hello" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ChildClass.hello
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ChildClass.hello(</span>
          <div class="yap func-sig-params"></div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">A random class method returning &quot;hello&quot;</Markdown>
        <h3 class="yap doc-str-heading">Returns</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">str</div>
            <div class="yap doc-str-elem-type">saying_hello</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">A string saying &quot;hello&quot;</Markdown>
          </div>
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
  <h1 class="yap module-title" id="tests-mock-file">
    <a aria-hidden="true" href="#tests-mock-file" tab_index="-1">
      <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
      </svg>
    </a>tests.mock_file
  </h1>
  <div class="yap doc-str-content">module docstring content more content</div>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">
      <a aria-hidden="true" href="#mock-function" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>mock_function
    </h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig">
        <span>mock_function(</span>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a, </div>
          <div class="yap func-sig-param">param_b=2</div>
        </div>
        <span>)</span>
      </div>
    </div>
    <div class="yap doc-str-content">
      <Markdown class="doc-str-content">A mock function returning a sum of param_a and param_b if positive numbers, else None</Markdown>
      <h3 class="yap doc-str-heading">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">A *test* _param_.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_b</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">Another *test* _param_.

| col A |: col B |
|-------|--------|
| boo   | baa    |</Markdown>
        </div>
      </div>
      <h3 class="yap doc-str-heading">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">summed_number</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">The sum of _param_a_ and _param_b_.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">None</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">None returned if values are negative.</Markdown>
        </div>
      </div>
      <h3 class="yap doc-str-heading">Raises</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">ValueError</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">Raises value error if params are not numbers.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap doc-str-heading">Notes</h3>
        <Markdown class="doc-str-content">```python
print(mock_function(1, 2))
# prints 3
```

Random text

_Random table_

| col A |: col B |
|-------|--------|
| boo   | baa    |</Markdown>
      </div>
    </div>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="parentclass">
      <a aria-hidden="true" href="#parentclass" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>ParentClass
    </h2>
    <Markdown class="doc-str-content">A parent class</Markdown>
    <h3 class="yap doc-str-heading">Properties</h3>
    <div class="yap class-prop-elem-container">
      <div class="yap class-prop-def">
        <div class="yap class-prop-def-name">parent_prop</div>
        <div class="yap class-prop-def-type">str</div>
      </div>
      <div class="yap class-prop-def-desc"></div>
    </div>
    <h3 class="yap doc-str-heading">Methods</h3>
    <section class="yap func">
      <h2 class="yap func-title" id="parentclass">
        <a aria-hidden="true" href="#parentclass" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ParentClass
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ParentClass(</span>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">Parent initialisation.</Markdown>
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Keyword args.</Markdown>
          </div>
        </div>
      </div>
    </section>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="childclass">
      <a aria-hidden="true" href="#childclass" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>ChildClass
    </h2>
    <p class="doc-str-content">Inherits from
      <a class="yap class-base" href="#parentclass">ParentClass</a>.
    </p>
    <Markdown class="doc-str-content">A child class</Markdown>
    <h3 class="yap doc-str-heading">Properties</h3>
    <div class="yap class-prop-elem-container">
      <div class="yap class-prop-def">
        <div class="yap class-prop-def-name">param_e</div>
        <div class="yap class-prop-def-type"></div>
      </div>
      <div class="yap class-prop-def-desc"></div>
    </div>
    <h3 class="yap doc-str-heading">Methods</h3>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass">
        <a aria-hidden="true" href="#childclass" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ChildClass
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ChildClass(</span>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">param_c=1.1, </div>
            <div class="yap func-sig-param">param_d=0.9, </div>
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">Child initialisation.</Markdown>
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_c</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Yet another test param.</Markdown>
          </div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_d</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">And another.</Markdown>
          </div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Keyword args.</Markdown>
          </div>
        </div>
      </div>
    </section>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass-hello">
        <a aria-hidden="true" href="#childclass-hello" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ChildClass.hello
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ChildClass.hello(</span>
          <div class="yap func-sig-params"></div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">A random class method returning &quot;hello&quot;</Markdown>
        <h3 class="yap doc-str-heading">Returns</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">str</div>
            <div class="yap doc-str-elem-type">saying_hello</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">A string saying &quot;hello&quot;</Markdown>
          </div>
        </div>
      </div>
    </section>
  </section>
</div>
</PageLayout>
'''

astro_file_default = '''
<div class="yap module">
  <h1 class="yap module-title" id="test-mock-file">
    <a aria-hidden="true" href="#test-mock-file" tab_index="-1">
      <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
      </svg>
    </a>test.mock_file
  </h1>
  <div class="yap doc-str-content">module docstring content more content</div>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">
      <a aria-hidden="true" href="#mock-function" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>mock_function
    </h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig">
        <span>mock_function(</span>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a, </div>
          <div class="yap func-sig-param">param_b=2</div>
        </div>
        <span>)</span>
      </div>
    </div>
    <div class="yap doc-str-content">
      <Markdown class="doc-str-content">A mock function returning a sum of param_a and param_b if positive numbers, else None</Markdown>
      <h3 class="yap doc-str-heading">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">A *test* _param_.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_b</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">Another *test* _param_.

| col A |: col B |
|-------|--------|
| boo   | baa    |</Markdown>
        </div>
      </div>
      <h3 class="yap doc-str-heading">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">summed_number</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">The sum of _param_a_ and _param_b_.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">None</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">None returned if values are negative.</Markdown>
        </div>
      </div>
      <h3 class="yap doc-str-heading">Raises</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">ValueError</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">Raises value error if params are not numbers.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap doc-str-heading">Notes</h3>
        <Markdown class="doc-str-content">```python
print(mock_function(1, 2))
# prints 3
```

Random text

_Random table_

| col A |: col B |
|-------|--------|
| boo   | baa    |</Markdown>
      </div>
    </div>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="parentclass">
      <a aria-hidden="true" href="#parentclass" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>ParentClass
    </h2>
    <Markdown class="doc-str-content">A parent class</Markdown>
    <h3 class="yap doc-str-heading">Properties</h3>
    <div class="yap class-prop-elem-container">
      <div class="yap class-prop-def">
        <div class="yap class-prop-def-name">parent_prop</div>
        <div class="yap class-prop-def-type">str</div>
      </div>
      <div class="yap class-prop-def-desc"></div>
    </div>
    <h3 class="yap doc-str-heading">Methods</h3>
    <section class="yap func">
      <h2 class="yap func-title" id="parentclass">
        <a aria-hidden="true" href="#parentclass" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ParentClass
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ParentClass(</span>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">Parent initialisation.</Markdown>
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Keyword args.</Markdown>
          </div>
        </div>
      </div>
    </section>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="childclass">
      <a aria-hidden="true" href="#childclass" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>ChildClass
    </h2>
    <p class="doc-str-content">Inherits from
      <a class="yap class-base" href="#parentclass">ParentClass</a>.
    </p>
    <Markdown class="doc-str-content">A child class</Markdown>
    <h3 class="yap doc-str-heading">Properties</h3>
    <div class="yap class-prop-elem-container">
      <div class="yap class-prop-def">
        <div class="yap class-prop-def-name">param_e</div>
        <div class="yap class-prop-def-type"></div>
      </div>
      <div class="yap class-prop-def-desc"></div>
    </div>
    <h3 class="yap doc-str-heading">Methods</h3>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass">
        <a aria-hidden="true" href="#childclass" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ChildClass
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ChildClass(</span>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">param_c=1.1, </div>
            <div class="yap func-sig-param">param_d=0.9, </div>
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">Child initialisation.</Markdown>
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_c</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Yet another test param.</Markdown>
          </div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_d</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">And another.</Markdown>
          </div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Keyword args.</Markdown>
          </div>
        </div>
      </div>
    </section>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass-hello">
        <a aria-hidden="true" href="#childclass-hello" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ChildClass.hello
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ChildClass.hello(</span>
          <div class="yap func-sig-params"></div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">A random class method returning &quot;hello&quot;</Markdown>
        <h3 class="yap doc-str-heading">Returns</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">str</div>
            <div class="yap doc-str-elem-type">saying_hello</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">A string saying &quot;hello&quot;</Markdown>
          </div>
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
  <h1 class="yap module-title" id="test-mock-file">
    <a aria-hidden="true" href="#test-mock-file" tab_index="-1">
      <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
      </svg>
    </a>test.mock_file
  </h1>
  <div class="yap doc-str-content">module docstring content more content</div>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">
      <a aria-hidden="true" href="#mock-function" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>mock_function
    </h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig">
        <span>mock_function(</span>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a, </div>
          <div class="yap func-sig-param">param_b=2</div>
        </div>
        <span>)</span>
      </div>
    </div>
    <div class="yap doc-str-content">
      <Markdown class="doc-str-content">A mock function returning a sum of param_a and param_b if positive numbers, else None</Markdown>
      <h3 class="yap doc-str-heading">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">A *test* _param_.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_b</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">Another *test* _param_.

| col A |: col B |
|-------|--------|
| boo   | baa    |</Markdown>
        </div>
      </div>
      <h3 class="yap doc-str-heading">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">summed_number</div>
          <div class="yap doc-str-elem-type">int | float</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">The sum of _param_a_ and _param_b_.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">None</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">None returned if values are negative.</Markdown>
        </div>
      </div>
      <h3 class="yap doc-str-heading">Raises</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name"></div>
          <div class="yap doc-str-elem-type">ValueError</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown class="doc-str-content">Raises value error if params are not numbers.</Markdown>
        </div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap doc-str-heading">Notes</h3>
        <Markdown class="doc-str-content">```python
print(mock_function(1, 2))
# prints 3
```

Random text

_Random table_

| col A |: col B |
|-------|--------|
| boo   | baa    |</Markdown>
      </div>
    </div>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="parentclass">
      <a aria-hidden="true" href="#parentclass" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>ParentClass
    </h2>
    <Markdown class="doc-str-content">A parent class</Markdown>
    <h3 class="yap doc-str-heading">Properties</h3>
    <div class="yap class-prop-elem-container">
      <div class="yap class-prop-def">
        <div class="yap class-prop-def-name">parent_prop</div>
        <div class="yap class-prop-def-type">str</div>
      </div>
      <div class="yap class-prop-def-desc"></div>
    </div>
    <h3 class="yap doc-str-heading">Methods</h3>
    <section class="yap func">
      <h2 class="yap func-title" id="parentclass">
        <a aria-hidden="true" href="#parentclass" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ParentClass
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ParentClass(</span>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">Parent initialisation.</Markdown>
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Keyword args.</Markdown>
          </div>
        </div>
      </div>
    </section>
  </section>
  <section class="yap class">
    <h2 class="yap class-title" id="childclass">
      <a aria-hidden="true" href="#childclass" tab_index="-1">
        <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
        </svg>
      </a>ChildClass
    </h2>
    <p class="doc-str-content">Inherits from
      <a class="yap class-base" href="#parentclass">ParentClass</a>.
    </p>
    <Markdown class="doc-str-content">A child class</Markdown>
    <h3 class="yap doc-str-heading">Properties</h3>
    <div class="yap class-prop-elem-container">
      <div class="yap class-prop-def">
        <div class="yap class-prop-def-name">param_e</div>
        <div class="yap class-prop-def-type"></div>
      </div>
      <div class="yap class-prop-def-desc"></div>
    </div>
    <h3 class="yap doc-str-heading">Methods</h3>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass">
        <a aria-hidden="true" href="#childclass" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ChildClass
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ChildClass(</span>
          <div class="yap func-sig-params">
            <div class="yap func-sig-param">param_c=1.1, </div>
            <div class="yap func-sig-param">param_d=0.9, </div>
            <div class="yap func-sig-param">**kwargs</div>
          </div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">Child initialisation.</Markdown>
        <h3 class="yap doc-str-heading">Parameters</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_c</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Yet another test param.</Markdown>
          </div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">param_d</div>
            <div class="yap doc-str-elem-type">float</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">And another.</Markdown>
          </div>
        </div>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">**kwargs</div>
            <div class="yap doc-str-elem-type"></div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">Keyword args.</Markdown>
          </div>
        </div>
      </div>
    </section>
    <section class="yap func">
      <h2 class="yap func-title" id="childclass-hello">
        <a aria-hidden="true" href="#childclass-hello" tab_index="-1">
          <svg ariaHidden="true" class="heading-icon" height="15px" viewbox="0 0 20 20" width="15px" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
" fill-rule="evenodd"></path>
          </svg>
        </a>ChildClass.hello
      </h2>
      <div class="yap func-sig-content">
        <div class="yap func-sig">
          <span>ChildClass.hello(</span>
          <div class="yap func-sig-params"></div>
          <span>)</span>
        </div>
      </div>
      <div class="yap doc-str-content">
        <Markdown class="doc-str-content">A random class method returning &quot;hello&quot;</Markdown>
        <h3 class="yap doc-str-heading">Returns</h3>
        <div class="yap doc-str-elem-container">
          <div class="yap doc-str-elem-def">
            <div class="yap doc-str-elem-name">str</div>
            <div class="yap doc-str-elem-type">saying_hello</div>
          </div>
          <div class="yap doc-str-elem-desc">
            <Markdown class="doc-str-content">A string saying &quot;hello&quot;</Markdown>
          </div>
        </div>
      </div>
    </section>
  </section>
</div>
</PageLayout>
'''
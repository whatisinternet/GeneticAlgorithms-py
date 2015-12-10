# GeneticAlgorithms-py

### Usage

All example functions are implemented as lambda functions that are passed into the genetic algorithm function. To see an example see `example.py`. To define your own:

```python
  def dejong(maximize):
      print 'Blackbox: deJongSphere function'
      black_box = (lambda x, y: (reduce(
          (lambda r, q: q + (int(x, 2) ** 2)), range(int(y, 2)), 0)))
      target_fitness = None
      variables = 2
      carry_over = 64
      params = {
          'objective_function': black_box,
          'iterations': 500,
          'mutation_probability': 0.01,
          "crossover_rate": 0.7,
          "constraint_range": range(5),
          "number_of_variables": variables,
          "carry_over": carry_over,
          "pool_size": 500,
          "target": target_fitness,
          "max": maximize,
          "function_name": "deJong Sphere maximized: {a}".format(a=maximize)
          }
      genetic_algorithms_py.__init__(params)
````

### Install Python

[Instructions here](https://www.python.org/)


### Install PIP (the python package manager):

[Instructions here](https://pip.pypa.io/en/stable/installing/)

### Install dependencies

```shell
    pip install -r requirements.txt
```

**Errors?**
- If MatPlotLib fails on Linux install the following:
  `freetype-devel, libpng-devel` and run pip again. If you still have errors you
can install from [here](http://matplotlib.org/users/installing.html).

### Running:

```shell
    echo False > debug
    python example.py
```

### Redirecting output
```shell
    echo False > debug
    python example.py > test.txt
```

### Testing:

*Set debug to false by modifying the debug file in the root directory contain
any string other than True*

### Install nose (requires PIP)

```shell
    [sudo] pip install nose
```
### Running the tests:

```shell
    echo False > debug
    nosetests
```

with coverage information

```shell
    echo False > debug
    nosetests --with-coverage --cover-html
```

### Automatic testing during development

Install Ruby 2.2.3, bundler, guard, and guard shell

- [Ruby instructions](https://www.ruby-lang.org/en/)

- To install bundler
```shell
    gem install bundler
```

- To install guard and guard shell
```shell
    bundle install
```

- Running guard
```
    echo False > debug
    guard
```
### Charting / Debugging:

*Set debug to True by modifying the debug file in the root directory contain
the string True*

Charts will be generated, and charts will be displayed. Pressing enter is
required to continue each objective function.

```shell
    echo True > debug
    python example.py
    echo False > debug
```

### Style:
  - See: [PEP 0008](https://www.python.org/dev/peps/pep-0008/)
  - See also: [Thoughbot Guides](https://github.com/thoughtbot/guides)

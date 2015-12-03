# GeneticAlgorithms-py

# Style:
  - See: [PEP 0008](https://www.python.org/dev/peps/pep-0008/)
  - See also: [Thoughbot Guides](https://github.com/thoughtbot/guides)

# Install Python

[Instructions here](https://www.python.org/)


# Install PIP (the python package manager):

[Instructions here](https://pip.pypa.io/en/stable/installing/)

## Install dependencies

```shell
    pip install -r requirements.txt
```

**Errors?**
- If MatPlotLib fails on Linux install the following:
  `freetype-devel, libpng-devel` and run pip again. If you still have errors you
can install from [here](http://matplotlib.org/users/installing.html).

# Running:

```shell
    python example.py
```
# Redirecting output
```shell
    python example.py > test.txt
```

# Testing:

*Set debug to false by modifying the debug file in the root directory contain
any string other than True*

### Install nose (requires PIP)

```shell
    [sudo] pip install nose
```
### Running the tests:

```shell
   nosetests
```

with coverage information

```shell
    nosetests --with-coverage --cover-html
```

## Automatic testing during development

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
    guard
```
# Charting / Debugging:

*Set debug to True by modifying the debug file in the root directory contain
the string True*

Charts will be generated, and charts will be displayed. Pressing enter is
required to continue each objective function.

```shell
    python example.py
```

## Notes:

All example functions are implemented as lambda functions that are passed into the genetic algorithm function. To see an example see `example.py`. To define your own:

```python
    def x_2():
        print '-------------------------'
        print 'Blackbox: x^2'
        black_box = (lambda x: int(x, 2) ** 2)
        genetic_algorithms_py.__init__(black_box, iterations, bit_size)
````


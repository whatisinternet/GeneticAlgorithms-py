from setuptools import setup

setup(name='genetic_algorithms_py',
        version='0.0.1',
        description='Implements the a simple genetic algorithm',
        url='http://github.com/whatisinternet/GeneticAlgorithms-py',
        author='Josh Teeter, Steven Gao, Irfan Lakha, Scott Smith',
        author_email='joshteeter@gmail.com',
        license='MIT',
        packages=['genetic_algorithms_py'],
        test_suite='nose.collector',
        tests_require=['nose'],
        zip_safe=False)

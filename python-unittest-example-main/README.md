# python-unittest-example

This is a simple, self-contained example demonstrating how to use Python's [unittest module](https://docs.python.org/3/library/unittest.html#).

The source files are in the `mypackage` folder. Files that begin with `test_` contain test cases. Files that do not begin with `test_` are 'normal' code files, they are what we want to test.

Generally, you want to keep your test cases in a distinct file from your 'real' code. This way, your 'real code' cannot mix with or get impacted by test code.


## Running unit tests

### Running all tests

Use the following command:

```sh
$ python3 -m unittest discover
```

Or, less verbosely:

```sh
$ python3 -m unittest
```

These two commands are equivalent. They will find all test cases in the project and execute them.

Please note that your test cases need to be inside of a directory with a `__init__.py` file. In other words, if you put your test cases inside of `test/database_tests.py`, then you need to make sure that `test/__init__.py` also exists.

There are other options available which allow you to run specific test cases.

### Running specific tests

You can provide the fully qualified name for a specific module, class, or function.

This will run all tests in `mypackage.test_examples`:

```sh
$ python3 -m unittest mypackage.test_examples
```

This will run all tests defined in the class `mypackage.test_examples.TestExamples`:

```sh
$ python3 -m unittest mypackage.test_examples.TestExamples
```

This will run the specific `test_add` test in the `TestExamples` class:

```sh
$ python3 -m unittest mypackage.test_examples.TestExamples.test_add
```


## Using unittest.main

At the bottom of your `test_xyx.py` file, include the following code:

```python
if __name__ == "__main__":
    unittest.main()
```

Then, invoke `test_xyz.py` as though it were any other executable Python script.

This is effectively redundant if you are using the `discover` functionality described above. So, including this in the test file is optional.


## About makefiles

Some projects may include a `makefile` which will run the relevant test commands on your behalf. This can save some typing if you run unit tests frequently.

If a `makefile` is present and has a `test` recipe, run the following command:

```sh
$ make test
```


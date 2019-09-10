# Development notes


## Testing

```
python -m pytest -v -s
```


## Create and upload version to PiPy

From the command prompt, navigate to `src/python`. Then you can create and upload a new release with the following commands:

```
python setup.py sdist --formats=zip
python -m pip install --user --upgrade twine
python -m twine upload dist/
```
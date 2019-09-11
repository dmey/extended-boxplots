# Development notes


## Testing

```
python -m pytest -v -s
```


## Create and upload version to PyPI

From the command prompt, create and upload a new release with the following commands:

```
python setup.py sdist --formats=zip
python -m pip install --upgrade twine
python -m twine upload dist/*
```
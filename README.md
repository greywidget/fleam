# What's this then?
It's just an example package to test publishing to testpypi

## Publishing Notes
- Generate a user-scoped token on TestPyPI (can't have a project-scoped one until the project exists)
- store it as an environment variable: `export TEST_USER_PYPI_TOKEN="pypi-......"`
- Add index configuration to `pyproject.toml`:
```
[tool.uv.indexes]
testpypi = "https://test.pypi.org/simple/"
```
- Publish like this: `uv publish --index testpypi --token $TEST_USER_PYPI_TOKEN`
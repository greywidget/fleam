# What's this then?
It's just an example package to test publishing to testpypi

## Publishing Notes
- Generate a user-scoped token on TestPyPI (can't have a project-scoped one until the project exists)
- store it in a `.env` file
- Add index configuration for testpypi to `pyproject.toml`:
```
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true

```
- Publish using `just` as it can load environment variables - see `justfile`

## Installing from testpypi
When I first tried this, I got issues as it tried to install **all** packages
from testpypi, not just this one (`fleam`) and so other things such as `typer`
either did not exist on testpypi or were an older version than required by the
dependencies in `pyproject.toml`. I did manage to install with:  

`uv add --index https://test.pypi.org/simple/ --index-strategy unsafe-best-match fleam`

The `pip` equivalent would be (according to ChatGPT):  
`pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple fleam`

You can also run `uv sync --index https://test.pypi.org/simple/ --index-strategy unsafe-best-match`


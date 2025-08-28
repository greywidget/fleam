set dotenv-load := true
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

test-env:
    @echo $env:NAME

publish:
    uv publish --index testpypi --token $env:TEST_PYPI_PROJECT_TOKEN

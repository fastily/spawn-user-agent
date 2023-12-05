# spawn-user-agent
[![Python 3.9+](https://upload.wikimedia.org/wikipedia/commons/4/4f/Blue_Python_3.9%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

`spawn_user_agent` is a library for generating a list of *recent* user agents (i.e. within the past year).  This makes it useful for testing purposes or for web spiders exercising discretion.

So how does this differ from everything else?  Well this is a simple & barebones library without any dependencies.  Generating user agents shouldn't be a difficult or complex problem, but just about every other library I could find struggles to [KISS](https://en.wikipedia.org/wiki/KISS_principle).

Some reasonable amount of effort will be applied to keep the list of UAs up to date.

## Installation
```bash
pip install spawn-user-agent
```

## Usage
```python
from spawn_user_agent.user_agent import SpawnUserAgent

# generate a list of firefox UAs
print(SpawnUserAgent.firefox())

# generate a list of chrome UAs
print(SpawnUserAgent.chrome())

# generate a list of safari UAs
print(SpawnUserAgent.safari())

# generate a list of mobile safari UAs
print(SpawnUserAgent.safari_mobile())

# generate a list of all UAs (combination of everything above)
print(SpawnUserAgent.generate_all())
```
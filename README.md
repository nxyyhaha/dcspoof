# dcspoof

one import, 5 modes for simplicity.

```python
from dcspoof import mode

# default is ios — no extra step
# switch at will:
mode("vr")
mode("ios")
mode("android")
mode("desktop")
```

```
pip install -U git+https://github.com/nxyyhaha/dcspoof
```

## Why this exists

Gateway identify payload accepts `$os`, `$browser`, `$device`. People package each combo as separate library (`discord-vr`, `discord-phone`, `discord-xbox`). Now you manage N packages that do the same thing.

One package. All modes. No conflicts.

---
name: greetings
inputs:
    name1: helloworld.artifact_types.strang:Strang
    name2: helloworld.artifact_types.strang:Strang
    name3: helloworld.artifact_types.strang:Strang
outputs:
    out1: helloworld.artifact_types.strang:Strang
    out2: helloworld.artifact_types.strang:Strang
    out3: helloworld.artifact_types.strang:Strang
---
## Greetings

In this workflow we will see how to properly greet 3 users.

```python
>>> from helloworld.functionality import hello
>>> out1 = hello(name1)
>>> out2 = hello(name2)
>>> out3 = hello(name3)
```

See how simple that was?

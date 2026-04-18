# AUDIENCE: developers working on that container
# Zooms inside one container (e.g. the API)
# showing its internal modules and responsibilities
# Question answered: "What is inside this container?"
# Note: only needed for complex containers

- Zoom:      Inside one container (e.g. the API)
- Shows:     Internal modules, classes, responsibilities
- Audience:  Developers working on that specific container
- Answers:   What is inside this container?
- Note:      Only create if the container is complex enough

```
    [FastAPI Container]
    ├── [Auth Module]
    ├── [Prediction Controller]
    ├── [Preprocessor]
    └── [Model Loader]`
```
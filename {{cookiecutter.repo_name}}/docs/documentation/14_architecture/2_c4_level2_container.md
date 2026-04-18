# AUDIENCE: technical team
# Zooms inside the system: deployable units
# (API, ML model, database, dashboard, pipelines)
# and how they communicate
# Question answered: "What are the main parts
# and how do they connect?"

- Zoom:      Inside the system
- Shows:     Deployable units: API, model, DB, dashboard
- Audience:  Technical team
- Answers:   What are the main parts? How do they talk?

```
    [User] → [FastAPI] → [ML Model]
                    ↓            ↓
                [SQL DB]   [MLflow Registry]
                    ↓
            [Streamlit Dashboard]
```
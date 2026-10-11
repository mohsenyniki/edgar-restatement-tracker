# 0007. Pin runtime dependencies, keep dev tools out

**Status:** Accepted
**Date:** 2026-10-09

## Context
The same code will run on a laptop, in Docker, and under Airflow. A different library version in production is a common source of "works on my machine" failures.

## Decision
`requirements.txt` pins exact versions of runtime dependencies (`requests`, `python-dotenv`, `pandas` and their dependencies). Dev-only tools such as Jupyter's `ipykernel` are not included.

## Consequences
- Production installs exactly what was tested.
- Upgrades are explicit commits.
- Dev tools need a separate list (`requirements-dev.txt`) once there are more of them.

import os

TRUTHY={"1", "true", "yes", "on"}


if os.getenv("SUPRESS_WARNINGS", '').strip().lower() in TRUTHY:
    import warnings
    warnings.filterwarnings("ignore")
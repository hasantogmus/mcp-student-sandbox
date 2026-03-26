import os
from typing import Optional


def get_secret(key: str) -> str:
    """
    Safely retrieve sensitive credential from environment variables.

    Args:
        key (str): Name of the environment variable.

    Returns:
        str: The secret value.

    Raises:
        ValueError: If the environment variable is not set.
    """
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Required environment variable '{key}' is not set. Please set it before running.")
    return value


def connect() -> None:
    """
    Connect using AWS credentials from environment variables.

    Note: Credentials should be stored in environment variables or secret management system.
    Never hardcode secrets in source code.
    """
    try:
        aws_secret_key = get_secret("AWS_SECRET_KEY")
        print("Connecting with AWS credentials (from environment)...")
        # Use the credentials for connecting
        # print(f"Connecting with: {aws_secret_key}")  # NEVER print secrets!
    except ValueError as e:
        print(f"Error: {e}")
        raise

"""
utils/logger.py – structured logging helper built on structlog.
"""

from __future__ import annotations

import logging
import structlog


def get_logger(name: str) -> structlog.BoundLogger:
    """Return a structlog logger bound to *name*."""
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.dev.ConsoleRenderer(),
        ],
    )
    return structlog.get_logger(name)

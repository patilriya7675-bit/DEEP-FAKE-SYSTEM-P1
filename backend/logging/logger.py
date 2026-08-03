import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Create logs directory
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "app.log"

# Rotating file handler
file_handler = RotatingFileHandler(
    filename=log_file,
    maxBytes=5 * 1024 * 1024,   # 5 MB
    backupCount=5
)

file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger = logging.getLogger("RTDD")
logger.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
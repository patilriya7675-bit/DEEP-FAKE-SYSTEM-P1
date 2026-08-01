from pathlib import Path

# Allowed video formats
ALLOWED_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv"
}

# Maximum file size (100 MB)
MAX_FILE_SIZE = 100 * 1024 * 1024


def validate_video_extension(filename: str):
    """
    Check whether uploaded file has a valid video extension.
    """
    extension = Path(filename).suffix.lower()
    return extension in ALLOWED_EXTENSIONS


def validate_file_size(file_size: int):
    """
    Check whether uploaded file size is within the allowed limit.
    """
    return file_size <= MAX_FILE_SIZE
class AppException(Exception):
    """Base application exception."""
    pass

class ValidationError(AppException):
    """Raised when input validation fails."""
    pass

class NotFoundError(AppException):
    """Raised when resource not found."""
    pass

class DatabaseError(AppException):
    """Raised on database errors."""
    pass

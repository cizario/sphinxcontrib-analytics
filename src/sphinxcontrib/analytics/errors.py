from sphinx.errors import ConfigError


class AnalyticsConfigError(ConfigError):
    """Analytics configuration error. Raised when a value is missing or misconfigured."""
    category = 'Analytics config error'

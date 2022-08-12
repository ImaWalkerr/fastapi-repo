from enum import Enum


class LogLevel(Enum):
    critical = 'critical'
    fatal = 'fatal'
    error = 'error'
    warn = 'warn'
    warning = 'warning'
    info = 'info'
    debug = 'debug'

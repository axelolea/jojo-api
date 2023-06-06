from enum import Enum

StatsValues = [
    'NULL',
    'A',
    'B',
    'C',
    'D',
    'E',
    'INFINITE',
    '?'
]

StatsEnum = Enum(
    'StatsValues',
    StatsValues
)

FAST_API_CONFIG = {
    'title': 'Jojo\'s API',
    'description': '',
    'version': '1.0.0',
    'redoc_url': None
}

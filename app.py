"""Arquivo Inicial do Servidor."""
from loguru import logger
from server import Servidor

logger.add(
    "logs/server.log",
    rotation="1 day",
    retention="10 days",
    level="DEBUG",
    encoding="utf-8",
    enqueue=True,
    compression="zip"
)


app = Servidor()
app.setup()

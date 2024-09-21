import asyncio
import httpx
import pytest 

from main import app
from database.connection import Settings
from models.event import Event
from models.user import User
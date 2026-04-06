"""Formation geometry helpers — generate target positions."""
import math
from swarm.agent import Agent

def ring_formation(n: int, radius: float, altitude: float) -> list[tuple[float,float,float]]:
    """Return n evenly-spaced (x,y,z) positions on a horizontal ring."""
    return [
        (radius * math.cos(2*math.pi*i/n),
         radius * math.sin(2*math.pi*i/n),
         altitude)
        for i in range(n)
    ]

def line_formation(n: int, spacing: float, altitude: float) -> list[tuple[float,float,float]]:
    """Return n positions in a straight line along the x-axis."""
    return [(i * spacing, 0.0, altitude) for i in range(n)]

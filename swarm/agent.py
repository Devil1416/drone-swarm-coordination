"""Minimal drone agent model for swarm simulation."""
from dataclasses import dataclass, field
from typing import Optional
import math

@dataclass
class Agent:
    agent_id: int
    x: float
    y: float
    z: float
    vx: float = 0.0
    vy: float = 0.0
    vz: float = 0.0
    neighbours: list[int] = field(default_factory=list)

    def distance_to(self, other: 'Agent') -> float:
        return math.sqrt(
            (self.x - other.x)**2 +
            (self.y - other.y)**2 +
            (self.z - other.z)**2
        )

    def step(self, dt: float):
        """Advance position by current velocity."""
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt

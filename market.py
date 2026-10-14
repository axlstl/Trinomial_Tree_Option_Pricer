from dataclasses import dataclass

@dataclass
class Market:
    S0 : float
    rf_rate : float
    volatility: float


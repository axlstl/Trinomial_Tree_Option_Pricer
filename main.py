import xml.etree.ElementTree as ET

from datetime import datetime as dt, timedelta

from model.trinomial import TrinomialModel
from options import VanillaOption
from market import Market
from model.binomial import BinomialModel


if __name__=="__main__":
    from datetime import datetime as dt,timedelta
    from market import Market
    from options import VanillaOption

    option=VanillaOption(strike=110,strike_date=dt.now(),option_type="call",exercise_type="european",mty_date=dt.now()+timedelta(days=365))
    market=Market(S0=100,rf_rate=0.05,volatility=0.2)
    maturity=dt.now()+timedelta(days=365)

    model=TrinomialModel(market,option,maturity,steps=3)


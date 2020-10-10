# Vanilla Option Pricing
[![Build Status](https://travis-ci.org/donlelef/vanilla-option-pricing.svg?branch=master)](https://travis-ci.org/donlelef/vanilla-option-pricing) 
[![Coverage Status](https://coveralls.io/repos/github/donlelef/vanilla-option-pricing/badge.svg?branch=master)](https://coveralls.io/github/donlelef/vanilla-option-pricing?branch=master)
[![Documentation Status](https://readthedocs.org/projects/vanilla-option-pricing/badge/?version=latest)](https://vanilla-option-pricing.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/vanilla-option-pricing)](https://pepy.tech/project/vanilla-option-pricing)

A simple Python package implementing stochastic models to price financial options.  
Theoretical background and comprehensive explanation of models and their paramenters
can be found is the paper *Fast calibration of two-factor models for energy option pricing*
by Emanuele Fabbiani, Andrea Marziali and Giuseppe De Nicolao, available on 
[arXiv](https://arxiv.org/abs/1809.03941)  

### Installing
The preferred way to install the package is using pip,
but you can also download the code and install the package from source

To install the package using pip:

```bash
pip install vanilla_option_pricing
```

### Quickstart
Let's create a sample call option

```python
from datetime import datetime, timedelta
from vanilla_option_princing.option import VanillaOption

option = VanillaOption(
    spot=100,
    strike=101,
    dividend=0,
    date=datetime.today(),
    maturity=datetime.today() + timedelta(days=30),
    option_type='c',
    price=1,
    instrument='TTF'
)
```

We can compute the implied volatility and create a Black-Sholes model 
with it. Of course, if now we ask the model to price the option, we'll
get the real option price.

```python
from vanilla_option_princing.models import GeometricBrownianMotion

volatility = option.implied_volatility_of_undiscounted_price
model = GeometricBrownianMotion(volatility)
model_price = model.price_option_black(option)
print(f'Actual price: {option.price}, model price: {model_price}')
```

We can also try and calibrate the parameters of a model against 
listed options.

```python
from datetime import date
from vanilla_option_princing.models import OrnsteinUhlenbeck
from vanilla_option_pricing.calibration import ModelCalibration

data_set = [
    VanillaOption('TTF', 'c', date(2018, 1, 1), 2, 101, 100, date(2018, 2, 1)),
    VanillaOption('TTF', 'p', date(2018, 1, 1), 2, 98, 100, date(2018, 2, 1)),
    VanillaOption('TTF', 'c', date(2018, 1, 1), 5, 101, 100, date(2018, 5, 31))
]

models = [
    GeometricBrownianMotion(0.2),
    OrnsteinUhlenbeck(p_0=0, l=100, s=2)
]
calibration = ModelCalibration(data_set)

print(f'Implied volatilities: {[o.implied_volatility_of_undiscounted_price for o in data_set]}\n')

for model in models:
    result, trained_model = calibration.calibrate_model(model)
    print('Optimization results:')
    print(result)
    print(f'Calibrated parameters: {trained_model.parameters}\n\n')
```

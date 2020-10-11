import itertools

import numpy as np
import pytest
from pytest import fixture

from tests.utils import check_exception_on_wrong_parameters
from vanilla_option_pricing.models import LogMeanRevertingToGeneralisedWienerProcess, \
    NumericalLogMeanRevertingToGeneralisedWienerProcess

p_0 = np.eye(2)


@fixture
def model():
    return LogMeanRevertingToGeneralisedWienerProcess(p_0, 1, 1, 0.05)


@fixture
def numerical_model():
    return NumericalLogMeanRevertingToGeneralisedWienerProcess(p_0, 1, 1, 0.05)


def test_variance(model):
    assert model.variance(1) == pytest.approx(0.967664270613846, abs=10e-4)


def test_properties(numerical_model):
    assert numerical_model.parameters == (1, 1, 0.05)


def test_exception_on_illegal_parameters():
    check_exception_on_wrong_parameters(
        LogMeanRevertingToGeneralisedWienerProcess,
        {'p_0': p_0, 'l': -1, 's_x': 1, 's_y': 1},
        {'p_0': p_0, 'l': 1, 's_x': 1, 's_y': 1},
        (1, 1, -1)
    )


def test_numerical_variance(numerical_model):
    assert numerical_model.variance(1) == pytest.approx(0.967664270613846, abs=10e-4)


def test_numerical_properties(model):
    assert model.parameters == (1, 1, 0.05)


def test_exception_on_illegal_parameters_numerical():
    check_exception_on_wrong_parameters(
        NumericalLogMeanRevertingToGeneralisedWienerProcess,
        {'p_0': p_0, 'l': -1, 's_x': 1, 's_y': 1},
        {'p_0': p_0, 'l': 1, 's_x': 1, 's_y': 1},
        (1, 1, -1)
    )


def test_analytical_numerical_consistency():
    ls = s_xs = s_ys = list(np.linspace(0.5, 5, 10))
    ts = np.linspace(10.0 / 365.0, 2, 10)
    params = list(itertools.product(ls, s_xs, s_ys))
    for l, s_x, s_y in params:
        for t in ts:
            lmrgw = LogMeanRevertingToGeneralisedWienerProcess(p_0, l, s_x, s_y)
            num_lmrgw = NumericalLogMeanRevertingToGeneralisedWienerProcess(p_0, l, s_x, s_y)
            var = lmrgw.variance(t)
            num_var = num_lmrgw.variance(t)
            assert var == pytest.approx(num_var, 10e-8)

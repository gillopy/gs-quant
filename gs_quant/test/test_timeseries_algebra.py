"""
Copyright 2018 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from pandas.util.testing import assert_series_equal
import numpy as np
from ..timeseries import *
from datetime import date


def test_add():
    dates1 = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
        date(2019, 1, 4),
    ]

    dates2 = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 1.0, 1.0, 1.0], index=dates1)
    y = pd.Series([1.0, 1.0, 1.0], index=dates2)

    result = algebra.add(x, y, Interpolate.INTERSECT)
    expected = pd.Series([2.0, 2.0, 2.0], index=dates2)
    assert_series_equal(result, expected, obj="Add intersect left")

    result = algebra.add(y, x, Interpolate.INTERSECT)
    expected = pd.Series([2.0, 2.0, 2.0], index=dates2)
    assert_series_equal(result, expected, obj="Add intersect right")

    result = algebra.add(x, y, Interpolate.NAN)
    expected = pd.Series([2.0, 2.0, 2.0, np.nan], index=dates1)
    assert_series_equal(result, expected, obj="Add NaN left")

    result = algebra.add(y, x, Interpolate.NAN)
    expected = pd.Series([2.0, 2.0, 2.0, np.nan], index=dates1)
    assert_series_equal(result, expected, obj="Add NaN right")

    result = algebra.add(x, y, Interpolate.ZERO)
    expected = pd.Series([2.0, 2.0, 2.0, 1.0], index=dates1)
    assert_series_equal(result, expected, obj="Add zero left")

    result = algebra.add(x, y, Interpolate.STEP)
    expected = pd.Series([2.0, 2.0, 2.0, 2.0], index=dates1)
    assert_series_equal(result, expected, obj="Add step right")


def test_subtract():
    dates1 = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
        date(2019, 1, 4),
    ]

    dates2 = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 1.0, 1.0, 1.0], index=dates1)
    y = pd.Series([1.0, 1.0, 1.0], index=dates2)

    result = algebra.subtract(x, y, Interpolate.INTERSECT)
    expected = pd.Series([0.0, 0.0, 0.0], index=dates2)
    assert_series_equal(result, expected, obj="Subtract intersect left")

    result = algebra.subtract(y, x, Interpolate.INTERSECT)
    expected = pd.Series([0.0, 0.0, 0.0], index=dates2)
    assert_series_equal(result, expected, obj="Subtract intersect right")

    result = algebra.subtract(x, y, Interpolate.NAN)
    expected = pd.Series([0.0, 0.0, 0.0, np.nan], index=dates1)
    assert_series_equal(result, expected, obj="Subtract NaN left")

    result = algebra.subtract(y, x, Interpolate.NAN)
    expected = pd.Series([0.0, 0.0, 0.0, np.nan], index=dates1)
    assert_series_equal(result, expected, obj="Subtract NaN right")

    result = algebra.subtract(x, y, Interpolate.ZERO)
    expected = pd.Series([0.0, 0.0, 0.0, 1.0], index=dates1)
    assert_series_equal(result, expected, obj="Subtract zero left")

    result = algebra.subtract(x, y, Interpolate.STEP)
    expected = pd.Series([0.0, 0.0, 0.0, 0.0], index=dates1)
    assert_series_equal(result, expected, obj="Subtract step right")


def test_multiply():
    dates1 = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
        date(2019, 1, 4),
    ]

    dates2 = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 2.0, 3.0, 4.0], index=dates1)
    y = pd.Series([2.0, 1.5, 2.0], index=dates2)

    result = algebra.multiply(x, y, Interpolate.INTERSECT)
    expected = pd.Series([2.0, 3.0, 6.0], index=dates2)
    assert_series_equal(result, expected, obj="Multiply intersect left")

    result = algebra.multiply(y, x, Interpolate.INTERSECT)
    expected = pd.Series([2.0, 3.0, 6.0], index=dates2)
    assert_series_equal(result, expected, obj="Multiply intersect right")

    result = algebra.multiply(x, y, Interpolate.NAN)
    expected = pd.Series([2.0, 3.0, 6.0, np.nan], index=dates1)
    assert_series_equal(result, expected, obj="Multiply NaN left")

    result = algebra.multiply(y, x, Interpolate.NAN)
    expected = pd.Series([2.0, 3.0, 6.0, np.nan], index=dates1)
    assert_series_equal(result, expected, obj="Multiply NaN right")

    result = algebra.multiply(x, y, Interpolate.ZERO)
    expected = pd.Series([2.0, 3.0, 6.0, 0.0], index=dates1)
    assert_series_equal(result, expected, obj="Multiply zero left")

    result = algebra.multiply(x, y, Interpolate.STEP)
    expected = pd.Series([2.0, 3.0, 6.0, 8.0], index=dates1)
    assert_series_equal(result, expected, obj="Multiply step left")


def test_divide():
    dates1 = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
        date(2019, 1, 4),
    ]

    dates2 = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 2.0, 3.0, 4.0], index=dates1)
    y = pd.Series([2.0, 1.0, 2.0], index=dates2)

    result = algebra.divide(x, y, Interpolate.INTERSECT)
    expected = pd.Series([0.5, 2.0, 1.5], index=dates2)
    assert_series_equal(result, expected, obj="Divide intersect left")

    result = algebra.divide(y, x, Interpolate.INTERSECT)
    expected = pd.Series([2.0, 0.5, 2/3], index=dates2)
    assert_series_equal(result, expected, obj="Divide intersect right")

    result = algebra.divide(x, y, Interpolate.NAN)
    expected = pd.Series([0.5, 2.0, 1.5, np.nan], index=dates1)
    assert_series_equal(result, expected, obj="Divide NaN left")

    result = algebra.divide(y, x, Interpolate.NAN)
    expected = pd.Series([2.0, 0.5, 2/3, np.nan], index=dates1)
    assert_series_equal(result, expected, obj="Divide NaN right")

    result = algebra.divide(x, y, Interpolate.ZERO)
    expected = pd.Series([0.5, 2.0, 1.5, np.inf], index=dates1)
    assert_series_equal(result, expected, obj="Divide zero left")

    result = algebra.divide(x, y, Interpolate.STEP)
    expected = pd.Series([0.5, 2.0, 1.5, 2.0], index=dates1)
    assert_series_equal(result, expected, obj="Divide step left")


def test_exp():

    dates = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 2.0, 3.0], index=dates)

    result = algebra.exp(x)
    expected = pd.Series([np.exp(1), np.exp(2), np.exp(3)], index=dates)
    assert_series_equal(result, expected, obj="Exp")


def test_log():

    dates = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 2.0, 3.0], index=dates)

    result = algebra.log(x)
    expected = pd.Series([np.log(1), np.log(2), np.log(3)], index=dates)
    assert_series_equal(result, expected, obj="Log")


def test_power():

    dates = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 2.0, 3.0], index=dates)

    result = algebra.power(x, 2)
    expected = pd.Series([1.0, 4.0, 9.0], index=dates)
    assert_series_equal(result, expected, obj="Pow")


def test_sqrt():

    dates = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 4.0, 9.0], index=dates)

    result = algebra.sqrt(x)
    expected = pd.Series([1.0, 2.0, 3.0], index=dates)
    assert_series_equal(result, expected, obj="Sqrt")


def test_abs():

    dates = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([-1.0, 2.0, -3.0], index=dates)

    result = algebra.abs_(x)
    expected = pd.Series([1.0, 2.0, 3.0], index=dates)
    assert_series_equal(result, expected, obj="Abs")


def test_floor():

    dates = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 2.0, 3.0], index=dates)

    result = algebra.floor(x, 2.0)
    expected = pd.Series([2.0, 2.0, 3.0], index=dates)
    assert_series_equal(result, expected, obj="Floor")


def test_ceil():

    dates = [
        date(2019, 1, 1),
        date(2019, 1, 2),
        date(2019, 1, 3),
    ]

    x = pd.Series([1.0, 2.0, 3.0], index=dates)

    result = algebra.ceil(x, 2.0)
    expected = pd.Series([1.0, 2.0, 2.0], index=dates)
    assert_series_equal(result, expected, obj="Ceil")
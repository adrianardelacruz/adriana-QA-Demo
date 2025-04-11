from app import php_to_usd, usd_to_php


def test_php_to_usd():
    assert php_to_usd(560) == 10.0
    assert php_to_usd(112) == 2.0


def test_usd_to_php():
    assert usd_to_php(10) == 560.0
    assert usd_to_php(2) == 112.0

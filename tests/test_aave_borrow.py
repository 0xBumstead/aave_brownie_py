from scripts.aave_borrow import approve_erc20, get_asset_price, get_lending_pool
from scripts.helpful_scripts import get_account
from brownie import config, network


def test_get_asset_price():
    # Arrange / Act
    asset_price = get_asset_price(
        config["networks"][network.show_active()]["dai_eth_price_feed"]
    )
    # Assert
    assert asset_price > 0


def test_get_lending_pool():
    # Arrange / Act
    lending_pool = get_lending_pool()
    # Assert
    assert lending_pool is not None


def test_approve_ert20():
    # Arrange
    account = get_account()
    lending_pool = get_lending_pool()
    amount = 1000000000000000000
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    # Act
    tx = approve_erc20(amount, lending_pool.address, erc20_address, account)
    # Assert
    assert tx is not True

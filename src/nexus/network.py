from cosmpy.aerial.contract import LedgerContract
from cosmpy.aerial.client import LedgerClient, NetworkConfig
from cosmpy.aerial.faucet import FaucetApi

from nexus.config import AgentNetwork, CONTRACT_ALMANAC, AGENT_NETWORK


if AGENT_NETWORK == AgentNetwork.FetchaiTestnet:
    _ledger = LedgerClient(NetworkConfig.fetchai_stable_testnet())
    _faucet_api = FaucetApi(NetworkConfig.latest_stable_testnet())
elif AGENT_NETWORK == AgentNetwork.FetchaiMainnet:
    _ledger = LedgerClient(NetworkConfig.fetchai_mainnet())
else:
    raise NotImplementedError

_contract = LedgerContract(None, _ledger, CONTRACT_ALMANAC)


def get_ledger() -> LedgerClient:
    return _ledger


def get_faucet() -> FaucetApi:
    return _faucet_api


def get_reg_contract() -> LedgerContract:
    return _contract

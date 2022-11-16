from cosmpy.aerial.client import NetworkConfig
from cosmpy.aerial.faucet import FaucetApi

from nexus.agent import Agent
from nexus.context import Context
from nexus.models import Model
from nexus.resolver import AlmanacResolver


class Message(Model):
    message: str


agent = Agent(
    name="bob",
    port=8001,
    seed="agent2 secret phrase",
    network="fetchai-testnet",
    endpoint="http://127.0.0.1:8001/submit",
    resolve=AlmanacResolver(),
)

ledger = agent.ledger
faucet_api = FaucetApi(NetworkConfig.latest_stable_testnet())

agent_balance = ledger.query_bank_balance(agent.wallet.address())

if agent_balance < 500000000000000000:
    # Add tokens to agent's wallet
    faucet_api.get_wealth(agent.wallet.address())

agent.register()


@agent.on_message(model=Message)
async def bob_rx_message(ctx: Context, sender: str, msg: Message):
    print(f"[{ctx.name:5}] From: {sender} {msg.message}")

    # send the response
    await ctx.send(sender, Message(message="hello there alice"))


if __name__ == "__main__":
    agent.run()
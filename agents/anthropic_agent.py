from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic, beta_tool

client = Anthropic()

@beta_tool
def get_weather(location:str) -> str:
    """Get the current weather in a given location.

    Args:
        location: The city, e.g  Cali, Colombia
    """
    return '{"temperature":"24°C", "condition": "Sunny"}'

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=[get_weather],
    messages=[{"role": "user", "content":"What's the weather in Cali"}],
)

print(runner.until_done().content)
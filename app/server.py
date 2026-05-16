from mcp.server.fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Simple Tools Server")

print("mcp server created")

# Tool 1: Add numbers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


# Tool 2: Get current time
@mcp.tool()
def get_current_time() -> str:
    """Return current system time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    mcp.run()
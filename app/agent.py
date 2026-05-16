import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client


async def run():
    # Connect to MCP server
    async with stdio_client("python server.py") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Call add_numbers tool
            result = await session.call_tool(
                "add_numbers",
                {"a": 5, "b": 7}
            )
            print("Addition Result:", result)

            # Call time tool
            time_result = await session.call_tool(
                "get_current_time",
                {}
            )
            print("Current Time:", time_result)


asyncio.run(run())
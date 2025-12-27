from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",   # only for sse transport
    port=8000,   # only for sse transport
)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        mcp.run(transport="stdio")
    elif transport == "sse":
        mcp.run(transport="sse")
    else:
        raise ValueError("Unsupported transport type. Use 'stdio' or 'sse'.")
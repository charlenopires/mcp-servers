from mcp.server.fastmcp import FastMCP
import asyncio
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PingPongServer(FastMCP):
    def __init__(self):
        super().__init__(name="PingPongServer")
        logger.info("PingPong server initialized")
        
        # Register the ping tool
        @self.tool(name="ping", description="Responds with 'pong' when pinged")
        async def handle_ping():
            """Handler for 'ping' messages. Responds with 'pong'."""
            logger.info("Received ping request")
            return "pong"

async def main():
    # Create and start the server
    server = PingPongServer()
    
    # Create a Starlette app that we can run with uvicorn
    app = server.streamable_http_app()
    
    # Run with uvicorn
    host = "localhost"
    port = 8000
    logger.info(f"Starting PingPong MCP server on {host}:{port}")
    
    # Start the server
    config = uvicorn.Config(app, host=host, port=port)
    server_instance = uvicorn.Server(config)
    await server_instance.serve()

if __name__ == "__main__":
    asyncio.run(main())
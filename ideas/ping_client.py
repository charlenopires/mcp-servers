from mcp.client.streamable_http import create_mcp_http_client
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_ping(host="localhost", port=8000):
    """
    Connect to the ping-pong server and test the ping functionality.
    
    Args:
        host (str): The host where the server is running
        port (int): The port on which the server is listening
    """
    try:
        # Connect to the server
        logger.info(f"Connecting to MCP server at {host}:{port}")
        url = f"http://{host}:{port}"
        
        # Create a client session with the server URL
        client = await create_mcp_http_client(url)
        logger.info("Connected to server")
        
        try:
            # Send a ping message
            logger.info("Sending 'ping' message...")
            response = await client.call_tool("ping")
            
            # Display the response
            logger.info(f"Received response: {response}")
            
            # Verify the response
            if response == "pong":
                logger.info("Ping test successful! ✅")
            else:
                logger.warning(f"Unexpected response: {response}")
        finally:
            # Close the client
            await client.close()
            
    except Exception as e:
        logger.error(f"Error during ping test: {e}")

async def main():
    await test_ping()
    
if __name__ == "__main__":
    asyncio.run(main())
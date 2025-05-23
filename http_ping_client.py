import asyncio
import httpx
import json
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_ping(host="localhost", port=8000):
    """
    Simple HTTP client to test the ping-pong MCP server
    
    Args:
        host (str): The host where the server is running
        port (int): The port on which the server is listening
    """
    url = f"http://{host}:{port}/tools/call"
    
    # Create a request payload for the "ping" tool
    payload = {
        "method": "tools/call",
        "id": 1,  # A simple ID for the request
        "params": {
            "name": "ping",
            "arguments": {}  # No arguments needed for ping
        }
    }
    
    try:
        logger.info(f"Connecting to MCP server at {url}")
        
        async with httpx.AsyncClient() as client:
            # Set the proper headers
            headers = {
                "Content-Type": "application/json"
            }
            
            # Send the request
            logger.info("Sending 'ping' request...")
            response = await client.post(url, json=payload, headers=headers)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                result = response.json()
                logger.info(f"Received response: {result}")
                
                # Check if we got the expected 'pong' response
                if "result" in result and result["result"] == "pong":
                    logger.info("Ping test successful! ✅")
                else:
                    logger.warning(f"Unexpected response format: {result}")
            else:
                logger.error(f"Request failed with status code: {response.status_code}")
                logger.error(f"Response content: {response.text}")
                
    except Exception as e:
        logger.error(f"Error during ping test: {e}")
        return False
    
    return True

async def main():
    # Parse command line arguments for host and port
    host = "localhost"
    port = 8000
    
    if len(sys.argv) > 1:
        host = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    
    success = await test_ping(host, port)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
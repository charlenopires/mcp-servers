#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting MCP Ping-Pong Test${NC}"

# Set the Python interpreter to use
PYTHON="python"

# Check if Python is available
if ! command -v $PYTHON &> /dev/null; then
    echo -e "${RED}Error: Python not found. Please make sure Python is installed.${NC}"
    exit 1
fi

# Directory where the scripts are located
DIR="$(dirname "$0")"
cd "$DIR"

# Install dependencies if needed
if ! $PYTHON -c "import uvicorn" &> /dev/null; then
    echo -e "${YELLOW}Installing dependencies...${NC}"
    $PYTHON -m pip install uvicorn httpx
fi

# Start the server in the background
echo -e "${YELLOW}Starting the ping server...${NC}"
$PYTHON ping_server.py &
SERVER_PID=$!

# Wait for the server to start
echo -e "${YELLOW}Waiting for server to initialize (3 seconds)...${NC}"
sleep 3

# Run the client
echo -e "${YELLOW}Testing the ping server...${NC}"
$PYTHON http_ping_client.py

# Store the client exit status
CLIENT_STATUS=$?

# Kill the server
echo -e "${YELLOW}Shutting down the server...${NC}"
kill $SERVER_PID

# Wait for the server to shut down
sleep 1

# Check if the client was successful
if [ $CLIENT_STATUS -eq 0 ]; then
    echo -e "${GREEN}Test completed successfully!${NC}"
    exit 0
else
    echo -e "${RED}Test failed!${NC}"
    exit 1
fi
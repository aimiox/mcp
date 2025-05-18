#!/bin/bash
#
# AMXNet MCP Server Docker Runner
# This script sets environment variables and launches the AMXNet MCP server in a Docker container
#

# Default configuration (can be overridden by environment variables)
AMXNET_DEVICE_PORT=${AMXNET_DEVICE_PORT:-8765}
AMXNET_SSE_PORT=${AMXNET_SSE_PORT:-8002}
AMXNET_IMAGE=${AMXNET_IMAGE:-"amxnet-mcp:latest"}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --device-port)
      AMXNET_DEVICE_PORT="$2"
      shift 2
      ;;
    --sse-port)
      AMXNET_SSE_PORT="$2"
      shift 2
      ;;
    --image)
      AMXNET_IMAGE="$2"
      shift 2
      ;;
    --help)
      echo "Usage: $0 [options]"
      echo "Options:"
      echo "  --device-port PORT   Set device WebSocket port (default: 8765)"
      echo "  --sse-port PORT      Set MCP SSE port (default: 8002)"
      echo "  --image IMAGE        Set Docker image name (default: amxnet-mcp:latest)"
      echo "  --help               Show this help message"
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      echo "Use --help for usage information"
      exit 1
      ;;
  esac
done

# Print configuration
echo "Starting AMXNet MCP Server with the following configuration:"
echo "  Device Port: $AMXNET_DEVICE_PORT"
echo "  MCP Port: $AMXNET_SSE_PORT"
echo "  Docker Image: $AMXNET_IMAGE"

# Run the Docker container
# - Map both ports
# - Pass environment variables
# - Run in detached mode with auto-removal
sudo docker run -d --rm \
  -p $AMXNET_DEVICE_PORT:$AMXNET_DEVICE_PORT \
  -p $AMXNET_SSE_PORT:$AMXNET_SSE_PORT \
  -e AMXNET_DEVICE_PORT=$AMXNET_DEVICE_PORT \
  -e AMXNET_SSE_PORT=$AMXNET_SSE_PORT \
  --name amxnet-mcp \
  $AMXNET_IMAGE 

echo "AMXNet MCP Server started in Docker container: amxnet-mcp"
echo "To view logs: sudo docker logs amxnet-mcp"
echo "To stop: sudo docker stop amxnet-mcp"

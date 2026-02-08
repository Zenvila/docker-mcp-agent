import os
from mcp.server.fastmcp import FastMCP

# 1. INITIALIZE FIRST
mcp = FastMCP("PrecisionServer")

# 2. THEN DEFINE TOOLS
@mcp.tool()
def get_system_status(status_type: str) -> str:
    """Returns a status report for Zen's projects."""
    if status_type.lower() == "neural":
        return "The Neural Scheduler: Active and monitoring kernel tasks."
    return f"Status for {status_type}: All systems normal."

@mcp.tool()
def read_voip_project(folder_name: str, file_name: str) -> str:
    """Reads a file from the mounted Freelance directory."""
    # The path inside Docker is /app/projects because of your bind mount
    full_path = f"/app/projects/{folder_name}/{file_name}"
    try:
        if not os.path.exists(full_path):
            return f"Error: File not found at {full_path}. Check folder/file name."
            
        with open(full_path, "r") as f:
            content = f.read()
        return f"Content of {file_name}:\n\n{content}"
    except Exception as e:
        return f"Error reading {full_path}: {str(e)}"

if __name__ == "__main__":
    mcp.run()
# docker-mcp-agent
A custom Model Context Protocol (MCP) server built with Python and Docker to bridge LLMs (Claude Desktop) with local system data and project files. Part of my MCP certification and ongoing research in Agentic AI.


# MCP Precision Agent 🛠️🤖

[![MCP](https://img.shields.io/badge/Protocol-MCP-orange)](https://modelcontextprotocol.io)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/)

## 📖 What is MCP?
The **Model Context Protocol (MCP)** is an open standard that enables AI models (like Claude) to safely and reliably interact with local data and tools. Think of it as **USB-C for Artificial Intelligence**—it provides a universal way to connect a "brain" (LLM) to "hands" (your local files, databases, or APIs).

## 🚀 About This Project
This repository is a **custom MCP Server** designed to bridge Claude Desktop with my local Windows environment. It allows the AI to autonomously retrieve project statuses and read specific research files (like VoIP and Kernel-level projects) directly from my system.

### Key Features:
* **Project Monitoring:** Custom logic to report the status of my "Neural Scheduler" research.
* **File Interaction:** Ability for the AI to read and summarize local project files using Docker Bind Mounts.
* **Containerized Security:** The server runs inside a Docker container, ensuring the AI only sees the folders I explicitly share.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10 (FastMCP Framework).
* **Infrastructure:** Docker Desktop (Windows).
* **Host:** Claude Desktop.

## 🔧 Installation & Setup

### 1. Build the Docker Image
Navigate to the project folder and run:
```powershell
docker build -t precision-mcp .

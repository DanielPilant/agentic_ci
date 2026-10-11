# 🚀 AI-CI: The AI-Powered CI/CD Agent for Developers

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/CLI-Typer-black.svg)](https://typer.tiangolo.com/)
[![AI](https://img.shields.io/badge/AI-LangGraph%20%7C%20MCP-orange.svg)](https://python.langchain.com/docs/langgraph)
[![Package Manager](https://img.shields.io/badge/Managed%20with-uv-purple.svg)](https://docs.astral.sh/uv/)

## 📖 Overview

**AI-CI** is a modern CLI tool and Internal Developer Platform (IDP) designed to bring enterprise-level DevOps and automated QA to freelance developers and small teams.

Instead of manually writing complex CI/CD pipelines or relying on static linters, AI-CI generates your infrastructure and embeds **autonomous LangGraph agents** directly into your CI pipeline. These agents read your code, analyze test failures using the Model Context Protocol (MCP), enforce quality standards, and provide actionable fixes before your code ever reaches production.

## ✨ Core Features

- **Zero-Config CI/CD:** Interactively generate optimal `.github/workflows` YAML files tailored to your specific language and testing framework.
- **Serverless Agentic QA:** AI agents run directly inside your GitHub Actions runner. No external SaaS servers to trust with your code; you control the environment and the API keys.
- **Context-Aware Reviews (MCP):** Agents don't just read diffs. Using MCP, they can securely inspect local files, read error logs from failed tests, and understand the deep context of a crash.
- **Language Agnostic Architecture:** Starting with Fullstack environments (JS/Python), the container-first design ensures future compatibility with system languages like C++ and Rust.

## 🏗️ System Architecture & Design

The project is divided into three primary tiers:

### 1. The Configuration Tier (CLI)

Built with **Python & Typer**, this local CLI acts as the developer's assistant. It asks interactive questions and scaffolds the necessary configuration files, Dockerfiles, and AI-agent scripts directly into the user's repository.

### 2. The Agent Tier (LangGraph)

The brain of the operation. Built using **LangGraph**, the agent is modeled as a state machine:

1.  **Ingestion:** Reads the Git Diff and recent commit messages.
2.  **Analysis:** Triggers CI tests. If a test fails, it uses MCP tools to read the specific stack trace.
3.  **Resolution:** Generates a human-readable summary of the failure and suggests a direct code fix via GitHub PR comments.

### 3. The Execution Tier (CI/CD)

The generated workflows run on **GitHub Actions**. The pipeline handles the actual build, testing, and artifact generation (Docker). Future iterations will include Canary Deployment integrations (e.g., ArgoCD) where the AI acts as a "Release Gatekeeper," monitoring live production logs for 10 minutes before allowing a full 100% rollout.

## 🛠️ Technology Stack

- **Language:** Python (Strictly typed)
- **Package Manager:** [uv](https://docs.astral.sh/uv/) (Blazing fast, Rust-based environment management)
- **CLI Framework:** [Typer](https://typer.tiangolo.com/) (For building the interactive terminal interface)
- **AI & LLM Orchestration:** [LangChain](https://www.langchain.com/) & [LangGraph](https://www.langchain.com/langgraph)
- **Context Protocol:** [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) (For securely giving the LLM filesystem and terminal access)
- **CI/CD Infrastructure:** GitHub Actions (Primary), Docker

## 🚀 Getting Started (Specs)

### Installation

Ensure you have `uv` installed, then clone the repository and set up the environment:

```bash
git clone https://github.com/yourusername/ai-ci.git
cd ai-ci
uv sync
```

### Usage

Run the CLI using `uv` to ensure you are in the isolated virtual environment:

```bash
# Initialize a new AI-powered pipeline in a project
uv run ai-ci init --language python

# Manually trigger the AI agent to analyze your current local codebase
uv run ai-ci analyze
```

## 🗺️ Roadmap

- [ ] **Phase 1 (Current):** Build the foundational Typer CLI to generate GitHub Action YAMLs.
- [ ] **Phase 2:** Integrate LangGraph and MCP to create the first automated code reviewer script.
- [ ] **Phase 3:** Package the CLI for global distribution (PyPI / standalone binary).
- [ ] **Phase 4:** Expand language support to C++ and Rust via universal Docker containers.
- [ ] **Phase 5:** CD Integration - AI-assisted monitoring for Canary and Blue/Green deployments.

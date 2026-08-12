# azure-devops-labs
30 to 60-Day Cloud &amp; DevOps Sprint: Hands-on automation, Infrastructure as Code (IaC), and CI/CD pipelines using Python, Bash, Azure, Terraform, and GitHub Actions.

# Day 1: Azure Status & Health Monitor

## Overview
A lightweight Python automation script that tests outbound connectivity to Azure endpoints, tracks system UTC execution time, and outputs formatted JSON diagnostic logs.

## Concepts Covered
* Standard Python libraries (`urllib.request`, `json`, `datetime`, `sys`)
* HTTP status codes & network timeout handling
* JSON reporting structure for automation pipelines

## How to Run
```bash
python3 app.py
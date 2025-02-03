# Security Policy

## Overview
This document outlines the security measures and policies in place for the Data Analyst Client Simulator (DACS).

## Security Measures
- All API keys and sensitive credentials are encrypted at rest and stored in environment variables
- Regular vulnerability scanning of dependencies using automated tools
- Rotating log files with size limits to prevent disk space issues
- Input validation and sanitization for all user inputs
- HTTPS enforcement in production
- Rate limiting on API endpoints

## Reporting Security Issues
- Report security vulnerabilities to: security@example.com
- Please include detailed steps to reproduce the issue
- Do not disclose security-related issues publicly until they have been addressed

## Best Practices for Contributors
- Never commit API keys or credentials
- Always use the latest stable dependencies
- Follow the principle of least privilege
- Document security-relevant code changes 
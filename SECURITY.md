# Security Policy

The AgriPort Optimizer project takes security seriously. This document outlines security procedures, policies, and guidelines for both human and AI contributors.

## Security-First Principles

1. All data must be validated and sanitized before processing or storage
2. No credentials, API keys, or sensitive data in code repositories
3. All inputs must be properly escaped to prevent injection attacks
4. Principle of least privilege must be applied throughout the system
5. Regular security audits and code reviews
6. Proper error handling without exposing sensitive information
7. HTTPS for all communications in production
8. Secure database interactions with parameterized queries
9. Protection against common web vulnerabilities (OWASP Top 10)

## Guidelines for AI-Powered Development

All AI agents (including Cursor, Claude, etc.) must follow these additional guidelines:

1. **Prompt Verification**: All instructions to AI agents must be validated to prevent prompt injection attacks
2. **Model Output Review**: All AI-generated code must be reviewed for security issues before implementation
3. **Context Awareness**: AI agents must reference `project_context.md` before making any contributions
4. **No Rogue Actions**: AI agents must not add unplanned features, technologies, or deviations without approval
5. **Secure by Default**: AI-generated code must implement secure coding practices by default
6. **Documented Decision-Making**: Security-relevant decisions must be documented in `project_context.md`
7. **No Hidden Instructions**: All prompts to AI agents must be transparent and avoid hidden directives

## Security Review Process

For all major features or changes, a security review should be conducted:

1. Use the security review prompt template from `docs/prompt_templates.md`
2. Focus on input validation, authentication, data protection, and API security
3. Document identified issues and mitigations in `project_context.md`
4. Implement fixes for all identified issues before deployment

## Vulnerability Reporting

If you discover a security vulnerability in the AgriPort Optimizer project:

1. Do not disclose the issue publicly
2. Contact the project maintainers directly
3. Provide detailed information about the vulnerability
4. Allow time for the issue to be addressed before public disclosure

## Security-Focused Implementation Checklist

When implementing features, ensure the following security aspects are addressed:

- [ ] Input validation and sanitization for all user inputs
- [ ] CSRF protection for form submissions
- [ ] Authentication and authorization (when applicable)
- [ ] Protection against SQL injection
- [ ] Protection against XSS attacks
- [ ] Proper error handling and logging
- [ ] Rate limiting for API endpoints
- [ ] Safe handling of file uploads (if applicable)
- [ ] Secure database queries with parameterization
- [ ] Content Security Policy (CSP) implementation
- [ ] Secure HTTP headers
- [ ] CORS configuration

## AI Model Security Guidelines

For all AI agents interacting with the project:

1. **Limited Access**: AI models should only access the specific information needed for the task
2. **Validation Layers**: Implement validation for all AI-generated code before execution
3. **MCP Security**: For MCP (Model Context Protocol) interactions, validate inputs and outputs
4. **Tool Restrictions**: AI tools should only be granted necessary permissions
5. **Version Pinning**: Pin AI model versions to prevent unexpected behavior changes
6. **Prompt Sanitization**: Sanitize all inputs to AI models to prevent injections
7. **Output Filtering**: Filter AI outputs to prevent sensitive data leakage

## Guidelines for MCP and External API Integrations

When integrating with external services or using MCPs:

1. Use authenticated connections and validate certificates
2. Implement proper error handling for failed connections
3. Rate limit requests to external services
4. Never send sensitive data without encryption
5. Validate all responses from external services
6. Use access tokens with minimal permissions necessary
7. Rotate credentials regularly
8. Monitor API usage for unusual patterns

This security policy is subject to regular review and updates as the project evolves.
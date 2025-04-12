# AgriPort Optimizer - Project Context

## Project Overview
- **Name**: AgriPort Optimizer
- **Purpose**: A webapp for agricultural companies in Argentina to select the most cost-effective port for shipping, based on port charges, logistics costs (fuel, distance), and sea freight.
- **Vision**: Enable logistics managers to input costs, view a map of Argentina divided by optimal port regions, and export results. Initial version for single-user use, with potential for multi-user scaling.
- **Core Features**:
  - Input form for costs (port charges, sea freight, fuel price).
  - 100x100 grid analysis, assigning optimal ports based on total cost.
  - Interactive map with color-coded regions and gradients at boundaries.
  - CSV export of grid assignments.

## Roadmap Adherence
This project follows the **Ultimate Vibe Architecting Roadmap for AI-Powered Development**. All AI actions must:
- Align with the specified phase (Creative Ideation, Deep Knowledge Acquisition, Targeted Implementation, Integration).
- Reference this file before starting work.
- Avoid unapproved features, frameworks, or skipping steps.
- Confirm with the user for any deviations from the plan.

## Current State
- **Phase**: Initial project structure created. Ready to proceed with Phase 1 (Creative Ideation & Strategic Brainstorming).
- **Progress**:
  - Repository created with robust structure
  - Core files and directories established
  - Security policy and rules defined
  - Prompt templates for AI agent interactions created
  - Basic Flask application with routes, models, and utilities set up
  - Docker and docker-compose configurations added
- **Next Step**: Complete Phase 1 exploration and proceed to research query preparation.

## Key Decisions
- **Tech Stack**:
  - Backend: Flask, GeoPandas, OSRM.
  - Frontend: Folium (Leaflet.js), Bootstrap.
  - Database: PostgreSQL/PostGIS (ports table, optional distances).
  - Deployment: Docker, AWS ECS or GCP Cloud Run.
- **Data Handling**:
  - 100x100 grid (~10,000 points) for initial version.
  - Precompute distances, store in CSV initially.
  - No fuel price API; users input averages.
- **Scope**:
  - Single-user focus, no authentication yet.
  - Map performance prioritized (<5 seconds rendering).
- **Security**:
  - Input validation and sanitization
  - Secure database handling with parameterized queries
  - HTTPS in production
  - AI agent security guidelines established

## Product Requirement Document (PRD) Summary
- **Status**: To be created during Phase 2.

## Tickets
- **Status**: To be created during Phase 2.

## Project Structure
- **Created Files**:
  - `app/__init__.py` - Flask application factory
  - `app/routes.py` - API endpoints and view routes
  - `app/models.py` - Database models for ports and grid points
  - `app/utils/gis.py` - Geospatial utilities
  - `app/utils/routing.py` - OSRM integration
  - `app/utils/cost.py` - Cost calculation logic
  - `app/templates/index.html` - Main UI template
  - `app.py` - Application entry point
  - `requirements.txt` - Python dependencies
  - `Dockerfile` and `docker-compose.yml` - Containerization
  - `.cursor/rules` - AI agent guidelines
  - `SECURITY.md` - Security policy
  - `docs/prompt_templates.md` - Templates for AI interactions
- **Repository**: [AgriPort-Optimizer](https://github.com/KineticNexus/AgriPort-Optimizer)

## Challenges
- OSRM setup requires ~10 GB RAM for Argentina's OSM data.
- Map performance with 10,000+ polygons needs optimization.
- Fuel price data unavailable; relying on user inputs.
- Boundary gradient visualization may be computationally intensive.

## Last Updated
- **Date**: April 12, 2025
- **Changes**: Initial project structure created. Established robust foundation with Flask, PostgreSQL, and OSRM integration. Added security policies and AI agent guidelines.

## Instructions for AI
- Always read this file before starting work.
- Follow the roadmap phase and step relevant to the current task.
- Reference the active ticket and PRD.
- Do not add features or change technologies without user approval.
- Update this file after each session with new decisions, progress, and challenges.

## Security Guidelines
- Validate all inputs to prevent injection attacks.
- Implement proper error handling and logging.
- Use HTTPS for all production deployments.
- Follow secure coding practices.
- No sensitive data should be stored in code repositories.
- AI agents must follow the security policy in SECURITY.md.
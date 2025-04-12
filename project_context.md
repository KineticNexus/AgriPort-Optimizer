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
- **Phase**: Phase 1 (Creative Ideation & Strategic Brainstorming) initial setup.
- **Progress**:
  - Project repository created.
  - Master context file established.
  - Ready to proceed with Phase 1 exploration.
- **Next Step**: Complete Phase 1 exploration and proceed to research query preparation.

## Key Decisions
- **Tech Stack** (Proposed):
  - Backend: Flask, GeoPandas, OSRM.
  - Frontend: Folium (Leaflet.js), Bootstrap.
  - Database: PostgreSQL/PostGIS (ports table, optional distances).
  - Deployment: Docker, AWS ECS or GCP Cloud Run.
- **Data Handling** (Proposed):
  - 100x100 grid (~10,000 points) for initial version.
  - Precompute distances, store in CSV initially.
  - No fuel price API; users input averages.
- **Scope** (Proposed):
  - Single-user focus, no authentication yet.
  - Map performance prioritized (<5 seconds rendering).

## Product Requirement Document (PRD) Summary
- **Status**: To be created during Phase 2.

## Tickets
- **Status**: To be created during Phase 2.

## Project Structure
- **Planned Files**:
  - `app/routes.py` (Flask routes)
  - `utils/gis.py` (GeoPandas helpers)
  - `utils/routing.py` (OSRM queries)
  - `utils/cost.py` (cost calculations)
  - `templates/index.html` (UI)
  - `data/distances.csv` (precomputed distances)
  - `models.py` (SQLAlchemy models)
- **Repository**: [AgriPort-Optimizer](https://github.com/KineticNexus/AgriPort-Optimizer)

## Challenges
- OSRM setup requires ~10 GB RAM for Argentina's OSM data.
- Map performance with 10,000+ polygons needs optimization.
- Fuel price data unavailable; relying on user inputs.

## Last Updated
- **Date**: April 12, 2025
- **Changes**: Initial project context file created.

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
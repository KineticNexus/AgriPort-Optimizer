# AgriPort Optimizer

A webapp for agricultural companies in Argentina to select the most cost-effective port for shipping, based on port charges, logistics costs (fuel, distance), and sea freight.

## Project Status

This project is currently in the **Initial Development Phase**. We are following the Ultimate Vibe Architecting Roadmap for AI-Powered Development.

Current Phase: **Phase 1 - Creative Ideation & Strategic Brainstorming**

## Project Vision

AgriPort Optimizer aims to help logistics managers at agricultural companies in Argentina make better decisions about which ports to use for shipping their products. By analyzing port charges, road transportation costs, and sea freight costs, the application will identify the most cost-effective port for each location in Argentina.

### Core Features

- Input form for costs (port charges, sea freight, fuel price)
- 100x100 grid analysis, assigning optimal ports based on total cost
- Interactive map with color-coded regions and gradients at boundaries
- CSV export of grid assignments

## Development Roadmap

We are following the Ultimate Vibe Architecting Roadmap:

1. **Phase 1**: Creative Ideation & Strategic Brainstorming
   - Initial creative exploration
   - Research query preparation

2. **Phase 2**: Deep Knowledge Acquisition & Structured Planning
   - Comprehensive technical research
   - Product Requirement Document (PRD) creation
   - Ticket generation & project breakdown

3. **Phase 3**: Targeted Implementation (Per Ticket)
   - Pre-implementation research
   - Architecture & planning
   - Implementation
   - Testing
   - Code cleanup & optimization

4. **Phase 4**: Integration & Project Finalization
   - Integration testing
   - Documentation creation
   - Retrospective & future planning

## Getting Started (Coming Soon)

Development setup instructions will be added as the project progresses.

## Technical Stack (Proposed)

- **Backend**: Flask, GeoPandas, OSRM
- **Frontend**: Folium (Leaflet.js), Bootstrap
- **Database**: PostgreSQL with PostGIS
- **Deployment**: Docker, AWS ECS or GCP Cloud Run

## Project Structure

For details on project structure, current status, and next steps, please refer to the [project_context.md](./project_context.md) file.

## Contributing

All contributions to this project must follow the development guidelines outlined in the [.cursor/rules](./.cursor/rules) file and adhere to the project context defined in [project_context.md](./project_context.md).

## Security

This project follows security-first principles:
- All user inputs are validated and sanitized
- No sensitive data is stored in code repositories
- Proper error handling and logging is implemented
- HTTPS is used for all communications in production

## License

This project is licensed under the MIT License - see the LICENSE file for details.
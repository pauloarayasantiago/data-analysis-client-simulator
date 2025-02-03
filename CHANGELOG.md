# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.1] - 2024-01-25
### Added
- Added simple percentage indicator for generation progress
- Added smooth progress animation from 0% to 100%

### Changed
- Simplified UI with cleaner white theme
- Improved spacing and alignment throughout
- Enhanced readability with better typography
- Fixed overlapping elements
- Streamlined loading state display

### Removed
- Removed progress bar steps
- Removed dark mode styles
- Removed unnecessary CSS variables
- Removed complex animations and transitions

## [1.3.0] - 2024-01-25
### Added
- Added progress bar with step indicators for generation process
- Added progress step transitions and animations
- Added visual feedback for completed and active steps

### Changed
- Completely redesigned UI with clean white theme
- Simplified color palette and reduced visual complexity
- Updated typography and spacing for better readability
- Improved card layouts and button styles
- Enhanced table styles with lighter borders and hover states
- Refined overall visual hierarchy

### Removed
- Removed dark theme styles and related variables
- Removed complex gradients and shadows
- Removed unused CSS classes and variables

## [1.2.5] - 2024-01-25
### Added
- Added CSV download functionality with browser compatibility
- Added download button with icon in dataset card
- Added card actions section for utility buttons

### Changed
- Improved header layout with better vertical centering
- Adjusted main content positioning and spacing
- Enhanced action card width and alignment
- Updated card header layout to include actions
- Refined overall UI spacing and proportions
- Simplified scenario and CSV generation prompts for better reliability
- Made generation parameters consistent across the application
- Added separate timeout checking for CSV generation
- Added delays between retries to improve API stability
- Enhanced error handling and logging in client generator

## [1.2.4] - 2024-01-25
### Added
- Added vertical scrolling for dataset table with custom scrollbar styling
- Added max-height to table container to ensure scrollability
- Added backdrop filter and shadow to action card

### Changed
- Redesigned header layout to be centered in viewport (Google-style)
- Increased header height to 45vh for better visual balance
- Updated gradient positioning to center
- Adjusted main content positioning with negative margin for overlap effect
- Modified action card styling for better contrast

## [1.2.3] - 2024-01-25
### Added
- Added interactive table display for CSV data
- Added CSV parsing functionality with quote handling
- Added table styles with sticky headers and hover effects

### Changed
- Increased container width to 1200px for better readability
- Improved scenario text display with better typography and spacing
- Enhanced client output formatting with justified text and larger font size
- Updated responsive design for new table layout

## [1.2.2] - 2024-01-25
### Removed
- Removed generated files section from UI
- Removed file list display and animations
- Removed file handling from API response
- Removed unused file-related CSS styles

## [1.2.1] - 2024-01-25
### Added
- Added CSV data display in UI with monospace font styling
- Added new card section for displaying generated datasets
- Added animation for CSV data section

### Changed
- Updated Flask route to handle tuple return values
- Modified frontend to display both scenario and CSV data
- Enhanced error handling for data generation failures

## [1.2.0] - 2024-01-25
### Added
- Added synthetic CSV dataset generation based on scenarios
- Added CSV prompt template for data generation
- Added two-stage generation process (scenario + CSV)
- Added CSV display in UI
- Added type hints for tuple returns

### Changed
- Updated client generator to return both scenario and CSV
- Renamed scenario prompt variable for clarity
- Improved error handling for two-stage generation

## [1.1.4] - 2024-01-25
### Removed
- Removed process logs section from UI
- Removed related CSS styles for log output
- Removed log display logic from JavaScript

## [1.1.3] - 2024-01-25
### Fixed
- Fixed gRPC timeout issues in Gemini API calls
- Added retry mechanism for failed API calls
- Added proper timeout handling
- Improved error logging for API calls
- Added generation configuration parameters
- Added type hints to client generator

## [1.1.2] - 2024-01-25
### Fixed
- Fixed header height and spacing for better proportions
- Corrected main content width and padding
- Improved button alignment and dimensions
- Fixed spinner positioning in button
- Adjusted card margins and padding
- Improved text alignment in header
- Fixed dark mode background colors
- Improved content spacing in action card
- Added proper word wrapping for client output
- Fixed container width consistency
- Improved overall vertical rhythm
- Fixed flex layout for better content distribution

## [1.1.1] - 2024-01-25
### Fixed
- Fixed header alignment and centering
- Fixed container width and box-sizing issues
- Improved header height and vertical alignment
- Fixed button dimensions and spacing
- Adjusted main content width for better readability
- Fixed header subtitle alignment and margins
- Improved action card spacing and flex layout

## [1.1.0] - 2024-01-25
### Added
- Docker containerization support
- Robust logging system with rotation
- Comprehensive security policy
- Keepalog methodology implementation
- Modern UI/UX design system
- Interactive animations and transitions
- Responsive layout improvements
- Dark mode support
- Added CSS variables for consistent design system
  - Color system with primary, secondary, and gray scales
  - Typography system with Inter and JetBrains Mono fonts
  - Spacing system from 0.25rem to 6rem
  - Shadow system with 5 levels of elevation
- Added responsive breakpoints for mobile devices
- Added dark mode support with system preference detection
- Added loading spinner component with centered alignment
- Added error message component with icon and auto-dismiss
- Added gradient backgrounds to cards and buttons
- Added hover effects with radial gradients
- Added decorative lines and accents to cards
- Added custom scrollbar styling for log output
- Added staggered animations for file list items
- Added smooth transitions for all interactive elements
- Added header subtitle for better context
- Added descriptive text under each section
- Added file icon SVG in file list items
- Added theme-color meta tag for browser UI

### Changed
- Improved project structure with src/ directory
- Enhanced documentation
- Switched from Conda to venv for environment management
- Updated Python version requirement to 3.11.7
- Updated Flask version to 3.0.0
- Consolidated README files for better clarity
- Improved installation and usage instructions
- Redesigned user interface with modern aesthetics
- Enhanced user experience with better feedback and interactions
- Updated button styling:
  - Added gradient background
  - Increased padding and border radius
  - Added hover and active states
  - Improved loading state with centered spinner
  - Added minimum width of 200px
- Updated card styling:
  - Increased border radius to 1.5rem
  - Added hover effect with radial gradient
  - Added subtle border
  - Improved shadow depth
- Updated typography:
  - Increased font weights for better hierarchy
  - Added letter spacing to headings
  - Improved line heights for readability
- Updated layout:
  - Increased container max-width to 1400px
  - Added more padding to header
  - Improved spacing between elements
- Updated animations:
  - Changed to cubic-bezier timing function
  - Added staggered delays for list items
  - Improved fade-in animation
- Updated dark mode:
  - Added custom surface color
  - Improved contrast ratios
  - Added gradient overlays
  - Adjusted shadow intensity

### Removed
- Removed redundant README-paulo.md
- Removed unused environment.yml and setup.sh files
- Removed one-time setup and cleanup scripts (setup.py, cleanup.py)

### Security
- Added security policy documentation
- Implemented secure logging practices
- Added API key encryption guidelines

### Fixed
- Corrected repository URLs in documentation
- Fixed application access URL in documentation
- Fixed loading spinner alignment in button
- Fixed dark mode color inconsistencies
- Fixed animation flickering issues
- Fixed mobile responsiveness issues
- Fixed card hover effect z-index
- Fixed file list item spacing
- Fixed error message stacking

## [1.0.0] - 2024-01-23
### Added
- Initial release
- Basic web UI for scenario generation
- Google Gemini API integration
- Dataset generation capabilities
- Environment management with conda
- Setup and cleanup scripts 
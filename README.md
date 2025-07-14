# Jira Project Manager 🚀

A beautiful and intuitive Streamlit application for managing and analyzing Jira projects with advanced analytics and export capabilities.

## Core Components

<pre class="font-ui border-border-100/50 overflow-x-scroll w-full rounded border-[0.5px] shadow-[0_2px_12px_hsl(var(--always-black)/5%)]"><table class="bg-bg-100 min-w-full border-separate border-spacing-0 text-sm leading-[1.88888] whitespace-normal"><thead class="border-b-border-100/50 border-b-[0.5px] text-left"><tr class="[tbody>&]:odd:bg-bg-500/10"><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] font-400 px-2 [&:not(:first-child)]:border-l-[0.5px]">Component</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] font-400 px-2 [&:not(:first-child)]:border-l-[0.5px]">Technology</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] font-400 px-2 [&:not(:first-child)]:border-l-[0.5px]">Description</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] font-400 px-2 [&:not(:first-child)]:border-l-[0.5px]">Key Features</th></tr></thead><tbody><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Jira Integration</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Jira Python Library</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Connects to Jira instance via API</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Authentication, issue fetching, JQL queries</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Data Processing</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Pandas</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Handles data manipulation and analysis</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">DataFrame operations, filtering, datetime handling</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>User Interface</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Streamlit</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Web application framework</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Sidebar config, main dashboard, responsive layout</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Visualization</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Plotly</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Interactive charts and analytics</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Pie charts, bar charts, metric cards</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Export System</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Pandas + OpenPyXL</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Data export functionality</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">CSV download, Excel with multiple sheets</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Styling Engine</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Custom CSS</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Visual theming and design</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Gradient backgrounds, status badges, responsive design</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Authentication</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">API Token</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Secure Jira connection</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Token-based auth, connection validation</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Filter System</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Streamlit Widgets</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Dynamic data filtering</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Multi-select dropdowns, real-time filtering</td></tr></tbody></table></pre>

## Features

### 🎯 Core Features

* **Real-time Jira Integration** : Connect directly to your Jira instance using API tokens
* **Interactive Dashboard** : Beautiful, responsive interface with gradient themes
* **Advanced Analytics** : Comprehensive charts and visualizations
* **Smart Filtering** : Multi-select filters for status, priority, and assignee
* **Export Capabilities** : Download data as CSV or Excel with summary sheets
* **Custom JQL Support** : Execute custom JQL queries for advanced filtering

### 📊 Analytics Dashboard

* **Status Distribution** : Pie chart showing issue distribution by status
* **Priority Analysis** : Bar chart displaying priority breakdown
* **Assignee Workload** : Horizontal bar chart of top assignees by issue count
* **Real-time Statistics** : Live metrics and percentages

### 🎨 UI/UX Features

* **Modern Design** : Gradient backgrounds and card-based layouts
* **Responsive Layout** : Works on desktop and mobile devices
* **Status Badges** : Color-coded badges for statuses and priorities
* **Interactive Charts** : Plotly-powered visualizations
* **Dark Theme** : Professional appearance with customizable styling

## Installation

### Prerequisites

* Python 3.7 or higher
* Jira account with API access
* Jira API token (generated from Atlassian account settings)

### Setup

1. **Clone or download the application**

   bash

   ```bash
   # Save the application as app.py
   ```
2. **Install required dependencies**

   bash

   ```bash
   pip install streamlit jira pandas plotly openpyxl
   ```
3. **Run the application**

   bash

   ```bash
   streamlit run app.py
   ```

## Configuration

### Jira API Token Setup

1. Go to [Atlassian Account Settings](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click "Create API token"
3. Give it a descriptive name (e.g., "Streamlit Jira Manager")
4. Copy the generated token (you won't be able to see it again)

### Application Settings

#### Connection Settings

* **Jira URL** : Your Jira instance URL (e.g., `https://yourcompany.atlassian.net`)
* **Email** : Your Jira account email address
* **API Token** : The token generated from Atlassian account settings

#### Query Settings

* **Project Key** : The key of your Jira project (e.g., `SPX`, `PROJ`, `DEV`)
* **Max Issues** : Maximum number of issues to fetch (5-500)

#### Advanced Options

* **Custom JQL** : Enable custom JQL queries for advanced filtering
* **Include Descriptions** : Toggle to include issue descriptions in the data
* **Show Charts** : Toggle analytics charts display

## Usage

### Basic Usage

<video src=
     "https://raw.githubusercontent.com/Akash-Gunasekar/Jira_Agent/main/Streamlit-Jir
     a-Demo.webm" controls loop autoplay muted></video>

1. **Configure Connection**
   * Enter your Jira URL, email, and API token in the sidebar
   * Specify the project key you want to analyze
2. **Fetch Issues**
   * Click the "🚀 Fetch Issues" button
   * Wait for the connection and data retrieval
3. **Analyze Data**
   * View the project overview metrics
   * Explore the analytics dashboard
   * Use filters to narrow down results
4. **Export Data**
   * Download filtered results as CSV or Excel
   * Excel export includes a summary sheet with key metrics

### Advanced Usage

#### Custom JQL Queries

Enable "Use custom JQL" in Advanced Options to write custom queries:

jql

```jql
# Examples:
project = SPX AND status = "In Progress" ORDER BY priority DESC
assignee = currentUser() AND created >= -30d
project = SPX AND priority in (High, Highest) AND status != Done
```

#### Filtering Options

* **Status Filter** : Multi-select filter for issue statuses
* **Priority Filter** : Filter by issue priorities
* **Assignee Filter** : Filter by assigned team members

## API Reference

### Jira Fields Retrieved

* **Key** : Issue key (e.g., SPX-123)
* **Summary** : Issue title/summary
* **Status** : Current status (To Do, In Progress, Done, etc.)
* **Assignee** : Person assigned to the issue
* **Reporter** : Person who created the issue
* **Priority** : Issue priority level
* **Issue Type** : Type of issue (Story, Bug, Task, etc.)
* **Created** : Creation timestamp
* **Updated** : Last update timestamp
* **Description** : Issue description (optional)

### Status Badge Classes

* `status-todo`: Gray badge for To Do items
* `status-progress`: Blue badge for In Progress items
* `status-review`: Yellow badge for Review items
* `status-done`: Green badge for Done items
* `status-blocked`: Red badge for Blocked items

### Priority Badge Classes

* `priority-highest`: Red badge for Highest priority
* `priority-high`: Orange badge for High priority
* `priority-medium`: Yellow badge for Medium priority
* `priority-low`: Teal badge for Low priority
* `priority-lowest`: Purple badge for Lowest priority

## Troubleshooting

### Common Issues

#### Authentication Errors

* **Check Jira URL format** : Must include `https://`
* **Verify email** : Use the email associated with your Jira account
* **Regenerate API token** : If token is old or compromised

#### Connection Issues

* **Network connectivity** : Ensure you can access Jira in your browser
* **Firewall settings** : Check if your network blocks the connection
* **Jira permissions** : Ensure you have access to the specified project

#### Data Issues

* **Empty results** : Check if the project key exists and you have access
* **Invalid JQL** : Verify your JQL syntax using Jira's query builder
* **Missing fields** : Some fields may be empty if not configured in Jira

### Error Messages

<pre class="font-ui border-border-100/50 overflow-x-scroll w-full rounded border-[0.5px] shadow-[0_2px_12px_hsl(var(--always-black)/5%)]"><table class="bg-bg-100 min-w-full border-separate border-spacing-0 text-sm leading-[1.88888] whitespace-normal"><thead class="border-b-border-100/50 border-b-[0.5px] text-left"><tr class="[tbody>&]:odd:bg-bg-500/10"><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] font-400 px-2 [&:not(:first-child)]:border-l-[0.5px]">Error</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] font-400 px-2 [&:not(:first-child)]:border-l-[0.5px]">Solution</th></tr></thead><tbody><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">"Please fill in all required fields!"</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Ensure Jira URL, email, API token, and project key are provided</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">"No issues found matching your criteria"</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Check project key and JQL query</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">"Failed to fetch issues"</td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">Verify connection settings and permissions</td></tr></tbody></table></pre>

## Dependencies

txt

```txt
streamlit>=1.28.0
jira>=3.5.0
pandas>=1.5.0
plotly>=5.15.0
openpyxl>=3.1.0
```

## File Structure

```
jira-project-manager/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .streamlit/
    └── config.toml       # Streamlit configuration (optional)
```

## Support

For support and questions:

* Check the troubleshooting section above
* Review Jira API documentation
* Check Streamlit documentation for UI issues

## Changelog

### Version 1.0.0

* Initial release with core functionality
* Jira integration and authentication
* Basic analytics dashboard
* CSV/Excel export capabilities
* Custom JQL support
* Responsive design with gradient themes

---

**Made with ❤️ using Streamlit and Jira API**

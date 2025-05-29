
import streamlit as st
from jira import JIRA
import pandas as pd
import io
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import base64

# Page configuration
st.set_page_config(
    page_title="Jira Project Manager",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for colorful theme
st.markdown(
    """
<style>
    /* Main background gradient */
    .main {
        background: #ffffff;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2C3E50 0%, #34495E 100%);
    }
    
    /* Custom card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .metric-card h3 {
        margin: 0;
        font-size: 2rem;
        font-weight: bold;
    }
    
    .metric-card p {
        margin: 0;
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    /* Status badges */
    .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        color: white;
        display: inline-block;
        margin: 0.1rem;
    }
    
    .status-todo { background-color: #6c757d; }
    .status-progress { background-color: #007bff; }
    .status-review { background-color: #ffc107; color: #000; }
    .status-done { background-color: #28a745; }
    .status-blocked { background-color: #dc3545; }
    
    /* Priority badges */
    .priority-highest { background-color: #dc3545; }
    .priority-high { background-color: #fd7e14; }
    .priority-medium { background-color: #ffc107; color: #000; }
    .priority-low { background-color: #20c997; }
    .priority-lowest { background-color: #6f42c1; }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar header */
    .sidebar-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Download button special styling */
    .download-btn {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .download-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Success/Error message styling */
    .stSuccess {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        border-radius: 10px;
    }
    
    .stError {
        background: linear-gradient(135deg, #dc3545 0%, #fd7e14 100%);
        border-radius: 10px;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #17a2b8 0%, #6f42c1 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    /* Chart container */
    .chart-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Helper functions
def get_status_class(status):
    status_lower = status.lower()
    if "done" in status_lower or "resolved" in status_lower:
        return "status-done"
    elif "progress" in status_lower:
        return "status-progress"
    elif "review" in status_lower:
        return "status-review"
    elif "blocked" in status_lower:
        return "status-blocked"
    else:
        return "status-todo"


def get_priority_class(priority):
    priority_lower = priority.lower()
    if "highest" in priority_lower:
        return "priority-highest"
    elif "high" in priority_lower:
        return "priority-high"
    elif "medium" in priority_lower:
        return "priority-medium"
    elif "low" in priority_lower:
        return "priority-low"
    else:
        return "priority-lowest"


def create_metric_card(title, value, subtitle=""):
    return f"""
    <div class="metric-card">
        <h3>{value}</h3>
        <p>{title}</p>
        {f"<small>{subtitle}</small>" if subtitle else ""}
    </div>
    """


# Sidebar configuration
with st.sidebar:
    st.markdown(
        """
    <div class="sidebar-header">
        <h2>🔐 Configuration</h2>
        <p>Connect to your Jira instance</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Connection settings
    st.subheader("🌐 Connection Settings")
    jira_url = st.text_input(
        "Jira URL",
        value="https://conceptvinesglobal.atlassian.net",
        help="Your Jira instance URL",
    )
    email = st.text_input(
        "Email", value="akashg@conceptvines.com", help="Your Jira account email"
    )
    api_token = st.text_input(
        "API Token", type="password", help="Generate from Atlassian account settings"
    )

    st.divider()

    # Query settings
    st.subheader("🔍 Query Settings")
    project_key = st.text_input(
        "Project Key", value="SPX", help="The key of your Jira project"
    )
    max_results = st.slider(
        "Max Issues",
        min_value=5,
        max_value=500,
        value=50,
        help="Maximum number of issues to fetch",
    )

    # Advanced options
    with st.expander("⚙️ Advanced Options"):
        use_custom_jql = st.checkbox("Use custom JQL")
        if use_custom_jql:
            jql_query = st.text_area(
                "JQL Query",
                value=f"project = {project_key} ORDER BY created DESC",
                help="Custom JQL query for advanced filtering",
            )
        else:
            jql_query = f"project = {project_key} ORDER BY created DESC"

        include_description = st.checkbox("Include descriptions", value=True)
        show_charts = st.checkbox("Show analytics charts", value=True)

    st.divider()

    # Fetch button
    fetch_button = st.button("🚀 Fetch Issues", use_container_width=True)

# Main content area
if fetch_button:
    if not all([jira_url, email, api_token, project_key]):
        st.error("❌ Please fill in all required fields!")
    else:
        try:
            with st.spinner("🔄 Connecting to Jira and fetching issues..."):
                # Connect to Jira
                jira = JIRA(server=jira_url, basic_auth=(email, api_token))

                # Test connection
                current_user = jira.current_user()
                st.success(f"✅ Connected successfully as {current_user}")

                # Fetch issues
                issues = jira.search_issues(
                    jql_query, maxResults=max_results, expand="changelog"
                )

                if not issues:
                    st.warning("⚠️ No issues found matching your criteria.")
                else:
                    # Convert issues to DataFrame
                    data = []
                    for issue in issues:
                        f = issue.fields
                        issue_data = {
                            "Key": issue.key,
                            "Summary": f.summary,
                            "Status": f.status.name,
                            "Assignee": f.assignee.displayName
                            if f.assignee
                            else "Unassigned",
                            "Reporter": f.reporter.displayName
                            if f.reporter
                            else "Unknown",
                            "Priority": f.priority.name if f.priority else "None",
                            "Issue Type": f.issuetype.name,
                            "Created": f.created,
                            "Updated": f.updated,
                        }

                        if include_description:
                            issue_data["Description"] = (
                                f.description or "No description"
                            )

                        data.append(issue_data)

                    df = pd.DataFrame(data)

                    # Convert datetime columns
                    df["Created"] = pd.to_datetime(df["Created"]).dt.strftime(
                        "%Y-%m-%d %H:%M"
                    )
                    df["Updated"] = pd.to_datetime(df["Updated"]).dt.strftime(
                        "%Y-%m-%d %H:%M"
                    )

                    # Display metrics
                    st.subheader("📊 Project Overview")

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.markdown(
                            create_metric_card(
                                "Total Issues", len(df), f"Project: {project_key}"
                            ),
                            unsafe_allow_html=True,
                        )

                    with col2:
                        assignees = df["Assignee"].nunique()
                        st.markdown(
                            create_metric_card(
                                "Team Members", assignees, "Active assignees"
                            ),
                            unsafe_allow_html=True,
                        )

                    with col3:
                        issue_types = df["Issue Type"].nunique()
                        st.markdown(
                            create_metric_card(
                                "Issue Types", issue_types, "Different types"
                            ),
                            unsafe_allow_html=True,
                        )

                    with col4:
                        statuses = df["Status"].nunique()
                        st.markdown(
                            create_metric_card(
                                "Statuses", statuses, "Different statuses"
                            ),
                            unsafe_allow_html=True,
                        )

                    # Charts section
                    if show_charts:
                        st.subheader("📈 Analytics Dashboard")

                        chart_col1, chart_col2 = st.columns(2)

                        with chart_col1:
                            # Status distribution
                            status_counts = df["Status"].value_counts()
                            fig_status = px.pie(
                                values=status_counts.values,
                                names=status_counts.index,
                                title="Issues by Status",
                                color_discrete_sequence=px.colors.qualitative.Set3,
                            )
                            fig_status.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                paper_bgcolor="rgba(0,0,0,0)",
                                font=dict(color="white"),
                            )
                            st.plotly_chart(fig_status, use_container_width=True)

                        with chart_col2:
                            # Priority distribution
                            priority_counts = df["Priority"].value_counts()
                            fig_priority = px.bar(
                                x=priority_counts.index,
                                y=priority_counts.values,
                                title="Issues by Priority",
                                color=priority_counts.values,
                                color_continuous_scale="Viridis",
                            )
                            fig_priority.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                paper_bgcolor="rgba(0,0,0,0)",
                                font=dict(color="white"),
                                xaxis=dict(title="Priority"),
                                yaxis=dict(title="Count"),
                            )
                            st.plotly_chart(fig_priority, use_container_width=True)

                        # Assignee workload
                        assignee_counts = df["Assignee"].value_counts().head(10)
                        if len(assignee_counts) > 0:
                            fig_assignee = px.bar(
                                x=assignee_counts.values,
                                y=assignee_counts.index,
                                orientation="h",
                                title="Top 10 Assignees by Issue Count",
                                color=assignee_counts.values,
                                color_continuous_scale="Blues",
                            )

                            fig_assignee.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                paper_bgcolor="rgba(0,0,0,0)",
                                font=dict(color="white"),
                                xaxis=dict(title="Number of Issues"),
                                yaxis=dict(title="Assignee"),
                            )
                            st.plotly_chart(fig_assignee, use_container_width=True)

                    # Issues table
                    st.subheader(f"📋 Issues from Project `{project_key}`")

                    # Add filters
                    filter_col1, filter_col2, filter_col3 = st.columns(3)

                    with filter_col1:
                        status_filter = st.multiselect(
                            "Filter by Status",
                            options=df["Status"].unique(),
                            default=df["Status"].unique(),
                        )

                    with filter_col2:
                        priority_filter = st.multiselect(
                            "Filter by Priority",
                            options=df["Priority"].unique(),
                            default=df["Priority"].unique(),
                        )

                    with filter_col3:
                        assignee_filter = st.multiselect(
                            "Filter by Assignee",
                            options=df["Assignee"].unique(),
                            default=df["Assignee"].unique(),
                        )

                    # Apply filters
                    filtered_df = df[
                        (df["Status"].isin(status_filter))
                        & (df["Priority"].isin(priority_filter))
                        & (df["Assignee"].isin(assignee_filter))
                    ]

                    # Display filtered table
                    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

                    # Download section
                    st.subheader("💾 Export Data")

                    download_col1, download_col2 = st.columns(2)

                    with download_col1:
                        # CSV download
                        csv_buffer = io.StringIO()
                        filtered_df.to_csv(csv_buffer, index=False)
                        csv_data = csv_buffer.getvalue().encode("utf-8")

                        st.download_button(
                            label="📥 Download as CSV",
                            data=csv_data,
                            file_name=f"{project_key}_jira_issues_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv",
                            use_container_width=True,
                        )

                    with download_col2:
                        # Excel download
                        excel_buffer = io.BytesIO()
                        with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
                            filtered_df.to_excel(
                                writer, sheet_name="Issues", index=False
                            )

                            # Add summary sheet
                            summary_data = {
                                "Metric": [
                                    "Total Issues",
                                    "Unique Assignees",
                                    "Issue Types",
                                    "Statuses",
                                ],
                                "Count": [
                                    len(filtered_df),
                                    filtered_df["Assignee"].nunique(),
                                    filtered_df["Issue Type"].nunique(),
                                    filtered_df["Status"].nunique(),
                                ],
                            }
                            summary_df = pd.DataFrame(summary_data)
                            summary_df.to_excel(
                                writer, sheet_name="Summary", index=False
                            )

                        excel_data = excel_buffer.getvalue()

                        st.download_button(
                            label="📊 Download as Excel",
                            data=excel_data,
                            file_name=f"{project_key}_jira_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True,
                        )

                    # Summary statistics
                    with st.expander("📈 Detailed Statistics"):
                        stat_col1, stat_col2 = st.columns(2)

                        with stat_col1:
                            st.write("**Status Distribution:**")
                            status_stats = filtered_df["Status"].value_counts()
                            for status, count in status_stats.items():
                                percentage = (count / len(filtered_df)) * 100
                                st.write(f"• {status}: {count} ({percentage:.1f}%)")

                        with stat_col2:
                            st.write("**Priority Distribution:**")
                            priority_stats = filtered_df["Priority"].value_counts()
                            for priority, count in priority_stats.items():
                                percentage = (count / len(filtered_df)) * 100
                                st.write(f"• {priority}: {count} ({percentage:.1f}%)")

                    # Ensure both df and filtered_df have datetime type for 'Updated'
                    df["Updated"] = pd.to_datetime(df["Updated"], errors="coerce")
                    filtered_df["Updated"] = pd.to_datetime(
                        filtered_df["Updated"], errors="coerce"
                    )

                    # Now safely get the most recently updated issues
                    recent_df = filtered_df.nlargest(5, "Updated")[
                        ["Key", "Summary", "Status", "Updated"]
                    ]

                    st.dataframe(recent_df, use_container_width=True, hide_index=True)

        except Exception as e:
            st.error(f"❌ Failed to fetch issues: {str(e)}")
            st.info("💡 **Troubleshooting Tips:**")
            st.write("• Check your Jira URL format (should include https://)")
            st.write("• Verify your email and API token are correct")
            st.write("• Ensure the project key exists and you have access")
            st.write("• Check your JQL syntax if using custom queries")

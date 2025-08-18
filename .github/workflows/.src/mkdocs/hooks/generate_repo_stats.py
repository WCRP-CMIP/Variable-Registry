
#!/usr/bin/env python3
"""
Repository statistics generator that creates a live stats page.
Uses gh CLI commands to extract actual repository data.
"""

import json
import subprocess
import sys
from datetime import datetime
import mkdocs_gen_files

class StatsGenerator:
    def __init__(self, repo_owner="WCRP-CMIP", repo_name="Variable-Registry"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.repo = f"{repo_owner}/{repo_name}"
        self.has_gh_cli = self.check_gh_cli()
        
    def check_gh_cli(self):
        """Check if GitHub CLI is available and authenticated."""
        try:
            result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ GitHub CLI authenticated successfully", file=sys.stderr)
                return True
            else:
                print("⚠️ GitHub CLI not authenticated", file=sys.stderr)
                return False
        except FileNotFoundError:
            print("⚠️ GitHub CLI not installed", file=sys.stderr)
            return False
        except Exception as e:
            print(f"⚠️ GitHub CLI check failed: {e}", file=sys.stderr)
            return False
    
    def run_gh_command(self, command):
        """Run a gh command and return JSON result."""
        if not self.has_gh_cli:
            return {}
            
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True,
                timeout=30  # Add timeout
            )
            return json.loads(result.stdout.strip()) if result.stdout.strip() else {}
        except (subprocess.CalledProcessError, json.JSONDecodeError, subprocess.TimeoutExpired) as e:
            print(f"⚠️ Command failed: {command}", file=sys.stderr)
            return {}
    
    def run_gh_command_text(self, command):
        """Run a gh command and return text result."""
        if not self.has_gh_cli:
            return ""
            
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True,
                timeout=30  # Add timeout
            )
            return result.stdout.strip()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return ""
    
    def get_repo_stats(self):
        """Get basic repository statistics."""
        return self.run_gh_command(f'gh repo view {self.repo} --json stargazerCount,forkCount,watchers,openIssues,createdAt,updatedAt,pushedAt,size,defaultBranchRef,licenseInfo,isPrivate,visibility')
    
    def get_contributors(self):
        """Get contributor information."""
        contributors = self.run_gh_command(f'gh api repos/{self.repo}/contributors --paginate')
        return contributors if isinstance(contributors, list) else []
    
    def get_languages(self):
        """Get programming languages."""
        return self.run_gh_command(f'gh api repos/{self.repo}/languages')
    
    def get_traffic_views(self):
        """Get traffic view statistics."""
        return self.run_gh_command(f'gh api repos/{self.repo}/traffic/views')
    
    def get_traffic_clones(self):
        """Get traffic clone statistics."""
        return self.run_gh_command(f'gh api repos/{self.repo}/traffic/clones')
    
    def get_popular_paths(self):
        """Get popular paths/files."""
        paths = self.run_gh_command(f'gh api repos/{self.repo}/traffic/popular/paths')
        return paths if isinstance(paths, list) else []
    
    def get_referrers(self):
        """Get referrer statistics."""
        referrers = self.run_gh_command(f'gh api repos/{self.repo}/traffic/popular/referrers')
        return referrers if isinstance(referrers, list) else []
    
    def get_releases(self):
        """Get release information."""
        releases = self.run_gh_command(f'gh api repos/{self.repo}/releases --paginate')
        return releases[:10] if isinstance(releases, list) else []
    
    def get_issue_stats(self):
        """Get issue and PR statistics."""
        if not self.has_gh_cli:
            return {'open_issues': 0, 'closed_issues': 0, 'open_prs': 0, 'closed_prs': 0}
            
        open_issues = self.run_gh_command_text(f'gh api search/issues -f q="repo:{self.repo} type:issue state:open" --jq ".total_count"')
        closed_issues = self.run_gh_command_text(f'gh api search/issues -f q="repo:{self.repo} type:issue state:closed" --jq ".total_count"')
        open_prs = self.run_gh_command_text(f'gh api search/issues -f q="repo:{self.repo} type:pr state:open" --jq ".total_count"')
        closed_prs = self.run_gh_command_text(f'gh api search/issues -f q="repo:{self.repo} type:pr state:closed" --jq ".total_count"')
        
        return {
            'open_issues': int(open_issues) if open_issues.isdigit() else 0,
            'closed_issues': int(closed_issues) if closed_issues.isdigit() else 0,
            'open_prs': int(open_prs) if open_prs.isdigit() else 0,
            'closed_prs': int(closed_prs) if closed_prs.isdigit() else 0
        }
    
    def create_fallback_page(self):
        """Create a fallback stats page when GitHub CLI is unavailable."""
        print("📝 Creating fallback stats page...", file=sys.stderr)
        
        fallback_content = """# :bar_chart: Repository Statistics

!!! warning "GitHub CLI Required"
    Live statistics require GitHub CLI authentication for data access.

## :gear: Setup Instructions

To enable live repository analytics:

### 1. Install GitHub CLI
```bash
# macOS
brew install gh

# Windows
winget install GitHub.cli

# Linux
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

### 2. Authenticate with GitHub
```bash
gh auth login
```

### 3. Rebuild Documentation
Once authenticated, rebuild your documentation and this page will automatically populate with:

---

## :chart_with_upwards_trend: Available Analytics

<div class="grid cards" markdown>

-   :material-star: **Repository Metrics**
    
    ---
    
    Stars, forks, watchers, and repository size

-   :material-eye: **Traffic Analytics**
    
    ---
    
    Page views, unique visitors, and popular content

-   :material-chart-line: **Activity Charts**
    
    ---
    
    Interactive commit timeline and code changes

-   :material-account-group: **Community Data**
    
    ---
    
    Contributor rankings and participation metrics

</div>

---

## :material-code-json: Technology Breakdown

When enabled, you'll see:

- Programming language distribution
- Code composition percentages  
- Repository structure analysis
- File type statistics

## :material-source-pull: Development Insights

Live tracking includes:

- Issue and pull request statistics
- Close/merge rates and trends
- Recent release timeline
- Project health indicators

## :material-chart-timeline: Interactive Features

- **Sortable tables** for all data lists
- **Interactive charts** powered by Plotly
- **Responsive design** for all screen sizes
- **Real-time updates** with each documentation build

---

*Configure GitHub CLI to unlock live repository analytics and interactive charts.*
"""
        
        with mkdocs_gen_files.open("auxilary/statistics.md", "w") as f:
            f.write(fallback_content)
        
        print("✅ Fallback stats page created", file=sys.stderr)
    
    def generate_stats_page(self):
        """Generate the statistics page with live data."""
        if not self.has_gh_cli:
            self.create_fallback_page()
            return
        
        print("🚀 Extracting live repository statistics...", file=sys.stderr)
        
        # Get current timestamp
        run_time = datetime.now().strftime('%Y-%m-%d at %H:%M:%S UTC')
        
        # Extract all statistics with progress reporting
        print("📊 Gathering repository metadata...", file=sys.stderr)
        repo_stats = self.get_repo_stats()
        
        print("👥 Gathering contributor data...", file=sys.stderr)
        contributors = self.get_contributors()
        
        print("💻 Analyzing programming languages...", file=sys.stderr)
        languages = self.get_languages()
        
        print("📈 Collecting traffic analytics...", file=sys.stderr)
        traffic_views = self.get_traffic_views()
        traffic_clones = self.get_traffic_clones()
        popular_paths = self.get_popular_paths()
        referrers = self.get_referrers()
        
        print("🚀 Gathering release information...", file=sys.stderr)
        releases = self.get_releases()
        
        print("🐛 Analyzing issue statistics...", file=sys.stderr)
        issue_stats = self.get_issue_stats()
        
        # Repository overview with safe fallbacks
        stars = repo_stats.get('stargazerCount', 0)
        forks = repo_stats.get('forkCount', 0)
        watchers = repo_stats.get('watchers', {}).get('totalCount', 0) if isinstance(repo_stats.get('watchers'), dict) else repo_stats.get('watchers', 0)
        open_issues = repo_stats.get('openIssues', 0)
        repo_size = repo_stats.get('size', 0) / 1024 if repo_stats.get('size') else 0  # Convert to MB
        default_branch = repo_stats.get('defaultBranchRef', {}).get('name', 'main') if repo_stats.get('defaultBranchRef') else 'main'
        last_push = repo_stats.get('pushedAt', '')[:10] if repo_stats.get('pushedAt') else 'Unknown'
        
        # Traffic statistics with safe fallbacks
        total_views = traffic_views.get('count', 0)
        unique_visitors = traffic_views.get('uniques', 0)
        total_clones = traffic_clones.get('count', 0)
        unique_cloners = traffic_clones.get('uniques', 0)
        
        # Calculate rates safely
        total_issues = issue_stats['open_issues'] + issue_stats['closed_issues']
        total_prs = issue_stats['open_prs'] + issue_stats['closed_prs']
        issue_close_rate = (issue_stats['closed_issues'] / total_issues * 100) if total_issues > 0 else 0
        pr_close_rate = (issue_stats['closed_prs'] / total_prs * 100) if total_prs > 0 else 0
        
        # Build the modern stats page
        content = f"""# :bar_chart: Repository Statistics

!!! success "Live Analytics Dashboard"
    **Last Updated:** {run_time} • **Source:** GitHub API • **Repository:** {self.repo}

---

## :rocket: Repository Overview

<div class="grid cards" markdown>

-   :material-star: **{stars:,} Stars**
    
    ---
    
    Community endorsements and popularity

-   :material-source-fork: **{forks:,} Forks**
    
    ---
    
    Development branches and contributions

-   :material-eye: **{watchers:,} Watchers**
    
    ---
    
    Users following project updates

-   :material-database: **{repo_size:.1f} MB**
    
    ---
    
    Repository storage size

</div>

### :information: Project Details

| :material-source-branch: Branch | :material-clock: Last Push | :material-alert-circle: Open Issues |
|:-------------------------------:|:---------------------------:|:-----------------------------------:|
| **{default_branch}** | **{last_push}** | **{open_issues:,}** |

---

## :chart_with_upwards_trend: Traffic & Engagement

### :globe_with_meridians: Visitor Analytics (Last 14 Days)

| :eyes: Page Views | :busts_in_silhouette: Unique Visitors | :arrow_down: Clones | :bust_in_silhouette: Unique Cloners |
|:-----------------:|:-------------------------------------:|:-------------------:|:-----------------------------------:|
| **{total_views:,}** | **{unique_visitors:,}** | **{total_clones:,}** | **{unique_cloners:,}** |

"""
        
        # Add popular files if available
        if popular_paths:
            content += """### :fire: Most Popular Content

| Rank | :material-file: Path | :eyes: Views | :busts_in_silhouette: Visitors |
|:----:|---------------------|:------------:|:-------------------------------:|
"""
            for i, path in enumerate(popular_paths[:10], 1):
                file_path = path.get('path', '')
                views = path.get('count', 0)
                uniques = path.get('uniques', 0)
                content += f"| **{i}** | `{file_path}` | **{views:,}** | **{uniques:,}** |\n"
            content += "\n"
        
        # Add traffic sources if available
        if referrers:
            content += """### :link: Traffic Sources

| Rank | :material-web: Source | :eyes: Views | :busts_in_silhouette: Visitors |
|:----:|----------------------|:------------:|:-------------------------------:|
"""
            for i, referrer in enumerate(referrers[:10], 1):
                source = referrer.get('referrer', 'Direct')
                views = referrer.get('count', 0)
                uniques = referrer.get('uniques', 0)
                content += f"| **{i}** | **{source}** | **{views:,}** | **{uniques:,}** |\n"
            content += "\n"
        
        content += "---\n\n"
        
        # Programming languages section
        if languages:
            total_bytes = sum(languages.values())
            content += """## :computer: Technology Profile

### :material-code-json: Programming Languages

<div class="grid cards" markdown>
"""
            # Get icon mapping for common languages
            lang_icons = {
                'Python': 'material-language-python',
                'JavaScript': 'material-language-javascript', 
                'TypeScript': 'material-language-typescript',
                'HTML': 'material-language-html5',
                'CSS': 'material-language-css3',
                'Java': 'material-language-java',
                'C++': 'material-language-cpp',
                'C': 'material-language-c',
                'Shell': 'material-console',
                'Dockerfile': 'material-docker',
                'YAML': 'material-file-code',
                'JSON': 'material-code-json',
                'Markdown': 'material-language-markdown'
            }
            
            # Add top 4 languages as cards
            sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)
            for lang, bytes_count in sorted_langs[:4]:
                percentage = (bytes_count / total_bytes * 100) if total_bytes > 0 else 0
                icon = lang_icons.get(lang, 'material-file-code')
                content += f"""
-   :{icon}: **{lang}**
    
    ---
    
    {percentage:.1f}% • {bytes_count:,} bytes
"""
            
            content += """
</div>

#### :material-chart-pie: Complete Language Breakdown

| Language | :material-database: Bytes | :material-percent: Percentage |
|----------|:-------------------------:|:-----------------------------:|
"""
            for lang, bytes_count in sorted_langs:
                percentage = (bytes_count / total_bytes * 100) if total_bytes > 0 else 0
                content += f"| **{lang}** | `{bytes_count:,}` | **{percentage:.1f}%** |\n"
            content += "\n---\n\n"
        
        # Issues and Pull Requests section
        content += f"""## :clipboard: Project Management

### :bug: Issues & Pull Requests Health

<div class="grid cards" markdown>

-   :material-alert-circle: **{issue_stats['open_issues']:,} Open Issues**
    
    ---
    
    Current problems and feature requests

-   :material-check-circle: **{issue_stats['closed_issues']:,} Closed Issues**
    
    ---
    
    {issue_close_rate:.1f}% close rate

-   :material-source-pull: **{issue_stats['open_prs']:,} Open PRs**
    
    ---
    
    Pending contributions under review

-   :material-check-all: **{issue_stats['closed_prs']:,} Merged PRs**
    
    ---
    
    {pr_close_rate:.1f}% merge rate

</div>

"""
        
        # Releases section
        if releases:
            content += f"""### :package: Recent Releases

!!! releases "Latest Versions • {len(releases)} Total Releases"

| :material-tag: Release | :material-source-branch: Tag | :material-calendar: Published |
|------------------------|:-----------------------------:|:-----------------------------:|
"""
            for release in releases:
                name = release.get('name') or release.get('tag_name', 'Unnamed')
                tag = release.get('tag_name', 'N/A')
                published = release.get('published_at', '')[:10] if release.get('published_at') else 'Unknown'
                content += f"| **{name}** | `{tag}` | **{published}** |\n"
            content += "\n"
        
        content += "---\n\n"
        
        # Contributors section
        content += f"""## :technologist: Community Recognition

### :trophy: Top Contributors

!!! success "Hall of Fame • {len(contributors)} Total Contributors"

| Rank | :material-account: Contributor | :material-source-commit: Contributions | :material-image: Avatar |
|:----:|-------------------------------|:--------------------------------------:|:-----------------------:|
"""
        
        # Add top 15 contributors with avatars
        for i, contributor in enumerate(contributors[:15], 1):
            username = contributor.get('login', 'Unknown')
            contributions = contributor.get('contributions', 0)
            avatar_url = contributor.get('avatar_url', '')
            avatar_html = f'<img src="{avatar_url}" width="32" height="32" style="border-radius: 50%; vertical-align: middle;" alt="{username}" loading="lazy">' if avatar_url else ':material-account-circle:'
            content += f"| **{i}** | **{username}** | **{contributions:,}** | {avatar_html} |\n"
        
        content += """
---

## :chart_increasing: Development Activity

### :calendar: Commit Timeline

!!! abstract "Weekly Development Rhythm"
    Interactive visualization of commit frequency over time.

<div id="commit-activity-chart" style="height:400px; width:100%;"></div>

### :chart_increasing: Code Evolution

!!! abstract "Lines Added vs Removed"
    Development intensity and code change patterns.

<div id="code-changes-chart" style="height:400px; width:100%;"></div>

---

## :information_source: Dashboard Information

!!! gear "Technical Details"
    
    === ":material-api: Data Sources"
        
        - **GitHub API**: Real-time repository metrics
        - **Traffic Data**: Visitor analytics and engagement
        - **Git History**: Commit and contribution analysis
        - **Community Data**: Contributor and issue tracking
    
    === ":material-refresh: Update Process"
        
        - **Frequency**: Every documentation build
        - **Method**: GitHub CLI with authenticated API access
        - **Latency**: < 1 minute (real-time)
        - **Scope**: All public repository data + traffic (requires push access)
    
    === ":material-chart-timeline: Interactive Features"
        
        - **Live Charts**: Plotly-powered visualizations
        - **Sortable Tables**: Click headers to sort data
        - **Responsive Cards**: Adaptive layout for all devices
        - **Progressive Loading**: Graceful degradation without GitHub CLI

"""
        
        # Ensure assets directory exists for charts
        try:
            with mkdocs_gen_files.open("assets/.gitkeep", "w") as f:
                f.write("# Generated assets directory\n")
        except Exception as e:
            print(f"⚠️ Could not create assets directory: {e}", file=sys.stderr)
        
        # Write the complete stats page to auxilary directory (override template)
        # Use statistics.md to match Variable-Registry naming convention
        with mkdocs_gen_files.open("auxilary/statistics.md", "w") as f:
            f.write(content)
        
        print("✅ Generated live statistics page (overwrote template placeholder)", file=sys.stderr)
        
        # Add interactive charts
        self.add_interactive_charts()
        
        print(f"✅ Live repository statistics generated!", file=sys.stderr)
        print(f"📊 {len(contributors)} contributors • 👁️ {total_views:,} views • ⭐ {stars:,} stars", file=sys.stderr)

    def add_interactive_charts(self):
        """Add interactive charts for commit activity and code frequency."""
        try:
            # Commit activity chart
            print("📈 Generating commit activity chart...", file=sys.stderr)
            commit_activity = self.run_gh_command(f'gh api repos/{self.repo}/stats/commit_activity')
            
            if commit_activity and isinstance(commit_activity, list) and len(commit_activity) > 0:
                weeks = []
                commits = []
                
                for week_data in commit_activity[-52:]:  # Last 52 weeks
                    if 'week' in week_data and 'total' in week_data:
                        week_timestamp = week_data['week']
                        week_date = datetime.fromtimestamp(week_timestamp).strftime('%Y-%m-%d')
                        weeks.append(week_date)
                        commits.append(week_data['total'])
                
                if weeks and commits:
                    chart_data = {
                        "data": [{
                            "type": "scatter",
                            "mode": "lines+markers",
                            "x": weeks,
                            "y": commits,
                            "name": "Weekly Commits",
                            "line": {"color": "rgb(29, 78, 216)", "width": 3},
                            "marker": {"size": 6, "color": "rgb(29, 78, 216)"},
                            "hovertemplate": "Week: %{x}<br>Commits: %{y}<extra></extra>"
                        }],
                        "layout": {
                            "title": {"text": "Weekly Commit Activity", "font": {"size": 18}},
                            "xaxis": {"title": "Week", "tickangle": 45},
                            "yaxis": {"title": "Number of Commits"},
                            "margin": {"l": 60, "r": 40, "t": 60, "b": 100},
                            "height": 400,
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)"
                        }
                    }
                    
                    with mkdocs_gen_files.open("assets/commits_time_series.json", "w") as f:
                        f.write(json.dumps(chart_data, indent=2))
                    
                    print("✅ Created commit activity chart data", file=sys.stderr)
            
            # Code frequency chart
            print("📊 Generating code frequency chart...", file=sys.stderr)
            code_frequency = self.run_gh_command(f'gh api repos/{self.repo}/stats/code_frequency')
            
            if code_frequency and isinstance(code_frequency, list) and len(code_frequency) > 0:
                weeks = []
                additions = []
                deletions = []
                
                for week_data in code_frequency[-52:]:  # Last 52 weeks
                    if len(week_data) >= 3:
                        week_timestamp = week_data[0]
                        week_date = datetime.fromtimestamp(week_timestamp).strftime('%Y-%m-%d')
                        weeks.append(week_date)
                        additions.append(week_data[1])
                        deletions.append(-week_data[2])  # Make positive for display
                
                if weeks and additions and deletions:
                    chart_data = {
                        "data": [
                            {
                                "type": "bar",
                                "x": weeks,
                                "y": additions,
                                "name": "Lines Added",
                                "marker": {"color": "rgb(34, 197, 94)"},
                                "hovertemplate": "Week: %{x}<br>Added: %{y} lines<extra></extra>"
                            },
                            {
                                "type": "bar",
                                "x": weeks,
                                "y": deletions,
                                "name": "Lines Removed",
                                "marker": {"color": "rgb(239, 68, 68)"},
                                "hovertemplate": "Week: %{x}<br>Removed: %{y} lines<extra></extra>"
                            }
                        ],
                        "layout": {
                            "title": {"text": "Weekly Code Changes", "font": {"size": 18}},
                            "xaxis": {"title": "Week", "tickangle": 45},
                            "yaxis": {"title": "Lines of Code"},
                            "barmode": "group",
                            "margin": {"l": 60, "r": 40, "t": 60, "b": 100},
                            "height": 400,
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)"
                        }
                    }
                    
                    with mkdocs_gen_files.open("assets/code_frequency.json", "w") as f:
                        f.write(json.dumps(chart_data, indent=2))
                    
                    print("✅ Created code frequency chart data", file=sys.stderr)
            
            # Add chart loading JavaScript to the stats page
            chart_script = '''

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Load commit activity chart
    if (typeof Plotly !== 'undefined') {
        fetch('../../assets/commits_time_series.json')
            .then(response => response.json())
            .then(data => {
                Plotly.newPlot('commit-activity-chart', data.data, data.layout, {
                    responsive: true,
                    displayModeBar: false
                });
            })
            .catch(error => {
                console.warn('Commit activity chart data not available:', error);
                const element = document.getElementById('commit-activity-chart');
                if (element) {
                    element.innerHTML = '<div style="display: flex; align-items: center; justify-content: center; height: 100%; color: var(--md-default-fg-color--light); font-style: italic;">Commit data not available</div>';
                }
            });
        
        // Load code frequency chart
        fetch('../../assets/code_frequency.json')
            .then(response => response.json())
            .then(data => {
                Plotly.newPlot('code-changes-chart', data.data, data.layout, {
                    responsive: true,
                    displayModeBar: false
                });
            })
            .catch(error => {
                console.warn('Code frequency chart data not available:', error);
                const element = document.getElementById('code-changes-chart');
                if (element) {
                    element.innerHTML = '<div style="display: flex; align-items: center; justify-content: center; height: 100%; color: var(--md-default-fg-color--light); font-style: italic;">Code frequency data not available</div>';
                }
            });
    } else {
        console.warn('Plotly not loaded - charts will not display');
    }
});
</script>'''
            
            # Append the JavaScript to the stats page
            with mkdocs_gen_files.open("auxilary/statistics.md", "a") as f:
                f.write(chart_script)
            
        except Exception as e:
            print(f"⚠️ Error generating interactive charts: {e}", file=sys.stderr)

# Main execution with better error handling
def main():
    try:
        print("🚀 Starting repository statistics generation...", file=sys.stderr)
        generator = StatsGenerator()
        generator.generate_stats_page()
        print("✅ Repository statistics generation completed successfully!", file=sys.stderr)
    except Exception as e:
        print(f"❌ Critical error in statistics generation: {e}", file=sys.stderr)
        
        # Always create a fallback page so something appears
        try:
            fallback_content = """# :bar_chart: Repository Statistics

!!! error "Statistics Generation Failed"
    There was an error generating live statistics. This is likely due to GitHub CLI configuration.

## :gear: Troubleshooting

### Common Issues

1. **GitHub CLI not installed**
   ```bash
   brew install gh  # macOS
   ```

2. **Not authenticated**
   ```bash
   gh auth login
   ```

3. **Repository access permissions**
   - Ensure you have read access to the repository
   - For private repos, ensure proper authentication

4. **Network connectivity**
   - Check internet connection
   - Verify GitHub API accessibility

## :chart_with_upwards_trend: Expected Features

When working properly, this page displays:

- **Repository metrics**: Stars, forks, watchers, size
- **Traffic analytics**: Views, visitors, popular content
- **Interactive charts**: Commit timeline and code changes
- **Community data**: Contributors and participation
- **Technology profile**: Programming language breakdown
- **Project health**: Issues, PRs, and release history

---

*Fix GitHub CLI configuration and rebuild to see live statistics.*
"""
            
            import mkdocs_gen_files
            with mkdocs_gen_files.open("auxilary/statistics.md", "w") as f:
                f.write(fallback_content)
            
            print("✅ Created error fallback stats page", file=sys.stderr)
            
        except Exception as fallback_error:
            print(f"❌ Could not create fallback stats page: {fallback_error}", file=sys.stderr)

# Only run if this is the main execution (not template processing)
if __name__ == "__main__":
    main()
else:
    # When run as gen-files script, execute main function
    main()



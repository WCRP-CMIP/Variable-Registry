
#!/usr/bin/env python3
"""
Repository statistics generator that creates a comprehensive stats page.
Uses gh CLI to fetch real GitHub data and combines with local repository analysis.
"""

import json
import subprocess
import sys
import os
from datetime import datetime
from pathlib import Path
import mkdocs_gen_files

class StatsGenerator:
    def __init__(self, repo_owner="WCRP-CMIP", repo_name="Variable-Registry"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.repo = f"{repo_owner}/{repo_name}"
        
    def run_gh_command(self, command):
        """Run a gh command and return JSON result."""
        try:
            print(f"🔄 Running: {command}", file=sys.stderr)
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True,
                timeout=30
            )
            if result.stdout.strip():
                return json.loads(result.stdout.strip())
            return {}
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Command failed: {command}", file=sys.stderr)
            print(f"⚠️ Error: {e.stderr}", file=sys.stderr)
            return {}
        except json.JSONDecodeError as e:
            print(f"⚠️ JSON decode error for command: {command}", file=sys.stderr)
            return {}
        except subprocess.TimeoutExpired:
            print(f"⚠️ Command timed out: {command}", file=sys.stderr)
            return {}
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}", file=sys.stderr)
            return {}
    
    def run_gh_command_text(self, command):
        """Run a gh command and return text result."""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True,
                timeout=30
            )
            return result.stdout.strip()
        except:
            return ""
    
    def get_repo_stats(self):
        """Get basic repository statistics."""
        return self.run_gh_command(
            f'gh repo view {self.repo} --json stargazerCount,forkCount,watchers,openIssues,createdAt,updatedAt,pushedAt,size,defaultBranchRef,licenseInfo,isPrivate,visibility,description'
        )
    
    def get_contributors(self):
        """Get contributor information."""
        contributors = self.run_gh_command(f'gh api repos/{self.repo}/contributors --paginate')
        return contributors if isinstance(contributors, list) else []
    
    def get_languages(self):
        """Get programming languages."""
        return self.run_gh_command(f'gh api repos/{self.repo}/languages')
    
    def get_releases(self):
        """Get release information."""
        releases = self.run_gh_command(f'gh api repos/{self.repo}/releases')
        return releases[:10] if isinstance(releases, list) else []
    
    def get_issue_stats(self):
        """Get issue and PR statistics."""
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
    
    def get_traffic_stats(self):
        """Get traffic statistics if available."""
        views = self.run_gh_command(f'gh api repos/{self.repo}/traffic/views')
        clones = self.run_gh_command(f'gh api repos/{self.repo}/traffic/clones')
        return {
            'views': views.get('count', 0) if views else 0,
            'unique_visitors': views.get('uniques', 0) if views else 0,
            'clones': clones.get('count', 0) if clones else 0,
            'unique_cloners': clones.get('uniques', 0) if clones else 0
        }
    
    def generate_stats_page(self):
        """Generate comprehensive statistics page with real data."""
        print("🚀 Generating comprehensive repository statistics...", file=sys.stderr)
        
        # Get current timestamp
        run_time = datetime.now().strftime('%Y-%m-%d at %H:%M:%S UTC')
        
        # Fetch all data
        print("📊 Fetching repository metadata...", file=sys.stderr)
        repo_stats = self.get_repo_stats()
        
        print("👥 Fetching contributor data...", file=sys.stderr)
        contributors = self.get_contributors()
        
        print("💻 Analyzing programming languages...", file=sys.stderr)
        languages = self.get_languages()
        
        print("🚀 Fetching release information...", file=sys.stderr)
        releases = self.get_releases()
        
        print("🐛 Analyzing issue statistics...", file=sys.stderr)
        issue_stats = self.get_issue_stats()
        
        print("📈 Fetching traffic data...", file=sys.stderr)
        traffic_stats = self.get_traffic_stats()
        
        # Process repository data
        stars = repo_stats.get('stargazerCount', 0)
        forks = repo_stats.get('forkCount', 0)
        watchers = repo_stats.get('watchers', {}).get('totalCount', 0) if isinstance(repo_stats.get('watchers'), dict) else repo_stats.get('watchers', 0)
        open_issues = repo_stats.get('openIssues', 0)
        repo_size = repo_stats.get('size', 0) / 1024 if repo_stats.get('size') else 0  # Convert to MB
        default_branch = repo_stats.get('defaultBranchRef', {}).get('name', 'main') if repo_stats.get('defaultBranchRef') else 'main'
        last_push = repo_stats.get('pushedAt', '')[:10] if repo_stats.get('pushedAt') else 'Unknown'
        created_date = repo_stats.get('createdAt', '')[:10] if repo_stats.get('createdAt') else 'Unknown'
        description = repo_stats.get('description', 'No description available')
        
        # Calculate rates
        total_issues = issue_stats['open_issues'] + issue_stats['closed_issues']
        total_prs = issue_stats['open_prs'] + issue_stats['closed_prs']
        issue_close_rate = (issue_stats['closed_issues'] / total_issues * 100) if total_issues > 0 else 0
        pr_close_rate = (issue_stats['closed_prs'] / total_prs * 100) if total_prs > 0 else 0
        
        # Build comprehensive stats page
        content = f"""# :bar_chart: Repository Statistics

!!! success "Live Repository Analytics"
    **Last Updated:** {run_time} • **Source:** GitHub API • **Repository:** [{self.repo}](https://github.com/{self.repo})

"""
        
        # Add description if available
        if description != 'No description available':
            content += f"""!!! quote "Repository Description"
    {description}

"""
        
        content += f"""---

## :rocket: Repository Overview

<div class="grid cards" markdown>

-   :material-star: **{stars:,} Stars**
    
    ---
    
    Community endorsements and bookmarks

-   :material-source-fork: **{forks:,} Forks**
    
    ---
    
    Independent development branches

-   :material-eye: **{watchers:,} Watchers**
    
    ---
    
    Users following project updates

-   :material-database: **{repo_size:.1f} MB**
    
    ---
    
    Total repository storage size

</div>

### :information: Project Metadata

| :material-source-branch: Default Branch | :material-clock: Last Push | :material-calendar: Created | :material-alert-circle: Open Issues |
|:----------------------------------------:|:---------------------------:|:---------------------------:|:-----------------------------------:|
| **{default_branch}** | **{last_push}** | **{created_date}** | **{open_issues:,}** |

---

## :chart_with_upwards_trend: Traffic & Engagement

### :globe_with_meridians: Repository Traffic (Last 14 Days)

| :eyes: Page Views | :busts_in_silhouette: Unique Visitors | :arrow_down: Clones | :bust_in_silhouette: Unique Cloners |
|:-----------------:|:-------------------------------------:|:-------------------:|:-----------------------------------:|
| **{traffic_stats['views']:,}** | **{traffic_stats['unique_visitors']:,}** | **{traffic_stats['clones']:,}** | **{traffic_stats['unique_cloners']:,}** |

---

## :computer: Technology Profile
"""

        # Programming languages section
        if languages:
            total_bytes = sum(languages.values())
            content += """
### :material-code-json: Programming Languages

<div class="grid cards" markdown>
"""
            # Language icon mapping
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
                'Markdown': 'material-language-markdown',
                'R': 'material-language-r',
                'Go': 'material-language-go'
            }
            
            # Show top 4 languages as cards
            sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)
            for lang, bytes_count in sorted_langs[:4]:
                percentage = (bytes_count / total_bytes * 100) if total_bytes > 0 else 0
                icon = lang_icons.get(lang, 'material-file-code')
                kb_count = bytes_count / 1024
                content += f"""
-   :{icon}: **{lang}**
    
    ---
    
    {percentage:.1f}% • {kb_count:,.0f} KB
"""
            
            content += """
</div>

#### :material-chart-pie: Complete Language Breakdown

| Language | :material-database: Size (KB) | :material-percent: Percentage |
|----------|:------------------------------:|:-----------------------------:|
"""
            for lang, bytes_count in sorted_langs:
                percentage = (bytes_count / total_bytes * 100) if total_bytes > 0 else 0
                kb_count = bytes_count / 1024
                content += f"| **{lang}** | `{kb_count:,.0f}` | **{percentage:.1f}%** |\n"
        else:
            content += """
### :material-help-circle: Programming Languages

No language data available - repository may be primarily data or documentation.
"""

        content += """

---

## :clipboard: Project Management

### :bug: Issues & Pull Requests Health

<div class="grid cards" markdown>

-   :material-alert-circle: **Open Issues**
    
    ---
    
"""
        content += f"    {issue_stats['open_issues']:,} active problems/requests\n"
        
        content += """
-   :material-check-circle: **Closed Issues**
    
    ---
    
"""
        content += f"    {issue_stats['closed_issues']:,} resolved ({issue_close_rate:.1f}% close rate)\n"
        
        content += """
-   :material-source-pull: **Open PRs**
    
    ---
    
"""
        content += f"    {issue_stats['open_prs']:,} pending contributions\n"
        
        content += """
-   :material-check-all: **Merged PRs**
    
    ---
    
"""
        content += f"    {issue_stats['closed_prs']:,} merged ({pr_close_rate:.1f}% merge rate)\n"
        
        content += """
</div>

"""

        # Releases section
        if releases:
            content += f"""### :package: Recent Releases

!!! releases "Version History • {len(releases)} Recent Releases"

| :material-tag: Release | :material-source-branch: Tag | :material-calendar: Published |
|------------------------|:-----------------------------:|:-----------------------------:|
"""
            for release in releases:
                name = release.get('name') or release.get('tag_name', 'Unnamed Release')
                tag = release.get('tag_name', 'N/A')
                published = release.get('published_at', '')[:10] if release.get('published_at') else 'Unknown'
                content += f"| **{name}** | `{tag}` | **{published}** |\n"
            content += "\n"

        content += """
---

## :technologist: Community & Contributors

"""
        
        if contributors:
            content += f"""### :trophy: Top Contributors

!!! success "Development Team • {len(contributors)} Total Contributors"

| Rank | :material-account: Contributor | :material-source-commit: Contributions | :material-link: Profile |
|:----:|-------------------------------|:--------------------------------------:|:----------------------:|
"""
            # Show top 15 contributors
            for i, contributor in enumerate(contributors[:15], 1):
                username = contributor.get('login', 'Unknown')
                contributions = contributor.get('contributions', 0)
                profile_url = f"https://github.com/{username}"
                content += f"| **{i}** | **{username}** | **{contributions:,}** | [:material-open-in-new:]({profile_url}) |\n"
        else:
            content += """### :material-help-circle: Contributors

No contributor data available.
"""

        community_interactions = stars + forks + watchers
        completed_items = issue_stats['closed_issues'] + issue_stats['closed_prs']
        health_score = (issue_close_rate + pr_close_rate) / 2
        contributor_ratio = (len(contributors) / max(stars, 1) * 1000)

        content += f"""

---

## :information_source: Repository Insights

### :material-chart-line: Key Metrics Summary

- **Community Engagement**: {community_interactions:,} total interactions (stars + forks + watchers)
- **Development Activity**: {completed_items:,} completed items (closed issues + merged PRs)
- **Project Health Score**: {health_score:.1f}% (average close/merge rate)
- **Contributors per 1000 Stars**: {contributor_ratio:.1f} contributor ratio

### :material-api: Data Sources

- **Repository Metadata**: GitHub API via `gh repo view`
- **Issue/PR Statistics**: GitHub Search API 
- **Language Analysis**: GitHub Languages API
- **Traffic Data**: GitHub Traffic API (requires repository access)
- **Release Information**: GitHub Releases API
- **Contributor Data**: GitHub Contributors API

---

*Statistics generated automatically during documentation build using GitHub CLI.*
"""

        # Write the comprehensive stats page
        with mkdocs_gen_files.open("auxilary/statistics.md", "w") as f:
            f.write(content)
        
        print("✅ Generated comprehensive statistics page with real data!", file=sys.stderr)
        print(f"📊 {len(contributors)} contributors • 👁️ {traffic_stats['views']:,} views • ⭐ {stars:,} stars", file=sys.stderr)

# Main execution
def main():
    try:
        print("🚀 Starting repository statistics generation...", file=sys.stderr)
        generator = StatsGenerator()
        generator.generate_stats_page()
        print("✅ Repository statistics generation completed successfully!", file=sys.stderr)
    except Exception as e:
        print(f"❌ Critical error in statistics generation: {e}", file=sys.stderr)
        
        # Create fallback page on error
        fallback_content = f"""# :bar_chart: Repository Statistics

!!! error "Statistics Generation Failed"
    Error: {str(e)}

## :gear: Troubleshooting

1. **Ensure GitHub CLI is installed**: `gh --version`
2. **Authenticate with GitHub**: `gh auth login` 
3. **Check repository access**: `gh repo view WCRP-CMIP/Variable-Registry`
4. **Rebuild documentation**: The build process will retry automatically

---

*This fallback page indicates an issue with GitHub CLI or repository access.*
"""
        
        try:
            import mkdocs_gen_files
            with mkdocs_gen_files.open("auxilary/statistics.md", "w") as f:
                f.write(fallback_content)
            print("✅ Created fallback statistics page", file=sys.stderr)
        except Exception as fallback_error:
            print(f"❌ Could not create fallback page: {fallback_error}", file=sys.stderr)

# Run the main function
if __name__ == "__main__":
    main()
else:
    main()



#!/usr/bin/env python3
"""
Script to generate LaTeX publication list from markdown files in _publications directory.

Usage:
    python3 generate_latex.py

Output:
    - Prints LaTeX itemize list to console
    - Saves to publications.tex file

Customization:
    - To add code URLs for publications, edit the get_code_url() function
    - To add special paper URLs (e.g., Google Drive), edit the get_paper_display_url() function
    - To add new conference macros, edit the conf_mappings dict in get_conference_macro()
"""

import os
import re
import glob
from pathlib import Path


def parse_markdown_file(filepath):
    """Parse a markdown publication file and extract metadata."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    yaml_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        return None
    
    yaml_content = yaml_match.group(1)
    
    # Parse YAML fields
    metadata = {}
    
    # Title
    title_match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', yaml_content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip('"\'')
    
    # Date
    date_match = re.search(r'^date:\s*(\d{4})-\d{2}-\d{2}', yaml_content, re.MULTILINE)
    if date_match:
        metadata['year'] = int(date_match.group(1))
    
    # Venue
    venue_match = re.search(r'^venue:\s*["\']?(.*?)["\']?\s*$', yaml_content, re.MULTILINE)
    if venue_match:
        metadata['venue'] = venue_match.group(1).strip('"\'')
    
    # Paper URL
    paperurl_match = re.search(r'^paperurl:\s*["\']?(.*?)["\']?\s*$', yaml_content, re.MULTILINE)
    if paperurl_match:
        metadata['paperurl'] = paperurl_match.group(1).strip('"\'')
    
    # Authors
    authors_match = re.search(r'^authors:\s*["\']?(.*?)["\']?\s*$', yaml_content, re.MULTILINE)
    if authors_match:
        metadata['authors'] = authors_match.group(1).strip('"\'')
    
    return metadata


def clean_authors(authors_str):
    """Convert HTML bold tags to LaTeX bold."""
    # Remove HTML tags but preserve bold formatting
    authors_str = authors_str.replace('<b>', r'\textbf{')
    authors_str = authors_str.replace('</b>', '}')
    return authors_str


def extract_venue_info(venue_str):
    """Extract conference name and year from venue string."""
    # Try to extract year from various patterns
    # Pattern 1: (ABC 2024) or (2024)
    year_match = re.search(r'\((?:\w+\s*)?(\d{4})\)', venue_str)
    if year_match:
        year = year_match.group(1)
    else:
        # Pattern 2: "2024 Conference" or just "2024"
        year_match = re.search(r'(\d{4})', venue_str)
        if year_match:
            year = year_match.group(1)
        else:
            # Pattern 3: Try to extract from "61st" -> assume 2024 for 61st DAC, 2023 for 60th, etc.
            # For DAC: 60th was 2023, 61st was 2024, 62th is 2025
            edition_match = re.search(r'(\d+)(?:st|nd|rd|th)\s+(?:ACM/IEEE\s+)?Design Automation Conference', venue_str, re.IGNORECASE)
            if edition_match:
                edition = int(edition_match.group(1))
                # DAC 60th was in 2023
                year = str(1963 + edition)
                return 'DAC', year
            
            # For ASPDAC: 30th is 2025
            edition_match = re.search(r'(\d+)(?:st|nd|rd|th)\s+Asia and South Pacific Design Automation Conference', venue_str, re.IGNORECASE)
            if edition_match:
                edition = int(edition_match.group(1))
                # ASPDAC 30th is in 2025
                year = str(1995 + edition)
                return 'ASPDAC', year
            
            return None, None
    
    # Try to extract conference name
    for conf in ['ICLR', 'ICCV', 'NeurIPS', 'DAC', 'EMNLP', 'ASPDAC', 'ASP-DAC', 'MIUA']:
        if conf.upper() in venue_str.upper():
            return conf, year
    
    return None, year


def get_conference_macro(venue_str):
    """Map venue string to LaTeX conference macro."""
    venue_upper = venue_str.upper()
    
    # Define conference mappings (order matters - check more specific patterns first)
    conf_mappings = {
        'ICLR': r'\ICLR',
        'ICCV': r'\ICCV',
        'NEURIPS': r'\NeurIPS',
        'ASIA AND SOUTH PACIFIC DESIGN AUTOMATION CONFERENCE': r'\ASPDAC',
        'ASP-DAC': r'\ASPDAC',
        'ASPDAC': r'\ASPDAC',
        'DESIGN AUTOMATION CONFERENCE': r'\DAC',
        'DAC': r'\DAC',
        'EMNLP': r'\EMNLP',
        'MIUA': r'\textit{Conference on Medical Image Understanding and Analysis (MIUA)}',
    }
    
    for conf_key, conf_macro in conf_mappings.items():
        if conf_key in venue_upper:
            conf_name, year = extract_venue_info(venue_str)
            if year:
                # Special handling for MIUA
                if conf_key == 'MIUA':
                    return conf_macro.replace('Conference', f'{year} Conference')
                return f"{conf_macro}[{year}]"
            return conf_macro
    
    # Check if it's an arxiv preprint - don't add "Accepted at"
    if 'ARXIV' in venue_upper or 'PREPRINT' in venue_upper:
        return None
    
    # If no match found, return the venue as-is in textit
    return f"\\textit{{{venue_str}}}"


def get_code_url(title, paperurl):
    """
    Get GitHub code URL for publications.
    
    To add a code URL for a publication:
    1. Add an entry to code_mappings with a keyword from the paper title
    2. The keyword will be matched case-insensitively
    
    Example: 'Progressive Mixed-Precision': 'https://github.com/yourname/repo'
    """
    # Mapping of paper titles/keywords to code URLs
    code_mappings = {
        'Progressive Mixed-Precision Decoding': 'https://github.com/SamsungLabs/PMPD',
        'FW-Merging': 'https://github.com/hmarkc/FW-Merging',
        'Parallel Prompt Decoding': 'https://github.com/hmarkc/parallel-prompt-decoding',
        # Add more mappings here as needed
    }
    
    for keyword, url in code_mappings.items():
        if keyword.lower() in title.lower():
            return url
    
    return None


def get_paper_display_url(paperurl, title):
    """
    Get the display URL for the paper.
    
    Use this to override the default paperurl from the markdown file.
    Useful for replacing ArXiv links with Google Drive, publisher links, etc.
    
    To add a custom paper URL:
    1. Add an entry to special_url_mappings with a keyword from the paper title
    2. Provide the full URL you want to use instead
    """
    # Special mappings for custom paper URLs (e.g., Google Drive links)
    special_url_mappings = {
        'FW-Merging': 'https://drive.google.com/file/d/1k7bGeHlr2ruaRclFuDNgZ6F--uevVsaN/view',
        'Quantum Code Generation': 'https://drive.google.com/file/d/1ownLmdFwH-5vJYLNzsuTtJjMCLPrPl8u/view',
        # Add more custom URLs here as needed
    }
    
    for keyword, url in special_url_mappings.items():
        if keyword.lower() in title.lower():
            return url
    
    # Default to the URL from the markdown file
    return paperurl


def generate_latex_item(pub_data):
    """Generate a single LaTeX publication item."""
    title = pub_data.get('title', '')
    authors = clean_authors(pub_data.get('authors', ''))
    venue_str = pub_data.get('venue', '')
    paperurl = pub_data.get('paperurl', '')
    
    # Get conference macro
    venue_latex = get_conference_macro(venue_str)
    
    # Get URLs
    display_url = get_paper_display_url(paperurl, title)
    code_url = get_code_url(title, paperurl)
    
    # Build LaTeX item
    latex = f"        \\item {authors}. {title}."
    
    # Add venue if it contains conference info
    if venue_latex:
        latex += f" Accepted at {venue_latex}."
    
    # Add paper link
    if display_url:
        latex += f" [\\href{{{display_url}}}{{Paper}}]"
    
    # Add code link if available
    if code_url:
        latex += f" [\\href{{{code_url}}}{{Code}}]"
    
    return latex


def main():
    """Main function to generate LaTeX publications list."""
    # Get the directory containing this script
    script_dir = Path(__file__).parent
    
    # Find all markdown files (excluding update.py)
    md_files = glob.glob(str(script_dir / "*.md"))
    
    # Parse all publications
    publications = []
    for md_file in md_files:
        pub_data = parse_markdown_file(md_file)
        if pub_data and 'title' in pub_data:
            publications.append(pub_data)
    
    # Sort by year (descending) and then by title
    publications.sort(key=lambda x: (-x.get('year', 0), x.get('title', '')))
    
    # Generate LaTeX
    print("\\begin{itemize}")
    for pub in publications:
        latex_item = generate_latex_item(pub)
        print(latex_item)
    print("\\end{itemize}")
    
    # Also save to a file
    output_file = script_dir / "publications.tex"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\\begin{itemize}\n")
        for pub in publications:
            latex_item = generate_latex_item(pub)
            f.write(latex_item + "\n")
        f.write("\\end{itemize}\n")
    
    print(f"\n\n=== LaTeX output also saved to: {output_file} ===")


if __name__ == "__main__":
    main()


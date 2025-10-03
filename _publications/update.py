import os
import re
import requests
from bs4 import BeautifulSoup
import time
from scholarly_publications import fetch_publications

def extract_publication_details(link):
    """Extract authors and venue from Google Scholar citation page"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    authors = "<b>Hao (Mark) Chen</b> et al."  # Default
    venue = "Arxiv"  # Default
    paper_url = None  # Will store the actual paper URL
    
    try:
        print(f"Fetching details from: {link}")
        response = requests.get(link, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract authors from Google Scholar page
        authors_field = soup.find('div', class_='gsc_oci_field', string='Authors')
        if authors_field:
            authors_value = authors_field.find_next_sibling('div', class_='gsc_oci_value')
            if authors_value:
                author_names = [name.strip() for name in authors_value.text.split(',')]
                formatted_authors = []
                for name in author_names:
                    # Highlight your name (check for various formats)
                    if 'Hao' in name and 'Chen' in name or 'Mark' in name and 'Chen' in name:
                        formatted_authors.append(f"<b>{name}</b>")
                    else:
                        formatted_authors.append(name)
                authors = ", ".join(formatted_authors)
        
        # Extract venue/conference from Google Scholar page
        conference_field = soup.find('div', class_='gsc_oci_field', string='Conference')
        if conference_field:
            conference_value = conference_field.find_next_sibling('div', class_='gsc_oci_value')
            if conference_value:
                venue = conference_value.text.strip()
        else:
            # Try journal if conference not found
            journal_field = soup.find('div', class_='gsc_oci_field', string='Journal')
            if journal_field:
                journal_value = journal_field.find_next_sibling('div', class_='gsc_oci_value')
                if journal_value:
                    venue = journal_value.text.strip()
            else:
                book_field = soup.find('div', class_='gsc_oci_field', string='Book')
                if book_field:
                    book_value = book_field.find_next_sibling('div', class_='gsc_oci_value')
                    if book_value:
                        venue = book_value.text.strip()
                else:
                    venue = "Arxiv"
        
        # Extract paper URL (look for arXiv or other links)
        scholar_articles = soup.find('div', id='gsc_oci_title_gg')
        if scholar_articles:
            link_tag = scholar_articles.find('a', href=True)
            if link_tag:
                paper_url = link_tag['href']
        
    except Exception as e:
        print(f"Error extracting details from {link}: {e}")
    
    return authors, venue, paper_url

def sanitize_filename(title, year):
    """Create a safe filename from title and year"""
    # Remove special characters and replace spaces with hyphens
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title)
    safe_title = safe_title.strip('-').lower()
    
    # Limit length to avoid filesystem issues
    if len(safe_title) > 50:
        safe_title = safe_title[:50].rstrip('-')
    
    return f"{year}-{safe_title}.md"

def generate_markdown_content(publication):
    """Generate markdown content for a publication"""
    title = publication.get('title', '')
    year = publication.get('year', '')
    link = publication.get('link', '')
    citations = publication.get('citations', '0')
    
    # Extract authors and venue from the publication link
    authors, venue, paper_url = extract_publication_details(link)
    
    # Use the extracted paper URL if available, otherwise use the original link
    final_paper_url = paper_url if paper_url else link
    
    # Create citation
    citation = f"{authors}. {title}. {year}."
    
    markdown_content = f"""---
title: "{title}"
collection: publications
date: {year}-01-01
venue: "{venue}"
paperurl: "{final_paper_url}"
authors: "{authors}"
citation: "{citation}"
citations: {citations}
---

# Abstract

"""
    
    return markdown_content

def create_publication_files(publications):
    """Create markdown files for publications that don't already exist"""
    publications_dir = os.path.dirname(os.path.abspath(__file__))
    
    for pub in publications:
        title = pub.get('title', '')
        year = pub.get('year', '')
        
        if not title or not year:
            continue
            
        filename = sanitize_filename(title, year)
        filepath = os.path.join(publications_dir, filename)
        old_filepath = os.path.join(publications_dir, 'old', filename)
        
        # Check if file already exists or under old/
        # if os.path.exists(filepath) or os.path.exists(old_filepath):
        #     print(f"File already exists: {filename}")
        #     continue
        
        # Generate markdown content
        content = generate_markdown_content(pub)
        
        # Write the file
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created: {filename}")
        except Exception as e:
            print(f"Error creating {filename}: {e}")

def main():
    # Fetch publications
    print("Fetching publications...")
    publications = fetch_publications('O6ajbEoAAAAJ')
    
    print(f"Found {len(publications)} publications")
    
    # Create markdown files for new publications
    create_publication_files(publications)
    
    print("Done!")

if __name__ == "__main__":
    main()

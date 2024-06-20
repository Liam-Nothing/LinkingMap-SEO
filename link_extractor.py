import sys
import requests
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlparse, urlunparse, urljoin
import matplotlib.pyplot as plt
import networkx as nx

def get_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        sys.exit(1)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    return links

def extract_domains(base_url, links):
    base_domain = urlparse(base_url).netloc
    domains = []
    for link in links:
        if link.startswith('/'):  # Relative link
            domains.append((base_domain, "self"))
        else:
            link_domain = urlparse(urljoin(base_url, link)).netloc
            if link_domain == base_domain:
                domains.append((link_domain, "self"))
            else:
                domains.append((link_domain, "external"))
    return domains

def count_domains(domains):
    domain_count = Counter(domains)
    return domain_count

def validate_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = urlunparse(('http',) + parsed_url[1:])
    return url

def plot_domain_distribution(domain_count, scanned_domain):
    G = nx.Graph()

    # Add the scanned domain as the central node
    G.add_node(scanned_domain, size=500, color='red', label=f"{scanned_domain}\n")

    # Add other domains as nodes and create edges from the central node
    for (domain, link_type), count in domain_count.items():
        color = 'green' if link_type == "self" else 'skyblue'
        label_suffix = " (self)" if link_type == "self" else ""
        G.add_node(domain, size=count * 50, color=color, label=f"{domain}\n{count}{label_suffix}")
        G.add_edge(scanned_domain, domain)

    pos = nx.spring_layout(G, center=(0.5, 0.5), scale=2)  # Layout the nodes
    sizes = [G.nodes[node]['size'] for node in G.nodes]
    colors = [G.nodes[node]['color'] for node in G.nodes]
    labels = {node: G.nodes[node]['label'] for node in G.nodes}

    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=sizes, node_color=colors, edge_color='gray', linewidths=1, font_size=10, font_color='black', font_weight='bold', alpha=0.7)
    plt.title('Distribution of Links by Domain')
    plt.tight_layout()
    plt.savefig('domain_distribution.png')  # Save the image
    plt.show()

def main(url):
    url = validate_url(url)
    scanned_domain = urlparse(url).netloc
    links = get_links(url)
    domains = extract_domains(url, links)
    domain_count = count_domains(domains)
    plot_domain_distribution(domain_count, scanned_domain)
    print("Domain distribution image saved as 'domain_distribution.png'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python link_extractor.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Validate URL format
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        print("Invalid URL. Please include the scheme (e.g., http:// or https://).")
        sys.exit(1)
    
    main(url)

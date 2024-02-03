#!/bin/bash

# Get domain input from the user
read -p "Enter the domain: " domain
mkdir /workspaces/16JabRamWebEditor/XSS/$domain
touch /workspaces/16JabRamWebEditor/XSS/$domain/subfinder-subdomains.txt
touch /workspaces/16JabRamWebEditor/XSS/$domain/assetfinder-subdomains.txt
touch /workspaces/16JabRamWebEditor/XSS/$domain/subdomains.txt
touch /workspaces/16JabRamWebEditor/XSS/$domain/sort.txt
touch /workspaces/16JabRamWebEditor/XSS/$domain/200_urls.txt
touch /workspaces/16JabRamWebEditor/XSS/$domain/filtered_urls.txt

# Set file paths
subfinderOutput="/workspaces/16JabRamWebEditor/XSS/$domain/subfinder-subdomains.txt"
assetfinderOutput="/workspaces/16JabRamWebEditor/XSS/$domain/assetfinder-subdomains.txt"
combinedSubdomains="/workspaces/16JabRamWebEditor/XSS/$domain/subdomains.txt"
sortedSubdomains="/workspaces/16JabRamWebEditor/XSS/$domain/sort.txt"
httpxOutput="/workspaces/16JabRamWebEditor/XSS/$domain/200_urls.txt"
paramspiderOutput="/workspaces/16JabRamWebEditor/XSS/$domain/filtered_urls.txt"

# Run subfinder
subfinder -d "$domain" -o "$subfinderOutput"

# Run assetfinder
assetfinder --subs-only "$domain" > "$assetfinderOutput"

# Combine subdomains from subfinder and assetfinder
cat "$subfinderOutput" "$assetfinderOutput" > "$combinedSubdomains"

# Remove duplicate subdomains and sort
sort -u "$combinedSubdomains" > "$sortedSubdomains"

# Run httpx to filter URLs with HTTP status 200
cat "$sortedSubdomains" | httpx -mc 200 > "$httpxOutput"

# Run paramspider on filtered URLs
while IFS= read -r URL; do
    python3 /workspaces/16JabRamWebEditor/Tools/ParamSpider/paramspider.py -d "${URL}"
done < "$httpxOutput"

# Run kxss on filtered URLs
cat "$paramspiderOutput" | kxss

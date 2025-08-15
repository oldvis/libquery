#!/bin/bash

# libquery Package Publisher
# Simple script to publish a new version to PyPI

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not in a git repository"
    exit 1
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "Warning: You have uncommitted changes"
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Get bump type from command line
if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <bump_type>"
    echo "Bump types: major, minor, patch"
    echo "Example: $0 patch"
    exit 1
fi

bump_type=$1
if [[ ! "$bump_type" =~ ^(major|minor|patch)$ ]]; then
    echo "Error: Invalid bump type. Use 'major', 'minor', or 'patch'"
    exit 1
fi

# Get current version
current_version=$(grep '^version = ' pyproject.toml | sed 's/.*version = "\([^"]*\)".*/\1/')
print_status "Current version: $current_version"

# Calculate new version
IFS='.' read -ra VERSION_PARTS <<< "$current_version"
major=${VERSION_PARTS[0]}
minor=${VERSION_PARTS[1]}
patch=${VERSION_PARTS[2]}

case $bump_type in
    major)
        major=$((major + 1))
        minor=0
        patch=0
        ;;
    minor)
        minor=$((minor + 1))
        patch=0
        ;;
    patch)
        patch=$((patch + 1))
        ;;
esac

new_version="${major}.${minor}.${patch}"
print_status "New version: $new_version"

# Confirm
read -p "Proceed with publishing version $new_version? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted"
    exit 1
fi

# Update version in pyproject.toml
if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "s/^version = \".*\"/version = \"$new_version\"/" pyproject.toml
else
    sed -i "s/^version = \".*\"/version = \"$new_version\"/" pyproject.toml
fi

# Build package
print_status "Building package..."
poetry build

# Commit and tag
git add pyproject.toml
git commit -m "Bump version to $new_version"
git tag "v$new_version"
git push origin "v$new_version"

print_success "Version $new_version published! GitHub workflow should now publish to PyPI."

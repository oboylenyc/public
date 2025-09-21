""" Day 35: Parse GitHub Repos JSON and Report Top Stars

Difficulty: Intermediate

Challenge Description: Write a function top_repos(json_text: str, n: int = 3) that parses a JSON array of GitHub-like repository objects and returns a string with the top n repositories by stargazers_count. Each output line should be formatted as:
repo_name — ★stars (language)
Rules:

Use only the standard library (json module).

Treat missing or null language as "Unknown".

Repos with missing or non-integer stargazers_count count as 0.

Break ties by repo_name (A–Z).

Do not make any network requests; operate only on the provided JSON text. """

import json

def top_repos(json_text: str, n: int = 3, min_stars: int = 0) -> str:
    try:
        repos = json.loads(json_text)
    except json.JSONDecodeError:
        return "Invalid JSON input."
    
    # Normalize and filter repos
    cleaned = []
    for repo in repos:
        name = repo.get("name", "Unknown")
        stars = repo.get("stargazers_count", 0)
        if not isinstance(stars, int):
            stars = 0
        language = repo.get("language") or "Unknown"
        
        if stars >= min_stars:
            cleaned.append((name, stars, language))
    
    # Sort by stars desc, then by name asc
    cleaned.sort(key=lambda x: (-x[1], x[0].lower()))
    
    # Pick top n
    top = cleaned[:n]
    
    # Format results
    return "\n".join(f"{name} — ★{stars} ({language})" for name, stars, language in top)


# Example usage
if __name__ == "__main__":
    sample_json = """
    [
      {"name": "alpha", "stargazers_count": 120, "language": "Python"},
      {"name": "beta", "stargazers_count": 305, "language": "TypeScript"},
      {"name": "gamma", "stargazers_count": 305, "language": null},
      {"name": "delta", "stargazers_count": 12}
    ]
    """
    print("Top 3 (no filter):")
    print(top_repos(sample_json, 3))
    print("\nTop 2 with min_stars=100:")
    print(top_repos(sample_json, 2, min_stars=100))
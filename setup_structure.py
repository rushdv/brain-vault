import os
from pathlib import Path

def create_structure():
    """
    Creates the scalable directory structure for Brain Vault.
    """
    base_path = Path.cwd()
    
    # Define the structure structure
    # Key is directory name, Value is list of subdirectories or nested dictionary
    structure = {
        "Computer-Science": {
            "Spring-2026": [
                "Algorithm-Design",
                "Math-III",
                "Electrical-Engineering",
                "Physics-II"
            ],
            # Placeholder for other semesters
            # "Fall-2025": ["..."], 
        },
        "Cybersecurity": [
            "Ethical-Hacking", 
            "Network-Traffic-Analysis"
        ],
        "Web-Development": [
            "React",
            "Python-Backend"
        ],
        "Projects": [
            "Nexum",
            "debug-ai"
        ]
    }

    print(f"Initializing Brain Vault Structure in: {base_path}")
    print("-" * 50)

    def build_tree(current_path, nodes):
        for key, value in nodes.items() if isinstance(nodes, dict) else enumerate(nodes):
            # Handle list items vs dict items
            name = key if isinstance(nodes, dict) else value
            children = value if isinstance(nodes, dict) else None
            
            dir_path = current_path / name
            
            if not dir_path.exists():
                dir_path.mkdir(parents=True)
                print(f"Created: {dir_path.relative_to(base_path)}")
            else:
                print(f"Exists:  {dir_path.relative_to(base_path)}")
            
            # Create a simple README in each leaf directory if it doesn't exist
            readme_path = dir_path / "README.md"
            if not readme_path.exists():
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(f"# {name.replace('-', ' ')}\n\nResources and notes for {name}.\n")
            
            # Recurse if there are children (for dict values)
            if children and isinstance(children, (dict, list)):
                 build_tree(dir_path, children)

    build_tree(base_path, structure)
    print("-" * 50)
    print("Structure setup complete!")

if __name__ == "__main__":
    create_structure()

import os

BASE_GITIGNORE = f"__pycache__/\n*.py[cod]\n*.so\n.Python\nenv/\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\n*.egg-info/\n.installed.cfg\n*.egg\n*.manifest\n*.spec\npip-log.txt\npip-delete-this-directory.txt\nhtmlcov/\n.tox/\n.coverage\n.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n*.mo\n*.pot\n*.log\ndocs/_build/\ntarget/\n.env\n*.db\n*.rdb\n.idea\n.vscode/\n*.code-workspace\n.spyproject/\n.ipynb_checkpoints/\n.DS_Store\n*.swp\n*.swo\n.mypy_cache/\n.venv/\n/models/\n/data/"
BASE_LICENSE = f"The MIT License (MIT)\nCopyright (c) 2016 DrivenData, Inc.\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."
BASE_MODULES = f"ipykernel\npython-dotenv"


PROJECT_STRUCTURE = {
    "data": {
        "external": {
            ".gitkeep": ""
        },
        "interim": {
            ".gitkeep": ""
        },
        "processed": {
            ".gitkeep": ""
        },
        "raw": {
            ".gitkeep": ""
        },
    },
    "models": {
        ".gitkeep": ""
    },
    "notebooks": {
        ".gitkeep": ""
    },
    "references": {
        ".gitkeep": ""
    },
    "reports": {
        "figures": {
            ".gitkeep": ""
        },
    },
    "src": {
        "modeling": {
            "__init__.py": "",
            "predict.py": "",
            "train.py": "",
        },
        "services": {
            "__init__.py": "",
        },
        "__init__.py": "",
        "config.py": "",
        "dataset.py": "",
        "features.py": "",
        "plots.py": "",
    },
    ".env.example": "",
    ".gitignore": BASE_GITIGNORE,
    "LICENCE": BASE_LICENSE,
    "README.md": "", 
    "requirements.txt": BASE_MODULES,
}


def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            with open(path, "w") as file:
                file.write(content)

def main():
    project_name = input("Project name: ")
    base_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(base_path, exist_ok=True)
    create_project_structure(base_path, PROJECT_STRUCTURE)
    print(f"Project '{project_name}' created on path: {base_path}")

if __name__ == "__main__":
    main()

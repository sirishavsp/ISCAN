import re
from typing import List, Dict, Union
from hcl import loads as parse_hcl
from radon.complexity import cc_visit
import networkx as nx
from fuzzywuzzy import fuzz

def extract_comments(file_contents: str) -> List[str]:
    comment_pattern = r'#.*'
    comments = re.findall(comment_pattern, file_contents)
    return [comment.strip('#').strip() for comment in comments]

def find_duplicates(file_contents: str) -> List[Dict[str, Union[str, int]]]:
    results = []
    lines = file_contents.split("\n")
    tokens = [re.findall(r'\w+|\S', line) for line in lines]  # Tokenize each line

    # Compare tokens for duplicates
    duplicates = set()
    for i, line_tokens in enumerate(tokens):
        if i in duplicates:
            continue
        for j in range(i + 1, len(tokens)):
            if line_tokens == tokens[j]:
                duplicates.add(j)
                results.append({
                    "issue": "Duplicate code detected",
                    "severity": "Medium",
                    "line_number": i + 1,
                    "recommendation": f"Review the duplicate code at line {j + 1} and consider consolidating it"
                                      f" into a reusable function or module."
                                      f" Remove any unused code to improve the readability and maintainability"
                                      f" of the Terraform file."
                                      f" If the duplicate code is necessary, document the reasons for it."
                                      f" Consider using Terraform modules to reduce duplication and improve"
                                      f" reusability."
                })

    # Analyze duplicate resource blocks with different configurations
    ast = parse_hcl(file_contents)
    resource_blocks = ast.get("resource", [])
    for i, block1 in enumerate(resource_blocks):
        for j in range(i + 1, len(resource_blocks)):
            block2 = resource_blocks[j]
            if block1["type"] == block2["type"] and block1 != block2:
                results.append({
                    "issue": "Duplicate resource block with different configuration",
                    "severity": "Medium",
                    "line_number": block2["lineno"],
                    "recommendation": f"Review the duplicate resource block at line {block2['lineno']}."
                                      f" Ensure that the configurations are intended and make the necessary changes."
                })

    comments = extract_comments(file_contents)
    for i, comment in enumerate(comments):
        for j in range(i + 1, len(comments)):
            similarity = fuzz.token_set_ratio(comment, comments[j])
            if similarity > 80:  # Adjust the threshold as per your needs
                results.append({
                    "issue": "Similar comments detected",
                    "severity": "Low",
                    "line_number": 0,
                    "recommendation": f"Review the similar comments at lines {i+1} and {j+1}."
                                      f" Consolidate or clarify the comments to improve code readability."
                })

    return results

def analyze_duplicate_code(file_path: str) -> List[Dict[str, Union[str, int]]]:
    results = []

    try:
        with open(file_path, 'r') as f:
            file_contents = f.read()

        # Perform code analysis
        duplicates = find_duplicates(file_contents)

        # Parse Terraform code into an AST
        ast = parse_hcl(file_contents)

        # Perform code complexity analysis
        complexity_results = cc_visit(file_path)
        for result in complexity_results:
            if result.complexity >= 10:  # Adjust the complexity threshold as per your needs
                results.append({
                    "issue": "High code complexity",
                    "severity": "High",
                    "line_number": result.lineno,
                    "recommendation": f"Refactor the code at line {result.lineno} to reduce complexity."
                })

        # Perform dependency analysis
        resource_graph = nx.DiGraph()

        for block in ast.get("resource", []):
            resource_type = block["type"]
            resource_name = block.get("name", "")
            resource_graph.add_node(resource_name)
            # Add edges for dependencies
            for dependency in block.get("depends_on", []):
                resource_graph.add_edge(dependency, resource_name)

        # Additional analysis or checks
        # <Add any other analysis or checks as per your requirements>

        # Merge all analysis results
        results += duplicates
        # <Merge other analysis results to the 'results' list>

    except Exception as e:
        # Handle any errors that may occur during analysis
        results.append({
            "issue": "Error occurred during analysis",
            "severity": "High",
            "line_number": 0,
            "recommendation": str(e)
        })

    return results

import subprocess
import json
from typing import List, Dict, Union

def test_check_for_insecure_system_access(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Checks for insecure system access patterns in Terraform code.
    
    Args:
        file_path (str): The path to the Terraform file.
    
    Returns:
        A list of dictionaries, where each dictionary represents an issue found in the file.
    """
    results = []
    with open(file_path, 'r') as f:
        terraform_code = f.read()
    
    # Perform checks for insecure system access patterns in the Terraform code
    # Example checks:
    if 'plaintext_secret' in terraform_code:
        results.append({
            "issue": "Insecure system access detected",
            "severity": "High",
            "line_number": 0,
            "recommendation": "Ensure that system resources or services are accessed with appropriate permissions or access controls."
        })
    
    # Add more checks for other insecure system access patterns
    
    return results

def test_warn_if_vulnerable_libraries(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Checks for the use of vulnerable libraries or modules in Terraform code.
    
    Args:
        file_path (str): The path to the Terraform file.
    
    Returns:
        A list of dictionaries, where each dictionary represents an issue found in the file.
    """
    results = []
    cmd = f"terraform init -backend=false && terraform get -update && terraform graph"
    try:
        output = subprocess.check_output(cmd, shell=True, cwd=os.path.dirname(file_path)).decode("utf-8")
    except subprocess.CalledProcessError:
        return results
    
    # Parse the Terraform graph and analyze dependencies for potential vulnerabilities
    # Example checks:
    if 'vulnerable_module' in output:
        results.append({
            "issue": "Potentially vulnerable library/module found",
            "severity": "High",
            "line_number": 0,
            "recommendation": "Update the library/module to a secure version or find an alternative if possible."
        })
    
    # Add more checks for other vulnerable libraries/modules
    
    return results

import os
import hcl
from typing import List, Dict, Union

def analyze_dependency(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Analyze the given Terraform file for resource dependencies and identify any issues.
    Return a list of dictionaries, where each dictionary represents a dependency issue found in the file.
    Each dictionary contains the keys "issue", "severity", "resource", "dependency", and "recommendation".

    Args:
        file_path (str): The path to the Terraform file.

    Returns:
        A list of dictionaries, where each dictionary represents a dependency issue found in the file.
    """
    results = []

    with open(file_path, "r") as f:
        data = hcl.load(f)

    for resource in data.get("resource", []):
        resource_type = resource["type"]
        resource_name = resource["name"]
        dependencies = resource.get("depends_on", [])

        for dependency in dependencies:
            if dependency not in data:
                results.append({
                    "issue": "Missing dependency",
                    "severity": "High",
                    "resource": f"{resource_type}.{resource_name}",
                    "dependency": dependency,
                    "recommendation": f"Add {dependency} as a dependency for {resource_type}.{resource_name}."
                })

            if dependency == f"{resource_type}.{resource_name}":
                results.append({
                    "issue": "Circular dependency",
                    "severity": "High",
                    "resource": f"{resource_type}.{resource_name}",
                    "dependency": dependency,
                    "recommendation": f"Remove the circular dependency between {resource_type}.{resource_name} and {dependency}."
                })

    return results


import os
import hcl
import re
from typing import List, Dict, Union

def enforce_naming_conventions(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Enforce naming conventions for resources in the Terraform file.
    Return a list of dictionaries, where each dictionary represents a resource naming issue found in the file.
    Each dictionary contains the keys "issue", "severity", "resource", and "recommendation".

    Args:
        file_path (str): The path to the Terraform file.

    Returns:
        A list of dictionaries, where each dictionary represents a resource naming issue found in the file.
    """
    results = []

    with open(file_path, "r") as f:
        data = hcl.load(f)

    for resource in data.get("resource", []):
        resource_type = resource["type"]
        resource_name = resource["name"]

        # Check if the resource name follows the desired naming convention
        if not re.match(r"^[\w-]+$", resource_name):
            results.append({
                "issue": "Invalid resource name",
                "severity": "Medium",
                "resource": f"{resource_type}.{resource_name}",
                "recommendation": "Use only alphanumeric characters, underscores, and hyphens in the resource name."
            })

        # Additional naming conventions checks can be added here
        # For example, you can check for prefix or suffix patterns, naming length, etc.

    return results

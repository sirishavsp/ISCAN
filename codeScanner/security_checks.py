import os
import re
import stat
import os
import re
from urllib.parse import urlparse

def test_warn_if_insecure_permissions(file_path):
    """
    Checks for insecure file permissions in the specified file path.

    Parameters:
    file_path (str): The path to the Terraform file to check.

    Returns:
    List[Dict]: A list of dictionaries representing any insecure file permissions found in the Terraform file.
    """
    if not os.path.exists(file_path):
        return []  # File does not exist, return empty list

    insecure_permissions = {"read": ["group", "other"], "write": ["group", "other"], "execute": ["other"]}
    issues = []

    with open(file_path, "r") as f:
        content = f.read()
        for line in content.split("\n"):
            if "user_data" in line:
                script_path = line.split("=")[1].strip().strip('"').replace("file://", "")
                if os.path.exists(script_path):
                    st = os.stat(script_path)
                    mode = st.st_mode
                    for perm, user in insecure_permissions.items():
                        if mode & getattr(stat, "S_I" + perm.upper()) and any(mode & getattr(stat, "S_I" + "GRP" + u.upper()) for u in user):
                            issues.append({
                                "issue": "Insecure file permissions found",
                                "severity": "High",
                                "line_number": content.count('\n', 0, content.index(line)) + 1,
                                "recommendation": "Ensure that sensitive files and directories have proper permissions set (e.g. 0600 for files, 0700 for directories)"
                            })
                else:
                    issues.append({
                        "issue": "Script file not found",
                        "severity": "High",
                        "line_number": content.count('\n', 0, content.index(line)) + 1,
                        "recommendation": "Ensure that the script file exists and the path is correct"
                    })

    return issues


def test_check_for_insecure_services(file_path):
    """
    Checks for the use of insecure services in the specified file path.

    Parameters:
    file_path (str): The path to the file to check.

    Returns:
    List of dictionaries: A list of dictionaries containing the issue details, including issue, severity, line number, and recommendation.
    """
    if not os.path.exists(file_path):
        return []  # File does not exist, return empty list

    # Regular expression pattern to match insecure services
    pattern = r"\b(http|ftp|telnet):\/\/\b"
    regex = re.compile(pattern)

    # Create a list to hold the results
    results = []

    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                matches = regex.finditer(line)
                for match in matches:
                    results.append({
                        "issue": "Insecure services detected in EC2 instances",
                        "severity": "High",
                        "line_number": line_num,
                        "recommendation": "Use secure protocols (e.g. HTTPS) to connect to services instead of insecure protocols (e.g. HTTP)"
                    })
    except IOError:
        print(f"Could not read file: {file_path}")
        
    return results

def test_check_for_security_issues(file_path):
    """
    Checks for security issues in the specified Terraform file.

    Parameters:
    file_path (str): The path to the file to check.

    Returns:
    List of dictionaries: A list of dictionaries containing the issue details, including issue, severity, line number, and recommendation.
    """
    if not os.path.exists(file_path):
        return []  # File does not exist, return empty list

    results = []

    with open(file_path, "r") as f:
        content = f.read()

    # Check for hardcoded credentials
    credentials_regex = r"(?i)(?:password|access_key|secret_key|token)\s*=\s*[\"']?\w+[\"']?"
    for match in re.finditer(credentials_regex, content):
        results.append({
            "issue": "Hardcoded credentials",
            "severity": "High",
            "line_number": content.count('\n', 0, match.start()) + 1,
            "recommendation": "Avoid hardcoding credentials. Use environment variables or other secure mechanisms."
        })

    # Check for unrestricted ingress
    ingress_regex = r"cidr_blocks\s*=\s*\[\"0\.0\.0\.0/0\"\]"
    if re.search(ingress_regex, content):
        results.append({
            "issue": "Unrestricted ingress",
            "severity": "Medium",
            "line_number": content.index(re.search(ingress_regex, content).group()),
            "recommendation": "Avoid using unrestricted ingress rules. Restrict access to specific IP ranges or security groups."
        })

    # Check for deprecated software/services
    deprecated_regex = r"(?i)deprecated|no_longer_maintained|insecure"
    if re.search(deprecated_regex, content):
        results.append({
            "issue": "Use of deprecated or insecure software/services",
            "severity": "Medium",
            "line_number": content.index(re.search(deprecated_regex, content).group()),
            "recommendation": "Avoid using deprecated or insecure software/services. Use supported and secure alternatives."
        })

    # Check for encryption configuration
    encryption_regex = r"(?i)encrypted\s*=\s*true"
    if not re.search(encryption_regex, content):
        results.append({
            "issue": "Missing encryption configuration",
            "severity": "Medium",
            "line_number": 0,
            "recommendation": "Enable encryption for data storage resources (e.g., databases, S3 buckets) to protect sensitive data."
        })

    # Check for logging and monitoring configuration
    logging_regex = r"(?i)logging|monitoring"
    if not re.search(logging_regex, content):
        results.append({
            "issue": "Missing logging and monitoring configuration",
            "severity": "Low",
            "line_number": 0,
            "recommendation": "Enable appropriate logging and monitoring configurations (e.g., AWS CloudTrail) for better visibility and security."
        })

    # Check for overly permissive IAM policies
    iam_policies_regex = r"(?i)effect\s*=\s*\"allow\"\s*\n\s*actions\s*=\s*\[\"(?:\*|.*:\*)\"\]\s*\n\s*resources\s*=\s*\[\"(?:\*|.*:\*)\"\]\s*\n"
    if re.search(iam_policies_regex, content):
        results.append({
            "issue": "Overly permissive IAM policies",
            "severity": "High",
            "line_number": content.index(re.search(iam_policies_regex, content).group()),
            "recommendation": "Avoid granting overly permissive IAM policies. Apply the principle of least privilege and restrict permissions to the necessary actions and resources."
        })

    # Check for unused resources
    resource_regex = r"resource\s+\"[^\"].+?\""
    resource_references = re.findall(resource_regex, content)
    resource_declarations = re.findall(r"(?<!#)resource\s+\"[^\"].+?\"", content)
    unused_resources = [resource for resource in resource_declarations if resource not in resource_references]
    for unused_resource in unused_resources:
        results.append({
            "issue": "Unused resource",
            "severity": "Medium",
            "line_number": content.index(unused_resource),
            "recommendation": "Remove unused resources to reduce potential attack surface and improve maintainability."
        })

    # Check for sensitive data exposure
    sensitive_data_regex = r"(?i)(?:password|secret|key|token)\s*=\s*\"[^\"].*?\""
    sensitive_data_matches = re.finditer(sensitive_data_regex, content)
    for match in sensitive_data_matches:
        results.append({
            "issue": "Sensitive data exposure",
            "severity": "High",
            "line_number": content.count('\n', 0, match.start()) + 1,
            "recommendation": "Avoid exposing sensitive data. Store credentials and secrets securely using tools like secrets managers or parameter stores."
        })

    # Check for cloud service misconfigurations
    cloud_service_regex = r"(?i)aws_[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+\."
    cloud_service_matches = re.finditer(cloud_service_regex, content)
    for match in cloud_service_matches:
        results.append({
            "issue": "Cloud service misconfiguration",
            "severity": "Medium",
            "line_number": content.count('\n', 0, match.start()) + 1,
            "recommendation": "Ensure proper configuration of cloud services (e.g., AWS S3 buckets, databases) to enforce security controls and prevent unauthorized access."
        })

    # Check for secure communication
    insecure_communication_regex = r"(?i)protocol\s*=\s*\"http\""
    if re.search(insecure_communication_regex, content):
        results.append({
            "issue": "Insecure communication",
            "severity": "Medium",
            "line_number": content.index(re.search(insecure_communication_regex, content).group()),
            "recommendation": "Use secure communication protocols (e.g., HTTPS) instead of plain HTTP to protect data in transit."
        })

    # Check for version control exclusions
    version_control_exclude_regex = r"(?i)exclude\s*=\s*\[\".+\"\]"
    if re.search(version_control_exclude_regex, content):
        results.append({
            "issue": "Version control exclusions",
            "severity": "Low",
            "line_number": content.index(re.search(version_control_exclude_regex, content).group()),
            "recommendation": "Avoid excluding Terraform files or directories from version control. Ensure all code changes are tracked and reviewed for security."
        })

    return results


def test_warn_if_unencrypted_network_protocols(file_paths):
    """
    Checks for unencrypted network protocols in the specified file paths.

    Parameters:
    file_paths (list): A list of file paths to check.

    Returns:
    List of dictionaries: A list of dictionaries containing details of any insecure network protocols found.
    """

    insecure_network_protocols = []

    insecure_protocol_patterns = [
        {
            "protocol": "http",
            "regex_pattern": r"(?i)\bhttp://",
            "severity": "High",
            "recommendation": "Replace HTTP with a secure protocol such as HTTPS."
        },
        {
            "protocol": "ftp",
            "regex_pattern": r"(?i)\bftp://",
            "severity": "High",
            "recommendation": "Avoid using unencrypted FTP. Consider using SFTP or FTPS instead."
        },
        {
            "protocol": "telnet",
            "regex_pattern": r"(?i)\btelnet://",
            "severity": "High",
            "recommendation": "Avoid using unencrypted Telnet. Use SSH for secure remote access."
        },
        # Add more insecure protocol patterns as needed
    ]

    for file_path in file_paths:
        if not os.path.isfile(file_path):
            continue

        with open(file_path, "r") as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                for protocol_pattern in insecure_protocol_patterns:
                    matches = re.finditer(protocol_pattern["regex_pattern"], line)
                    for match in matches:
                        protocol = match.group()
                        issue = {
                            "issue": f"Potentially unencrypted or unauthenticated {protocol.upper()} network protocol found in file: {file_path}",
                            "severity": protocol_pattern["severity"],
                            "line_number": line_num,
                            "line_content": line,
                            "protocol": protocol,
                            "recommendation": protocol_pattern["recommendation"]
                        }
                        insecure_network_protocols.append(issue)

    return insecure_network_protocols
import re
import logging

logging.basicConfig(level=logging.INFO)

def detect_weak_passwords_in_line(line, line_num):
    password_pattern = re.compile(r'password\s*=\s*("|\'|\`)[^\s("|\'|\`)]*\1')
    password_matches = password_pattern.findall(line)

    results = []
    for match in password_matches:
        results.append({
            "issue": "Weak password detected",
            "severity": "High",
            "line_number": line_num,
            "context": line.strip(),
            "recommendation": "Use a strong and complex password or passphrase."
        })
    return results

def detect_weak_secrets_in_line(line, line_num, secrets):
    results = []
    for secret in secrets:
        if secret in line and not line.strip().startswith("#"):  # exclude comments
            results.append({
                "issue": "Found weak secret",
                "severity": "High",
                "line_number": line_num,
                "context": line.strip(),
                "recommendation": "Store secrets in a secure and encrypted location (e.g. AWS Secrets Manager), and use appropriate access controls to protect them."
            })
    return results

def analyze_file_for_weak_passwords_and_secrets(file_path):
    """
    Checks for weak secrets in Terraform file.

    Returns:
        A list of recommendations for fixing the issue.
    """
    secrets = ["password", "pwd", "secret", "access_key", "secret_key", "private_key", "ssh_key"]
    results = []

    try:
        with open(file_path, "r") as f:
            for line_num, line in enumerate(f, 1):
                results.extend(detect_weak_passwords_in_line(line, line_num))
                results.extend(detect_weak_secrets_in_line(line, line_num, secrets))
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
    except IOError:
        logging.error(f"Could not open file {file_path}.")

    return results

import re
import logging

logging.basicConfig(level=logging.INFO)

def test_warn_if_insecure_config(file_path):
    insecure_patterns = [
        (re.compile(pattern, re.I), message, severity) for pattern, message, severity in [
        (r'(?i)\bmd5\b', "Use of insecure hash function", "High"),
        (r'(?i)\bsha1\b', "Use of insecure hash function", "High"),
        (r'(?i)\brc4\b', "Use of insecure encryption algorithm", "High"),
        (r'(?i)\btls1\b', "Use of insecure network protocol", "High"),
        (r'(?i)\bssl2\b', "Use of insecure network protocol", "High"),
        (r'(?i)\bssl3\b', "Use of insecure network protocol", "High"),
        (r'(?i)\bdes\b', "Use of weak encryption algorithm", "Medium"),
        (r'(?i)\brc2\b', "Use of weak encryption algorithm", "Medium"),
        (r'(?i)\bplaintext\b', "Use of plaintext data transmission", "High"),
        (r'(?i)\bftp\b', "Use of insecure network protocol", "High"),
        (r'(?i)\btelnet\b', "Use of insecure network protocol", "High"),
        (r'(?i)\brlogin\b', "Use of insecure network protocol", "High"),
        (r'(?i)\brsh\b', "Use of insecure network protocol", "High"),
        (r'(?i)\btftp\b', "Use of insecure network protocol", "High"),
        (r'(?i)\bsendmail\b', "Use of insecure email server", "Medium"),
        (r'(?i)\bsmtp\b', "Use of insecure email server", "Medium"),
        (r'(?i)\bxp_cmdshell\b', "Use of insecure command shell", "High"),
        (r'(?i)\bexec\b', "Use of insecure command execution", "High"),
        (r'(?i)\bshell\b', "Use of insecure command shell", "High"),
        (r'(?i)\bxp_regwrite\b', "Use of insecure registry write", "High"),
        (r'(?i)\bxp_regdelete\b', "Use of insecure registry delete", "High"),
        (r'(?i)\bxp_fileexist\b', "Use of insecure file existence check", "Medium"),
        (r'(?i)\bxp_filecopy\b', "Use of insecure file copy", "Medium"),
        (r'\b(api_key|api_secret|password|secret|token)\s*=\s*("|\'|\`)[^\s("|\'|\`)]*\1', "Hardcoded secrets found", "High"),
        (r'\bchmod\s+[467][0-7][0-7]', "Insecure file permissions", "Medium"),
        (r'\bTRACE\b', "Use of insecure HTTP method", "Medium"),
        (r'\bTRACK\b', "Use of insecure HTTP method", "Medium"),
        ]
    ]

    unique_results = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

            for i, line in enumerate(lines, start=1):
                if line.strip().startswith("#"):  # ignore comments
                    continue

                for insecure_pattern, message, severity in insecure_patterns:
                    if insecure_pattern.search(line):
                        result = {
                            'line_number': i,
                            'recommendation': message,
                            'severity': severity,
                            'issue': 'Config issue found',
                            'context': line.strip(),
                        }
                        unique_results.add(frozenset(result.items()))
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
    except IOError:
        logging.error(f"Could not open file {file_path}.")
    except UnicodeDecodeError:
        logging.error(f"File {file_path} is not in UTF-8 format.")

    return sorted((dict(item) for item in unique_results), key=lambda x: x['line_number'])

from typing import List, Dict, Union
import hcl

def test_check_for_unintended_destruction(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Parse the Terraform file and identify any resources or data that may be unintentionally destroyed.
    Return a list of dictionaries, where each dictionary represents an issue found in the file.
    Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

    Args:
        file_path (str): The path to the Terraform file.
        severity_levels (Dict[str, str]): A dictionary specifying the severity levels for different issues.

    Returns:
        A list of dictionaries, where each dictionary represents an issue found in the file.
    """
    # Define custom severity levels for different issues
    severity_levels = {
        "Unintended resource destruction detected": "High",
        "Unintended data destruction detected": "High"
    }

    with open(file_path, "r") as f:
        data = f.read()
        parsed_data = hcl.loads(data)

    issues = []
    process_blocks(parsed_data, issues, severity_levels)

    return issues

def process_blocks(blocks, issues, severity_levels, parent_path="", parent_line_number=0):
    if isinstance(blocks, dict):  # Add this line to check if blocks is a dictionary
        for block_type, block_list in blocks.items():
            for block in block_list:
                if isinstance(block, dict):  # Add this line to check if block is a dictionary
                    block_id = block.get('_terraform_id')
                    if isinstance(block_id, list) and len(block_id) > 0:
                        block_path = f"{parent_path}.{block_type}[{block_id[0]}]"
                    else:
                        block_path = f"{parent_path}.{block_type}"

                    line_number = block["_terraform_id"][1] + parent_line_number
                    process_lifecycle(block, block_path, line_number, issues, severity_levels)
                    if "resource" in block:
                        process_blocks(block["resource"], issues, severity_levels, block_path, line_number)
                    if "data" in block:
                        process_blocks(block["data"], issues, severity_levels, block_path, line_number)


def process_lifecycle(block, block_path, line_number, issues, severity_levels):
    if block.get("lifecycle") and block["lifecycle"].get("prevent_destroy"):
        issue_type = "Unintended resource destruction detected" if block.get("resource") else "Unintended data destruction detected"
        severity = severity_levels.get(issue_type, "High")
        recommendation = f"Check if the 'prevent_destroy' argument is intended for {block_path}."
        issues.append({
            "issue": issue_type,
            "severity": severity,
            "line_number": line_number,
            "recommendation": recommendation
        })



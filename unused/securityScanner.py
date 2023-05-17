import os
import re
import stat
from typing import List, Dict, Union
import hcl
import subprocess

def test_warn_if_insecure_permissions(file_path):
    """
    Checks for insecure file permissions in the specified file path.

    Parameters:
    file_path (str): The path to the Terraform file to check.

    Returns:
    List[Dict]: A list of dictionaries representing any insecure file permissions found in the Terraform file.
    """
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
                                "line_num": content.count('\n', 0, content.index(line)) + 1,
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


def test_check_for_hardcoded_ips_or_domains(file_path):
    """
    Checks for hard-coded IP addresses or domains in the specified file path.

    Parameters:
    file_path (str): The path to the file to check.

    Returns:
    List of dictionaries: A list of dictionaries containing the issue details, including issue, severity, line number, and recommendation.
    """
    results = []

    with open(file_path, "r") as f:
        content = f.read()

    ip_regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    domain_regex = r"\b(?:https?://)?(?:www\.)?([a-zA-Z0-9-]+)\.([a-zA-Z]{2,})(?:\.[a-zA-Z]{2,})?\b"

    for match in re.finditer(ip_regex, content):
        results.append({
            "issue": "Hard-coded IPs or domains",
            "severity": "High",
            "line_number": content.count('\n', 0, match.start()) + 1,
            "recommendation": f"aws_security_group_rule.allow_all cidr_blocks = {match.group()}"
        })

    for match in re.finditer(domain_regex, content):
        results.append({
            "issue": "Hard-coded IPs or domains",
            "severity": "High",
            "line_number": content.count('\n', 0, match.start()) + 1,
            "recommendation": "aws_security_group_rule.allow_all cidr_blocks = allow only specific IP"
        })

    return results


def test_warn_if_unencrypted_network_protocols(file_path):
    """
    Checks for unencrypted network protocols in the specified file path.

    Parameters:
    file_path (str): The path to the file to check.

    Returns:
    List of dictionaries: A list of dictionaries containing details of any insecure network protocols found.
    """

    insecure_network_protocols = []
    with open(file_path, "r") as f:
        content = f.read()
        network_fields = re.findall(r"(?i)user_data\s*=\s*[\"'](?P<url>http://[^\"']+)[\"']", content)
        if network_fields:
            for network_field in network_fields:
                line_num = content.count('\n', 0, content.index(network_field[0])) + 1
                insecure_network_protocols.append({
                    "issue": "Potentially unencrypted or unauthenticated network protocols found in the code",
                    "severity": "High",
                    "line_number": line_num,
                    "recommendation": "Ensure that all network protocols are encrypted and authenticated"
                })
    return insecure_network_protocols


def test_check_for_insecure_services(file_path):
    # Open Terraform file
    with open(file_path, 'r') as f:
        file_contents = f.read()

    # Regular expression pattern to match insecure services
    pattern = r"\b(http|ftp|telnet):\/\/\b"

    matches = re.finditer(pattern, file_contents)

    # Create a list to hold the results
    results = []

    # Check if matches exist and add results to the list
    for match in matches:
                line_num = file_contents.count('\n', 0, match.start()) + 1
                results.append({
                    "issue": "Insecure services detected in EC2 instances",
                    "severity": "High",
                    "line_number": line_num,
                    "recommendation": "Use secure protocols (e.g. HTTPS) to connect to services instead of insecure protocols (e.g. HTTP)"
                })
    return results

#working

def test_check_for_weak_passwords(file_path):
    """
    Checks for weak secrets in Terraform file.

    Returns:
        A list of recommendations for fixing the issue.
    """
    secrets = ["password", "pwd", "secret", "access_key", "secret_key", "private_key", "ssh_key"]
    results = []
    with open(file_path, "r") as f:
        content = f.read()

    # Check for weak passwords
    password_matches = re.findall(r'password\s*=\s*("|\'|\`)[^("|\'|\`)]*\1', content)
    for match in password_matches:
        line_num = content.count('\n', 0, content.index(match))+1
        results.append({
            "issue": "Weak password detected",
            "severity": "High",
            "line_number": line_num,
            "recommendation": "Use a strong and complex password or passphrase."
        })

    # Check for weak secrets
    lines = content.split("\n")
    for i, line in enumerate(lines):
        for secret in secrets:
            if secret in line:
                results.append({
                        f"issue": "Found weak secret",
                         "severity": "High",
                        "line_number": i+1,
                        "recommendation": "Store secrets in a secure and encrypted location (e.g. AWS Secrets Manager), and use appropriate access controls to protect them."
                })

    return results
import re

#not working
def test_warn_if_insecure_config(file_path):
    with open('terra.tf', 'r') as f:
        iac_code = f.read()

    insecure_patterns = [
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
    
    unique_results = set()
    for i, line in enumerate(iac_code.split('\n'), start=1):
        for insecure_pattern, message, severity in insecure_patterns:
            matches = re.findall(insecure_pattern, line)
            if matches:
                result = {
                    'line_number': i,
                    'recommendation': message,
                    'severity': severity,
                    'issue': 'Config issue found',
                }
                unique_results.add(frozenset(result.items()))

    results = [dict(item) for item in unique_results]


    return results

def test_find_duplicates(file_contents):
    """
    Identifies duplicate lines in the given file contents.

    Args:
    file_contents (str): The contents of the file to scan.

    Returns:
    A list of dictionaries containing the duplicate line number, severity, issue description, and recommendation.
    """
    results = []
    duplicates = []

    lines = file_contents.split("\n")
    for i, line in enumerate(lines):
        if line in duplicates:
            continue
        for j in range(i + 1, len(lines)):
            if line == lines[j]:
                duplicates.append(line)
                line_num = i + 1
                results.append({
                    "issue": "Duplicate code detected",
                    "severity": "Medium",
                    "line_number": line_num,
                    "recommendation": f"Review the duplicate code at line {j + 1} and consider consolidating it"
                                    f" into a reusable function or module."
                                    f" Remove any unused code to improve the readability and maintainability"
                                    f" of the Terraform file."
                                    f" If the duplicate code is necessary, document the reasons for it."
                                    f" Consider using Terraform modules to reduce duplication and improve"
                                    f" reusability."
                })
                break

    return results

def test_suggest_security_improvements(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Check the given Terraform file for security vulnerabilities and suggest improvements.
    """
    results = []
    try:
        with open(file_path, "r") as f:
            data = f.read()
            parsed_data = hcl.loads(data)
            for block in parsed_data.get("resource", []):
                if block.get("provider") and block.get("type") and block["provider"][0] == "aws":
                    deprecated_resources = {
                        "aws_security_group_rule": {
                            "issue": "Ingress and egress rules are too permissive",
                            "severity": "High",
                            "line_number": block["lineno"],
                            "recommendation": f"Review the ingress and egress rules for {block['type']} "
                                              f"at line {block['lineno']} and limit access to the minimum "
                                              f"required for your use case."
                        },
                        "aws_s3_bucket_policy": {
                            "issue": "S3 bucket policy is too permissive",
                            "severity": "High",
                            "line_number": block["lineno"],
                            "recommendation": f"Review the S3 bucket policy at line {block['lineno']} and "
                                              f"limit access to the minimum required for your use case."
                        },
                        "aws_db_instance": {
                            "issue": "RDS instance is publicly accessible",
                            "severity": "High",
                            "line_number": block["lineno"],
                            "recommendation": f"Update the {block['type']} at line {block['lineno']} to "
                                              f"not be publicly accessible, or use a private subnet."
                        },
                        "aws_ssm_parameter": {
                            "issue": "Sensitive data is stored in plaintext",
                            "severity": "Medium",
                            "line_number": block["lineno"],
                            "recommendation": f"Review the {block['type']} at line {block['lineno']} "
                                              f"and encrypt the parameter value or use SSM Parameter Store's "
                                              f"SecureString parameter type."
                        },
                        "aws_db_password": {
                            "issue": "Database password is stored in plaintext",
                            "severity": "Medium",
                            "line_number": block["lineno"],
                            "recommendation": f"Review the {block['type']} at line {block['lineno']} and "
                                              f"update it to use AWS Secrets Manager to store and manage "
                                              f"secrets securely."
                        }
                    }
                    if block["type"] in deprecated_resources:
                        results.append(deprecated_resources[block["type"]])

    except Exception:
        pass  # ignore any errors and continue with the rest of the scan

    return results


def test_check_for_unintended_destruction(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Parse the Terraform file and identify any resources or data that may be unintentionally destroyed.
    Return a list of dictionaries, where each dictionary represents an issue found in the file.
    Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

    Args:
        file_path (str): The path to the Terraform file.

    Returns:
        A list of dictionaries, where each dictionary represents an issue found in the file.
    """
    with open(file_path, "r") as f:
        data = f.read()
        parsed_data = hcl.loads(data)

    issues = []
    for block_type in parsed_data:
        for block in parsed_data[block_type]:
            if block_type == "resource":
                if block.get("lifecycle") and block["lifecycle"].get("prevent_destroy"):
                    issue = "Unintended resource destruction detected"
                    severity = "High"
                    line_number = block["_terraform_id"][1]
                    recommendation = f"Check if the 'prevent_destroy' argument is intended for resource at line {line_number}."
                    issues.append({"issue": issue, "severity": severity, "line_number": line_number, "recommendation": recommendation})

            elif block_type == "data":
                if block.get("lifecycle") and block["lifecycle"].get("prevent_destroy"):
                    issue = "Unintended data destruction detected"
                    severity = "High"
                    line_number = block["_terraform_id"][1]
                    recommendation = f"Check if the 'prevent_destroy' argument is intended for data at line {line_number}."
                    issues.append({"issue": issue, "severity": severity, "line_number": line_number, "recommendation": recommendation})

    return issues

results = []


def test_check_for_insecure_system_access():
    """
    Checks for the use of system resources or services without appropriate permissions or access controls
    
    Returns:
    bool: True if insecure system access is found, False otherwise
    """
    try:
        subprocess.run(["whoami"], check=True)
    except subprocess.CalledProcessError:
        results.append({
            "issue": "Insecure system access detected",
            "severity": "High",
            "line_number": 0,
            "recommendation": "Ensure that system resources or services are accessed with appropriate permissions or access controls."
        })
        return True
    else:
        return False


def test_warn_if_vulnerable_libraries():
    """
    Checks for the use of vulnerable libraries and prints a warning message if any are found.
    
    Returns:
    bool: True if any vulnerable libraries are found, False otherwise
    """
    import subprocess
    import json
    
    cmd = "npm audit --json"
    output = subprocess.check_output(cmd, shell=True)
    data = json.loads(output)

    vulnerabilities = []
    for key in data["advisories"]:
        advisory = data["advisories"][key]
        if advisory["severity"] == "high" or advisory["severity"] == "critical":
            vulnerabilities.append(advisory)

    if vulnerabilities:
        results = []
        for vulnerability in vulnerabilities:
            results.append({
                "issue": f"Potentially vulnerable library found: {vulnerability['title']}",
                "severity": vulnerability["severity"],
                "line_number": "",
                "recommendation": f"Update the library to a secure version or find an alternative library if possible."
            })
        return results
    else:
        return False

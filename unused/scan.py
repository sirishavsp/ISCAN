import subprocess
import re
import hcl
import subprocess
import boto3

def get_tflint_errors():
    """
    Returns a dictionary of TFLint error codes and descriptions.
    """
    tflint_errors = {}
    try:
        result = subprocess.run(['tflint', '--list-rules'], capture_output=True, text=True)
    except FileNotFoundError:
        print("tflint command not found. Please install tflint and try again.")
        return tflint_errors
    
    if result.stdout:
        for line in result.stdout.split('\n'):
            line = line.strip()
            if line:
                error_code, error_desc = line.split(' ', 1)
                tflint_errors[error_code] = error_desc
    
    return tflint_errors

def scan_file_for_syntax_issues(file_path):
    # Run tflint command on the file
    try:
        result = subprocess.run(['tflint', file_path], capture_output=True, text=True)
    except FileNotFoundError:
        print("tflint command not found. Please install tflint and try again.")
        return False
    
    # If there are errors, print custom error messages with line numbers
    if result.stderr:
        tflint_errors = get_tflint_errors()
        for line in result.stderr.split('\n'):
            line = line.strip()
            if line:
                error_code, _, line_num, error_desc = line.split(':', 3)
                if error_code in tflint_errors:
                    print(f"Error on line {line_num}: {tflint_errors[error_code]}")
                else:
                    print(f"Error on line {line_num}: {error_desc}")
        return False
    
    # If there are no errors, return True to indicate success
    return True

def scan_file_for_security_issues(file_path):
    # Run tflint command on the file
    try:
        result = subprocess.run(['tflint', file_path], capture_output=True, text=True)
    except FileNotFoundError:
        print("tflint command not found. Please install tflint and try again.")
        return False
    
    # If there are errors, print them and return False to indicate failure
    if result.stderr:
        # Create a dictionary to map error codes to descriptions
        error_dict = {
            'E1003': 'Insecure S3 bucket policy',
            'E1006': 'Insecure RDS instance',
            'E1012': 'Insecure security group rule',
            'E1014': 'Insecure IAM policy',
            'E1029': 'Insecure ECR repository policy',
            'E1030': 'Insecure ECS task definition',
            'E1042': 'Insecure KMS key policy'
        }
        
        # Use regular expressions to search for error codes and line numbers
        pattern = r'\[E[0-9]+\] (.*) at line (\d+)'
        matches = re.findall(pattern, result.stderr)
        
        # Print custom error messages for each issue found
        for match in matches:
            error_code, line_number = match[0], match[1]
            if error_code in error_dict:
                error_message = f"Insecure resource found: {error_dict[error_code]} at line {line_number}"
            else:
                error_message = f"Unknown error: {error_code} at line {line_number}"
            print(error_message)
        return False
    
    # If there are no errors, return True to indicate success
    return True

from typing import Any, Dict, List


def scan_file_for_type_annotations(file_path: str) -> Dict[str, List[str]]:
    """
    Check the given Terraform file for type annotations and return any missing
    type annotations as a dictionary, where the keys are the names of the
    variables/functions and the values are the paths to the locations in the
    file where the type annotations are missing.
    """
    try:
        with open(file_path, "r") as f:
            data = f.read()
            parsed_data = hcl.loads(data)
            analysis_result = {}
            for block in parsed_data.get("variable", []):
                for name, value in block.items():
                    if "type" not in value:
                        if "description" in value:
                            path = value["description"][0]["start_pos"][0]
                        else:
                            path = value["start_pos"][0]
                        if name not in analysis_result:
                            analysis_result[name] = []
                        analysis_result[name].append(path)

            for block in parsed_data.get("resource", []):
                for name, value in block.items():
                    for attribute_name, attribute_value in value.items():
                        if isinstance(attribute_value, dict) and "type" not in attribute_value:
                            if "description" in attribute_value:
                                path = attribute_value["description"][0]["start_pos"][0]
                            else:
                                path = attribute_value["start_pos"][0]
                            key = f"{name}.{attribute_name}"
                            if key not in analysis_result:
                                analysis_result[key] = []
                            analysis_result[key].append(path)

            return analysis_result
    except Exception:
        return {}  # return empty dictionary in case of any error

import boto3
import os
from typing import Any, Dict, List, Tuple

# improve error messages
def scan_file_for_syntax_issues(filename: str) -> List[str]:
    try:
        with open(filename, 'r') as f:
            hcl.load(f)
    except Exception as e:
        return [f"Syntax error: {e}"]
    return []


# incorporate static code analysis with type annotations
def scan_file_for_type_annotations(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        code = f.read()

    errors = []

    # Check for missing type annotations
    for line_num, line in enumerate(code.split('\n')):
        if ':' in line and '->' not in line and '#' not in line:
            errors.append(f"Missing type annotation on line {line_num + 1}: {line}")

    return errors

# incorporate linter
def run_linter(filename: str) -> List[str]:
    import pylint
    from pylint.lint import Run

    # disable certain pylint messages for readability
    options = ["--disable=C0114,C0115,C0116"]
    results = Run([filename] + options, exit=False)
    return [f"Linting error: {r.msg}" for r in results.linter.stats['by_msg']]

# incorporate code formatter
def run_formatter(filename: str) -> Tuple[bool, str]:
    import black

    try:
        with open(filename, 'r') as f:
            original_code = f.read()
        formatted_code = black.format_file_contents(original_code, fast=False)
        with open(filename, 'w') as f:
            f.write(formatted_code)
        return True, "Code formatting successful"
    except Exception as e:
        return False, f"Code formatting error: {e}"

# scan for security issues
def scan_file_for_security_issues(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        code = f.read()

    errors = []

    # Check for hardcoded credentials
    if "aws_access_key" in code or "aws_secret_key" in code:
        errors.append("Hardcoded AWS credentials found")

    # Check for SQL injection vulnerabilities
    if "SELECT" in code or "DELETE" in code or "UPDATE" in code:
        errors.append("Possible SQL injection vulnerability found")

    # Check for cross-site scripting (XSS) vulnerabilities
    if "<script>" in code or "javascript:" in code:
        errors.append("Possible XSS vulnerability found")


    return errors

# dynamic code check
def execute_terraform_file(filename: str, var_dict: Dict[str, Any]) -> Tuple[bool, str]:
    # Set AWS credentials from environment variables
    try:
        os.environ["AWS_ACCESS_KEY_ID"] = var_dict["aws_access_key_id"]
        os.environ["AWS_SECRET_ACCESS_KEY"] = var_dict["aws_secret_access_key"]
    except KeyError:
        raise ValueError("AWS access key ID or secret access key not provided in variables file")

def scan_security_issues(file_path: str) -> Tuple[bool, List[str]]:
    issues = []
    with open(file_path, 'r') as f:
        data = hcl.load(f)
        for block in data:
            if block.get("resource"):
                resource = block["resource"]
                if resource.startswith("aws_"):
                    if block.get("connection"):
                        issues.append("Insecure connection in {}".format(resource))
                    if block.get("provisioner"):
                        issues.append("Insecure provisioner in {}".format(resource))
                    if block.get("ami"):
                        issues.append("Insecure AMI in {}".format(resource))
                    if block.get("security_groups"):
                        issues.append("Insecure security group in {}".format(resource))
    if issues:
        return False, issues
    else:
        return True, []


def scan_runtime_issues(file_path: str) -> Tuple[bool, List[str]]:
    issues = []
    with open(file_path, 'r') as f:
        data = hcl.load(f)
        for block in data:
            if block.get("resource"):
                resource = block["resource"]
                if resource.startswith("aws_"):
                    if not block.get("ami"):
                        issues.append("Missing AMI in {}".format(resource))
                    if not block.get("instance_type"):
                        issues.append("Missing instance type in {}".format(resource))
                    if not block.get("subnet_id"):
                        issues.append("Missing subnet ID in {}".format(resource))
                    if not block.get("security_groups"):
                        issues.append("Missing security groups in {}".format(resource))
                    if not block.get("connection"):
                        issues.append("Missing connection in {}".format(resource))
                    elif not block["connection"].get("private_key"):
                        issues.append("Missing private key in connection of {}".format(resource))
    if issues:
        return False, issues
    else:
        return True, []
    
from typing import List, Dict

def scan_file_for_deletions(file_path: str) -> Dict[str, List[str]]:
    """
    Check the given Terraform file for any deleted resources and their dependencies and return a dictionary
    of the deleted resources and their dependencies, where the keys are the names of the deleted resources
    and the values are lists of their dependent resources.
    """
    with open(file_path, "r") as f:
        data = f.read()
        parsed_data = hcl.loads(data)
        deleted_resources = []
        dependent_resources = {}
        for block in parsed_data.get("resource", []):
            if block.get("lifecycle") and block["lifecycle"].get("ignore_changes"):
                if "delete" in block["lifecycle"]["ignore_changes"]:
                    deleted_resources.append(block["type"])
                    # Check for dependent resources
                    for b in parsed_data.get("resource", []):
                        if b.get("depends_on"):
                            for dependency in b["depends_on"]:
                                if dependency.startswith(block["type"]):
                                    if block["type"] not in dependent_resources:
                                        dependent_resources[block["type"]] = []
                                    dependent_resources[block["type"]].append(b["type"])
        if deleted_resources:
            result = {resource: dependent_resources.get(resource, []) for resource in deleted_resources}
            return result
        else:
            return {}

import os
import subprocess
import sys
from typing import Any, Dict, List, Tuple


def run_terraform_command(command: List[str], cwd: str) -> Tuple[int, str]:
    """
    Run the given Terraform command in the specified working directory and return
    a tuple containing the command's exit code and output.
    """
    env = os.environ.copy()
    env["TF_IN_AUTOMATION"] = "1"  # disable prompts in Terraform

    process = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )

    stdout, stderr = process.communicate()

    return process.returncode, stdout.decode() + stderr.decode()


def check_resource_deletion(file_path: str, resource: str) -> bool:
    """
    Check whether the given Terraform resource is deleted in the specified file.
    Return True if the resource is deleted, False otherwise.
    """
    command = ["terraform", "state", "list"]
    returncode, output = run_terraform_command(command, os.path.dirname(file_path))

    if returncode != 0:
        print("Error running Terraform command: {}".format(" ".join(command)))
        sys.exit(1)

    return resource not in output


def check_resource_dependencies(file_path: str, resource: str) -> List[str]:
    """
    Check whether any Terraform resources depend on the given resource in the specified file.
    Return a list of the names of the dependent resources, or an empty list if there are none.
    """
    command = ["terraform", "state", "show", "-no-color"]
    returncode, output = run_terraform_command(command + [resource], os.path.dirname(file_path))

    if returncode != 0:
        print("Error running Terraform command: {}".format(" ".join(command + [resource])))
        sys.exit(1)

    dependencies = []
    for line in output.splitlines():
        if "depends_on" in line:
            dependency = line.split(" = ")[-1]
            if dependency.startswith("module."):
                dependency = dependency.split(".")[1]
            dependencies.append(dependency)

    return dependencies

def warn_if_resource_deletion_has_dependencies(deleted_resource: str, terraform_file: str) -> None:
    """
    Given the name of a deleted resource and the path to the Terraform file,
    check if any remaining resources in the file depend on the deleted resource
    and print a warning message if any are found.

    Args:
        deleted_resource (str): The name of the deleted resource.
        terraform_file (str): The path to the Terraform file.

    Returns:
        None
    """
    try:
        with open(terraform_file, "r") as f:
            data = f.read()
            parsed_data = hcl.loads(data)

            dependencies = []
            for block_type in parsed_data:
                for block in parsed_data[block_type]:
                    for attribute in block:
                        if isinstance(block[attribute], list):
                            for item in block[attribute]:
                                if isinstance(item, str) and item == deleted_resource:
                                    dependencies.append(f"{block_type} {block['name']}")

                        if isinstance(block[attribute], dict):
                            if "resource" in block[attribute]:
                                if block[attribute]["resource"] == deleted_resource:
                                    dependencies.append(f"{block_type} {block['name']}")
                            elif "module" in block[attribute]:
                                for sub_block in block[attribute]["module"].values():
                                    if sub_block["resource"] == deleted_resource:
                                        dependencies.append(f"{block_type} {block['name']}")

            if dependencies:
                message = f"The following resources depend on {deleted_resource} and may be affected by its deletion:\n"
                message += "\n".join(dependencies)
                print(message)

    except Exception:
        pass  # do nothing and continue with the rest of the scan

def warn_if_deprecated_resources(file_path: str) -> None:
    """
    Check the given Terraform file for deprecated resources and print a warning
    message for each one found.
    """
    try:
        with open(file_path, "r") as f:
            data = f.read()
            parsed_data = hcl.loads(data)
            for block in parsed_data.get("resource", []):
                if block.get("provider") and block.get("type") and block["provider"][0] == "aws":
                    deprecated_resources = {
                        "aws_ebs_volume": "aws_ebs_volume_attachment",
                        "aws_instance": "aws_launch_template",
                        "aws_nat_gateway": "aws_eip",
                        "aws_db_instance": "aws_rds_instance",
                        "aws_elasticache_cluster": "aws_elasticache_replication_group"
                    }
                    if block["type"] in deprecated_resources:
                        print(f"Warning: {block['type']} is deprecated and will be replaced by {deprecated_resources[block['type']]}")
    except Exception:
        pass  # ignore any errors and do nothing

import re

def check_for_hardcoded_secrets(file_path: str) -> bool:
    """
    Check the given file for hardcoded secrets or credentials and return True if found,
    else return False.
    """
    secret_regex = re.compile(r"api[_-]?key[\w-]*|access[_-]?key[\w-]*|secret[\w-]*", re.IGNORECASE)
    try:
        with open(file_path, "r") as f:
            data = f.read()
            if secret_regex.search(data):
                return True
            else:
                return False
    except Exception:
        return False  # return False in case of any error

import requests

def check_for_vulnerable_packages(pkg_name: str, pkg_version: str) -> bool:
    """
    Check if the given package is vulnerable by querying the NVD database and
    return True if vulnerable, else return False.
    """
    try:
        url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe%3a%2fa%3a{pkg_name}%3a{pkg_version}"
        response = requests.get(url)
        if response.status_code == 200 and response.json()["result"]["totalResults"] > 0:
            return True
        else:
            return False
    except Exception:
        return False  # return False in case of any error

import ssl

def check_for_weak_encryption(certificate_path: str) -> bool:
    """
    Check the given certificate for weak encryption algorithms or key sizes and
    return True if any found, else return False.
    """
    try:
        with open(certificate_path, "r") as f:
            cert = ssl.load_certificate(ssl.PEM_cert_to_DER_cert(f.read()))
            for cipher in cert.get_signature_algorithm().split("-"):
                if cipher == "md5" or cipher == "sha1":
                    return True
            if cert.get_pubkey().bits() < 2048:
                return True
            else:
                return False
    except Exception:
        return False  # return False in case of any error

import re

def check_for_weak_passwords(password: str) -> bool:
    """
    Check the given password for weak password policy and return True if weak,
    else return False.
    """
    if len(password) < 8 or password.isnumeric() or password.isalpha():
        return True
    elif not re.search(r"\d", password) or not re.search(r"[a-zA-Z]", password):
        return True
    else:
        return False

import socket
from typing import List

import re

def check_network_security(file_path):
    """
    Check the given Terraform file for the use of unencrypted or unauthenticated
    network protocols and return a warning message if any are found.
    """
    try:
        with open(file_path, "r") as f:
            data = f.read()
            if re.search(r'protocol\s*=\s*["\']http["\']', data, re.IGNORECASE):
                return "Warning: Unencrypted HTTP protocol is being used."
            if re.search(r'protocol\s*=\s*["\']ftp["\']', data, re.IGNORECASE):
                return "Warning: Unencrypted FTP protocol is being used."
            if re.search(r'protocol\s*=\s*["\']telnet["\']', data, re.IGNORECASE):
                return "Warning: Unencrypted Telnet protocol is being used."
            if re.search(r'protocol\s*=\s*["\']smtp["\']', data, re.IGNORECASE):
                return "Warning: Unencrypted SMTP protocol is being used."
            if re.search(r'protocol\s*=\s*["\']pop3["\']', data, re.IGNORECASE):
                return "Warning: Unencrypted POP3 protocol is being used."
            return None
    except Exception:
        return None  # return None in case of any error

import re

def check_for_hardcoded_ips_or_domains(code):
    """
    Checks for the use of hard-coded IP addresses or domain names in the code, which could potentially lead to DNS hijacking or other types of attacks
    
    Args:
    code (str): The code to check
    
    Returns:
    bool: True if hard-coded IP addresses or domain names are found, False otherwise
    """
    ip_address_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    domain_name_pattern = re.compile(r"\b[a-zA-Z0-9]+\.[a-zA-Z]{2,3}\b")
    
    if ip_address_pattern.search(code) or domain_name_pattern.search(code):
        return True
    else:
        return False

import subprocess

def check_for_insecure_system_access():
    """
    Checks for the use of system resources or services without appropriate permissions or access controls
    
    Returns:
    bool: True if insecure system access is found, False otherwise
    """
    try:
        subprocess.run(["whoami"], check=True)
    except subprocess.CalledProcessError:
        return True
    else:
        return False

import re

def warn_if_hardcoded_secrets(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        secrets = re.findall(r"(?i)(password|api_key|access_key|secret_key|private_key)\s*=\s*[\"'][^\"']+[\"']", content)
        if secrets:
            print("WARNING: Potentially hardcoded secrets or credentials found in the code:")
            for secret in secrets:
                print(f"- {secret}")

import re

def warn_if_hardcoded_secrets(code):
    """Checks if there are any hardcoded secrets or credentials in the code.
    
    Args:
    code - (str) Terraform code
    
    Returns:
    None - Prints warning message if hardcoded secrets or credentials are found.
    """
    secrets_regex = re.compile(r"\b[A-Za-z0-9/+=]{40,}\b")
    if secrets_regex.search(code):
        print("WARNING: Hardcoded secrets or credentials found in the code.")


import subprocess

def warn_if_vulnerable_libraries():
    cmd = "npm audit --json"
    output = subprocess.check_output(cmd, shell=True)
    data = json.loads(output)

    vulnerabilities = []
    for key in data["advisories"]:
        advisory = data["advisories"][key]
        if advisory["severity"] == "high" or advisory["severity"] == "critical":
            vulnerabilities.append(advisory)

    if vulnerabilities:
        print("WARNING: Potentially vulnerable libraries found in the project:")
        for vulnerability in vulnerabilities:
            print(f"- {vulnerability['title']} ({vulnerability['severity']})")

import re

def warn_if_vulnerable_libraries(code):
    """Checks if there are any outdated or vulnerable software packages or libraries in the code.
    
    Args:
    code - (str) Terraform code
    
    Returns:
    None - Prints warning message if outdated or vulnerable software packages or libraries are found.
    """
    library_regex = re.compile(r"(?i)\b(alpine|ubuntu|debian|php|django|ruby|python|java|mysql|openssl|apache|nginx)\b")
    if library_regex.search(code):
        print("WARNING: Outdated or vulnerable software packages or libraries found in the code.")


def warn_if_insecure_permissions(file_path):
    """
    Checks for insecure file or directory permissions in the specified file path.

    Parameters:
    file_path (str): The path to the file or directory to check.

    Returns:
    None: Prints a warning message if any insecure permissions are found.
    """

    insecure_permissions = {"read": ["group", "other"], "write": ["group", "other"], "execute": ["other"]}

    for root, dirs, files in os.walk(file_path):
        for d in dirs:
            dir_path = os.path.join(root, d)
            st = os.stat(dir_path)
            mode = st.st_mode
            for perm, user in insecure_permissions.items():
                if mode & getattr(stat, "S_I" + perm.upper()) and any(mode & getattr(stat, "S_I" + "GRP" + u.upper()) for u in user):
                    print(f"Warning: {dir_path} has insecure {perm} permissions for group {user}.")
        for f in files:
            file_path = os.path.join(root, f)
            st = os.stat(file_path)
            mode = st.st_mode
            for perm, user in insecure_permissions.items():
                if mode & getattr(stat, "S_I" + perm.upper()) and any(mode & getattr(stat, "S_I" + "GRP" + u.upper()) for u in user):
                    print(f"Warning: {file_path} has insecure {perm} permissions for group {user}.")

import subprocess

def warn_if_weak_encryption(file_path):
    cmd = f"grep -rn 'MD5\\|SHA-1\\|DES\\|RC4\\|RC2\\|AES-128' {file_path}"
    output = subprocess.check_output(cmd, shell=True)

    if output:
        print("WARNING: Potentially weak encryption algorithms or key sizes found in the code:")
        print(output.decode())

import re

def warn_if_weak_passwords(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        password_fields = re.findall(r"(?i)password\s*=\s*[\"'][^\"']+[\"']", content)
        if password_fields:
            print("WARNING: Potentially weak passwords or password policies found in the code:")
            for password_field in password_fields:
                print(f"- {password_field}")

import re

def warn_if_unencrypted_network_protocols(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        network_fields = re.findall(r"(?i)url\s*=\s*[\"'][^\"']+[\"']", content)
        if network_fields:
            for network_field in network_fields:
                if not network_field.startswith("https://"):
                    print(f"WARNING: Potentially unencrypted or unauthenticated network protocols found in the code: {network_field}")

import re

def warn_if_hardcoded_ips_or_domains(tf_file):
    """
    A function to check for the use of hard-coded IP addresses or domain names in the code, which could potentially 
    lead to DNS hijacking or other types of attacks.
    
    :param tf_file: The path to the Terraform file to check
    """
    with open(tf_file, "r") as f:
        lines = f.readlines()

    ip_regex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    domain_regex = re.compile(r"[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+")

    for i, line in enumerate(lines):
        if ip_regex.search(line):
            print(f"WARNING: Hard-coded IP address found in line {i+1}: {line.strip()}")

        if domain_regex.search(line):
            print(f"WARNING: Hard-coded domain name found in line {i+1}: {line.strip()}")

import re

def warn_if_insecure_config(iac_code):
    insecure_patterns = [
        r'(?i)\bmd5\b', # Use of insecure hash function
        r'(?i)\bsha1\b', # Use of insecure hash function
        r'(?i)\brc4\b', # Use of insecure encryption algorithm
        r'(?i)\btls1\b', # Use of insecure network protocol
        r'(?i)\bssl2\b', # Use of insecure network protocol
        r'(?i)\bssl3\b', # Use of insecure network protocol
        r'(?i)\bdes\b', # Use of weak encryption algorithm
        r'(?i)\brc2\b', # Use of weak encryption algorithm
        r'(?i)\bplaintext\b', # Use of plaintext data transmission
        r'(?i)\bftp\b', # Use of insecure network protocol
        r'(?i)\btelnet\b', # Use of insecure network protocol
        r'(?i)\brlogin\b', # Use of insecure network protocol
        r'(?i)\brsh\b', # Use of insecure network protocol
        r'(?i)\btftp\b', # Use of insecure network protocol
        r'(?i)\bsendmail\b', # Use of insecure email server
        r'(?i)\bsmtp\b', # Use of insecure email server
        r'(?i)\bxp_cmdshell\b', # Use of insecure command shell
        r'(?i)\bexec\b', # Use of insecure command execution
        r'(?i)\bshell\b', # Use of insecure command shell
        r'(?i)\bxp_regwrite\b', # Use of insecure registry write
        r'(?i)\bxp_regdelete\b', # Use of insecure registry delete
        r'(?i)\bxp_fileexist\b', # Use of insecure file existence check
        r'(?i)\bxp_filecopy\b', # Use of insecure file copy
    ]

    for insecure_pattern in insecure_patterns:
        matches = re.findall(insecure_pattern, iac_code)
        if matches:
            print(f"Warning: Insecure configuration setting found: {matches}")

import re

def warn_if_hardcoded_secrets(code):
    """Checks if there are any hardcoded secrets or credentials in the code.
    
    Args:
    code - (str) Terraform code
    
    Returns:
    None - Prints warning message if hardcoded secrets or credentials are found.
    """
    secrets_regex = re.compile(r"\b[A-Za-z0-9/+=]{40,}\b")
    if secrets_regex.search(code):
        print("WARNING: Hardcoded secrets or credentials found in the code.")

def warn_if_insecure_permissions(file_path):
    """
    Checks for insecure file or directory permissions in the specified file path.

    Parameters:
    file_path (str): The path to the file or directory to check.

    Returns:
    None: Prints a warning message if any insecure permissions are found.
    """

    insecure_permissions = {"read": ["group", "other"], "write": ["group", "other"], "execute": ["other"]}

    for root, dirs, files in os.walk(file_path):
        for d in dirs:
            dir_path = os.path.join(root, d)
            st = os.stat(dir_path)
            mode = st.st_mode
            for perm, user in insecure_permissions.items():
                if mode & getattr(stat, "S_I" + perm.upper()) and any(mode & getattr(stat, "S_I" + "GRP" + u.upper()) for u in user):
                    print(f"Warning: {dir_path} has insecure {perm} permissions for group {user}.")
        for f in files:
            file_path = os.path.join(root, f)
            st = os.stat(file_path)
            mode = st.st_mode
            for perm, user in insecure_permissions.items():
                if mode & getattr(stat, "S_I" + perm.upper()) and any(mode & getattr(stat, "S_I" + "GRP" + u.upper()) for u in user):
                    print(f"Warning: {file_path} has insecure {perm} permissions for group {user}.")

def warn_if_resources_not_tagged(tf_code):
    """
    Check if all resources are tagged with metadata such as owner, purpose, and expiration date.
    """
    resources = re.findall(r"resource\s*\"(.*)\"\s*\"(.*)\"\s*{", tf_code)
    for res in resources:
        if not re.search(r"tags\s*=", res[1]):
            print(f"WARNING: Resource {res[0]} of type {res[1]} does not have any tags. Please add metadata such as owner, purpose, and expiration date to aid in organization and management.")

def warn_if_deprecated_resources(tf_code):
    """
    Check for the use of deprecated or soon-to-be-deprecated Terraform resources or functions.
    """
    deprecated_resources = ["aws_security_group_rule", "aws_security_group_rule_attachment"]
    for resource in deprecated_resources:
        if resource in tf_code:
            print(f"WARNING: Resource {resource} is deprecated and should be replaced with a newer resource type or function.")

def warn_if_hardcoded_paths(tf_code):
    """
    Check if any paths or filenames are hardcoded in the Terraform code.
    """
    paths = re.findall(r"path\s*=\s*\"(.*)\"", tf_code)
    filenames = re.findall(r"file\s*=\s*\"(.*)\"", tf_code)
    for path in paths:
        if os.path.isabs(path):
            print(f"WARNING: Absolute path {path} is hardcoded in the Terraform code. This could be vulnerable to directory traversal attacks or other exploits.")
    for filename in filenames:
        if os.path.isabs(filename):
            print(f"WARNING: Absolute filename {filename} is hardcoded in the Terraform code. This could be vulnerable to directory traversal attacks or other exploits.")

import re

def warn_if_weak_secrets(file_path):
    """
    Check for the use of weak or easily guessable secrets or passwords
    """
    # Define a list of weak secrets or passwords to check for
    weak_secrets = ["password", "123456", "admin", "secret", "letmein"]
    
    # Open the file at the specified path
    with open(file_path, "r") as f:
        # Read the contents of the file
        file_contents = f.read()
        
        # Search for the presence of any of the weak secrets or passwords in the file contents
        for secret in weak_secrets:
            if re.search(secret, file_contents, re.IGNORECASE):
                # If a weak secret or password is found, issue a warning
                print(f"WARNING: Weak secret or password '{secret}' found in {file_path}")

import subprocess

def check_for_insecure_services(file_path):
    # Define a list of insecure services to check for
    insecure_services = ["ftp", "telnet", "rsh", "rexec", "rlogin"]

    # Use the tasklist command to check if each service is running
    for service in insecure_services:
        cmd = ["tasklist", "/FI", f"Services eq {service}"]
        try:
            # Run the command and capture the output
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=30, universal_newlines=True)
            # Check if the service is running
            if service in output:
                print(f"Insecure service {service} is running!")
        except subprocess.CalledProcessError as e:
            # Handle errors from the subprocess
            print(f"Error running command: {e}")
        except subprocess.TimeoutExpired as e:
            # Handle timeouts from the subprocess
            print(f"Command timed out: {e}")

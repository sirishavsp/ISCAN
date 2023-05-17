
1. `test_warn_if_insecure_permissions(file_path)`: This function checks for insecure file permissions in the specified file path. It reads the file, searches for specific patterns related to file permissions, and returns a list of dictionaries representing any insecure file permissions found in the Terraform file. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

2. `test_check_for_hardcoded_ips_or_domains(file_path)`: This function checks for hard-coded IP addresses or domains in the specified file path. It reads the file, searches for specific patterns related to IP addresses or domains, and returns a list of dictionaries representing any hard-coded IPs or domains found in the Terraform file. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

3. `test_warn_if_unencrypted_network_protocols(file_path)`: This function checks for unencrypted network protocols in the specified file path. It reads the file, searches for specific patterns related to network protocols, and returns a list of dictionaries representing any unencrypted network protocols found in the Terraform file. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

4. `test_check_for_insecure_services(file_path)`: This function checks for insecure services in the specified file path. It reads the file, searches for specific patterns related to insecure services, and returns a list of dictionaries representing any insecure services found in the Terraform file. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

5. `test_check_for_weak_passwords(file_path)`: This function checks for weak passwords and weak secrets in the specified file path. It reads the file, searches for specific patterns related to weak passwords and secrets, and returns a list of dictionaries representing any weak passwords or secrets found in the Terraform file. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

6. `test_warn_if_insecure_config(file_path)`: This function checks for insecure configurations in the specified file path. It reads the file, searches for specific patterns related to insecure configurations, and returns a list of dictionaries representing any insecure configurations found in the Terraform file. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

7. `test_find_duplicates(file_contents)`: This function identifies duplicate lines in the given file contents. It takes the file contents as input, splits the contents into lines, and compares each line with subsequent lines to find duplicates. It returns a list of dictionaries representing the duplicate lines found in the Terraform file. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

8. `test_suggest_security_improvements(file_path)`: This function checks the given Terraform file for security vulnerabilities and suggests improvements. It reads the file, parses the HCL data, and examines specific resource blocks to identify potential security issues. It returns a list of dictionaries representing the security vulnerabilities and suggestions for improvements. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

9. `test_check_for_unintended_destruction(file_path)`: This function parses the Terraform file and identifies any resources or data that may be unintentionally destroyed. It reads the file, parses the HCL data, and examines resource and data blocks to check for the "prevent_destroy" attribute. It returns a list of dictionaries representing the issues found in the Terraform file. Each dictionary contains the keys "issue", "severity", "line_number", and "recommendation".

10. `test_check_for_insecure_system_access()`: This function checks for the use of system resources or services without appropriate permissions or access controls. It returns a boolean value indicating whether insecure system access is found or not.

11. `test_warn_if_vulnerable_libraries()`: This function checks for the use of vulnerable libraries and returns a boolean value indicating whether any vulnerable libraries are found or not.

The `run_terraform_scan(filepath)` function invokes these individual test functions and collects the results. It returns a list of all the results from each test function.
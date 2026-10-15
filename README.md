# CodeAlpha Secure Coding Review - Task 3

This repository contains a security code review, vulnerability assessment, and remediation report conducted as part of the **CodeAlpha Cybersecurity Internship**.

---

## 1. Project Overview
The target application is a Python Flask web service containing intentional security vulnerabilities to demonstrate code auditing, static analysis, and secure coding practices.

---

## 2. Code Audit & Vulnerability Findings

### Vulnerability 1: SQL Injection (SQLi)
- **Location:** `app.py` inside the `/login` route.
- **Severity:** High / Critical
- **Description:** User inputs (`username` and `password`) are directly concatenated into the SQL query string without sanitization or parameterization. 
- **Impact:** An attacker can bypass authentication entirely by injecting malicious SQL payloads (e.g., `' OR '1'='1`).

---

## 3. Tools Used
- **Bandit:** A security linter designed to find common security issues in Python source code.

---

## 4. Remediation & Secure Coding Best Practices

To secure the application against SQL Injection, parameterized queries (prepared statements) must be implemented instead of string formatting:

### Before (Vulnerable):
```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

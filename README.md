# Password Strength Checker 🔒

A **Python CLI tool** to check the strength and security of passwords. It validates passwords against common rules, checks for common passwords, and calculates entropy to measure randomness.

---

## Features ✅
- Detects common passwords from a list (`a.txt`).  
- Checks password rules:
  - Minimum 8 characters  
  - At least one uppercase letter  
  - At least one lowercase letter  
  - At least one digit  
  - At least one special symbol (`@!#$%^&*()<>?/\\|}{~:`)  
- Calculates **entropy** to quantify password strength.  
- Provides **feedback and suggestions** for improvement.  
- Works via **CLI** or interactive prompt.

---

## Usage 💻

Run with a password as argument:

```bash
python password_checker.py "YourPassword123!"
Or run interactively:

python password_checker.py
Enter Password: MyPass123!
Example output:

pgsql
=
🔢 Entropy score: 45.67 bits
❌ Weak password. Issues found in: symbol
👉 Add at least one special symbol.
👉 Entropy is strong — good job.
Installation 🛠️
Clone the repo:


git clone https://github.com/MannanDS/Fernet-File-Locker.git
cd Fernet-File-Locker
Make sure you have Python 3 installed.

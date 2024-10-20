# Zeotap-assignment-rule-engine-weather-system
Rule Engine with AST
# Zeotap-assignment-rule-engine-weather-system

## Application 1: Rule Engine with AST

### Overview
This application implements a simple rule engine using an Abstract Syntax Tree (AST) to determine user eligibility based on various attributes such as age, department, income, and experience. The system allows for dynamic creation, combination, and evaluation of rules.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aj240917/zeotap-assignment-rule-engine-weather-system.git
   cd zeotap-assignment-rule-engine-weather-system/rule_engine

2.Install dependencies (if any):
pip install -r requirements.txt

USAGE 
To create and evaluate rules, you can use the rule_engine.py file. Here are some example commands you can run in a Python environment:

python

from rule_engine import create_rule, evaluate_rule

# Example rule creation
rule = create_rule("((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)")

# Example data for evaluation
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

# Evaluate the rule
result = evaluate_rule(rule, data)
print(result)  # Outputs: True or False
Testing
To run the tests for the rule engine:

bash

python -m unittest test_rule_engine.py
License
This project is licensed under the MIT License.

Contributors
Ayush Joshi


### Instructions for Using the README.md

1. **Create or Edit the README.md File**:
   - Open or create the `README.md` file in your `rule_engine` directory.

2. **Paste the Updated Content**:
   - Copy the updated README content above and paste it into the file.

3. **Save the File**:
   - Save your changes.

4. **Commit and Push**:
   - Follow the previous instructions to commit and push the changes to your GitHub repository.


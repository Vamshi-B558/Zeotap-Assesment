from flask import Flask, request, jsonify
from rule_evaluator import RuleEvaluator  # Adjust the import based on your actual file structure

app = Flask(__name__)
rule_evaluator = RuleEvaluator()

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    data = request.get_json()
    rules = data.get('rules', [])
    attributes = data.get('attributes', {})
    
    result = rule_evaluator.evaluate(rules, attributes)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

class RuleCombiner:
    def combine(self, rules):
        """
        Combine a list of rules into a single rule or AST.
        """
        # Simple example: combine the rules with AND operator
        if not rules:
            return None
        
        combined_rule = f"({rules[0]})"
        
        for rule in rules[1:]:
            combined_rule = f"({combined_rule} AND ({rule}))"
        
        return combined_rule

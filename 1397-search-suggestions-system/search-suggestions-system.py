class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        sorted_products = sorted(products) 
        result = [] 

        for i in range(1, len(searchWord) + 1): 
            prefix = searchWord[:i] 

            idx = bisect_left(sorted_products, prefix) 
            suggestions = [] 

            for j in range(idx, min(idx + 3, len(sorted_products))): 
                if sorted_products[j].startswith(prefix): 
                    suggestions.append(sorted_products[j]) 

            result.append(suggestions) 

        return result 
                                                            
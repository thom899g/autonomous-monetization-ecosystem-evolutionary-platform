import logging
from typing import Dict, List

class KnowledgeBaseInterface:
    def __init__(self):
        self.logger = logging.getLogger("KnowledgeBaseInterface")
        self.logger.setLevel(logging.INFO)
        
        self.strategy_data = {}  # type: Dict[str, Dict]
        
    def save_strategy(self, strategy_name: str, data: Dict) -> None:
        """Saves a monetization strategy and its performance."""
        try:
            self.strategy_data[strategy_name] = data
            self.logger.info(f"Saved strategy {strategy_name}")
        except Exception as e:
            self.logger.error(f"Failed to save strategy: {str(e)}")

    def retrieve_strategy(self, strategy_name: str) -> Optional[Dict]:
        """Retrieves a saved monetization strategy."""
        try:
            return self.strategy_data.get(strategy_name)
        except Exception as e:
            self.logger.error(f"Failed to retrieve strategy: {str(e)}")
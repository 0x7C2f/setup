# plugins/filter/example_filter.py

from ansible.plugins.filter.core import FilterModule as CoreFilterModule

class FilterModule(CoreFilterModule):
    def filters(self):
        return {
            'example_filter': self.example_filter
        }

    def example_filter(self, value):
        # Custom filter logic
        return f"Filtered value: {value}"
# py_logging_test
test configuration for handling logging
- Implements a basic logging setup for a fictitous vfx company - Analog Domain. 
- separates loggers into root and ad loggers
- provides a custom filter to decorate LogRecords with contextual Analog Domain information gleaned from the environment
- provides a custom function to update a config dict with another config dict provided the supplied predicate evaluates to true
- run example.py to see this in action

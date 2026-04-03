# Step 1: Import the module normally first
import orchestrator

# Step 2: Force Python to reload the module to pick up any changes
import importlib
importlib.reload(orchestrator)

# Step 3: Import the updated class or function from the reloaded module
from orchestrator import Run

# Step 4: Use the class as usual
orchestrate = Run()
df = orchestrate.file_upload()
date_validation = orchestrate.validate_date()
key_validation = orchestrate.validate_key()

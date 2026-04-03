# Step 1: Import the module normally first
import orchestrator

# Step 2: Force Python to reload the module to pick up any changes
import importlib
importlib.reload(orchestrator)

# Step 3: Import the updated class
from orchestrator import Run

# Step 4: Run the pipeline (MAIN ENTRY POINT)
orchestrate = Run()
orchestrate.run()

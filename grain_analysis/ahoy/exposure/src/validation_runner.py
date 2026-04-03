%%writefile validation_runner.py
import importlib

def load_validation_modules():
    """
    Wrapper function to dynamically import/reload validation modules
    and fetch their main functions/classes.
    Returns a dictionary with callable references.
    """
    # List of module names in order
    modules_to_reload = [
        "upload",
        "validate_date",
        "validate_key",
        "orchestrator"
    ]

    # Dictionary to store the reloaded modules
    reloaded_modules = {}

    # Import/reload modules
    for mod_name in modules_to_reload:
        if mod_name in globals():
            mod = globals()[mod_name]
            # globals() is a special built-in Python function (we don't define it)
            # that gives a box of all the stuff (variables, modules) in this file.
            # We check it to see if a module is already loaded before importing or reloading it
            importlib.reload(mod)
        else:
            mod = importlib.import_module(mod_name) # get the module because it’s not loaded yet
            # import_module is a function inside importlib
            # import_module loads a module by its name so we can use it in the code
            reloaded_modules[mod_name] = mod # save it in the dictionary for later use

    # Grab functions/classes
    modules_refs = {
        "load": getattr(reloaded_modules["upload"], "upload_file"),
        "valid_key": getattr(reloaded_modules["validate_key"], "validate_primary_key"),
        "valid_date": getattr(reloaded_modules["validate_date"], "DateValidation"),
        "Run": getattr(reloaded_modules["orchestrator"], "Run")
        # getattr → just grabs the function/class object from the module, ready to run.
        # Nothing executes yet; you just have a reference.
    }

    return modules_refs

#!/usr/bin/env python3
"""
Baby's First Computer - Installation Test Script

This script verifies that the installation is working correctly.
Run this script to check if all dependencies are installed and
the project is ready to use.
"""

import sys
import os
import subprocess
from importlib.metadata import version, PackageNotFoundError


def print_success(message):
    """Print success message in green."""
    print(f"✅ {message}")


def print_warning(message):
    """Print warning message in yellow."""
    print(f"⚠️  {message}")


def print_error(message):
    """Print error message in red."""
    print(f"❌ {message}")


def print_info(message):
    """Print info message in cyan."""
    print(f"ℹ️  {message}")


def check_python_version():
    """Check if Python version meets requirements (>= 3.7)."""
    print_info("Checking Python version...")
    
    python_version = sys.version_info
    min_version = (3, 7)
    
    if python_version >= min_version:
        print_success(f"Python {python_version.major}.{python_version.minor}.{python_version.micro} is compatible (requires >= 3.7)")
        return True
    else:
        print_error(f"Python {python_version.major}.{python_version.minor}.{python_version.micro} is too old. Requires Python >= 3.7")
        return False


def check_package(package_name, min_version=None):
    """Check if a package is installed and meets minimum version requirements."""
    try:
        installed_version = version(package_name)
        
        if min_version:
            # Simple version comparison
            installed_parts = list(map(int, installed_version.split('.')[:3]))
            min_parts = list(map(int, min_version.split('.')[:3]))
            
            if installed_parts >= min_parts:
                print_success(f"{package_name} {installed_version} is installed (requires >= {min_version})")
                return True
            else:
                print_error(f"{package_name} {installed_version} is installed but version is too old. Requires >= {min_version}")
                return False
        else:
            print_success(f"{package_name} {installed_version} is installed")
            return True
            
    except PackageNotFoundError:
        print_error(f"{package_name} is not installed")
        return False


def check_pygame():
    """Special check for pygame with fallback for older Python versions."""
    try:
        import pygame
        pygame_version = pygame.version.ver
        
        # Check if it's at least 2.0.0
        version_parts = list(map(int, pygame_version.split('.')[:3]))
        if version_parts >= [2, 0, 0]:
            print_success(f"pygame {pygame_version} is installed (requires >= 2.0.0)")
            return True
        else:
            print_error(f"pygame {pygame_version} is installed but version is too old. Requires >= 2.0.0")
            return False
            
    except ImportError:
        print_error("pygame is not installed")
        return False


def test_import_main_script():
    """Test if the main Python script can be imported without errors."""
    print_info("Testing import of main game script...")
    
    script_path = os.path.join("python", "babycolor.py")
    
    if not os.path.exists(script_path):
        print_error(f"Main script not found at: {script_path}")
        return False
    
    try:
        # Add python directory to path for import
        sys.path.insert(0, "python")
        
        # Try to import the module
        import babycolor
        
        # Check if main function exists
        if hasattr(babycolor, 'main'):
            print_success("Main script imports successfully and has a main() function")
            return True
        else:
            print_warning("Main script imports but doesn't have a main() function")
            return False
            
    except ImportError as e:
        print_error(f"Failed to import main script: {e}")
        return False
    except Exception as e:
        print_error(f"Unexpected error importing main script: {e}")
        return False
    finally:
        # Clean up path modification
        if "python" in sys.path:
            sys.path.remove("python")


def check_web_files():
    """Check if required web files exist."""
    print_info("Checking web files...")
    
    web_files = [
        "web/index.html",
    ]
    
    all_files_exist = True
    
    for web_file in web_files:
        if os.path.exists(web_file):
            print_success(f"{web_file} exists")
        else:
            print_error(f"{web_file} not found")
            all_files_exist = False
    
    return all_files_exist


def check_requirements_file():
    """Check if requirements.txt exists."""
    print_info("Checking requirements file...")
    
    if os.path.exists("requirements.txt"):
        print_success("requirements.txt exists")
        return True
    else:
        print_warning("requirements.txt not found")
        return False


def main():
    """Run all installation checks."""
    print("=" * 60)
    print("Baby's First Computer - Installation Test")
    print("=" * 60)
    print()
    
    results = []
    
    # Run all checks
    results.append(("Python Version", check_python_version()))
    print()
    
    results.append(("pygame", check_pygame()))
    results.append(("numpy", check_package("numpy", "1.20.0")))
    print()
    
    results.append(("Main Script Import", test_import_main_script()))
    print()
    
    results.append(("Web Files", check_web_files()))
    print()
    
    check_requirements_file()
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    # Count results
    total = len(results)
    passed = sum(1 for _, status in results if status)
    failed = total - passed
    
    print(f"Total checks: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    # Print detailed results
    for check_name, status in results:
        status_symbol = "✅" if status else "❌"
        print(f"  {status_symbol} {check_name}")
    
    print()
    
    if failed == 0:
        print_success("All checks passed! Installation is working correctly.")
        print()
        print("You can run the game with:")
        print("  python python/babycolor.py")
        print("  or")
        print("  babygame  (if installed with pip)")
    else:
        print_error(f"{failed} check(s) failed. Please fix the issues above.")
        print()
        print("To install missing dependencies, run:")
        print("  pip install -r requirements.txt")
        print("  or")
        print("  pip install pygame>=2.0.0 numpy>=1.20.0")
    
    print()
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

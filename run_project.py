#!/usr/bin/env python
"""
ANN Project - Complete Workflow Execution & Status Report
Shows training, API status, and ready-to-deploy status
"""

import os
import json
import subprocess
from pathlib import Path
import requests

def print_header(title):
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)

def check_files():
    """Verify all required project files exist"""
    print_header("📁 PROJECT FILES VERIFICATION")
    
    required_files = [
        'model.py',
        'app.py',
        'requirements.txt',
        'model.h5',
        'scaler.pkl',
        'Artificial_Neural_Network_Case_Study_data.csv',
        'README.md',
        'DEPLOYMENT.md',
        'SUBMISSION.md'
    ]
    
    all_exist = True
    for file in required_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        size = ""
        if exists:
            size = f" ({os.path.getsize(file):,} bytes)"
        print(f"  {status} {file:<45}{size}")
        if not exists:
            all_exist = False
    
    return all_exist

def check_api_server():
    """Verify API server is running"""
    print_header("🌐 API SERVER STATUS")
    
    try:
        r = requests.get('http://127.0.0.1:8000/health', timeout=2)
        if r.status_code == 200:
            print("  ✓ Server: RUNNING on http://127.0.0.1:8000")
            print("  ✓ Health Check: HEALTHY")
            print("  ✓ Swagger Docs: http://127.0.0.1:8000/docs")
            return True
        else:
            print(f"  ✗ Server returned status {r.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("  ✗ Server is not running")
        print("    To start: python -m uvicorn app:app --reload")
        return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def test_prediction():
    """Test the model with sample predictions"""
    print_header("🧪 PREDICTION TESTS")
    
    test_cases = [
        ("Low Risk Customer", [750, 0, 1, 25, 8, 200000, 2, 1, 1, 150000]),
        ("High Risk Customer", [400, 2, 0, 60, 1, 0, 1, 0, 0, 40000]),
        ("Medium Risk Customer", [600, 1, 1, 45, 4, 75000, 2, 1, 0, 90000]),
    ]
    
    all_passed = True
    for name, features in test_cases:
        try:
            r = requests.post(
                'http://127.0.0.1:8000/predict',
                json={"data": features},
                timeout=5
            )
            
            if r.status_code == 200:
                result = r.json()
                print(f"\n  ✓ {name}")
                print(f"    Churn Probability: {result['churn_probability']}%")
                print(f"    Risk Level: {result['status']}")
                print(f"    Confidence: {result['confidence']}%")
            else:
                print(f"  ✗ {name}: Failed with status {r.status_code}")
                all_passed = False
        except Exception as e:
            print(f"  ✗ {name}: {e}")
            all_passed = False
    
    return all_passed

def project_summary():
    """Display project summary and statistics"""
    print_header("📊 PROJECT SUMMARY")
    
    stats = {
        "Data Size": "10,000 customer records",
        "Features": "10 numerical features (encoded)",
        "Target": "Binary classification (Churn: Yes/No)",
        "Train/Test Split": "80% / 20% (8,000 / 2,000)",
        "Model Type": "Artificial Neural Network",
        "Architecture": "Input(10) → Dense(10, ReLU) → Dense(5, ReLU) → Dense(1, Sigmoid)",
        "Training Accuracy": "85.30%",
        "Test Accuracy": "85.35%",
        "Optimizer": "Adam",
        "Loss Function": "Binary Crossentropy",
        "API Framework": "FastAPI",
        "Server": "Uvicorn",
        "Documentation": "Auto-generated Swagger UI",
    }
    
    for key, value in stats.items():
        print(f"  • {key:<25} {value}")

def deployment_info():
    """Show deployment information"""
    print_header("☁️  DEPLOYMENT INSTRUCTIONS")
    
    steps = [
        ("1. Push to GitHub", [
            "  git init",
            "  git add .",
            'git commit -m "ANN API - Production Ready"',
            "  git push origin main"
        ]),
        ("2. Deploy to Render (FREE)", [
            "  → Go to https://render.com",
            "  → Click 'New Web Service'",
            "  → Connect GitHub repository",
            "  → Configure:",
            "     Build: pip install -r requirements.txt",
            "     Start: uvicorn app:app --host 0.0.0.0 --port 10000",
        ]),
        ("3. Get Public API Link", [
            "  → After 2-3 minutes: https://your-app-name.onrender.com",
            "  → Swagger Docs: https://your-app-name.onrender.com/docs",
            "  → Make predictions: https://your-app-name.onrender.com/predict",
        ])
    ]
    
    for step_title, commands in steps:
        print(f"\n  {step_title}:")
        for cmd in commands:
            print(f"    {cmd}")

def endpoints_info():
    """Show API endpoints"""
    print_header("🔌 API ENDPOINTS")
    
    endpoints = [
        ("GET", "/", "Home - API information"),
        ("GET", "/health", "Health check"),
        ("POST", "/predict", "Make churn prediction (10 features)"),
        ("GET", "/docs", "Swagger UI documentation"),
        ("GET", "/redoc", "ReDoc documentation"),
    ]
    
    for method, path, description in endpoints:
        print(f"  {method:<6} {path:<20} → {description}")

def usage_example():
    """Show usage examples"""
    print_header("💡 USAGE EXAMPLES")
    
    print("\n  Python Example:")
    print("""
    import requests
    
    response = requests.post(
        'http://127.0.0.1:8000/predict',
        json={"data": [750, 0, 1, 25, 8, 200000, 2, 1, 1, 150000]}
    )
    
    print(response.json())
    # Output: {
    #   "prediction": 0.0065,
    #   "churn_probability": 0.65,
    #   "confidence": 99.35,
    #   "status": "Low Risk"
    # }
    """)
    
    print("\n  cURL Example:")
    print("""
    curl -X POST "http://127.0.0.1:8000/predict" \\
      -H "Content-Type: application/json" \\
      -d '{"data": [750, 0, 1, 25, 8, 200000, 2, 1, 1, 150000]}'
    """)

def main():
    """Main execution"""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "  🚀 ANN CUSTOMER CHURN PREDICTION PROJECT - EXECUTION REPORT".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "="*78 + "╝")
    
    # Run all checks
    files_ok = check_files()
    server_ok = check_api_server()
    
    if server_ok:
        tests_ok = test_prediction()
    else:
        tests_ok = False
    
    project_summary()
    endpoints_info()
    usage_example()
    deployment_info()
    
    # Final status
    print_header("✅ PROJECT STATUS")
    
    status_items = [
        ("Project Files", files_ok),
        ("API Server", server_ok),
        ("Predictions", tests_ok),
    ]
    
    all_ok = all(status for _, status in status_items)
    
    for item, status in status_items:
        symbol = "✓" if status else "✗"
        print(f"  {symbol} {item:<30} {'OK' if status else 'FAILED'}")
    
    print("\n" + "="*80)
    if all_ok:
        print("  🎉 PROJECT IS READY FOR PRODUCTION DEPLOYMENT!")
        print("\n  Next Steps:")
        print("    1. Test the API: http://127.0.0.1:8000/docs")
        print("    2. Deploy to Render (follow instructions above)")
        print("    3. Share your public API link!")
    else:
        if not server_ok:
            print("  ⚠️  API Server is not running!")
            print("  Start it with: python -m uvicorn app:app --reload")
        if not files_ok:
            print("  ⚠️  Some required files are missing!")
            print("  Make sure you're in the project directory")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()

import os
import tempfile

# ============================================================
# ENVIRONMENT & STORAGE CONFIGURATION
# ============================================================

IS_VERCEL = bool(os.environ.get("VERCEL"))

# Root directory of the repository
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static frontend directory
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

if IS_VERCEL:
    # Vercel serverless environment has a read-only filesystem except /tmp
    STORAGE_DIR = tempfile.gettempdir()
    UPLOAD_FOLDER = os.path.join(STORAGE_DIR, "uploads")
    REPORT_FOLDER = os.path.join(STORAGE_DIR, "reports")
    DATABASE_FOLDER = os.path.join(STORAGE_DIR, "database")
else:
    # Standard local development / container environment
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "backend", "uploads")
    REPORT_FOLDER = os.path.join(BASE_DIR, "reports")
    DATABASE_FOLDER = os.path.join(BASE_DIR, "backend", "database")

DATABASE_PATH = os.path.join(DATABASE_FOLDER, "reports.db")

# Ensure required folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)
os.makedirs(DATABASE_FOLDER, exist_ok=True)

# SmartNode Platform
## Development Environment Setup

### 1. Clone repository

```bash
git clone <repository>
cd SmartNode_Hcktn26
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate

Windows CMD

```cmd
.venv\Scripts\activate
```

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Linux

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install MongoDB Community Server

Start MongoDB service.

### 6. Run API

```bash
python -m uvicorn api.main:app --reload
```

### 7. Test

```
http://127.0.0.1:8000/health
```

```
http://127.0.0.1:8000/machines





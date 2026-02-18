# Executive Lens — GHC Business Case Workshop
## Setup & Deployment Guide

---

## Project Structure

```
executive-lens/
├── app_engine.py          # Core logic, UI, AI coaching (shared)
├── shared_styles.py       # CSS design system (shared)
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── secrets.toml       # Your API key (never commit this)
├── scenario_1/app.py      # The AI Tool Nobody Approved
├── scenario_2/app.py      # The Feature That Keeps Getting Bumped
├── scenario_3/app.py      # The Headcount Request
├── scenario_4/app.py      # The Infrastructure Upgrade
└── scenario_5/app.py      # The New Market Opportunity
```

---

## Local Development

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your API key
Edit `.streamlit/secrets.toml`:
```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```

### 3. Run any scenario
```bash
# From the executive-lens root directory:
streamlit run scenario_1/app.py
streamlit run scenario_2/app.py
# etc.
```

---

## Deploying to Streamlit Community Cloud (Recommended for Workshop)

Deploy each scenario as a **separate Streamlit app** so load is distributed.

### Steps (repeat for each scenario):

1. **Push to GitHub**
   - Create one GitHub repo (e.g. `executive-lens`)
   - Push the entire project

2. **Deploy on Streamlit Community Cloud** (streamlit.io/cloud)
   - Click "New app"
   - Select your repo
   - Set the **Main file path** to: `scenario_1/app.py` (change per scenario)
   - Under **Advanced settings → Secrets**, paste:
     ```
     ANTHROPIC_API_KEY = "sk-ant-your-key-here"
     ```
   - Deploy

3. **Repeat** for scenarios 2–5, changing only the main file path

### You'll get 5 URLs like:
```
https://executive-lens-s1.streamlit.app
https://executive-lens-s2.streamlit.app
https://executive-lens-s3.streamlit.app
https://executive-lens-s4.streamlit.app
https://executive-lens-s5.streamlit.app
```

---

## Workshop Day Setup

### Table Assignment
| Table | Scenario | QR Code URL |
|-------|----------|-------------|
| 1A, 1B, 1C, 1D | Scenario 1 | executive-lens-s1.streamlit.app |
| 2A, 2B, 2C, 2D | Scenario 2 | executive-lens-s2.streamlit.app |
| 3A, 3B, 3C, 3D | Scenario 3 | executive-lens-s3.streamlit.app |
| 4A, 4B, 4C, 4D | Scenario 4 | executive-lens-s4.streamlit.app |
| 5A, 5B, 5C, 5D | Scenario 5 | executive-lens-s5.streamlit.app |

### Generate QR Codes
Use qr-code-generator.com or similar — one QR per scenario URL.
Print and place on tables before the session.

### Pre-Workshop Checklist
- [ ] All 5 apps deployed and accessible
- [ ] API key loaded in Streamlit secrets for each app
- [ ] Test each app end-to-end the day before
- [ ] QR codes printed and on tables
- [ ] Backup: screenshot of model answers in case of WiFi issues
- [ ] Projector showing QR codes at session start

---

## The App Flow (What Attendees Experience)

1. Scan QR code → land on their scenario
2. Read the scenario card
3. **Stage 1 — Executive Translation**
   - Answer: "How would you approach your business leaders to get this approved?"
   - Get scored /10 with coaching + one coaching question
   - Up to 3 attempts; auto-advance at 8+ or after 3 tries
   - See model answer with explanation before Stage 2
4. **Stage 2 — Financial Credibility**
   - Same structure — financial framing challenge
   - Up to 3 attempts, model answer revealed
5. **Stage 3 — Hard Questions**
   - AI generates 2 tough executive pushback questions
   - Attendee responds once
   - Receives final score + closing coaching insight
6. **Completion screen** — average score across all 3 stages

---

## Customization

### To change the pass threshold (currently 8/10):
Edit `app_engine.py` line: `PASS_SCORE = 8`

### To change max attempts (currently 3):
Edit `app_engine.py` line: `MAX_ATTEMPTS_PER_STAGE = 3`

### To update a scenario:
Edit only the relevant `scenario_X/app.py` — the engine is untouched.

### To rebrand:
Edit `shared_styles.py` for colors/fonts and the `el-logo` div in `render_header()` in `app_engine.py`.

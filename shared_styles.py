EXECUTIVE_LENS_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --gold: #C9A84C;
    --gold-light: #E8C97A;
    --dark: #0D0D0D;
    --dark-2: #161616;
    --dark-3: #1E1E1E;
    --dark-4: #2A2A2A;
    --text-primary: #F0EDE8;
    --text-secondary: #A09A8E;
    --text-muted: #666;
    --border: rgba(201, 168, 76, 0.2);
    --border-strong: rgba(201, 168, 76, 0.5);
    --success: #4CAF82;
    --warning: #E8A44C;
}

/* Global reset */
.stApp {
    background-color: var(--dark) !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Hide streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 2rem !important;
    max-width: 860px !important;
}

/* ── HEADER ── */
.el-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.2rem 2rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
    background: linear-gradient(180deg, rgba(201,168,76,0.06) 0%, transparent 100%);
}
.el-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--gold);
    letter-spacing: 0.05em;
}
.el-logo span {
    color: var(--text-secondary);
    font-weight: 400;
    font-size: 0.85rem;
    display: block;
    font-family: 'DM Sans', sans-serif;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}
.el-badge {
    background: rgba(201,168,76,0.1);
    border: 1px solid var(--border-strong);
    color: var(--gold);
    padding: 0.3rem 0.8rem;
    border-radius: 2px;
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* ── SCENARIO CARD ── */
.scenario-card {
    background: var(--dark-2);
    border: 1px solid var(--border);
    border-left: 3px solid var(--gold);
    border-radius: 4px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.5rem;
    position: relative;
}
.scenario-label {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.6rem;
}
.scenario-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    color: var(--text-primary);
    margin-bottom: 1rem;
    font-weight: 600;
}
.scenario-body {
    color: var(--text-secondary);
    font-size: 0.92rem;
    line-height: 1.75;
}
.scenario-ask {
    margin-top: 1.2rem;
    padding: 1rem 1.2rem;
    background: rgba(201,168,76,0.06);
    border-left: 2px solid var(--gold);
    color: var(--text-primary);
    font-size: 0.9rem;
    border-radius: 0 4px 4px 0;
}

/* ── STAGE INDICATOR ── */
.stage-track {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    align-items: center;
}
.stage-pip {
    height: 4px;
    flex: 1;
    border-radius: 2px;
    background: var(--dark-4);
    transition: background 0.4s ease;
}
.stage-pip.active { background: var(--gold); }
.stage-pip.complete { background: var(--success); }
.stage-label {
    font-size: 0.72rem;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    white-space: nowrap;
}
.stage-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    color: var(--text-primary);
    margin-bottom: 0.3rem;
}
.stage-subtitle {
    font-size: 0.82rem;
    color: var(--text-muted);
    margin-bottom: 1.2rem;
}

/* ── CHAT MESSAGES ── */
.msg-user {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 1rem;
}
.msg-user .bubble {
    background: rgba(201,168,76,0.12);
    border: 1px solid var(--border);
    color: var(--text-primary);
    padding: 0.9rem 1.2rem;
    border-radius: 12px 12px 2px 12px;
    max-width: 78%;
    font-size: 0.9rem;
    line-height: 1.6;
}
.msg-ai {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 1rem;
    gap: 0.6rem;
    align-items: flex-start;
}
.msg-ai .avatar {
    width: 28px;
    height: 28px;
    background: var(--gold);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.65rem;
    color: var(--dark);
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 2px;
    letter-spacing: 0.03em;
}
.msg-ai .bubble {
    background: var(--dark-3);
    border: 1px solid var(--dark-4);
    color: var(--text-secondary);
    padding: 0.9rem 1.2rem;
    border-radius: 2px 12px 12px 12px;
    max-width: 78%;
    font-size: 0.9rem;
    line-height: 1.7;
}

/* ── SCORE BADGE ── */
.score-row {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 0.6rem;
}
.score-badge {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
}
.score-badge .denom {
    font-size: 0.9rem;
    color: var(--text-muted);
    font-family: 'DM Sans', sans-serif;
}
.score-bar-track {
    flex: 1;
    height: 6px;
    background: var(--dark-4);
    border-radius: 3px;
    overflow: hidden;
}
.score-bar-fill {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, var(--gold), var(--gold-light));
    transition: width 0.6s ease;
}

/* ── MODEL ANSWER ── */
.model-answer {
    background: linear-gradient(135deg, rgba(201,168,76,0.08), rgba(201,168,76,0.03));
    border: 1px solid var(--border-strong);
    border-radius: 6px;
    padding: 1.5rem;
    margin: 1rem 0;
}
.model-answer-label {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}
.model-answer-label::before {
    content: '★';
    font-size: 0.8rem;
}
.model-answer p {
    color: var(--text-primary);
    font-size: 0.92rem;
    line-height: 1.75;
    margin: 0;
}

/* ── ATTEMPTS COUNTER ── */
.attempts-row {
    display: flex;
    gap: 0.4rem;
    align-items: center;
    margin-bottom: 1rem;
}
.attempt-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--dark-4);
    border: 1px solid var(--border);
}
.attempt-dot.used { background: var(--gold); border-color: var(--gold); }
.attempt-dot.remaining { background: transparent; border-color: var(--border-strong); }
.attempts-text {
    font-size: 0.75rem;
    color: var(--text-muted);
    margin-left: 0.3rem;
}

/* ── INPUT AREA ── */
.stTextArea textarea {
    background: var(--dark-3) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    color: var(--text-primary) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    line-height: 1.65 !important;
    padding: 1rem !important;
    resize: vertical !important;
}
.stTextArea textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 1px rgba(201,168,76,0.3) !important;
}
.stTextArea textarea::placeholder { color: var(--text-muted) !important; }

/* ── BUTTONS ── */
.stButton > button {
    background: var(--gold) !important;
    color: var(--dark) !important;
    border: none !important;
    border-radius: 3px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.05em !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: var(--gold-light) !important;
    transform: translateY(-1px) !important;
}
.stButton > button[disabled] {
    background: var(--dark-4) !important;
    color: var(--text-muted) !important;
    transform: none !important;
}

/* ── COMPLETION SCREEN ── */
.completion-card {
    text-align: center;
    padding: 3rem 2rem;
    background: var(--dark-2);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    margin: 2rem 0;
}
.completion-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}
.completion-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: var(--gold);
    margin-bottom: 0.5rem;
}
.completion-sub {
    color: var(--text-secondary);
    font-size: 0.9rem;
    max-width: 400px;
    margin: 0 auto 1.5rem;
    line-height: 1.7;
}
.final-score-display {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    color: var(--gold);
    font-weight: 700;
}
.final-score-label {
    font-size: 0.8rem;
    color: var(--text-muted);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 0.3rem;
}

/* ── DIVIDER ── */
.el-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5rem 0;
}

/* streamlit containers */
div[data-testid="stVerticalBlock"] > div { background: transparent !important; }
</style>
"""

# mini_ai_agent
---

### Python 3.10+ recommended
### Installation
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### Create and update the configuration in `.env` file from `.env.example`
   ```shell
   cp .env.example .env
   ```
- Now edit the `.env` file for your local configuration
### Run
```bash
python main.py
```
### Example output
```bash
Welcome to the AI Agent System. Type your query (or 'exit'):
hello
Evaluating query: hello
Response: Hello there! How can I help you today?

What is 12.5% of 243
Evaluating query: What is 12.5% of 243
Response: 12.5% of 243 is (12.5/100) * 243 = 0.125 * 243 = 30.375

```

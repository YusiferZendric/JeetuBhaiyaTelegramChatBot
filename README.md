# Telegram Chatbot

This is a Telegram chatbot that uses the `neuralintents` library for natural language processing and integrates with various APIs to provide responses to user queries.

## Files

- `bot.py`: Contains the `telegram_chatbot` class for interacting with the Telegram API.
- `chatbot.py`: Contains the `reply` function which processes user messages and generates responses.
- `main.py`: The main script that runs the bot, fetching updates and sending responses.
- `intents.json`: Contains the training data for the chatbot.
- `manners.json`, `questions.json`, `rankings.json`: JSON files used for storing user data and questions.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Telegram bot:**
   - Create a new bot on Telegram by talking to [BotFather](https://core.telegram.org/bots#botfather).
   - Replace the `self.token` value in `bot.py` with your bot's token.

4. **Run the bot:**
   ```bash
   python main.py
   ```

## Usage

- **Casual Chatting:** Just mention "jeetu" in your text.
- **Contribute a Question:** `jeetu question of (subject name) is (question content) answer (answer content)`
- **Get an Answer:** `jeetu answer of [question number] of [subject]`
- **Ask a Question:** `jeetu give me question of (subject name)`
- **Get Information:** `jeetu who is [name]` or `jeetu what is [topic]`
- **Solve a Query:** `jeetu solve [query]`
- **Check Leaderboard:** `jeetu leaderboard` or `jeetu lb`
- **Help:** `jeetu help`

# Discord F1 Bot 🏎️

A Discord bot that provides real-time Formula 1 information, including standings, race results, schedules, news, and more. Built with Python and Discord.py.

## Features 🚀

- **F1 Standings**: Get current driver and constructor standings
- **Race Results**: View the most recent race results
- **Race Schedule**: Check upcoming F1 race dates
- **F1 News**: Latest Formula 1 news from Motorsport.com
- **Driver Information**: Get details about F1 drivers
- **Random F1 GIFs**: Fun F1-related GIFs from Giphy
- **Real-time Updates**: Live data from F1 APIs

## Commands 📋

| Command | Description |
|---------|-------------|
| `$gif` | Get a random F1 GIF |
| `$standings` | Get current F1 driver standings |
| `$constructorstandings` | Get current F1 constructor standings |
| `$results` | Get most recent F1 race results |
| `$schedule` | Get current F1 race schedule |
| `$news` | Get latest F1 news |
| `$driver` | Get information about a specific F1 driver |
| `$team` | Get information about a specific F1 team |
| `$help` | Display this help message |

## Prerequisites 📋

- Python 3.7 or higher
- Discord Bot Token
- News API Key
- Giphy API Key (optional, for GIFs)

## Installation 🛠️

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd Discord_Bot
   ```

2. **Install required Python packages**
   ```bash
   pip install discord.py requests newsapi-python
   ```

3. **Configure your bot**
   - Create a Discord application and bot at [Discord Developer Portal](https://discord.com/developers/applications)
   - Get your bot token
   - Get a News API key from [NewsAPI](https://newsapi.org/)
   - Update the `config.json` file with your keys

4. **Set up config.json**
   ```json
   {
       "token": "YOUR_DISCORD_BOT_TOKEN",
       "api_key": "YOUR_API_KEY",
       "news_api_key": "YOUR_NEWS_API_KEY"
   }
   ```

## Usage 🚀

1. **Start the bot**
   ```bash
   python Discord_Bot.py
   ```

2. **Invite the bot to your server**
   - Use the OAuth2 URL from Discord Developer Portal
   - Select the necessary permissions (Send Messages, Read Message History)

3. **Use commands in Discord**
   - Type `$help` to see all available commands
   - Use any of the commands listed above in your Discord server

## API Sources 🌐

- **F1 Data**: [Ergast API](https://ergast.com/mrd/) via Jolpi
- **News**: [NewsAPI](https://newsapi.org/) - Motorsport.com articles
- **GIFs**: [Giphy API](https://giphy.com/)

## Project Structure 📁

```
Discord_Bot/
├── Discord_Bot.py      # Main bot file with all functionality
├── f1_news.py          # Standalone F1 news script
├── config.json         # Configuration file with API keys
└── README.md           # This file
```

## Features in Detail 🔍

### Driver Standings
- Shows top 20 drivers with position, points, and wins
- Includes team information for each driver

### Constructor Standings
- Displays team standings with points and wins
- Shows current constructor championship order

### Race Results
- Automatically finds the most recent race with results
- Shows top 20 finishers with points

### Race Schedule
- Complete F1 season calendar
- Includes round numbers and dates

### F1 News
- Latest 5 articles from Motorsport.com
- Focused on Formula 1 content
- Includes article links and descriptions

## Troubleshooting 🔧

**Bot not responding?**
- Check if the bot is running
- Verify your Discord bot token is correct
- Ensure the bot has proper permissions in your server

**API errors?**
- Verify your API keys are correct
- Check if you've exceeded API rate limits
- Ensure internet connectivity

**Commands not working?**
- Make sure the bot has permission to send messages
- Check if the bot is online in your server
- Try using `$help` to see available commands

## Contributing 🤝

Feel free to contribute to this project by:
- Adding new F1-related commands
- Improving error handling
- Adding more data sources
- Enhancing the user interface

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Support 💬

If you encounter any issues or have questions:
- Check the troubleshooting section above
- Review the Discord.py documentation
- Ensure all dependencies are properly installed

---

**Happy Racing! 🏁**

*Built with ❤️ for the F1 community*

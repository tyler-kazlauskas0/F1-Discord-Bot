from os import name
import discord  
import requests
import json
from newsapi import NewsApiClient


with open('config.json') as f:
  d= json.load(f)
  token = d['token']
  api_key = d['api_key']
  news_api_key = d['news_api_key']
  


def get_gif():
    # always assign to the same name before you use it
    response = requests.get('https://api.giphy.com/v1/gifs/random?api_key=ypaas79YLlE4VbcUQLISZHU8ytmOf98i&tag=F1&rating=g')
    # you can also shortcut to .json()
    data = response.json()
    first = data['data']
    page_url = first['url']
    return page_url

def get_standings():
    url = "https://api.jolpi.ca/ergast/f1/2025/driverstandings/"
    response = requests.get(url)
    data = response.json()

    # Navigate to the correct part of the JSON
    try:
        standings = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    except (KeyError, IndexError):
        return "No standings data available."

    message = "**F1 Driver Standings:**\n"
    for driver in standings[:20]:  # Show top 20
        pos = driver.get("position")
        points = driver.get("points")
        wins = driver.get("wins")
        driver_info = driver.get("Driver", {})
        name = f"{driver_info.get('givenName', '')} {driver_info.get('familyName', '')}"
        team = driver.get("Constructors", [{}])[0].get("name", "Unknown")
        message += f"{pos}. {name} ({team}) - {points} pts, {wins} wins\n"
    return message

def get_constructor_standings():
  url = "https://api.jolpi.ca/ergast/f1/2025/constructorstandings/"
  response = requests.get(url)
  data = response.json()
  standings = data["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]
  message = "**F1 Constructor Standings:**\n"
  for constructor in standings[:20]:
    pos = constructor.get("position")
    points = constructor.get("points")
    wins = constructor.get("wins")
    constructor_info = constructor.get("Constructor", {})
    name = constructor_info.get("name", "")
    message += f"{pos}. {name} - {points} pts, {wins} wins\n"
  return message

def get_results():
    # Step 1: Get the schedule to find all rounds
    schedule_url = "https://api.jolpi.ca/ergast/f1/2025.json"
    schedule_response = requests.get(schedule_url)
    schedule_data = schedule_response.json()
    races = schedule_data["MRData"]["RaceTable"]["Races"]
    if not races:
        return "No races found for this season."

    # Step 2: Work backwards to find the latest race with results
    for race in reversed(races):
        round_num = race["round"]
        results_url = f"https://api.jolpi.ca/ergast/f1/2025/{round_num}/results.json"
        results_response = requests.get(results_url)
        results_data = results_response.json()
        try:
            results = results_data["MRData"]["RaceTable"]["Races"][0]["Results"]
            if results:  # If results exist, return them
                message = f"**F1 Race Results ({race['raceName']}):**\n"
                for result in results[:20]:
                    pos = result.get("position")
                    driver_info = result.get("Driver", {})
                    name = f"{driver_info.get('givenName', '')} {driver_info.get('familyName', '')}"
                    message += f"{pos}. {name} - {result.get('points', 'N/A')} pts\n"
                return message
        except (KeyError, IndexError):
            continue  # No results for this race, check the previous one

    return "No race results available yet for this season."

def get_schedule():
  Schedule_URL = "https://api.jolpi.ca/ergast/f1/2025/races/"
  Schedule_Response = requests.get(Schedule_URL)
  Schedule_Data = Schedule_Response.json()
  races = Schedule_Data["MRData"]["RaceTable"]["Races"]
  if not races:
    return "No races found for this season."
  message = "**F1 Schedule:**\n"
  for race in races:
    message += f"{race['round']}. {race['raceName']} - {race['date']}\n"
  return message

def get_news():
    API_KEY = news_api_key
    newsapi = NewsApiClient(api_key=API_KEY)
    all_articles = newsapi.get_everything(domains='motorsport.com', q='Formula1', language='en', sort_by='publishedAt')
    articles = all_articles['articles'][:5]  # Get only the first 5 articles

    if not articles:
        return "No news articles found."

    message = "**Latest F1 News:**\n"
    for article in articles:
        title = article.get('title', 'No Title')
        url = article.get('url', '')
        message += f"- [{title}]({url})\n"
    return message

def get_driver_info(driver_name):
  url = "https://api.jolpi.ca/ergast/f1/2025/drivers/"
  response = requests.get(url)
  data = response.json()
  driver_info = data["MRData"]["DriverTable"]["Drivers"][0]
  message = f"**Driver Information:**\n"
  message += f"Name: {driver_info['givenName']} {driver_info['familyName']}\n"
  message += f"Date of Birth: {driver_info['dateOfBirth']}\n"
  message += f"Nationality: {driver_info['nationality']}\n"
  message += f"Number: {driver_info['permanentNumber']}\n"
  return message

def help_message():
  help_text = """ Here are the commands you can use:
$gif - Get a random F1 GIF 
$standings - Get the current F1 standings
$constructorstandings - Get the current F1 constructor standings
$results - Get the most recent F1 race results 
$schedule - Get the current F1 schedule 
$news - Get the latest F1 news 
$driver - Get information about a specific F1 driver 
$team - Get information about a specific F1 team
$help - Get help"""
  return help_text

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$gif'):
      await message.channel.send(get_gif())
    if message.content.startswith('$help'):
      await message.channel.send(help_message())
    if message.content.startswith('$standings'):
      await message.channel.send(get_standings())
    if message.content.startswith('$constructorstandings'):
      await message.channel.send(get_constructor_standings())
    if message.content.startswith('$results'):
      await message.channel.send(get_results())
    if message.content.startswith('$schedule'):
      await message.channel.send(get_schedule())
    if message.content.startswith('$news'):
      await message.channel.send(get_news())
    if message.content.startswith('$driver'):
      await message.channel.send(get_driver_info(message.content[6:]))
    if message.content.startswith('$team'):
      await message.channel.send(get_team_info(message.content[5:]))



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)


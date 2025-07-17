import discord
import requests
import json

with open('config.json') as f:
  d= json.load(f)
  token = d['token']
  api_key = d['api_key']


def get_gif():
    # always assign to the same name before you use it
    response = requests.get('https://api.giphy.com/v1/gifs/random?api_key=ypaas79YLlE4VbcUQLISZHU8ytmOf98i&tag=F1&rating=g')
    # you can also shortcut to .json()
    data = response.json()
    first = data['data']
    page_url = first['url']
    return page_url

def get_standings():
    url = "https://hyprace-api.p.rapidapi.com/v1/drivers-standings"
    querystring = {"pageSize":"-2147483648"}
    headers = {
	    "x-rapidapi-key": api_key,
	    "x-rapidapi-host": "hyprace-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def help_message():
  help_text = """ Here are the commands you can use:
$gif - Get a random F1 GIF
$standings - Get the current F1 standings 
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

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)


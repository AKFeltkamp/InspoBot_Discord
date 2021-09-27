import discord
import os
import requests
import json
import random
from awake import keep_awake

client = discord.Client()

stressed_words = ['work hard', 'stressed', 'overwhelmed', 'burnt out', 'too tired', 'overworked', 'work too hard']

encouragements = ['Work hard, but nap hard, too.', 'Be kind to yourself.', 'Take a break.', 'Everyone takes time to chill sometimes.']

def get_quote():
  response = requests.get("Https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote 


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$inspo'):
    await message.channel.send(get_quote())

  if any(word in message.content for word in stressed_words):
    await message.channel.send(random.choice(encouragements))


my_secret = os.environ['inspotoken']

keep_awake()
client.run(my_secret)

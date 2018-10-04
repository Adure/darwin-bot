import discord
import asyncio
from auth import bot_token
client = discord.Client()

@client.event
async def on_message(message):
	if message.content.startswith("/region"):
		region_list = ["OCE", "SEA", "Americas", "Europe", "Asia"]
		americas_list = ["americas", "na", "us", "america"]

		entered_team = message.content.split(" ")[1].lower()
		if entered_team == "oce":
			entered_team = "OCE"
		elif entered_team == "sea":
			entered_team = "SEA"
		elif entered_team in americas_list:
			entered_team = "Americas"
		elif entered_team == "europe" or "eu":
			entered_team = "Europe"
		elif entered_team == "asia":
			entered_team = "Asia"
		else:
			entered_team = ""
		role = discord.utils.get(message.server.roles, name=entered_team)

		if role is None or role.name not in region_list:
			await client.send_message(message.channel, "Region role not found. Available region roles are OCE, SEA, Americas, Europe, and Asia.")
			parts = message.content.split(" ")
			print("{0}#{1} tried to add {2} role, but it was not found  <{3}>".format(message.author.name, message.author.discriminator, parts[1], message.server.name))
			return
		elif role in message.author.roles:
			await client.send_message(message.channel, "You already have this role.")
			print("{0}#{1} already has {2} role  <{3}>".format(message.author.name, message.author.discriminator, role.name, message.server.name))
		else:
			try:
				await client.add_roles(message.author, role)
				await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
				print("Added role {0} to {1}#{2}  <{3}>".format(role.name,message.author.name, message.author.discriminator, message.server.name))
			except discord.Forbidden:
				await client.send_message(message.channel, "I don't have perms to add roles.")
				print("Forbidden Error!")

	if message.content.startswith("/platform"):
		platform_list = ["PC", "PS4", "XB1"]
		entered_team = message.content.split(" ")[1].lower()
		if entered_team == "pc":
			entered_team = "PC"
		elif entered_team == "ps4":
			entered_team = "PS4"
		elif entered_team == "xb1" or "xbox":
			entered_team = "XB1"
		role = discord.utils.get(message.server.roles, name=entered_team)

		if role is None or role.name not in platform_list:
			await client.send_message(message.channel, "Platform role not found. Available platform roles are PC, PS4, and XB1.")
			print("{0}#{1} tried to add {2} role, but it was not found  <{3}>".format(message.author.name, message.author.discriminator, role.name, message.server.name))
			return
		elif role in message.author.roles:
			await client.send_message(message.channel, "You already have this role.")
			print("{0}#{1} already has {2} role  <{3}>".format(message.author.name, message.author.discriminator, role.name, message.server.name))
		else:
			try:
				await client.add_roles(message.author, role)
				await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
				print("Added role {0} to {1}#{2}  <{3}>".format(role.name,message.author.name, message.author.discriminator, message.server.name))
			except discord.Forbidden:
				await client.send_message(message.channel, "I don't have perms to add roles.")
				print("Forbidden Error!")

@client.event
async def on_ready():
    print("ready!")

async def dontcrash():
	channels = client.get_all_channels()
	asyncio.sleep(50)

client.loop.create_task(dontcrash())

client.run(bot_token)
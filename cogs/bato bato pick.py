import discord
import random
from discord.ext import commands

class rock_paper_scissors(commands.Cog):
		def __init__(self, client):
			self.client = client


		@commands.Cog.listener()
		async def on_ready(self):
			print("I am BBP, I'm fully running right now!")


		@commands.command(name = "Bato bato pick!", aliases = ['bbp', 'BBP'], help = "Rock paper scissors in Filipino!")
		async def bato_bato_pick(self, ctx, *,choice = '-'):
			msg = f'{ctx.author.mention}'
			my_turn = ['gunting',
						'papel',
						'bato']
			emoji = [':scissors:',
						':newspaper:',
						':rock:']
			if choice == 'gunting'.casefold():
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nNAG TIE TAYO! :face_with_symbols_over_mouth:".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nNANALO KA WTF, U NERD :nerd:!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nI FOOKIN WIN U SCRUB :innocent:!".format(emoji[2],my_turn[2]))
			elif choice == 'papel'.casefold():
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nTALO KA NGAYON NUB :smiling_imp:!".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nANG CORNY NAG TIE PA TAYO :unamused:!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nTAE KA NATALO MO KO :cry:!".format(emoji[2],my_turn[2]))
			elif choice == 'bato'.casefold():
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nTANGINA TALO PA AKO :face_with_symbols_over_mouth:!".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nEZ MO NAMAN KALABAN :joy:!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nBAKIT YAN PINILI MO? WALA TULOY NANALO :confounded:!".format(emoji[2],my_turn[2]))
			else:
				await ctx.send(msg + " u gotta pick something scrub \nbato \npapel \ngunting")


		@commands.command(name = "Rock paper scissors", aliases = ["rps", "RPS"], help = "Rock paper scissors, what else did you think it was?")
		async def rock_paper_scissors(self, ctx, *,choice = '-'):
			msg = f'{ctx.author.mention}'
			my_turn = ['Scissors',
						'Paper',
						'Rock']
			emoji = [':scissors:',
						':newspaper:',
						':rock:']
			if choice == 'Scissors'.casefold():
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nWE TIED! :face_with_symbols_over_mouth:".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nYOU WON WTF, U NERD :nerd:!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nI FOOKIN WIN U SCRUB :innocent:!".format(emoji[2],my_turn[2]))
			elif choice == 'Paper'.casefold():
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nI WIN THIS TIME NOOB :smiling_imp:!".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nGFDI WHY DID WE TIE :unamused:!?!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nYOU BEAT ME THIS TIME SCRUB :sob:!".format(emoji[2],my_turn[2]))
			elif choice == 'Rock'.casefold():
				random_attack = random.randint(0,2)
				attack = my_turn[random_attack]
				if attack == my_turn[0]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nFEK IDK HOW U DID IT BUT U WIN :face_with_symbols_over_mouth:!".format(emoji[0],my_turn[0]))
				elif attack == my_turn[1]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nYOU'RE TOO EZ, I WIN :joy:!".format(emoji[1],my_turn[1]))
				elif attack == my_turn[2]:
					await ctx.send(msg + " MY CHOICE IS: {0} {1} \nWHY WOULD YOU PICK THAT? NOW WE TIED GRRR :confounded:!".format(emoji[2],my_turn[2]))
			elif choice == 'nuke'.casefold():
				await ctx.send(msg + ":mega:WTF WE'RE GETTING NUKED:mega:")
				await ctx.send(msg + ":three:")
				await ctx.send(msg + ":two:")
				await ctx.send(msg + ":one:")
				await ctx.send(msg + ":exploding_head::exploding_head::exploding_head::exploding_head:")
			elif choice == 'tractor'.casefold():
				await ctx.send(msg + "WTF ARE YOU GROWING PLANTS NOW?")
				await ctx.send(msg + ":tractor:")
				await ctx.send(msg + ":four_leaf_clover:")
				await ctx.send(msg + ":herb:")
				await ctx.send(msg + ":palm_tree:")
				await ctx.send(msg + ":christmas_tree:")
				await ctx.send(msg + "GREAT YOU GREW A CHRISTMAS TREE WTF")
			
			else:
				await ctx.send(msg + " u gotta pick something scrub \nRock \nPaper \nScissors")


def setup(client):
	client.add_cog(rock_paper_scissors(client))
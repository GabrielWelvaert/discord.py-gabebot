import discord
import random
import time
import sys
from datetime import datetime
from dateutil import tz, parser
from discord.ext import commands

#TOKEN = private!

bot = commands.Bot(command_prefix='.gb ', help_command=None)

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name =".gb help"))
	print('bot startup successful')

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('I dont understand that command. Try ".gb help"')

@bot.command()
async def help(ctx):
	await ctx.send("• My name is gabebot. I am a discord.py bot running on a Raspberry Pi\n• You can talk to me by using .gb\n• I understand: help, hello, decide, react, coinflip, joke, gamenight, quantity, back4blood, ironman\n• decide ex: .gb decide choice1 choice2 etc\n• ironman ex: .gb ironman player1 player2 etc")


@bot.command()
async def ironman(ctx, *args:str):

	roster = ["<:zelda:823394228708179998>","<:younglink:823394228473430018>","<:yoshi:823394236874489856>","<:shiek:823394228779745300>","<:samus:823394228742127646>","<:roy:823394228721418290>","<:pikachu:823395069704011776>","<:pichu:823394228679868416>","<:peach1:823394228523499561>","<:jigglypuff:823394228339605575>","<:kirby:823394228692058112>","<:link1:823394228671217684>","<:luigi:823394228675018782>","<:mario:823394228779745301>","<:marth:823394228692189224>","<:mewtwo:823394228629012530>","<:mrgamewatch:823394234589642782>","<:ness:823394228692320356>","<:bowser:823394228331347988>","<:cfalcon:823394234463158313>","<:DK:823394228348387338>","<:dr:823394228427948052>","<:falco:823394228624556052>","<:fox1:823394228435943505>","<:ganondorf:823394228351795201>","<:iceclimbers:823394228667154432>"]
	sent = []
	hightier = ["<:fox1:823394228435943505>","<:marth:823394228692189224>","<:jigglypuff:823394228339605575>","<:falco:823394228624556052>","<:shiek:823394228779745300>","<:cfalcon:823394234463158313>","<:peach1:823394228523499561>"]
	lowtier = ["<:DK:823394228348387338>", "<:link1:823394228671217684>", "<:younglink:823394228473430018>","<:mrgamewatch:823394234589642782>", "<:mewtwo:823394228629012530>", "<:roy:823394228721418290>","<:pichu:823394228679868416>", "<:ness:823394228692320356>", "<:zelda:823394228708179998>","<:kirby:823394228692058112>", "<:bowser:823394228331347988>"]
	pokemon = ["<:jigglypuff:823394228339605575>", "<:pikachu:823395069704011776>", "<:mewtwo:823394228629012530>","<:pichu:823394228679868416>"]
	midtier = ['<:yoshi:823394236874489856>', '<:samus:823394228742127646>', '<:pikachu:823395069704011776>', '<:luigi:823394228675018782>', '<:mario:823394228779745301>', '<:dr:823394228427948052>', '<:ganondorf:823394228351795201>', '<:iceclimbers:823394228667154432>']
	args = list(args)

	if len(args) == 0:
		await ctx.send("Invalid user amount. Please enter 1 to 4 users \nExample: .gb ironman gabebot " + ctx.author.name )
		return False

	if args[0].strip("-").isnumeric():
		if int(args[0]) < 1 or int(args[0]) > 26:
			await ctx.send("Invalid character amount. For a custom character amount, please enter 1 to 26 characters \nExample: .gb ironman 12 gabebot " + ctx.author.name)
			return False
		roster = random.sample(roster, int(args[0]))
		args.pop(0)
	elif args[0].lower() == "hightier":
		roster = random.sample(hightier, len(hightier))
		args.pop(0)
	elif args[0].lower() == "lowtier":
		roster = random.sample(lowtier, len(lowtier))
		args.pop(0)
	elif args[0].lower() == "pokemon":
		roster = random.sample(pokemon, len(pokemon))
		args.pop(0)
	elif args[0].lower() == "midtier":
		roster = random.sample(midtier, len(midtier))
		args.pop(0)
	if len(args) > 4 or len(args) < 1:
		await ctx.send("Invalid user amount. Please enter 1 to 4 users \nExample: .gb ironman gabebot " + ctx.author.name )
		return False

	for item in args:
		i = 5
		charlist = random.sample(roster, len(roster))
		while i < len(roster) + 4:
			charlist.insert(i,"\n")
			i += 6
		charlist = ", ".join(charlist)
		charlist = charlist.replace(",", "")
		await ctx.send(str(item) + ":\n " + charlist)
		sent.append(item)
		if len(sent) < len(args):
			await ctx.send("_ _")

@bot.command()
async def back4blood(ctx):
	now = datetime.now(tz=tz.tzlocal())
	back4bloodrelease = parser.parse("October 17, 2021")
	back4bloodrelease = back4bloodrelease.replace(tzinfo=tz.gettz("America/New_York"))
	a = str(back4bloodrelease - now)
	a = a.split()
	del(a[1])
	a = ":".join(a)
	a = a.replace(":0",":")
	a = a.split(":")
	#a = [0,0,0,0] # <- tester!
	def sp0(num, timetype):
		if num == "":
			timetype = ""
			return timetype
		elif  num == 1:
	        	return str(num) + " " + str(timetype) + " "
		else:
			return str(num) + " " + str(timetype) + "s " 
	timetypes = ["day", "hour", "minute"]
	valuetimes = []
	i = 0
	for item in timetypes:
	    result = sp0(int(a[i]), item)
	    valuetimes.append(result)
	    i += 1
	result = sp0(float(a[i]), "second")
	valuetimes.append(result)
	valuetimes = "".join(valuetimes)
	valuetimes = valuetimes.split()
	i = 1
	if len(valuetimes) > 4:
		for item in a:
			while i < len(valuetimes)-1:
				valuetimes[i] = valuetimes[i] + ","
				i += 2
	if len(valuetimes) > 2:
		valuetimes[len(valuetimes)-2] = "& " + valuetimes[len(valuetimes)-2]
	valuetimes = " ".join(valuetimes)
	if now >= back4bloodrelease or a == [0,0,0,0]:
		await ctx.send("Back4Blood has released!")
	else:
		await ctx.send("Back4Blood will release in " + valuetimes)

@bot.command()
async def quantity(ctx):
	await ctx.send("Approximately " + str(random.randint(0,sys.maxsize)))

@bot.command()
async def joke(ctx):
	jokes = ["What do you call a fake noodle? An Impasta",'I would avoid the sushi if I was you. It’s a little fishy.','Want to hear a joke about paper? Nevermind it’s tearable','I used to work in a shoe recycling shop. It was sole destroying','What do you call a belt with a watch on it? A waist of time','How do you organize an outer space party? You planet','I went to a seafood disco last week... and pulled a mussel','Why did the octopus beat the shark in a fight? Because it was well armed','There’s a new type of broom out, it’s sweeping the nation','What did the Buffalo say to his little boy when he dropped him off at school? Bison','The shovel was a ground breaking invention','A Buddhist walks up to a hot dog stand and says, "Make me one with everything','Did you hear about the guy who lost the left side of his body? He is alright now','Do you know sign language? You should learn it, it’s pretty handy','After the accident, the juggler didn’t have the balls to do it','I used to be afraid of hurdles, but I got over it','What should you do if you are cold? Stand in the corner. It’s 90 degrees','How does Moses make coffee? Hebrews it','The energizer bunny went to jail. He was charged with battery','The soldier who survived mustard gas and pepper spray was a seasoned veteran','Why shouldn’t you trust atoms? They make up everything','Want to hear a pizza joke? Nevermind, it’s too cheesy','What kind of car does a sheep drive? Their SuBAHHru','What do you call a line of rabbits marching backwards? A receding hairline','How do trees access the internet? They log on','I saw an ad for burial plots, and thought to myself this is the last thing I need','Have you ever tried to eat a clock? It is very time consuming','I wondered why the baseball was getting bigger. Then it hit me','Yesterday a clown held the door for me. It was a nice jester','I used to go fishing with Skrillex but he kept dropping the bass','The wedding was so emotional even the cake was in tiers','I owe a lot to the sidewalks. They’ve been keeping me off the streets for years','What do you call crystal clear urine? 1080pee','An untalented gymast walks into a bar','Einstein developed a theory about space, and it was about time too','Cartoonist found dead in home. Details are sketchy','Did you hear about the crime in the parking garage? It was wrong on so many levels','Why are there fences on graveyards? Because people are dying to get in','Why do trees have so many friends? They branch out','Never discuss infinity with a mathematician, they can go on about it forever','Don’t trust people that do acupuncture, they’re back stabbers','A persistent banker wouldn’t stop hitting on me so I asked him to leave me a loan','People say i look better without glasses but i just can not see it','Jill broke her finger today, but on the other hand she was completely fine','I flipped a coin over an issue the other day, it was quite the toss-up','I got hit in the head with a can of soda? Luckily it was a soft drink','I heard that the post office was a male dominated industry','Why isn’t suntanning an Olympic sport? Because the best you can ever get is bronze','These reversing cameras are great. Since I got one I haven’t looked back','The candle quit his job because he felt burned out','The plane flight brought my acrophobia to new heights','Novice pirates make terrible singers because they can’t hit the high seas','The earths rotation really makes my day','After eating the ship, the sea monster said, I can’t believe I ate the hull thing','Smaller babies may be delivered by stork but the heavier ones need a crane','I had a pun about insanity but then I lost it','Why don’t cannibals eat clowns? Because they taste funny','The tale of the haunted refrigerator was chilling','If you wear cowboy clothes are you ranch dressing?','Simba, youre falling behind. I must ask you to Mufasa','I feel sorry for shopping carts. Theyre always getting pushed around','Want to hear a pun about ghosts? Thats the spirit','I used to make clown shoes… which was no small feat','Did you hear about the circus that caught on fire? It was in tents','The best time of day to eat eggs is at the crack of dawn','Long fairy tales have a tendency to dragon','I really look up to my tall friends','Dont ever have multiple people wash dishes together. Its hard for them to stay in sink']
	await ctx.send(random.choice(jokes))

@bot.command()
async def coinflip(ctx):
	await ctx.send("Choose heads or tails! I'll flip the coin in 5 seconds!")
	time.sleep(5)
	await ctx.send(random.choice(["Heads!","Tails!"]))

@bot.command()
async def react(ctx):
	x = "<:weak:689242114222981314> <:thanos:689943431459373130> <:steve:796938741113552899> <:spongebob:796938708183023657> <:riptheskin:775596377069191189> <:pip:762911962149027850> <:pe:724040299231445173> <:keanu:788098382148534302> <:jackie:771903098171031582> <:isforme:765273143648321566> <:imstuff:762911984122593304> <:harry:774508889211142154> <:harambe:792554042278019083> <:grum2:788618238492934145> <:grum:788617183378800670> <:gordon:712544812565397534> <:gnomechild:774508922165133344> <:doinks:740970214413435000> <:doge:689577757545463829> <:deadcrewmate:762911919660204043> <:bubsy:788110947570155540> <:bonk:689242003485360150> <:bigtimetommie:768628473681412116> <:bigstu:764539472804053052> <:berniechad:765287160009457695> <:arnold:766865888124731453>"
	x = x.split(" ")
	await ctx.send(random.choice(x))

@bot.command()
async def testreact(ctx):
#	emoji = random.choice(guild.emojis)
	await ctx.send("test")


@bot.command()
async def hello(ctx):
	i = random.randint(0,50)
	if i > 0:
		pass
	else:
		await ctx.send(":)")
		return

	i = random.randint(0,10)
	if i <= 1:
		i = "Howdy"
	elif i == 2 or i == 3 or i == 4:
		i = "Hey"
	elif i == 5 or i == 6:
		i = "Hi"
	elif i >= 7:
		i = "Hello"
	await ctx.send(i + " " + (ctx.author.name))

@bot.command()
async def decide(ctx,*args:str):
	await ctx.send("I have decided: " + random.choice(args))

@bot.command()
async def gamenight(ctx):
	await ctx.send("gamenight or else")
	await ctx.send("gamenight or else")
	await ctx.send("gamenight or else")

@bot.command()
async def JTerm(ctx):
	x = ["<:DrHirosky:795139350550675496>, <:bigbrain:795140043639095327>"]
	await ctx.send(random.choice(x))
	await ctx.send("It's done. Congratulations boys!")
	await ctx.send(random.choice(x))

bot.run(TOKEN)

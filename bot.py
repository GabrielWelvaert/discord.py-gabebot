import discord
import random
import time
from discord.ext import commands

TOKEN = # private!

bot = commands.Bot(command_prefix='.gb ', help_command=None)

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name =".gb help"))
	print('bot startup successful')

@bot.command()
async def help(ctx):
	await ctx.send("• My name is gabebot. I am a WIP Raspi discord.py bot")
	await ctx.send('• You can talk to me by using .gb')
	await ctx.send("• I understand: help, hello, decide, react, coinflip, joke ")
	await ctx.send("• decide ex: .gb decide choice1 choice2 etc")

@bot.command()
async def joke(ctx):
	jokes = ["What do you call a fake noodle? An Impasta",'I would avoid the sushi if I was you. It’s a little fishy.','Want to hear a joke about paper? Nevermind it’s tearable','I used to work in a shoe recycling shop. It was sole destroying','What do you call a belt with a watch on it? A waist of time','How do you organize an outer space party? You planet','I went to a seafood disco last week... and pulled a mussel','Why did the octopus beat the shark in a fight? Because it was well armed','There’s a new type of broom out, it’s sweeping the nation','What did the Buffalo say to his little boy when he dropped him off at school? Bison','The shovel was a ground breaking invention','A Buddhist walks up to a hot dog stand and says, "Make me one with everything','Did you hear about the guy who lost the left side of his body? He is alright now','Do you know sign language? You should learn it, it’s pretty handy','After the accident, the juggler didn’t have the balls to do it','I used to be afraid of hurdles, but I got over it','What should you do if you are cold? Stand in the corner. It’s 90 degrees','How does Moses make coffee? Hebrews it','The energizer bunny went to jail. He was charged with battery','The soldier who survived mustard gas and pepper spray was a seasoned veteran','Why shouldn’t you trust atoms? They make up everything','Want to hear a pizza joke? Nevermind, it’s too cheesy','What kind of car does a sheep drive? Their SuBAHHru','What do you call a line of rabbits marching backwards? A receding hairline','How do trees access the internet? They log on','I saw an ad for burial plots, and thought to myself this is the last thing I need','Have you ever tried to eat a clock? It is very time consuming','I wondered why the baseball was getting bigger. Then it hit me','Yesterday a clown held the door for me. It was a nice jester','I used to go fishing with Skrillex but he kept dropping the bass','The wedding was so emotional even the cake was in tiers','I owe a lot to the sidewalks. They’ve been keeping me off the streets for years','What do you call crystal clear urine? 1080pee','An untalented gymast walks into a bar','Einstein developed a theory about space, and it was about time too','Cartoonist found dead in home. Details are sketchy','Did you hear about the crime in the parking garage? It was wrong on so many levels','Why are there fences on graveyards? Because people are dying to get in','Why do trees have so many friends? They branch out','Never discuss infinity with a mathematician, they can go on about it forever','Don’t trust people that do acupuncture, they’re back stabbers','A persistent banker wouldn’t stop hitting on me so I asked him to leave me a loan','People say i look better without glasses but i just can not see it','Jill broke her finger today, but on the other hand she was completely fine','I flipped a coin over an issue the other day, it was quite the toss-up','I got hit in the head with a can of soda? Luckily it was a soft drink','I heard that the post office was a male dominated industry','Why isn’t suntanning an Olympic sport? Because the best you can ever get is bronze','These reversing cameras are great. Since I got one I haven’t looked back','The candle quit his job because he felt burned out','The plane flight brought my acrophobia to new heights','Novice pirates make terrible singers because they can’t hit the high seas','The earths rotation really makes my day','After eating the ship, the sea monster said, I can’t believe I ate the hull thing','Smaller babies may be delivered by stork but the heavier ones need a crane','I had a pun about insanity but then I lost it','Why don’t cannibals eat clowns? Because they taste funny','The tale of the haunted refrigerator was chilling','If you wear cowboy clothes are you ranch dressing?','Simba, youre falling behind. I must ask you to Mufasa','I feel sorry for shopping carts. Theyre always getting pushed around','Want to hear a pun about ghosts? Thats the spirit','I used to make clown shoes… which was no small feat','Did you hear about the circus that caught on fire? It was in tents','The best time of day to eat eggs is at the crack of dawn','Long fairy tales have a tendency to dragon','I really look up to my tall friends','Dont ever have multiple people wash dishes together. Its hard for them to stay in sink']
	await ctx.send(random.choice(jokes))

@bot.command()
async def coinflip(ctx):
	await ctx.send("Choose heads or tails! I'll flip the coin in 5 seconds!")
	time.sleep(5)
	i = random.randint(0,1)
	if i == 0:
		await ctx.send("Heads!")
	else:
		await ctx.send("Tails!")

@bot.command()
async def react(ctx):
	x = "<:weak:689242114222981314> <:thanos:689943431459373130> <:steve:796938741113552899> <:spongebob:796938708183023657> <:riptheskin:775596377069191189> <:pip:762911962149027850> <:pe:724040299231445173> <:mollywario:785966585395019816> <:keanu:788098382148534302> <:jackie:771903098171031582> <:isforme:765273143648321566> <:imstuff:762911984122593304> <:harry:774508889211142154> <:harambe:792554042278019083> <:grum2:788618238492934145> <:grum:788617183378800670> <:gordon:712544812565397534> <:gnomechild:774508922165133344> <:doinks:740970214413435000> <:doge:689577757545463829> <:deadcrewmate:762911919660204043> <:bubsy:788110947570155540> <:bonk:689242003485360150> <:bigtimetommie:768628473681412116> <:bigstu:764539472804053052> <:berniechad:765287160009457695> <:arnold:766865888124731453>"
	x = x.split(" ")
	i = random.randint(0,len(x)-1)
	await ctx.send(x[i])

@bot.command()
async def hello(ctx):
	i = random.randint(0,50)
	if i > 0:
		pass
	else:
		await ctx.send("Greetings")
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


bot.run(TOKEN)


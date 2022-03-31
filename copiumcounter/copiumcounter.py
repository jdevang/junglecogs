from redbot.core import commands, checks
from discord.ext import tasks
from redbot.core import Config
from redbot.core.utils import AsyncIter

class CopiumCounter(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=696969696969)
        default_global = {
            "days": 0
        }
        self.config.register_global(**default_global)
        self.updatejigyaacope.start()

    @commands.command()
    async def jigyaacope(self, ctx):
        day_counter = await self.config.days()
        await ctx.send(f'{day_counter} days since Jigyaa ate Junk food!')

    @commands.command()
    @checks.is_owner()
    async def jigyaacopereset(self, ctx):
        await self.config.days.set(0)
        await ctx.send("Whoops! Counter has been reset cuz jigyaa broke the promise. Spam <@553118521412812801> and ask her about her copium!")
    
    @tasks.loop(hours=24)
    async def updatejigyaacope(self):
        day_counter = await self.config.days()
        await self.config.days.set(day_counter + 1)
    
    @updatejigyaacope.before_loop
    async def before_updatejigyaacope():
        hour = 24
        minute = 00
        await bot.wait_until_ready()
        now = datetime.now()
        future = datetime.datetime(now.year, now.month, now.day, hour, minute)
        if now.hour >= hour and now.minute > minute:
            future += timedelta(days=1)
        await asyncio.sleep((future-now).seconds)

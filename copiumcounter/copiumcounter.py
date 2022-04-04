from redbot.core import commands, checks
from discord.ext import tasks
from redbot.core import Config
from datetime import datetime, timedelta
import asyncio

class CopiumCounter(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=696969696969)
        default_global = {
            "days": 0,
            "record": 0
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
        days = int(await self.config.days())
        record_days = int(await self.config.record())
        record_days = record_days if record_days > days else days
        await self.config.record.set(record_days)
        await self.config.days.set(0)
        await ctx.send(f"Whoops! Counter has been reset cuz jigyaa broke the promise. Her current record is {record_days}. Spam <@553118521412812801> and ask her about her copium!")

    @commands.command()
    @checks.is_owner()
    async def jigyaacopeset(self, ctx, new_value):
        await self.config.days.set(new_value)
        await ctx.send(f"Day value set to {new_value}")

    
    @commands.command()
    @checks.is_owner()
    async def jigyaacoperecordset(self, ctx, new_value):
        await self.config.days.set(new_value)
        await ctx.send(f"Record value set to {new_value}")


    @commands.command()
    @checks.is_owner()
    async def jigyaacoperecordreset(self, ctx):
        record_days = await self.config.record()
        record_days = 0
        await self.config.record.set(record_days)
    
    @tasks.loop(hours=24)
    async def updatejigyaacope(self):
        day_counter = int(await self.config.days())
        day_counter = day_counter + 1
        await self.config.days.set(day_counter)
    
    @updatejigyaacope.before_loop
    async def before_updatejigyaacope(self):
        hour = 0
        minute = 0
        await self.bot.wait_until_ready()
        now = datetime.now()
        future = datetime(now.year, now.month, now.day, hour, minute)
        if now.hour >= hour and now.minute > minute:
            future += timedelta(days=1)
        await asyncio.sleep((future-now).seconds)

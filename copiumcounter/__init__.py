from .copiumcounter import CopiumCounter


def setup(bot):
    bot.add_cog(CopiumCounter(bot))
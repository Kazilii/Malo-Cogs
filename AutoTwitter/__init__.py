from .autotwit import AutoTwit

async def setup(bot):
    await bot.add_cog(AutoTwit(bot))
from redbot.core import commands

class AutoTwit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testcom(self, ctx):
        """I don't know what it does"""
        await ctx.send("We changed the output lmao")
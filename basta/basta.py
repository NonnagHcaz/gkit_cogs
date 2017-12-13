"""And so the lord said to me, BASTA!

I'm telling you, IT'S ENOUGH! BASTA, SATAN! BASTA!
"""

import discord
from discord.ext import commands


BASTA_STR = '_**BASTA**_'


class BASTA:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='basta', pass_context=True)
    async def basta(self, context):
        if context.invoked_subcommand is None:
            await self.bot.say("Type `[p]help basta` for info.")

    @basta.command(name='user', pass_context=True)
    async def user(self, context, user: discord.Member=None):
        if user is None:
            user = context.message.author
        await self.bot.say(
            '{b}, {u}! {b}!'.format(b=BASTA_STR, u=user.mention))

    @basta.command(name='satan', pass_context=False)
    async def satan(self):
        """BASTA, SATAN! BASTA!"""
        await self.bot.say(
            '{b}, {u}! {b}!'.format(b=BASTA_STR, u='SATAN'))

    @basta.command(name='santa', pass_context=False)
    async def santa(self):
        """BASTA, SANTA! BASTA!"""
        await self.bot.say(
            '{b}, {u}! {b}!'.format(b=BASTA_STR, u='SANTA'))

    @basta.command(name='stan', pass_context=False)
    async def stan(self):
        """BASTA, STAN! BASTA!"""
        await self.bot.say(
            '{b}, {u}! {b}!'.format(b=BASTA_STR, u='STAN'))


def setup(bot):
    bot.add_cog(BASTA(bot))

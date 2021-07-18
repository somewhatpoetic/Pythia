'''
Feature to create watch parties.
Use command .watchparty 

use .watchparty
send direct message to user
ask for:
What are you watching?
When are you hosting the watch party? (now, in x hours, at 3 pm [cst, gmt])
How early do you want to send a reminder for the watch party (15, 30, hour)
private or open?
if private - who are invited? (@username#1234)
'''

from discord.ext.commands import Cog, Command

class WatchParty(Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(WatchParty(bot))
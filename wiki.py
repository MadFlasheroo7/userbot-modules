import asyncio
import pprint

import wikipedia as wiki
from wikipedia.exceptions import DisambiguationError, PageError
import telethon as tg

from .. import command, module

class WikiUtils(module.Module):
    name = "Wikipedia"
    disabled = False

    @command.desc("Wikipedia Parser")
    async def cmd_wiki(self, ctx: command.Context):
        query = ctx.input

        await ctx.respond("Searching...")
        # await asyncio.sleep(1)

        try:
            wiki.summary(query, sentences = 3)
        except DisambiguationError as error:
            await ctx.respond("Disambiguated page not found...")
            return
        except PageError as pageerror:
            await ctx.respond("Page Not Found...")
        
        # result = pprint.pprint(wiki.summary(query, sentences = 3))
        result = wiki.summary(query, sentences = 3)
        await ctx.respond("```"+result+"...```")
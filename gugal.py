import asyncio
import os
import pprint

import google_images_download as gimg
from search_engine_parser.core.engines.google import Search as GoogleSearch 
import telethon as tg

from .. import command, module

class gugalUtils(module.Module):
    name = "Gugal"
    disabled = False

    @command.desc("Gives a google search result")
    @command.usage("Requiers a query to search for")
    async def cmd_google(self, ctx: command.Context):
        query = ctx.input
        await ctx.respond("Searching...")
        # await asyncio.sleep(1)
        search_args = (query,0)
        gsearch = GoogleSearch()
        gresults = await gsearch.async_search(*search_args)
        # a = {"Google": gresults}
        # msgId = ctx.msg.chat_id
        for i in range(10):
            try:
                title = gresults["titles"][i]
                link = gresults["links"][i]
                desc = gresults["descriptions"][i]
                msg += f"[{title}]({link})\n`{desc}`\n\n"
            except IndexError:
                break
        result = ("**Query :**\n" + query + "\n\n**Result :**\n" + msg, link_preview = False)
        await ctx.respond(result)
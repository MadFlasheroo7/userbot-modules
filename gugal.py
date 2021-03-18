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
        a = {"Google": gresults}
        msgId = ctx.msg.chat_id

        for k, v in a.items():
            for result in v:
                await ctx.respond(f"-------------{k}------------")
                await asyncio.sleep(1)
                final_result = pprint.pprint(result)
                await ctx.respond(final_result)
                # await self.bot.client.send_message(msgId,result)
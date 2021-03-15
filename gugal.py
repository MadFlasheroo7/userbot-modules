import asyncio
import os
import pprint

import google_images_download as gimg
from search_engine_parser.core.engines.google import Search as gSearch 
import telethon as tg

from .. import command, module

class gugalUtils(module.Module):
    name = "Gugal"
    disabled = False

    @command.desc("Gives a google search result")
    @command.usage("Requiers a query to search for")
    async def cmd_google(self, ctx: command.Context):
        query = ctx.input
        search_args = (query,1)
        gresults = gSearch.search(*search_args)
        a = {"Google": gresults}

        for k, v in a.items():
            pprint.pprint(f"-------------{k}------------")
            for result in v:
                pprint.pprint(result) 
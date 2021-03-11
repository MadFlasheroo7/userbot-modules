import asyncio

import telethon as tg

from .. import command, module

fishing_chat = -1001463155229


class FishingUtils(module.Module):
    name = "Fishing"
    disabled = False
    running = False

    @command.desc("Start Fishing!")
    async def cmd_startfish(self, ctx: command.Context):
        self.running = True
        await ctx.respond("`-> Fishing Started!`")
        while self.running:
            await self.bot.client.send_message(fishing_chat, "/fish@CalsiBot")
            await asyncio.sleep(3)

    @command.desc("Stop Fishing!")
    async def cmd_stopfish(self, ctx: command.Context):
        if self.running == True:
            self.running = False
            await ctx.respond("`-> Fishing stopped!`")
        else:
            await ctx.respond("`You are not fishing currently`\n do it by 'startfish'")

    async def on_message(self, event: tg.events.NewMessage.Event) -> None:
        if event.is_group and str(event.chat_id) == str(fishing_chat):
            await self.bot.client.send_read_acknowledge(
                event.chat, event.message, clear_mentions=True
            )

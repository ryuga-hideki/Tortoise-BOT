import logging
import traceback
import discord
from discord.ext import commands

logger = logging.getLogger(__name__)


class Bot(commands.Bot):
    error_log_channel_id = 690650346665803777

    def __init__(self, *args, prefix, **kwargs):
        super(Bot, self).__init__(*args, command_prefix=prefix, **kwargs)
        self.add_command(self.load)

    async def on_ready(self):
        logger.info("Successfully logged in and booted...!")
        logger.info(f"Logged in as {self.user.name} with ID {self.user.id} \t d.py version: {discord.__version__}")

    async def on_error(self, event: str, *args, **kwargs):
        msg = f"{event} event error exception!\n{traceback.format_exc()}"
        logger.critical(msg)
        await self.log_error(msg)

    async def log_error(self, message: str):
        if not self.is_ready() or self.is_closed():
            return

        message = message[:1980] + "...too long" if len(message) > 1980 else message
        error_log_channel = self.get_channel(Bot.error_log_channel_id)
        await error_log_channel.send(f"```{message}```")

    @commands.command(hidden=True)
    @commands.has_any_role("Admin")
    async def load(self, ctx, extension_name):
        """
        Loads an extension.
        :param extension_name: extension name, example 'moderation'
        """
        extension_path = f"cogs.{extension_name}"
        self.load_extension(extension_path)
        await ctx.send(f"{extension_path} loaded.")

    @commands.command(hidden=True)
    @commands.has_any_role("Admin")
    async def unload(self, ctx, extension_name):
        """
        Unloads an extension.
        :param extension_name: extension name, example 'moderation'
        """
        extension_path = f"cogs.{extension_name}"
        self.unload_extension(extension_path)
        await ctx.send(f"{extension_path} unloaded.")

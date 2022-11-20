from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='4istoLifeBot',
	auth_token='502585ab02e7df1a-cad9a043e2934597-51240acd2c19b41c'
)
viber = Api(bot_configuration)
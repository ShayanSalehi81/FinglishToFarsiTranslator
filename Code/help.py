from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class HelpSkill(Skill):
    @match_regex(r"help")
    async def ping(self, event):
        help_string = "Hello there! You are talking with Finglish2Persian bot.\nThis bot can convert Finglish texts to Persian. You just need to send your Finglish text in this format:\nconvert [YOUR_FINGLISH_SENTENCE]"
        await event.respond(help_string)

import sys
sys.path.append('.')

from opsdroid.skill import Skill
from opsdroid.matchers import match_parse
from convert import convert
from consider_biwords import consider_biwords
from chose_best_sentence import return_best_sentence


class PingSkill(Skill):
    @match_parse(r"convert {message}")
    async def ping(self, event):
        user_input = str(event.entities['message']['value'])
        sentences = convert(user_input)
        sentences = consider_biwords(sentences)
        await event.respond(f"Persian: {sentences[0][1]}")

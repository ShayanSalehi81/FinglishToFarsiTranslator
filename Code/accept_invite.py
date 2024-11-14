from opsdroid.skill import Skill
from opsdroid.matchers import match_event
from opsdroid.events import UserInvite, JoinRoom

class AcceptInvites(Skill):
    @match_event(UserInvite)
    async def user_invite(self, invite):
        if isinstance(invite, UserInvite):
            await invite.respond(JoinRoom())

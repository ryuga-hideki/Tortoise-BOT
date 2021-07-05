

class AuthorizedGuild(object):

    def __init__(self, guild_json: dict):
        self.id = guild_json.get('id')
        self.mod_mail = guild_json.get('mod_mail', False)
        self.bug_report = guild_json.get('bug_report', False)
        self.suggestions = guild_json.get('suggestions', False)
        self.event_submission = guild_json.get('event_submission', False)

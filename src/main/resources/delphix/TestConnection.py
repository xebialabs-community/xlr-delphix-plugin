from delphixpy.web.selfservice.bookmark import bookmark

from delphix.lib.DelphixSession import DelphixSession

dlpx_obj = DelphixSession.create(configuration)

# Test Connection by calling this api.
bookmark.get_all(dlpx_obj.server_session)
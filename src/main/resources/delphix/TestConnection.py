from delphixpy.v1_9_0.web.jetstream.bookmark import bookmark

from delphix.lib.DelphixSession import DelphixSession

dlpx_obj = DelphixSession.create(configuration)

# Test Connection by calling this api.
bookmark.get_all(dlpx_obj.server_session)
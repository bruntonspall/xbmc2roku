from pyramid.view import view_config
import model

@view_config(route_name='feed', renderer='feed.mako')
def feed_view(request):
    return {'shows': model.get_all_shows(request.db)}

@view_config(route_name='show', renderer='show.mako')
def show_view(request):
    return {
        'show': model.get_show(request.db, request.matchdict['showid']), 
        'episodes': model.get_all_episodes(request.db, request.matchdict['showid'])
    }

@view_config(route_name='media')
def media_view(request):
    settings = request.registry.settings
    
    episode = model.get_episode(request.db, request.matchdict['showid'], request.matchdict['episodeid'])
    path = episode['path'].replace(settings['path.trim'], settings['path.replace'])
    log.info("Streaming %s" % path)
    request.response.content_type = 'video/mpeg4'
    request.response.body_file = open(path)
    return request.response
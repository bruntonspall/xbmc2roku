# -*- coding: utf-8 -*- 
<rss>
	<channel>
		<title>${show['name']}</title>
		<link>${show['url']}</link>
		<description${show['description']}</description>
		<theme>video</theme>
		<lastBuildDate>Tue, 25 Jun 2013 07:26:12 GMT</lastBuildDate>
		<generator>PyRSS2Gen-1.0.0</generator>
		<docs>http://blogs.law.harvard.edu/tech/rss</docs>
% for item in episodes:
		<item>
			<link>${item['url']}</link>
			<title>S${item['season']} E${item['episode']} ${item['name']}</title>
			<description>${item['description']}</description>
			<enclosure url="${item['url']}" length="${item['length']}" type="video/mp4"></enclosure>

			<image>http://192.168.0.5:8001/media?res=223%2C200&amp;name=tv%2Farrow%2Fseason+1%2FS01E11-arrow-s01e11-720p-hdtv-x264-dimension-mkv-thumb.jpg&amp;key=video</image>
			<filetype>mp4</filetype>
			<ContentType>movie</ContentType>
			<StreamFormat>mp4</StreamFormat>
			<description>Video</description>
			<guid isPermaLink="false">${item['url']}</guid>
			<pubDate>Tue, 25 Jun 2013 07:26:12 GMT</pubDate>
		</item>
% endfor
	</channel>
</rss>
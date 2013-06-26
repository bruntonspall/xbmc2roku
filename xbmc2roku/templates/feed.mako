# -*- coding: utf-8 -*- 
<rss>
	<channel>
		<title>My Personal Videos</title>
		<link>/feed</link>
		<description>My Media</description>
		<theme>video</theme>
		<lastBuildDate>Tue, 25 Jun 2013 07:26:12 GMT</lastBuildDate>
		<generator>PyRSS2Gen-1.0.0</generator>
		<docs>http://blogs.law.harvard.edu/tech/rss</docs>
% for item in shows:
		<item>
			<link>http://localhost:8080/feed/${item['id']}</link>
			<title>${item['name']}</title>
			<pubDate>Tue, 25 Jun 2013 07:26:12 GMT</pubDate>
			<guid isPermaLink="false">http://localhost:8080/feed/${item['id']}</guid>
		</item>
% endfor
	</channel>
</rss>
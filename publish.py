import os, json, urllib2

files = {}
for name in os.listdir('.'):
    try:
        files[name] = {'content': open(name).read().decode('utf-8')}
    except:
        print 'skipping', name

data = {
    'description': "the description for this gist",
    'public': True,
    'files': files,
}

req = urllib2.Request('https://api.github.com/gists')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
html_url = json.loads(response.read())['html_url']
hash = html_url.split('/')[-1]
print 'gist:', html_url
print 'showcase:', 'https://rawgit.com/anonymous/' + hash + '/raw/index.html'

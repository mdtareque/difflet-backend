import wikipedia as w
w.search("india")
wikipedia.suggest("india")
wikipedia.suggest("India")
wikipedia.summary("India")
w.search("planet mercury")
w.search("earth")
w.search("paroot")
w.search("parrot")
w.page("parrot")
p=w.page("parrot")
p
p.sections
p
p.categories
india=w.page("India")
india.categories
p.content
p.images
p.images[:2]
p.title
p.url
p.links
p.content.find("infobox")
p.content.find("Infobox")
p.content.find("Info")
p.content
p.content.find("External")
p.content > out
write(p.content, out)
out = file()
"infobox" in p.content
"box" in p.content
p.content("box")
p.content.find("box")
p.content[p.content.find("box"):1000]
i=p.content.find("box")
p.content[i:i+100]
p.content[i-100:i]
p.content > /tmp/a
f=open("out", 'w')
f.write(p.content)
f.write(p.content.encode("UTF-8"))
f.close
f.close()
?
history?
import readline
for i in range(readline.get_current_history_length()):
print readline.get_history_item(i + 1)


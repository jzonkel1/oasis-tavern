"""v4: teal badge brand from the newer Facebook page (oasistavern78418): their photos, four-night lineup, their slogan."""
import json, os
from PIL import Image, ImageOps

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
keep = json.load(open("research/fb2-keep.json"))
def fb2(i): return "research/fb2/" + keep[i]

jobs = {
    "hero-d.jpg": (fb2(24), 2000), "hero-m.jpg": (fb2(21), 1200),
    "n-crowd.jpg": (fb2(25), 1400), "n-drums.jpg": (fb2(22), 1400), "n-listen.jpg": (fb2(82), 1200), "n-teddy.jpg": (fb2(62), 1400),
    "n-halloween.jpg": (fb2(59), 1400), "n-karaoke.jpg": (fb2(65), 1400), "n-guitar.jpg": (fb2(4), 1200), "n-drummer.jpg": (fb2(2), 1200),
    "n-singer.jpg": (fb2(49), 1200), "n-ladies.jpg": (fb2(51), 1400), "n-red.jpg": (fb2(67), 1200), "n-band.jpg": (fb2(7), 1400),
    "fly-openmic.jpg": (fb2(96), 900), "fly-ladies.jpg": (fb2(98), 900), "fly-karaoke.jpg": (fb2(97), 900), "fly-football.jpg": (fb2(90), 900),
}
for name, (src, w) in jobs.items():
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save("assets/img/" + name, quality=82, optimize=True, progressive=True)
for old in ["fly-bday.jpg", "fly-pool.jpg"]:
    if os.path.exists("assets/img/" + old):
        os.remove("assets/img/" + old)
print("images ok")

p = "index.html"
s = open(p, encoding="utf-8").read()
n = 0
def rep(a, b):
    global s, n
    assert a in s, a[:80]
    s = s.replace(a, b); n += 1

rep("<h1>Cold beer. Live music.<br><em>Friendly faces.</em></h1>", "<h1>Good drinks. Good people.<br><em>Good times.</em></h1>")
rep("<p>Flour Bluff's neighborhood bar on NAS Drive. Local bands and open mic on the patio, karaoke Saturdays, pool tables inside, and a bartender who remembers your name.</p>",
    "<p>Flour Bluff's neighborhood bar on NAS Drive. Cold beer, live music and open jam on the patio, karaoke Saturdays, football Sundays, pool tables inside. Everyone has a seat at our table.</p>")
rep('alt="Live music on the covered patio at Oasis Tavern, Flour Bluff"', 'alt="A full patio under the string lights at Oasis Tavern, Flour Bluff"')
rep(".week{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem}", ".week{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem}")
rep("@media (max-width:900px){.week{grid-template-columns:repeat(2,minmax(0,1fr))}.wk:last-child{grid-column:1/-1;max-width:calc(50% - .5rem);margin-inline:auto;width:100%}}",
    "@media (max-width:1000px){.week{grid-template-columns:repeat(2,minmax(0,1fr))}}")
rep("@media (max-width:600px){.week{grid-template-columns:minmax(0,1fr)}.wk:last-child{max-width:none}.wk__img{aspect-ratio:16/10}}",
    "@media (max-width:600px){.week{grid-template-columns:minmax(0,1fr)}.wk__img{aspect-ratio:16/10}}")
rep(".wk__body h3{font-size:1.5rem}", ".wk__body h3{font-size:1.35rem}")

start = s.index('    <div class="week">'); end = s.index('    <p class="week-note rv">')
cards = """    <div class="week">
      <article class="wk rv">
        <div class="wk__img"><img src="assets/img/fly-openmic.jpg" alt="Oasis Tavern Open Jam flyer" loading="lazy"><span class="wk__day">Wednesdays</span></div>
        <div class="wk__body"><h3>Open Jam &amp; 8-Ball</h3><p>Open jam hosted by Darren McGill. All musicians welcome. 8-ball pool tournament inside.</p><span class="time">7:30 PM</span></div>
      </article>
      <article class="wk rv">
        <div class="wk__img"><img src="assets/img/fly-ladies.jpg" alt="Oasis Tavern Ladies Night flyer" loading="lazy"><span class="wk__day">Fridays</span></div>
        <div class="wk__body"><h3>Ladies Night</h3><p>Grab your girls and kick off the weekend at the O. 50&cent; off beers for the ladies.</p><span class="time">All night</span></div>
      </article>
      <article class="wk rv">
        <div class="wk__img"><img src="assets/img/fly-karaoke.jpg" alt="Oasis Tavern Saturday Night Karaoke flyer" loading="lazy"><span class="wk__day">Saturdays</span></div>
        <div class="wk__body"><h3>Karaoke Night</h3><p>Karaoke with Tune in a Bucket. Where every voice matters, whether you can sing or not.</p><span class="time">7:30 PM</span></div>
      </article>
      <article class="wk rv">
        <div class="wk__img"><img src="assets/img/fly-football.jpg" alt="Oasis Tavern Football Sunday flyer" loading="lazy"><span class="wk__day">Sundays</span></div>
        <div class="wk__body"><h3>Football Sunday</h3><p>Game on at the O. Somebody is always cooking, so come hungry.</p><span class="time">Kickoff</span></div>
      </article>
    </div>
"""
s = s[:start] + cards + s[end:]; n += 1
rep("<p>Cold beer every day. These are the nights the place fills up.</p>", "<p>Small town vibes, big good times. These are the nights the place fills up.</p>")

gs = s.index('    <div class="gal rv">'); ge = s.index("</div>\n  </div>\n</section>\n\n<!-- ====== FIND US")
gal = """    <div class="gal rv">
      <figure><img src="assets/img/n-crowd.jpg" alt="A full patio on a live music night" loading="lazy"></figure>
      <figure><img src="assets/img/n-singer.jpg" alt="Karaoke night at the Oasis" loading="lazy"></figure>
      <figure><img src="assets/img/n-teddy.jpg" alt="Regulars on the patio" loading="lazy"></figure>
      <figure><img src="assets/img/n-guitar.jpg" alt="Live music on the patio" loading="lazy"></figure>
      <figure><img src="assets/img/sign-wall.jpg" alt="The original hand-painted Oasis Tavern sign" loading="lazy"></figure>
      <figure><img src="assets/img/n-ladies.jpg" alt="Ladies night at the Oasis" loading="lazy"></figure>
      <figure><img src="assets/img/n-drums.jpg" alt="Band under the string lights" loading="lazy"></figure>
      <figure><img src="assets/img/n-red.jpg" alt="Karaoke singer with a mic" loading="lazy"></figure>
      <figure><img src="assets/img/g-front.jpg" alt="Oasis Tavern front on NAS Drive" loading="lazy"></figure>
      <figure><img src="assets/img/n-halloween.jpg" alt="Halloween costume party" loading="lazy"></figure>
      <figure><img src="assets/img/n-drummer.jpg" alt="Drummer on the patio stage" loading="lazy"></figure>
      <figure><img src="assets/img/n-listen.jpg" alt="Friends listening to the band" loading="lazy"></figure>
      <figure><img src="assets/img/n-band.jpg" alt="Full band on the patio" loading="lazy"></figure>
      <figure><img src="assets/img/g-fish.jpg" alt="Fish fry night" loading="lazy"></figure>
      <figure><img src="assets/img/n-karaoke.jpg" alt="Karaoke crowd" loading="lazy"></figure>
      <figure><img src="assets/img/sign-road.jpg" alt="The blue Oasis Tavern sign on the roof" loading="lazy"></figure>
    """
s = s[:gs] + gal + s[ge:]; n += 1
rep("<title>Oasis Tavern | Beer, Live Music, Pool &amp; Karaoke in Flour Bluff — Corpus Christi, TX</title>",
    "<title>Oasis Tavern | Good Drinks, Good People, Good Times — Flour Bluff, Corpus Christi</title>")
rep("<p>Between the base and Lakeside. Free parking, covered patio out back. Cash bar, BYOB set-ups, 21 and up.</p>",
    "<p>Between the base and Lakeside. Free parking, covered patio out back. Beer bar, BYOB and set-ups, cash only, 21 and up.</p>")
open(p, "w", encoding="utf-8").write(s)
print("html edits", n)

o = open("research/og.html", encoding="utf-8").read()
o = o.replace("<h1>Cold beer. Live music.<br><em>Friendly faces.</em></h1>", "<h1>Good drinks. Good people.<br><em>Good times.</em></h1>")
o = o.replace("<span>Karaoke · Pool · Patio</span>", "<span>Live music · Karaoke · Pool</span>")
open("research/og.html", "w", encoding="utf-8").write(o)
print("og ok")

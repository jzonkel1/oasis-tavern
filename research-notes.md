# Oasis Tavern (Flour Bluff) — research notes, 2026-09-24

## Confirmed GBP data
- Name: Oasis Tavern  |  Category: Bar
- Address: 722 NAS Dr, Corpus Christi, TX 78418 (Flour Bluff)
- Phone: (361) 937-1911
- Google rating: 4.2 / 129 reviews (Maps, 9/24/26)
- Hours (directory listings, not confirmed on GBP): Mon-Fri 9am-12am, Sat 9am-1am, Sun 10am-12am
- Website field on GBP: http://oasis-tavern-corpus-christi.edan.io/  (see Domain section)
- Maps CID link: https://www.google.com/maps?cid=13462220105153479128
- Feature id: 0x8668f76e44e144c7:0xbad369dc17cb81d8
- Owner: Teddy (per Jeffrey; not public anywhere online)
- Facebook: facebook.com/oasistavern361 — 325 followers, tagline "Cold Beer and a Friendly Faces!",
  "locally owned and operated", category Beer Bar. Posts: open mic (Robert McCoy Music, 7-10pm),
  birthday nights w/ live music (Ely), munchies.
- Tripadvisor: unclaimed, 0 reviews. Yelp: only an "Oasis Pub" at 427 NAS Dr (old listing, scrape blocked).

## Review themes (Google topic chips)
atmosphere 7, karaoke 5, friendly staff 5, big patio 4, pool tournaments 3, bar games 3,
dive bar 2, chill spot 2, pool tables 2, snacks 2. Pool = 75 cents/game (directory copy).
Real excerpts usable on demo:
- Bethany Pepper (5*, 3 mo): "This is the Karaoke spot... The KJ is energetic and fun. Nice chill spot. Indoor and outdoor seating."
- Steve Steffen (5*, 5 mo): "the charro beans are to die for, they are the best I have ever eaten. Staff was great"
- Leo Duque (5*, 7 mo): "Really cool spot...super comfortable environment. Shout out to Rachel"
- Stacy Thurman (5*, 7 yr): "Gypsy is the best waitress... good atmosphere. Flour bluff"
- Peggy Blimline (5*, 8 yr): "Best Bartender on Sat, Sunday and Tuesday nights!"
Negatives seen: cash-only / no cards (3*), small karaoke area on smoking patio.

## Wisconsin mix-up question
No bar named "Oasis Tavern" exists in Wisconsin (Maps + web). WI has Oasis Bar & Grill (Endeavor,
Milwaukee, Arcadia), Club Oasis (Sparta), Rubicon Oasis, Kroghville Oasis, Black Saddle Tavern & Oasis
(Green Bay). None of the 10 visible Google reviews reference WI, fish fry, snow, or another city.
Only 10 of 129 reviews were readable (Google limited view; RPC endpoint 403), so the full set is
unverified, but nothing supports the mix-up theory. Nearby confusion candidates are local:
Oasis Grill & Bar (4425 S Alameda, 3.9/118) and the old Oasis Pub listing at 427 NAS Dr.

## Domain question
Teddy owns ZERO domains. The site Google links to is an edan.io subdomain: an auto-generated
listing-farm page (AdSense pub-8048584578917928, Yandex Metrika, fake reviews "Theodore Rivera"/
"Hazel Rao", generic "craft cocktails and mixology classes" copy, "Manage Listing" claim link).
It is built for the Corpus Christi location (address/phone/coords match), not Wisconsin.
Pitch angle: the only "website" Google shows for them is a spam page someone else profits from.
Fix on signing: set GBP website to the new domain; optionally claim/delete the edan.io listing.

## Reviews math (4.2 @ 129)
- To display 4.5 (rounds at 4.45): ~59 new five-star reviews.
- To hit a true 4.5: ~78 new five-star reviews (range 65-91 depending on where the hidden avg sits in 4.15-4.25).
- To display 4.3: ~5; to display 4.4: ~28.

## Gaps / flags
- Hours not read from GBP directly (limited view); confirm before demo.
- No logo found; FB profile photo not pulled. No photos scraped yet.
- Full review list not scraped (limited view). Demo uses only the real excerpts above.

## Build (9/24/26)
- Live preview: https://jzonkel1.github.io/oasis-tavern/  (repo jzonkel1/oasis-tavern, Pages on main, noindex)
- Deal: $250 one-off site, hosted free on GitHub Pages; custom domain later via Pages custom domain (CNAME) since no old github.io links exist for this one.
- Type: Zilla Slab + Mulish (first use of both). Accent = mustard gold sampled from their painted wall sign.
- Photos: 276 FB photos harvested (research/fb-harvest.json, 205 unique); hero = twilight patio band, mobile hero = guitarist under lights.
- Weekly lineup copied from their own flyers: Wed open mic jam (Robert McCoy) + 8-ball, Sat karaoke w/ Tune in a Bucket 7:30, monthly birthday pot-luck. CONFIRM with Teddy before launch.
- Hours on the page are from directories, not GBP. CONFIRM with Teddy.
- No logo exists; wordmark is set in type. Their painted sign photo carries the brand.
- Launch checklist: domain -> Pages CNAME + HTTPS, drop noindex meta, set canonical/og URLs to the domain (research/set_canonical_host.py pattern from Hot Box), set GBP website field to the domain, flag/claim the edan.io listing.

## v2 (9/24/26, after Jeffrey's tone feedback)
- Rejected v1: "hipsterish", "too much information", "reviews should be higher", "feels like a smoke shop". v1 saved at research/index-v1.html.
- Mark = the real hand-painted yellow sign (FB photo 62, perspective-corrected -> assets/img/sign.jpg). Timeline: yellow board was the original gable sign (old Google exterior photo), blue roof sign replaced it (2022 FB photos); yellow now hangs on the patio wall. Both real; blue shown in Find Us as the landmark.
- Fonts Antonio + Source Sans 3. Accent #c9a54a (sign yellow, brightened from the weathered #b7a05f sample). Removed: grain, kickers, info band, checklist section.
- Order: hero -> reviews -> what's on -> photos -> find us. OG card v2 uses the sign; headline measured inside the 285-915 safe box.

## v4 (9/24/26 evening) — match the NEW Facebook page's brand
- Second FB page: facebook.com/oasistavern78418 (page id 61591361201758), 112 followers, someone other than Teddy runs it. Round teal badge logo + "From Dive Bar to Superstar" cover, both AI art. 142 photos in research/fb2/.
- Logo: assets/img/logo.png (circle-cut from the 1254px profile pic), logo-512.png, favicon. Accent teal #3eabad (sampled), teal text #5fd0d2. Font stays Lilita One.
- Hero photo now the new page's full-patio-at-dusk shot (fb2 keep #24); mobile = dancing couple (#21). Yellow painted sign moved to the gallery.
- Weekly = 4 nights from their "This Week at the O" flyers (Sept 2026): Wed Open Jam w/ Darren McGill 7:30 + 8-ball; Fri Ladies Night 50c off beers; Sat Karaoke w/ Tune in a Bucket 7:30; Sun Football + food.
- H1 = their slogan "Good drinks. Good people. Good times." OG card v6 uses the badge.
- Old versions: research/index-v1.html (Zilla), index-v3-yellow.html (yellow sign / Lilita).

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

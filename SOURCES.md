# Music Sources & Reference Points

These are the touchstones for The Flip. When researching tracks, use these as
the compass — labels, comps, and artists that define the right zone for each genre.

---

## Bubblegum (60s-70s)
- **Compilations:** The Super K Kollection Vols 1-2 (closest thing to a Pebbles for bubblegum)
- **Labels:** Buddah Records, Bell Records, Super K Productions, ABC Records
- **Key figures:** Kasenetz & Katz (producers), Joey Levine (vocalist/writer — 15+ pseudonyms), Artie Resnick (co-writer)
- **Deep cuts:** Bohanna ("Jamaica"), The Tricycle (ABC, 1969), Crazy Elephant B-sides, Patty Flabbies' Coughed Engine
- **Radio:** Mr. Mustard's "Can't Come Down" on KKUP — https://spinitron.com/KKUP/show/9259/Can-t-Come-Down — *see General Sources below*
- **Blog:** bubblegumreviews.wordpress.com — Terminal Boredom equivalent for this world
- **YouTube:** GROOVY OBSCURITIES channel, Dub-Tel bubblegum playlist
- *Avoid: The Archies "Sugar Sugar," Ohio Express hits, 1910 Fruitgum Co. hits, anything with significant radio play. Kasenetz-Katz is too mainstream UNLESS it's an obscure B-side or deep cut that didn't chart. Aim for Super K deep cuts, Joey Levine pseudonym projects, one-off 45s on small labels.*

## Beat / 60s Beat Music
- **Labels:** Star-Club Records
- **Shows/Channels:** Beat Club, https://www.youtube.com/@beatclub
- *German TV beat show — goldmine for live footage of obscure acts*

## Power Pop
- **Compilations:** Powerpearls series, Kids On The Street
- **Artists:** Stiv Bators, The Records
- **Labels:** Bomp Records
- **Scenes:** Paisley Underground

## Punk
- **Compilations:** Killed By Death series, 70s UK punk comps
- **Artists:** Johnny Thunders, The Dead Boys, The Boys

## Glam
- **Compilations:** Junkshop Glam, All the Young Droogs, Velvet Tinmine
- *Junkshop glam = the cheap B-side UK glam stuff — avoid T. Rex, Bowie, and anything mainstream*

## Garage
- **Compilations:** Pebbles, Back From The Grave, Nuggets, Garage Beat '66, GS I Love You, Girls In The Garage
- *GS = Group Sounds, Japanese garage — deep well*
- *Girls In The Garage = female-fronted 60s garage, underused*

---

## Blog Post HTML — Canonical Snippets

These are exact strings to use when building post HTML. Copy verbatim — do not improvise.

### Playlist links block (both links present)
```html
<div class="playlist-links">
  <div class="playlist-link">&#9654; <a href="SONGS_AUTOPLAY_URL" target="_blank">PLAY THE TRACKS &rarr;</a></div>
  <div class="playlist-link">&#9654; <a href="COMMENTARY_AUTOPLAY_URL" target="_blank">PLAY THE TRACKS WITH DJ MIKE 2000 &rarr;</a></div>
</div>
```

### Playlist links block (songs only, no commentary yet)
```html
<div class="playlist-links">
  <div class="playlist-link">&#9654; <a href="SONGS_AUTOPLAY_URL" target="_blank">PLAY THE TRACKS &rarr;</a></div>
</div>
```

### Autoplay URL format (required — never use `playlist?list=` format)
```
https://www.youtube.com/watch?list=PLAYLIST_ID&v=FIRST_VIDEO_ID&autoplay=1
```

---

## General Sources (Cross-Genre)
- **Mr. Mustard's "Can't Come Down" on KKUP** — https://spinitron.com/KKUP/show/9259/Can-t-Come-Down
  - Covers obscure 60s and 70s records across genres: bubblegum, garage, power pop, beat, glam, etc.
  - Spinitron playlists are scrapeable — use this as a primary discovery source for any post
  - When building a new post, check recent episodes for relevant tracks
